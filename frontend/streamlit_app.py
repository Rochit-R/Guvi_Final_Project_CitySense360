import streamlit as st
from components.theme import apply_theme

st.set_page_config(
    page_title="CitySense360 AI",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_theme()

# Enhanced Sidebar
st.sidebar.markdown("""
    <style>
    .sidebar-title {
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 1s ease-out;
    }
    
    .sidebar-subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.70);
        font-size: 0.95rem;
        margin-bottom: 2rem;
        padding: 0 1rem;
        line-height: 1.6;
    }
    
    .feature-item {
        padding: 0.6rem 1rem;
        margin: 0.5rem 0;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        border-left: 3px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .feature-item:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateX(5px);
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-title">🏙️ CitySense360</div>', unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-subtitle">
AI-Powered Smart City Intelligence Platform
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.markdown("### 🎯 Core Features")

st.sidebar.markdown("""
<div class="feature-item">
<strong>🚦 Traffic Management</strong><br>
Real-time congestion prediction
</div>

<div class="feature-item">
<strong>🌍 Environment Monitoring</strong><br>
Air quality & pollution tracking
</div>

<div class="feature-item">
<strong>💬 NLP Analysis</strong><br>
Citizen sentiment insights
</div>

<div class="feature-item">
<strong>📈 LSTM Forecasting</strong><br>
Predictive urban analytics
</div>

<div class="feature-item">
<strong>🤖 RAG Chatbot</strong><br>
Intelligent city assistant
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem 0; color: rgba(255,255,255,0.6); font-size: 0.85rem;">
<p>🚀 Powered by Advanced AI</p>
<p>🌐 Version 2.0</p>
</div>
""", unsafe_allow_html=True)

# Main Content Area - ENHANCED
st.markdown("""
    <style>
    .hero-section {
        text-align: center;
        padding: 2rem 0 3rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        text-shadow: 0 0 40px rgba(102, 126, 234, 0.3);
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: rgba(255, 255, 255, 0.85);
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .feature-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
        animation: fadeIn 0.8s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .feature-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .feature-box:hover::before {
        opacity: 1;
    }
    
    .feature-box:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .feature-icon {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        display: block;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #fff;
        position: relative;
    }
    
    .feature-desc {
        color: rgba(255, 255, 255, 0.75);
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 4rem 0;
        padding: 3rem 2rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .cta-section {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
        border-radius: 20px;
        border: 1px solid rgba(102, 126, 234, 0.3);
        margin: 3rem 0;
        backdrop-filter: blur(10px);
    }
    
    .cta-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
    }
    
    .cta-subtitle {
        color: rgba(255,255,255,0.8);
        font-size: 1.2rem;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero-section">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">🏙️ CitySense360</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Smart City AI Platform - Transforming Urban Living Through Intelligence</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Features Grid
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

st.markdown("""
<div class="feature-box">
    <span class="feature-icon">🚦</span>
    <div class="feature-title">Traffic Intelligence</div>
    <p class="feature-desc">
    LSTM-powered traffic prediction with 95% accuracy. Real-time congestion monitoring 
    and intelligent route optimization for smoother urban mobility.
    </p>
</div>

<div class="feature-box">
    <span class="feature-icon">🌍</span>
    <div class="feature-title">Environmental Monitoring</div>
    <p class="feature-desc">
    Continuous air quality tracking, pollution analytics, and noise level monitoring 
    to ensure healthier living conditions for all citizens.
    </p>
</div>

<div class="feature-box">
    <span class="feature-icon">💬</span>
    <div class="feature-title">Sentiment Analysis</div>
    <p class="feature-desc">
    Advanced NLP processes citizen feedback in real-time, providing actionable insights 
    into public opinion and emerging concerns.
    </p>
</div>

<div class="feature-box">
    <span class="feature-icon">🤖</span>
    <div class="feature-title">AI Assistant</div>
    <p class="feature-desc">
    RAG-powered chatbot delivers instant, accurate answers about city services, 
    policies, and real-time conditions 24/7.
    </p>
</div>

<div class="feature-box">
    <span class="feature-icon">📊</span>
    <div class="feature-title">Urban Analytics</div>
    <p class="feature-desc">
    Comprehensive scoring system evaluates city health across multiple dimensions, 
    enabling data-driven governance decisions.
    </p>
</div>

<div class="feature-box">
    <span class="feature-icon">📈</span>
    <div class="feature-title">Predictive Insights</div>
    <p class="feature-desc">
    Machine learning models forecast trends and patterns, helping cities stay ahead 
    of challenges and optimize resource allocation.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Statistics Section
st.markdown("""
<div class="stats-container">
    <div class="stat-item">
        <div class="stat-number">95%</div>
        <div class="stat-label">Prediction Accuracy</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">24/7</div>
        <div class="stat-label">Real-Time Monitoring</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">10+</div>
        <div class="stat-label">AI Models</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">∞</div>
        <div class="stat-label">Scalability</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Call to Action Section
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">Ready to Transform Your City?</h2>
    <p class="cta-subtitle">
    Navigate using the sidebar to explore traffic prediction, urban analytics, 
    sentiment analysis, and more powerful features.
    </p>
</div>
""", unsafe_allow_html=True)

# Action Buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🚦 Predict Traffic", use_container_width=True, type="primary"):
        st.info("👈 Navigate to 'Traffic Prediction' page from sidebar")

with col2:
    if st.button("📊 View Dashboard", use_container_width=True, type="primary"):
        st.info("👈 Navigate to 'Dashboard' page from sidebar")

with col3:
    if st.button("🤖 Ask AI", use_container_width=True, type="primary"):
        st.info("👈 Navigate to 'City Chatbot' page from sidebar")

with col4:
    if st.button("📈 Analytics", use_container_width=True, type="primary"):
        st.info("👈 Navigate to 'Urban Analytics' page from sidebar")

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: rgba(0, 0, 0, 0.45);">
    <p style="font-size: 1.1rem; margin-bottom: 0.5rem;"><strong>🏙️ CitySense360</strong> - Built with Deep Learning, NLP, LSTM & RAG</p>
    <p style="font-size: 1rem;">🌍 Empowering Smart Governance for Next-Generation Cities</p>
    <p style="margin-top: 1rem; font-size: 0.9rem;">© 2024 CitySense360. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)