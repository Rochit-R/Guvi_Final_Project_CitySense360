import streamlit as st
from components.charts import gauge_chart, pie_chart
import plotly.graph_objects as go

st.markdown("""
    <style>
    .dashboard-header {
        text-align: center;
        padding: 1rem 0 2rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        animation: fadeIn 0.8s ease-out;
        text-align: center;
    }
    
    .metric-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.4);
        background: rgba(255, 255, 255, 0.08);
    }
    
    .info-panel {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .status-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.3rem;
        font-size: 0.9rem;
    }
    
    .badge-success {
        background: rgba(76, 175, 80, 0.2);
        border: 1px solid rgba(76, 175, 80, 0.5);
        color: #4CAF50;
    }
    
    .badge-warning {
        background: rgba(255, 193, 7, 0.2);
        border: 1px solid rgba(255, 193, 7, 0.5);
        color: #FFC107;
    }
    
    .badge-info {
        background: rgba(33, 150, 243, 0.2);
        border: 1px solid rgba(33, 150, 243, 0.5);
        color: #2196F3;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="dashboard-header">', unsafe_allow_html=True)
st.title("📊 City Intelligence Dashboard")
st.markdown("### Real-time Urban Analytics & Monitoring")
st.markdown('</div>', unsafe_allow_html=True)

# Key Metrics Row
st.markdown("## 🎯 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Urban Score", "88", "+4", delta_color="normal")
    st.markdown("🟢 Excellent", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Traffic Index", "73", "-2", delta_color="inverse")
    st.markdown("🟡 Moderate", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Air Quality", "156", "+8", delta_color="inverse")
    st.markdown("🟠 Moderate", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Response Time", "4.2 min", "-0.3", delta_color="inverse")
    st.markdown("🟢 Fast", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Gauges Section
st.markdown("## 📈 Live Monitoring")

col1, col2, col3 = st.columns(3)

with col1:
    fig1 = gauge_chart(73, "Traffic Congestion", 100)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = gauge_chart(156, "Air Quality Index", 300)
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    fig3 = gauge_chart(62, "Noise Level (dB)", 100)
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# City Services Distribution
st.markdown("## 🏙️ City Services Status")

col1, col2 = st.columns(2)

with col1:
    # Service distribution pie chart
    services = ['Transportation', 'Healthcare', 'Education', 'Public Safety', 'Utilities']
    values = [30, 25, 20, 15, 10]
    fig_pie = pie_chart(services, values, "Service Resource Allocation")
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    # Incident response times
    categories = ['Emergency', 'Maintenance', 'Complaints', 'Queries']
    response_times = [3.2, 8.5, 12.3, 5.7]
    
    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=response_times,
            marker=dict(
                color=['#4CAF50', '#FFC107', '#FF5722', '#2196F3'],
                line=dict(color='rgba(255,255,255,0.3)', width=2)
            ),
            text=[f'{t} min' for t in response_times],
            textposition='auto',
            hovertemplate='<b>%{x}</b><br>Response Time: %{y} min<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title=dict(
            text="Average Response Times",
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
            title="Minutes",
            title_font=dict(color='white')
        ),
        height=400,
        margin=dict(l=40, r=40, t=80, b=40)
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# City Summary Panel
st.markdown("## 📋 Operational Summary")

st.markdown("""
<div class="info-panel">
<h3>📌 Current City Status - All Systems Operational</h3>
<br>

<span class="status-badge badge-warning">🚦 Traffic Monitoring Active</span>
<span class="status-badge badge-success">🌱 Air Quality Stable</span>
<span class="status-badge badge-success">🚨 Emergency Services Ready</span>
<span class="status-badge badge-info">🚇 Metro 98% Capacity</span>

<br><br>

<strong>📊 Today's Highlights:</strong>
<ul>
<li><strong>Traffic:</strong> Morning rush hour peak at 9:15 AM with 78% congestion in downtown area</li>
<li><strong>Environment:</strong> PM2.5 levels decreased by 12% compared to yesterday</li>
<li><strong>Public Transport:</strong> Metro ridership increased by 15% this week</li>
<li><strong>Safety:</strong> Response time improved to 4.2 minutes (target: 5 min)</li>
<li><strong>Citizen Engagement:</strong> 847 service requests processed today, 94% satisfaction rate</li>
</ul>

<strong>⚠️ Attention Required:</strong>
<ul>
<li>Construction on Main Street causing 20% traffic delay - estimated completion in 3 days</li>
<li>Air quality expected to worsen in evening due to weather conditions</li>
<li>Schedule maintenance for traffic signals in Zone 3 this weekend</li>
</ul>

<strong>✅ Recent Achievements:</strong>
<ul>
<li>Successfully reduced average traffic congestion by 8% this month</li>
<li>Implemented new smart parking system in 15 locations</li>
<li>Citizen satisfaction with digital services at 92% (up from 87%)</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Quick Actions
st.markdown("## ⚡ Quick Actions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🚨 View Alerts", use_container_width=True):
        st.info("No critical alerts at this time")

with col2:
    if st.button("📊 Generate Report", use_container_width=True):
        st.success("Report generation initiated...")

with col3:
    if st.button("🔍 Analyze Trends", use_container_width=True):
        st.info("Opening trend analysis...")

with col4:
    if st.button("📈 Export Data", use_container_width=True):
        st.success("Data export started...")

st.markdown("---")

# Recent Activity Timeline
st.markdown("## 🕐 Recent System Activity")

st.markdown("""
<div class="info-panel">
<ul style="list-style: none; padding-left: 0;">
<li style="padding: 0.5rem 0; border-left: 3px solid #4CAF50; padding-left: 1rem; margin-bottom: 0.5rem;">
<strong>10:45 AM</strong> - Traffic signal optimization completed in Zone 7
</li>
<li style="padding: 0.5rem 0; border-left: 3px solid #2196F3; padding-left: 1rem; margin-bottom: 0.5rem;">
<strong>10:30 AM</strong> - Air quality sensor network updated successfully
</li>
<li style="padding: 0.5rem 0; border-left: 3px solid #FFC107; padding-left: 1rem; margin-bottom: 0.5rem;">
<strong>10:15 AM</strong> - 23 citizen feedback entries processed
</li>
<li style="padding: 0.5rem 0; border-left: 3px solid #4CAF50; padding-left: 1rem; margin-bottom: 0.5rem;">
<strong>10:00 AM</strong> - Traffic prediction model updated with new data
</li>
<li style="padding: 0.5rem 0; border-left: 3px solid #2196F3; padding-left: 1rem; margin-bottom: 0.5rem;">
<strong>09:45 AM</strong> - Emergency response drill completed successfully
</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="text-align: center; padding: 1rem 0; color: rgba(0, 0, 0, 0.45);">
<p>🔄 Dashboard auto-refreshes every 5 minutes | Last updated: Just now</p>
</div>
""", unsafe_allow_html=True)