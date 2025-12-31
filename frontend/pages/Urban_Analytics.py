import streamlit as st
import requests
from components.charts import gauge_chart
import plotly.graph_objects as go

st.markdown("""
    <style>
    .analytics-header {
        text-align: center;
        padding: 1rem 0 2rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .slider-section {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 1.5rem 0;
    }
    
    .score-display {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 3rem;
        border: 2px solid rgba(102, 126, 234, 0.4);
        margin: 2rem 0;
        text-align: center;
        animation: fadeIn 0.6s ease-out;
    }
    
    .score-number {
        font-size: 5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 1rem 0;
    }
    
    .category-good {
        color: #4CAF50;
        font-size: 2rem;
        font-weight: 700;
        text-shadow: 0 0 20px rgba(76, 175, 80, 0.5);
    }
    
    .category-moderate {
        color: #FFC107;
        font-size: 2rem;
        font-weight: 700;
        text-shadow: 0 0 20px rgba(255, 193, 7, 0.5);
    }
    
    .category-poor {
        color: #F44336;
        font-size: 2rem;
        font-weight: 700;
        text-shadow: 0 0 20px rgba(244, 67, 54, 0.5);
    }
    
    .info-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .metric-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .metric-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
        background: rgba(255, 255, 255, 0.08);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="analytics-header">', unsafe_allow_html=True)
st.title("📊 Urban Analytics Engine")
st.markdown("### AI-Powered City Health Assessment")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Information Section
st.markdown("""
<div class="info-card">
<h3>🎯 What is Urban Score?</h3>
<p>
The Urban Score is a composite metric that evaluates overall city health by analyzing multiple 
environmental and infrastructure factors. Our AI model processes traffic congestion, pollution levels, 
and noise data to generate a comprehensive health score.
</p>
<br>
<strong>Score Categories:</strong>
<ul>
<li><strong>🟢 Good (75-100):</strong> Excellent urban conditions, high quality of life</li>
<li><strong>🟡 Moderate (50-74):</strong> Acceptable conditions with room for improvement</li>
<li><strong>🔴 Poor (0-49):</strong> Significant issues requiring immediate attention</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Input Section
st.markdown("## 📥 City Metrics Input")

st.markdown('<div class="slider-section">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🚦 Traffic Congestion")
    traffic = st.slider(
        "Traffic Level",
        min_value=0,
        max_value=100,
        value=50,
        help="0 = No congestion, 100 = Severe congestion"
    )
    
    # Visual indicator
    if traffic < 40:
        st.success(f"🟢 Low: {traffic}%")
    elif traffic < 70:
        st.warning(f"🟡 Moderate: {traffic}%")
    else:
        st.error(f"🔴 High: {traffic}%")
    
    st.progress(traffic / 100)

with col2:
    st.markdown("### 🌫️ Air Pollution")
    pollution = st.slider(
        "Pollution Index",
        min_value=0,
        max_value=100,
        value=40,
        help="0 = Clean air, 100 = Heavily polluted"
    )
    
    # Visual indicator
    if pollution < 40:
        st.success(f"🟢 Low: {pollution}%")
    elif pollution < 70:
        st.warning(f"🟡 Moderate: {pollution}%")
    else:
        st.error(f"🔴 High: {pollution}%")
    
    st.progress(pollution / 100)

with col3:
    st.markdown("### 🔊 Noise Level")
    noise = st.slider(
        "Noise Level (dB)",
        min_value=0,
        max_value=100,
        value=30,
        help="0 = Silent, 100 = Very loud"
    )
    
    # Visual indicator
    if noise < 40:
        st.success(f"🟢 Low: {noise}%")
    elif noise < 70:
        st.warning(f"🟡 Moderate: {noise}%")
    else:
        st.error(f"🔴 High: {noise}%")
    
    st.progress(noise / 100)

st.markdown('</div>', unsafe_allow_html=True)

# Preset scenarios
st.markdown("#### 🎭 Try Preset Scenarios:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🌟 Ideal City", use_container_width=True):
        st.session_state.preset = {"traffic": 20, "pollution": 15, "noise": 25}

with col2:
    if st.button("🏙️ Average City", use_container_width=True):
        st.session_state.preset = {"traffic": 50, "pollution": 40, "noise": 45}

with col3:
    if st.button("⚠️ Struggling City", use_container_width=True):
        st.session_state.preset = {"traffic": 75, "pollution": 70, "noise": 65}

with col4:
    if st.button("🚨 Crisis Mode", use_container_width=True):
        st.session_state.preset = {"traffic": 90, "pollution": 85, "noise": 80}

# Apply preset if selected
if 'preset' in st.session_state:
    traffic = st.session_state.preset["traffic"]
    pollution = st.session_state.preset["pollution"]
    noise = st.session_state.preset["noise"]
    del st.session_state.preset
    st.rerun()

# Calculate Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔮 Calculate Urban Score", use_container_width=True, type="primary")

st.markdown("---")

# Results Section
if predict_button:
    with st.spinner("🤖 AI Model Calculating..."):
        payload = {
            "traffic": traffic,
            "pollution": pollution,
            "noise": noise
        }

        try:
            res = requests.post(
                "http://127.0.0.1:8000/analytics/predict",
                json=payload
            )

            if res.status_code == 200:
                result = res.json()

                # Safe extraction
                raw_score = result.get("urban_score")

                if isinstance(raw_score, dict):
                    score = float(raw_score.get("urban_score", 0))
                    category = raw_score.get("category", "Unknown")
                else:
                    score = float(raw_score)
                    category = result.get("category", "Unknown")

                # Display Score
                if category == "Good":
                    category_class = "category-good"
                    icon = "🟢"
                    message = "Excellent urban health! Keep up the great work."
                    color = "#4CAF50"
                elif category == "Moderate":
                    category_class = "category-moderate"
                    icon = "🟡"
                    message = "Acceptable conditions. Focus on improvements."
                    color = "#FFC107"
                else:
                    category_class = "category-poor"
                    icon = "🔴"
                    message = "Critical issues detected. Immediate action required."
                    color = "#F44336"

                st.markdown(f"""
                <div class="score-display">
                    <h2 style="color: white; margin-bottom: 0.5rem;">Urban Health Score</h2>
                    <div class="score-number">{score:.1f}</div>
                    <div class="{category_class}">{icon} {category}</div>
                    <p style="color: rgba(255,255,255,0.8); margin-top: 1.5rem; font-size: 1.2rem;">
                    {message}
                    </p>
                </div>
                """, unsafe_allow_html=True)

                # Detailed Breakdown
                st.markdown("### 📊 Detailed Analysis")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    # Gauge chart for score
                    fig_gauge = gauge_chart(score, "Urban Health Score", 100)
                    st.plotly_chart(fig_gauge, use_container_width=True)
                
                with col2:
                    # Contribution breakdown
                    contributions = {
                        'Traffic': 100 - traffic,
                        'Air Quality': 100 - pollution,
                        'Noise Control': 100 - noise
                    }
                    
                    fig = go.Figure(data=[
                        go.Bar(
                            x=list(contributions.keys()),
                            y=list(contributions.values()),
                            marker=dict(
                                color=list(contributions.values()),
                                colorscale='RdYlGn',
                                line=dict(color='rgba(255,255,255,0.3)', width=2)
                            ),
                            text=[f'{v:.0f}%' for v in contributions.values()],
                            textposition='auto',
                        )
                    ])
                    
                    fig.update_layout(
                        title=dict(
                            text="Factor Contributions",
                            font=dict(size=20, color='white'),
                            x=0.5,
                            xanchor='center'
                        ),
                        template="plotly_dark",
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        xaxis=dict(showgrid=False, title_font=dict(color='white')),
                        yaxis=dict(
                            showgrid=True,
                            gridwidth=1,
                            gridcolor='rgba(255,255,255,0.1)',
                            title="Health Score",
                            title_font=dict(color='white'),
                            range=[0, 100]
                        ),
                        height=400
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                # Recommendations
                st.markdown("### 💡 Recommendations")
                
                recommendations = []
                
                if traffic > 60:
                    recommendations.append("🚦 **Traffic:** Implement smart traffic management, promote public transport")
                elif traffic > 30:
                    recommendations.append("🚦 **Traffic:** Monitor peak hours, optimize signal timing")
                else:
                    recommendations.append("🚦 **Traffic:** Maintain current traffic management strategies")
                
                if pollution > 60:
                    recommendations.append("🌫️ **Pollution:** Urgent action needed - increase green cover, restrict vehicle emissions")
                elif pollution > 30:
                    recommendations.append("🌫️ **Pollution:** Monitor air quality, promote clean energy initiatives")
                else:
                    recommendations.append("🌫️ **Pollution:** Continue environmental protection measures")
                
                if noise > 60:
                    recommendations.append("🔊 **Noise:** Enforce noise regulations, create quiet zones")
                elif noise > 30:
                    recommendations.append("🔊 **Noise:** Monitor noise levels in residential areas")
                else:
                    recommendations.append("🔊 **Noise:** Maintain current noise control measures")
                
                for rec in recommendations:
                    st.markdown(f"""
                    <div class="info-card">
                    {rec}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.success("✅ Urban score calculated successfully!")

            else:
                st.error("❌ Backend service unavailable. Please check if the server is running.")

        except Exception as e:
            st.error("❌ Error connecting to backend service.")
            st.exception(e)

st.markdown("---")

# Additional Information
st.markdown("## 🎯 Understanding the Metrics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
    <h4>📊 How Scoring Works</h4>
    <ul>
    <li>AI model analyzes all three factors</li>
    <li>Weighted algorithm calculates composite score</li>
    <li>Real-time processing and instant results</li>
    <li>Historical data improves accuracy</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
    <h4>🎯 Use Cases</h4>
    <ul>
    <li>Policy decision-making</li>
    <li>Resource allocation planning</li>
    <li>Citizen communication</li>
    <li>Long-term urban development</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="text-align: center; padding: 1rem 0; color: rgba(0, 0, 0, 0.45);">
<p>🤖 Powered by Machine Learning | 📊 Real-Time Analytics | 🎯 Data-Driven Insights</p>
</div>
""", unsafe_allow_html=True)