import streamlit as st
from components.api_client import ask_city_bot

st.markdown("""
    <style>
    .chatbot-header {
        text-align: center;
        padding: 1rem 0 2rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .info-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .quick-question-btn {
        margin: 0.3rem;
    }
    
    /* Chat message styling */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 18px 18px 4px 18px;
        margin: 1rem 0;
        margin-left: 20%;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        animation: fadeIn 0.3s ease-out;
    }
    
    .bot-message {
        background: rgba(30, 30, 50, 0.9) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.3);
        color: white !important;
        padding: 1rem 1.5rem;
        border-radius: 18px 18px 18px 4px;
        margin: 1rem 0;
        margin-right: 20%;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        animation: fadeIn 0.3s ease-out;
    }
    
    .bot-message * {
        color: white !important;
    }
    
    .bot-message p {
        color: white !important;
        margin: 0;
    }
    
    .message-label {
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
        opacity: 0.8;
    }
    
    .message-content {
        font-size: 1rem;
        line-height: 1.6;
        color: white !important;
    }
    
    .bot-message .message-content {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    .user-message .message-content {
        color: white !important;
    }
    
    .empty-chat {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        margin: 2rem 0;
    }
    
    .feature-box {
        text-align: center;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .feature-box:hover {
        background: rgba(255, 255, 255, 0.05);
        transform: translateY(-3px);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="chatbot-header">', unsafe_allow_html=True)
st.title("🤖 CitySense360 AI Assistant")
st.markdown("### RAG-Powered Smart City Intelligence")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Information Section
st.markdown("""
<div class="info-card">
<h3>💡 How to Use</h3>
<p>
Ask me anything about traffic conditions, city services, air quality, emergency services, 
public transport, policies, or any urban information. I'm powered by Retrieval-Augmented 
Generation (RAG) technology to provide accurate, context-aware answers.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Quick Question Buttons
st.markdown("### 💬 Quick Questions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚦 Traffic Status", use_container_width=True):
        st.session_state.quick_question = "What is the current traffic situation in the city?"
        st.rerun()
    
    if st.button("🏥 Emergency Services", use_container_width=True):
        st.session_state.quick_question = "Where are the nearest emergency services?"
        st.rerun()

with col2:
    if st.button("🌫️ Air Quality", use_container_width=True):
        st.session_state.quick_question = "How is the air quality today?"
        st.rerun()
    
    if st.button("🚇 Public Transport", use_container_width=True):
        st.session_state.quick_question = "What are the public transport options available?"
        st.rerun()

with col3:
    if st.button("🏛️ City Services", use_container_width=True):
        st.session_state.quick_question = "What city services are available for citizens?"
        st.rerun()
    
    if st.button("⚠️ Safety Info", use_container_width=True):
        st.session_state.quick_question = "Tell me about city safety measures"
        st.rerun()

st.markdown("---")

# Input Section
st.markdown("### 💭 Ask Your Question")

# Check if quick question was selected
default_question = ""
if "quick_question" in st.session_state:
    default_question = st.session_state.quick_question
    del st.session_state.quick_question

question = st.text_input(
    "Type your question here",
    value=default_question,
    placeholder="Example: What are the peak traffic hours? How can I report a pothole?",
    help="Ask about traffic, safety, pollution, services, or any city-related information",
    key="question_input"
)

col1, col2 = st.columns([3, 1])

with col1:
    ask_button = st.button("🚀 Ask AI", use_container_width=True, type="primary")

with col2:
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

st.markdown("---")

# Process Question
if ask_button and question.strip():
    with st.spinner("🤖 AI Assistant is thinking..."):
        try:
            # Add user message to history
            st.session_state.chat_history.append({
                "role": "user",
                "content": question
            })
            
            # Get AI response
            answer = ask_city_bot(question)
            
            # Add bot response to history
            st.session_state.chat_history.append({
                "role": "bot",
                "content": answer["answer"]
            })
            
            st.rerun()
            
        except Exception as e:
            st.error("❌ Error: Unable to get response. Please check if the backend service is running.")
            st.exception(e)

elif ask_button and not question.strip():
    st.warning("⚠️ Please enter a question to ask the AI assistant.")

# Display Chat History
if st.session_state.chat_history:
    st.markdown("### 💬 Conversation")
    
    # Display messages using Streamlit's native approach
    for idx, message in enumerate(st.session_state.chat_history):
        if message["role"] == "user":
            # User message - right aligned
            st.markdown(f"""
            <div class="user-message">
                <div class="message-label">👤 You</div>
                <div class="message-content">{message["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Bot message - left aligned
            st.markdown(f"""
            <div class="bot-message">
                <div class="message-label">🤖 AI Assistant</div>
                <div class="message-content">{message["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Add some spacing at the bottom
    st.markdown("<br>", unsafe_allow_html=True)

else:
    # Empty state
    st.markdown("""
    <div class="empty-chat">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🤖</div>
        <h3 style="color: white;">Hello! I'm your CitySense360 AI Assistant</h3>
        <p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-top: 1rem;">
        I'm here to help you with information about traffic, city services, air quality, 
        and more. Choose a quick question above or type your own!
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Example Questions Section
st.markdown("## 📚 Example Questions You Can Ask")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
    <h4>🚦 Traffic & Transportation</h4>
    <ul>
    <li>What are the peak traffic hours in the city?</li>
    <li>How can I check real-time bus schedules?</li>
    <li>Are there any road closures today?</li>
    <li>What's the best route to avoid traffic?</li>
    <li>Is the metro running on schedule?</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
    <h4>🌍 Environment & Health</h4>
    <ul>
    <li>What's the current air quality index?</li>
    <li>Are there any pollution alerts today?</li>
    <li>Where are the nearest green spaces?</li>
    <li>How can I report environmental issues?</li>
    <li>What are the noise pollution levels?</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
    <h4>🏛️ City Services</h4>
    <ul>
    <li>How do I pay my property taxes?</li>
    <li>Where can I apply for permits?</li>
    <li>What are the garbage collection timings?</li>
    <li>How do I report a street light issue?</li>
    <li>Where are the public libraries?</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
    <h4>🚨 Safety & Emergency</h4>
    <ul>
    <li>What's the emergency contact number?</li>
    <li>Where are the nearest hospitals?</li>
    <li>How do I report a crime?</li>
    <li>Are there any safety alerts?</li>
    <li>Where are the police stations located?</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Features Section
st.markdown("## ✨ AI Assistant Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🧠</div>
        <h4>Smart Understanding</h4>
        <p style="color: rgba(255,255,255,0.7);">
        Natural language processing understands context and intent
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">📚</div>
        <h4>Knowledge Base</h4>
        <p style="color: rgba(255,255,255,0.7);">
        Access to comprehensive city information and policies
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">⚡</div>
        <h4>Instant Responses</h4>
        <p style="color: rgba(255,255,255,0.7);">
        Get accurate answers in seconds, 24/7 availability
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="text-align: center; padding: 1rem 0; color: rgba(0, 0, 0, 0.45);">
<p>🤖 Powered by RAG (Retrieval-Augmented Generation) | 💬 Natural Language Processing | ⚡ Real-Time Intelligence</p>
</div>
""", unsafe_allow_html=True)