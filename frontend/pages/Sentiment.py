import streamlit as st
from components.api_client import analyze_sentiment
import plotly.graph_objects as go

st.markdown("""
    <style>
    .sentiment-header {
        text-align: center;
        padding: 1rem 0 2rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .feedback-input {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 1rem 0;
    }
    
    .result-positive {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.2) 0%, rgba(139, 195, 74, 0.2) 100%);
        border: 2px solid rgba(76, 175, 80, 0.5);
    }
    
    .result-negative {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.2) 0%, rgba(233, 30, 99, 0.2) 100%);
        border: 2px solid rgba(244, 67, 54, 0.5);
    }
    
    .result-neutral {
        background: linear-gradient(135deg, rgba(158, 158, 158, 0.2) 0%, rgba(189, 189, 189, 0.2) 100%);
        border: 2px solid rgba(158, 158, 158, 0.5);
    }
    
    .result-box {
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        text-align: center;
        animation: fadeIn 0.6s ease-out;
    }
    
    .sentiment-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .sentiment-label {
        font-size: 2rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .polarity-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .info-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="sentiment-header">', unsafe_allow_html=True)
st.title("📝 Citizen Feedback Analysis")
st.markdown("### AI-Powered Sentiment Analysis with NLP")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Information Section
st.markdown("""
<div class="info-card">
<h3>🤖 How It Works</h3>
<p>
Our advanced Natural Language Processing (NLP) system analyzes citizen feedback to determine 
sentiment polarity and emotional tone. This helps city administrators understand public opinion 
and respond to concerns effectively.
</p>
<br>
<strong>Sentiment Categories:</strong>
<ul>
<li><strong>Positive</strong>: Polarity > 0 (Citizens are satisfied and happy)</li>
<li><strong>Neutral</strong>: Polarity = 0 (Objective or mixed feelings)</li>
<li><strong>Negative</strong>: Polarity < 0 (Concerns or dissatisfaction expressed)</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Input Section
st.markdown("## 💬 Submit Citizen Feedback")

st.markdown('<div class="feedback-input">', unsafe_allow_html=True)

text = st.text_area(
    "Enter feedback text",
    height=200,
    placeholder="Example: The new metro service is excellent! It has reduced my commute time significantly. However, the ticketing system could be improved...",
    help="Type or paste citizen feedback for sentiment analysis"
)

# Sample feedback buttons
st.markdown("#### 📋 Try Sample Feedback:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("😊 Positive Sample", use_container_width=True):
        st.session_state.sample_text = "The new park renovation is fantastic! My family loves the playground and the walking trails. The city has done an excellent job maintaining public spaces."

with col2:
    if st.button("😐 Neutral Sample", use_container_width=True):
        st.session_state.sample_text = "The traffic signal at Main Street has been updated. The timing seems different from before. Will need some time to adjust to the new pattern."

with col3:
    if st.button("😟 Negative Sample", use_container_width=True):
        st.session_state.sample_text = "The garbage collection in our area has been very inconsistent lately. Sometimes they skip our street entirely. This needs immediate attention from the municipality."

# Use sample text if available
if 'sample_text' in st.session_state:
    text = st.text_area(
        "Sample feedback loaded",
        value=st.session_state.sample_text,
        height=200,
        key="sample_feedback"
    )
    del st.session_state.sample_text

st.markdown('</div>', unsafe_allow_html=True)

# Analyze Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_button = st.button("🔍 Analyze Sentiment", use_container_width=True, type="primary")

st.markdown("---")

# Results Section
if analyze_button:
    if text.strip():
        with st.spinner("🤖 Analyzing feedback with NLP..."):
            try:
                result = analyze_sentiment(text)
                sentiment = result["sentiment"]
                polarity = result["polarity"]
                
                # Determine styling based on sentiment
                if sentiment == "Positive":
                    result_class = "result-positive"
                    icon = "😊"
                    color = "#4CAF50"
                    message = "Citizens are expressing satisfaction!"
                elif sentiment == "Negative":
                    result_class = "result-negative"
                    icon = "😟"
                    color = "#F44336"
                    message = "Concerns detected - requires attention."
                else:
                    result_class = "result-neutral"
                    icon = "😐"
                    color = "#9E9E9E"
                    message = "Mixed or objective feedback received."
                
                # Display Results
                st.markdown(f"""
                <div class="result-box {result_class}">
                    <div class="sentiment-icon">{icon}</div>
                    <h2 style="color: white;">Sentiment Analysis Result</h2>
                    <div class="sentiment-label" style="color: {color};">{sentiment}</div>
                    <p style="color: rgba(255,255,255,0.8); font-size: 1.1rem; margin-top: 1rem;">
                    {message}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Metrics Row
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"""
                    <div style="background: rgba(255, 255, 255, 0.05); padding: 2rem; border-radius: 12px; text-align: center;">
                        <h3 style="color: rgba(255,255,255,0.7); margin-bottom: 1rem;">Polarity Score</h3>
                        <div class="polarity-value">{round(polarity, 3)}</div>
                        <p style="color: rgba(255,255,255,0.6); margin-top: 1rem;">Range: -1.0 to +1.0</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    # Gauge chart for polarity
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=polarity,
                        domain={'x': [0, 1], 'y': [0, 1]},
                        title={'text': "Sentiment Polarity", 'font': {'size': 20, 'color': 'white'}},
                        gauge={
                            'axis': {'range': [-1, 1], 'tickcolor': "white"},
                            'bar': {'color': color},
                            'bgcolor': "rgba(255,255,255,0.1)",
                            'borderwidth': 2,
                            'bordercolor': "rgba(255,255,255,0.3)",
                            'steps': [
                                {'range': [-1, -0.3], 'color': 'rgba(244, 67, 54, 0.3)'},
                                {'range': [-0.3, 0.3], 'color': 'rgba(158, 158, 158, 0.3)'},
                                {'range': [0.3, 1], 'color': 'rgba(76, 175, 80, 0.3)'}
                            ],
                            'threshold': {
                                'line': {'color': "white", 'width': 4},
                                'thickness': 0.75,
                                'value': polarity
                            }
                        }
                    ))
                    
                    fig.update_layout(
                        template="plotly_dark",
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font={'color': "white"},
                        height=300
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                # Interpretation
                st.markdown("### 📊 Interpretation")
                
                if polarity > 0.5:
                    interpretation = "Strong positive sentiment - citizens are very satisfied"
                    action = "Continue current initiatives and share success stories"
                elif polarity > 0:
                    interpretation = "Mild positive sentiment - generally favorable feedback"
                    action = "Maintain quality and look for improvement opportunities"
                elif polarity == 0:
                    interpretation = "Neutral sentiment - objective or balanced feedback"
                    action = "Gather more specific feedback to identify areas of focus"
                elif polarity > -0.5:
                    interpretation = "Mild negative sentiment - some concerns expressed"
                    action = "Investigate issues and communicate action plans"
                else:
                    interpretation = "Strong negative sentiment - significant dissatisfaction"
                    action = "Immediate attention required - prioritize resolution"
                
                st.markdown(f"""
                <div class="info-card">
                <p><strong>📌 Analysis:</strong> {interpretation}</p>
                <p><strong>💡 Recommended Action:</strong> {action}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.success("✅ Sentiment analysis completed successfully!")
                
            except Exception as e:
                st.error("❌ Error: Unable to analyze sentiment. Please check if the backend service is running.")
                st.exception(e)
    else:
        st.warning("⚠️ Please enter feedback text to analyze.")

st.markdown("---")

# Additional Information
st.markdown("## 💡 Understanding Sentiment Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
    <h4>🎯 Key Benefits</h4>
    <ul>
    <li>Real-time public opinion monitoring</li>
    <li>Early identification of emerging issues</li>
    <li>Data-driven policy adjustments</li>
    <li>Improved citizen engagement</li>
    <li>Proactive problem resolution</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
    <h4>📊 Technical Details</h4>
    <ul>
    <li>Advanced NLP algorithms</li>
    <li>Context-aware analysis</li>
    <li>Multi-language support ready</li>
    <li>Emotion detection capabilities</li>
    <li>Continuous learning system</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Use Cases
st.markdown("## 🎯 Real-World Applications")

st.markdown("""
<div class="info-card">
<strong>🏛️ Municipal Services:</strong> Track satisfaction with garbage collection, water supply, and road maintenance<br><br>
<strong>🚇 Public Transport:</strong> Monitor feedback on metro, bus services, and infrastructure<br><br>
<strong>🏥 Healthcare:</strong> Analyze patient feedback on public hospitals and clinics<br><br>
<strong>🏫 Education:</strong> Understand parent and student satisfaction with schools<br><br>
<strong>🌳 Environment:</strong> Gauge public opinion on parks, pollution control, and green initiatives<br><br>
<strong>🏗️ Infrastructure:</strong> Collect feedback on construction projects and urban development
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="text-align: center; padding: 1rem 0; color: rgba(0, 0, 0, 0.45);">
<p>🤖 Powered by Advanced NLP | 💬 Real-Time Sentiment Analysis | 🎯 Actionable Insights</p>
</div>
""", unsafe_allow_html=True)