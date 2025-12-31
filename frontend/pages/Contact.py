import streamlit as st

st.markdown("""
    <style>
    .contact-header {
        text-align: center;
        padding: 2rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .contact-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .contact-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.3);
        background: rgba(255, 255, 255, 0.08);
    }
    
    .contact-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
    }
    
    .social-button {
        display: inline-block;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 0.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        text-decoration: none;
        color: white;
    }
    
    .social-button:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    .info-box {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid #667eea;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="contact-header">', unsafe_allow_html=True)
st.title("📞 Contact Us")
st.markdown("### Get in Touch with CitySense360")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Contact Information Section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="contact-card">
        <span class="contact-icon">📧</span>
        <h3 style="text-align: center;">Email</h3>
        <p style="text-align: center;">
            <strong>General Inquiries:</strong><br>
            smartcity@urbanpulse.ai<br><br>
            <strong>Technical Support:</strong><br>
            support@citysense360.ai<br><br>
            <strong>Sales:</strong><br>
            sales@citysense360.ai
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-card">
        <span class="contact-icon">📍</span>
        <h3 style="text-align: center;">Location</h3>
        <p style="text-align: center;">
            <strong>Headquarters:</strong><br>
            Smart City Innovation Hub<br>
            Bangalore, Karnataka<br>
            India - 560001<br><br>
            <strong>Regional Office:</strong><br>
            Delhi NCR, India
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="contact-card">
        <span class="contact-icon">📱</span>
        <h3 style="text-align: center;">Phone</h3>
        <p style="text-align: center;">
            <strong>Main Office:</strong><br>
            +91 80 1234 5678<br><br>
            <strong>Support Line:</strong><br>
            +91 80 8765 4321<br><br>
            <strong>Hours:</strong><br>
            Mon-Fri: 9 AM - 6 PM IST
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Quick Contact Form Section
st.markdown("## 💬 Send Us a Message")

st.markdown('<div class="contact-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Your Name", placeholder="John Doe")
    email = st.text_input("Email Address", placeholder="john@example.com")
    
with col2:
    phone = st.text_input("Phone Number", placeholder="+91 98765 43210")
    subject = st.selectbox(
        "Subject",
        ["General Inquiry", "Technical Support", "Sales", "Partnership", "Demo Request", "Other"]
    )

message = st.text_area("Message", placeholder="Tell us how we can help you...", height=150)

if st.button("📤 Send Message", use_container_width=True):
    if name and email and message:
        st.success("✅ Thank you! Your message has been received. We'll get back to you within 24 hours.")
    else:
        st.error("⚠️ Please fill in all required fields (Name, Email, and Message)")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Social Media & Links
st.markdown("## 🌐 Connect With Us")

st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <a class="social-button" href="#" target="_blank">🔗 LinkedIn</a>
    <a class="social-button" href="#" target="_blank">🐦 Twitter</a>
    <a class="social-button" href="#" target="_blank">📘 Facebook</a>
    <a class="social-button" href="#" target="_blank">💻 GitHub</a>
    <a class="social-button" href="#" target="_blank">📺 YouTube</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Support & Resources
st.markdown("## 🎯 Support & Resources")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-box">
    <h3>📚 Documentation</h3>
    Access our comprehensive guides, API documentation, and tutorials to get the most out of CitySense360.
    
    <ul>
    <li>Getting Started Guide</li>
    <li>API Reference</li>
    <li>Video Tutorials</li>
    <li>Best Practices</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <h3>🤝 Partnership Opportunities</h3>
    Interested in partnering with us? We collaborate with:
    
    <ul>
    <li>Municipal Governments</li>
    <li>Technology Providers</li>
    <li>Research Institutions</li>
    <li>Smart City Initiatives</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
    <h3>🎓 Training & Workshops</h3>
    We offer comprehensive training programs for your team:
    
    <ul>
    <li>Platform Onboarding</li>
    <li>Data Analytics Training</li>
    <li>Custom Workshops</li>
    <li>Certification Programs</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <h3>💼 Careers</h3>
    Join our mission to build smarter cities:
    
    <ul>
    <li>AI/ML Engineers</li>
    <li>Data Scientists</li>
    <li>Full Stack Developers</li>
    <li>Urban Planning Experts</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# FAQ Section
st.markdown("## ❓ Frequently Asked Questions")

with st.expander("🔍 What is CitySense360?"):
    st.markdown("""
    CitySense360 is an AI-powered smart city analytics platform that combines machine learning, 
    natural language processing, and predictive analytics to help cities make data-driven decisions 
    for traffic management, environmental monitoring, and citizen services.
    """)

with st.expander("🚀 How can I get started?"):
    st.markdown("""
    Getting started is easy! Contact our sales team for a personalized demo, or explore our 
    documentation to understand the platform capabilities. We offer flexible deployment options 
    including cloud-based and on-premise solutions.
    """)

with st.expander("💰 What are the pricing options?"):
    st.markdown("""
    We offer flexible pricing based on city size, features required, and deployment model. 
    Contact our sales team for a customized quote. We also provide pilot programs for municipalities 
    interested in testing the platform.
    """)

with st.expander("🔒 How secure is the platform?"):
    st.markdown("""
    Security is our top priority. We employ enterprise-grade encryption, regular security audits, 
    role-based access control, and comply with international data protection standards including 
    GDPR and ISO 27001.
    """)

with st.expander("🛠️ Do you provide technical support?"):
    st.markdown("""
    Yes! We offer 24/7 technical support for all enterprise clients, along with dedicated account 
    managers, regular system health checks, and proactive monitoring to ensure optimal performance.
    """)

st.markdown("---")

# Office Hours & Availability
st.markdown("## 🕐 Office Hours & Availability")

st.markdown("""
<div class="contact-card">
<div style="text-align: center;">

**Support is available when you need it most**

📞 **Phone Support:** Monday - Friday, 9:00 AM - 6:00 PM IST  
💬 **Live Chat:** Monday - Saturday, 8:00 AM - 8:00 PM IST  
📧 **Email Support:** 24/7 (Response within 24 hours)  
🚨 **Emergency Hotline:** 24/7 for Critical Issues  

</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: rgba(0, 0, 0, 0.45);">
    <p><strong>🏙️ CitySense360 AI - Building Smarter Cities</strong></p>
    <p>🌍 Serving smart city initiatives across India and beyond</p>
    <p>🚀 Powered by Advanced AI & Machine Learning Technologies</p>
    <p style="margin-top: 1rem;">© 2024 CitySense360. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)