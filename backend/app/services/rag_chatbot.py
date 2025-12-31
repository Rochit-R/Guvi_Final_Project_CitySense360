from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

def load_rag_chain():
    # Load the expanded knowledge base
    loader = TextLoader("app/data/city_knowledge.txt", encoding='utf-8')
    docs = loader.load()

    # Better chunking strategy for comprehensive content
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = splitter.split_documents(docs)

    print(f"✅ Loaded {len(chunks)} knowledge chunks")

    # Create embeddings (same as before - works great)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )

    # Create vector database
    vector_db = FAISS.from_documents(chunks, embeddings)
    print("✅ Vector database created")

    # 🔥 UPGRADED MODEL: FLAN-T5-Large (3x better than base)
    model_name = "google/flan-t5-large"
    
    print(f"⏳ Loading {model_name}... (first time will download ~3GB)")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True
    )
    
    # Optimized text generation pipeline
    llm_pipeline = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=400,
        do_sample=True,
        temperature=0.5,
        top_p=0.92,
        repetition_penalty=1.2,
        no_repeat_ngram_size=3
    )

    llm = HuggingFacePipeline(pipeline=llm_pipeline)
    print("✅ Model loaded successfully!")

    # Improved prompt template
    prompt_template = """You are a helpful city assistant. Answer the question based on the context below.

Context:
{context}

Question: {question}

Provide a clear and detailed answer. If the information is not in the context, say "I don't have that information."

Answer:"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    # Create the RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}
        ),
        return_source_documents=False,
        chain_type_kwargs={"prompt": PROMPT}
    )

    print("✅ CitySense360 RAG Assistant Ready!\n")
    
    return qa_chain


# Initialize the chain when module loads
print("🚀 Initializing CitySense360 AI Assistant...")
rag_chain = load_rag_chain()


def ask_city_bot(query: str):
    """
    Process user query and return AI-generated answer
    """
    try:
        result = rag_chain.invoke({"query": query})
        answer = result.get("result", str(result))
        
        # Clean up response
        answer = answer.strip()
        
        # Remove any prompt artifacts
        if "Answer:" in answer:
            answer = answer.split("Answer:")[-1].strip()
        
        return answer
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return "I encountered an error. Please try rephrasing your question."