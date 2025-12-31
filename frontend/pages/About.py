import streamlit as st

st.markdown("""
    <style>
    .about-header {
        text-align: center;
        padding: 2rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        animation: fadeIn 0.8s ease-out;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.3);
        background: rgba(255, 255, 255, 0.08);
    }
    
    .tech-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stat-container {
        text-align: center;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="about-header">', unsafe_allow_html=True)
st.title("About CitySense360 AI")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
<h2>🌆 Transforming Urban Living with Intelligence</h2>

**CitySense360 AI** is a next-generation smart city analytics platform that combines cutting-edge artificial intelligence, machine learning, and natural language processing to revolutionize urban decision-making and governance.

Our platform empowers city administrators, urban planners, and citizens with real-time insights, predictive analytics, and intelligent automation to create more livable, sustainable, and efficient cities.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Key Features Section
st.markdown("## 🚀 Core Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h3>🚦 Smart Traffic Management</h3>
    Advanced LSTM neural networks predict traffic congestion patterns with high accuracy, enabling proactive traffic management and route optimization.
    
    <ul>
    <li>Real-time congestion monitoring</li>
    <li>Predictive traffic flow analysis</li>
    <li>Intelligent signal optimization</li>
    <li>Emergency vehicle routing</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
    <h3>📊 Urban Analytics Engine</h3>
    Multi-dimensional scoring system evaluates city health across traffic, pollution, noise, and quality of life metrics.
    
    <ul>
    <li>Composite urban health scores</li>
    <li>Environmental impact assessment</li>
    <li>Quality of life indicators</li>
    <li>Trend analysis and forecasting</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>🤖 AI Chatbot Assistant</h3>
    RAG-powered conversational AI provides instant answers about city services, policies, and real-time conditions.
    
    <ul>
    <li>24/7 citizen support</li>
    <li>Multi-topic knowledge base</li>
    <li>Context-aware responses</li>
    <li>Service request handling</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
    <h3>💬 Sentiment Analysis</h3>
    Advanced NLP algorithms analyze citizen feedback to gauge public sentiment and identify emerging concerns.
    
    <ul>
    <li>Real-time feedback processing</li>
    <li>Emotion detection</li>
    <li>Issue categorization</li>
    <li>Trend identification</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Technology Stack
st.markdown("## 🛠️ Technology Stack")

st.markdown("""
<div class="feature-card">
<span class="tech-badge">🐍 Python</span>
<span class="tech-badge">🤖 TensorFlow</span>
<span class="tech-badge">🧠 LSTM Networks</span>
<span class="tech-badge">💬 NLP</span>
<span class="tech-badge">🔍 RAG</span>
<span class="tech-badge">📊 Plotly</span>
<span class="tech-badge">⚡ FastAPI</span>
<span class="tech-badge">🎨 Streamlit</span>
<span class="tech-badge">🔬 Scikit-learn</span>
<span class="tech-badge">📈 Pandas</span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Statistics Section
st.markdown("## 📈 Impact Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-container">
    <div class="stat-number">95%</div>
    <div>Prediction Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-container">
    <div class="stat-number">24/7</div>
    <div>Real-Time Monitoring</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-container">
    <div class="stat-number">10+</div>
    <div>Data Sources</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-container">
    <div class="stat-number">∞</div>
    <div>Scalability</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Use Cases
st.markdown("## 🎯 Real-World Applications")

st.markdown("""
<div class="feature-card">

### 🏙️ Municipal Government
- Traffic flow optimization and congestion management
- Environmental monitoring and pollution control
- Resource allocation and emergency response
- Citizen engagement and feedback analysis

### 👨‍💼 Urban Planners
- Data-driven city development strategies
- Infrastructure impact assessment
- Neighborhood vitality scoring
- Long-term sustainability planning

### 👥 Citizens
- Real-time service information
- Traffic and route planning
- Air quality alerts
- Direct communication with city services

### 🏢 Businesses
- Location intelligence for site selection
- Foot traffic analysis
- Market opportunity identification
- Risk assessment
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Vision Statement
st.markdown("""
<div class="feature-card" style="text-align: center;">
<h2>🌟 Our Vision</h2>

**"Building smarter, more responsive cities through the power of artificial intelligence"**

We believe that data-driven decision-making, powered by advanced AI and machine learning, is the key to creating urban environments that are more efficient, sustainable, and livable for all citizens.

CitySense360 bridges the gap between raw data and actionable insights, empowering stakeholders at every level to make informed decisions that improve quality of life.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="text-align: center; padding: 2rem 0; color:rgba(0, 0, 0, 0.45)
;">
<p>🚀 Powered by Advanced AI & Machine Learning</p>
<p>🌍 Building the Cities of Tomorrow, Today</p>
</div>
""", unsafe_allow_html=True)