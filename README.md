# CitySense360 – AI-Powered Smart City Intelligence Platform

CitySense360 (UrbanPulse-AI) is a full-stack AI-driven Smart City Analytics platform that integrates Machine Learning, Deep Learning (LSTM), Natural Language Processing, and Retrieval-Augmented Generation (RAG) to analyze, predict, and assist in urban decision-making.

The system is designed as a modular, scalable, multi-page AI application with a crystal-style dashboard UI and real-time analytics.

---

## Key Features

### 1. Citizen Sentiment Analysis (NLP)
- Analyzes public feedback using NLP
- Extracts sentiment and polarity
- Helps authorities understand citizen opinions

### 2. Urban Analytics & Scoring (ML)
- Predicts an overall Urban Health Score
- Inputs: Traffic, Pollution, Noise
- Outputs: Score and Category (Good / Moderate / Poor)

### 3. Traffic Congestion Prediction (LSTM)
- Uses time-series forecasting
- Predicts future traffic congestion levels
- Visualized using interactive charts

### 4. CitySense360 AI Assistant (RAG)
- Retrieval-Augmented chatbot
- Answers city-related questions using internal knowledge
- Topics: Traffic, Pollution, Safety, Emergency Services

---

## AI Technologies Used

NLP: TextBlob  
Machine Learning: Scikit-learn  
Deep Learning: TensorFlow (LSTM)  
Vector Database: FAISS  
Embeddings: Sentence Transformers  
LLM: FLAN-T5  
Backend: FastAPI  
Frontend: Streamlit  
Charts: Plotly  

---

## System Architecture

Frontend (Streamlit)  
→ REST API Communication  
Backend (FastAPI)  
→ NLP, ML, LSTM, RAG Services  

---

## Project Structure

UrbanPulse-AI/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── data/
│   └── run.py
│
├── frontend/
│   ├── assets/
│   │   └── style.css
│   ├── components/
│   │   ├── api_client.py
│   │   ├── charts.py
│   │   └── theme.py
│   ├── pages/
│   │   ├── Dashboard.py
│   │   ├── Sentiment.py
│   │   ├── Urban_Analytics.py
│   │   ├── Traffic_Prediction.py
│   │   ├── City_Chatbot.py
│   │   ├── About.py
│   │   └── Contact.py
│   └── streamlit_app.py
│
└── README.md

---

## Installation & Setup

1. Create virtual environment

python -m venv venv  
venv\Scripts\activate  

2. Install dependencies

pip install -r requirements.txt

---

## Running the Application

Start Backend (FastAPI)

cd backend  
python run.py  

Backend URL:  
http://127.0.0.1:8000  

Start Frontend (Streamlit)

cd frontend  
streamlit run streamlit_app.py  

Frontend URL:  
http://localhost:8501  

---

## Sample Inputs for Testing

Sentiment Analysis  
"Traffic congestion is terrible but the new metro line is helpful."

Urban Analytics  
Traffic: 73  
Pollution: 100  
Noise: 91  

Traffic Prediction  
T-3: 40  
T-2: 55  
T-1: 70  

RAG Chatbot  
"How does the city manage traffic congestion?"

---

## Output Examples

Sentiment: Positive / Negative / Neutral  
Urban Score: Numeric Score with Category  
Traffic Forecast: Congestion Index  
Chatbot: Context-aware AI response  

---

## Use Cases

Smart City Governance  
Urban Planning  
Traffic Management  
Pollution Monitoring  
Citizen Feedback Analysis  

---

## Project Status

All 4 AI modules implemented  
Frontend and Backend fully integrated  
Visualization enabled  
Project is submission-ready  

---

## Developed By

Rochit R  
4rth Year – Artificial Intelligence & Machine Learning  
Sri Krishna College of Technology  

---

## Future Enhancements

Real-time IoT data integration  
Cloud deployment  
Mobile application  
Multilingual chatbot  
Admin analytics dashboard  
