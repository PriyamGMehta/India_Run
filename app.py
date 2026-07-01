import streamlit as st

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(
    page_title="Talent Intelligence Platform",
    layout="wide"
)

import pandas as pd
from candidates_df import hidden_talent_score
from candidates_df import compare_candidates
from candidates_df import recommend_candidates
from candidates_df import create_segments
from talent_score_breakdown import get_score_breakdown
from load_data import load_all_data
from feature_engineering import master_df
from market_value_predictor import train_market_model
@st.cache_resource
def load_market_model():
    return train_market_model(master_df.fillna(0))

market_model = load_market_model()
from agentic_recruiter import generate_outreach_email


# ======================================
# LOAD DATA
# ======================================

(
    candidates_df,
    career_df,
    skills_df,
    certifications_df,
    education_df,
    languages_df,
    signals_df,
    assessments_df
) = load_all_data()



st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: left; background: -webkit-linear-gradient(45deg, #0f172a, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; margin-bottom: 5px; font-size: 42px; margin-top: 0;'>
        Talent Intelligence Platform
    </h1>
    <hr style='border-top: 2px solid #e2e8f0; margin-top: 0px; margin-bottom: 25px;'>
""", unsafe_allow_html=True)

# ======================================
# TOP NAVIGATION BAR
# ======================================

with st.sidebar:
    # Premium Custom Logo
    st.markdown('''
    <div style="display: flex; align-items: center; gap: 15px; padding: 10px 0 30px 0;">
        <div style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); border-radius: 14px; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; color: white; font-size: 22px; font-weight: 900; box-shadow: 0 4px 15px rgba(59,130,246,0.3);">⚡</div>
        <div style="font-size: 24px; font-weight: 900; color: #0f172a; letter-spacing: -0.5px; font-family: 'Inter', sans-serif;">Talent OS</div>
    </div>
    ''', unsafe_allow_html=True)
    
    from streamlit_option_menu import option_menu
    
    is_dark = st.session_state.get("dark_mode", False)
    
    app_mode_styles = {
        "container": {"padding": "6px", "background-color": "#1e293b" if is_dark else "#f1f5f9", "border-radius": "16px", "margin-bottom": "20px", "border": "1px solid #334155" if is_dark else "1px solid #e2e8f0", "box-shadow": "0 0 0 100px #1e293b" if is_dark else "none"},
        "icon": {"display": "none"},
        "nav-link": {"font-size": "13px", "font-weight": "600", "font-family": "'Inter', sans-serif", "text-align": "center", "margin":"0px", "padding": "10px 0px", "--hover-color": "#334155" if is_dark else "#e2e8f0", "color": "#cbd5e1" if is_dark else "#64748b"},
        "nav-link-selected": {"background-color": "#0f172a" if is_dark else "white", "color": "#ffffff" if is_dark else "#0f172a", "font-weight": "800", "box-shadow": "0 2px 6px rgba(0,0,0,0.2)" if is_dark else "0 2px 6px rgba(0,0,0,0.06)", "border-radius": "12px"},
    }
    
    # iOS-style segmented control
    app_mode = option_menu(
        menu_title=None,
        options=["📂 Data", "🤖 Dashboard"],
        icons=["", ""],
        default_index=1,
        orientation="horizontal",
        styles=app_mode_styles
    )
    
    if app_mode == "🤖 Dashboard":
        st.markdown('<div style="font-size: 11px; font-weight: 800; color: #94a3b8; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 10px; margin-bottom: 10px; padding-left: 16px; font-family: \'Inter\', sans-serif;">Analytics Menu</div>', unsafe_allow_html=True)
        
        dashboard_menu_styles = {
            "container": {"padding": "0px", "background-color": "#1e293b" if is_dark else "transparent", "box-shadow": "0 0 0 100px #1e293b" if is_dark else "none"},
            "icon": {"display": "none"},
            "nav-link": {
                "font-size": "14px", "font-weight": "600", "font-family": "'Inter', sans-serif", "text-align": "left", 
                "margin":"4px 0", "padding": "12px 16px", 
                "--hover-color": "#334155" if is_dark else "#f1f5f9", "color": "#cbd5e1" if is_dark else "#475569", 
                "border-radius": "12px", "transition": "all 0.2s ease"
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg, #3b82f6, #2563eb)", 
                "color": "white", "font-weight": "700", 
                "box-shadow": "0 4px 12px rgba(37,99,235,0.25)"
            },
        }
        
        selected_tab = option_menu(
            menu_title=None,
            options=["📊 Dashboard", "👤 Profile", "🎯 Hidden Talent", "🏆 Top Candidates", "🛠 Skills Analytics", "⚖ Comparison", "🤖 Recommendation", "🧠 Semantic Match", "📌 Segments", "⭐ Score Breakdown", "🤖 AI Copilot", "📄 JD Match"],
            icons=["", "", "", "", "", "", "", "", "", "", "", ""],
            default_index=0,
            orientation="vertical",
            styles=dashboard_menu_styles
        )
    else:
        st.markdown('<div style="font-size: 11px; font-weight: 800; color: #94a3b8; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 10px; margin-bottom: 10px; padding-left: 16px; font-family: \'Inter\', sans-serif;">Data Sources</div>', unsafe_allow_html=True)
        
        data_menu_styles = {
            "container": {"padding": "0px", "background-color": "#1e293b" if is_dark else "transparent", "box-shadow": "0 0 0 100px #1e293b" if is_dark else "none"},
            "icon": {"display": "none"},
            "nav-link": {
                "font-size": "14px", "font-weight": "600", "font-family": "'Inter', sans-serif", "text-align": "left", 
                "margin":"4px 0", "padding": "12px 16px", 
                "--hover-color": "#334155" if is_dark else "#f1f5f9", "color": "#cbd5e1" if is_dark else "#475569", 
                "border-radius": "12px", "transition": "all 0.2s ease"
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg, #8b5cf6, #7c3aed)", 
                "color": "white", "font-weight": "700", 
                "box-shadow": "0 4px 12px rgba(139,92,246,0.25)"
            },
        }
        
        selected_data_tab = option_menu(
            menu_title=None,
            options=["👥 Candidates", "💼 Career", "🛠 Skills", "🏅 Certifications", "🎓 Education", "🗣 Languages", "📈 Signals", "📋 Assessments"],
            icons=["", "", "", "", "", "", "", ""],
            default_index=0,
            orientation="vertical",
            styles=data_menu_styles
        )

    st.markdown('<hr style="margin: 20px 0; border-top: 1px dashed #cbd5e1;">', unsafe_allow_html=True)
    st.toggle("🙈 Blind Hiring Mode", key="blind_mode")
    st.toggle("🌙 Dark Mode", key="dark_mode")

    if st.session_state.get("dark_mode", False):
        st.markdown("""
        <style>
        /* Base Streamlit Theme Overrides */
        [data-testid="stAppViewContainer"] { background-color: #0f172a; color: #f8fafc; }
        [data-testid="stSidebar"] { background-color: #1e293b; }
        [data-testid="stHeader"] { background-color: transparent; }
        
        /* Streamlit Native Widgets (Inputs, Dropdowns, Text Areas, Buttons) */
        [data-baseweb="base-input"], [data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"] > div,
        div.stButton > button, div.stFormSubmitButton > button, div.stDownloadButton > button, .stButton button {
            background-color: #1e293b !important;
            border: 1px solid #334155 !important;
        }
        
        /* Ensure input text fields are transparent so they inherit the dark slate background */
        .stTextInput input, .stTextArea textarea, textarea, input, .stSelectbox [data-baseweb="select"] > div * {
            background-color: transparent !important;
            color: #f8fafc !important;
            caret-color: #f8fafc !important;
        }
        ::placeholder {
            color: #94a3b8 !important;
            opacity: 1 !important;
        }
        
        div.stButton > button, div.stFormSubmitButton > button, div.stDownloadButton > button, .stButton button {
            color: #f8fafc !important;
        }
        div.stButton > button:hover, div.stFormSubmitButton > button:hover, div.stDownloadButton > button:hover, .stButton button:hover {
            background-color: #334155 !important;
            border-color: #475569 !important;
            color: #ffffff !important;
        }
        
        /* Streamlit Pills (AI Recommendation Engine) - Dark Mode Fix */
        /* Forcing the pill labels/buttons to have a dark background and light text */
        button[data-testid="stBaseButton-pills"] {
            background-color: #1e293b !important;
            border: 1px solid #475569 !important;
        }
        button[data-testid="stBaseButton-pills"] p,
        button[data-testid="stBaseButton-pills"] div {
            color: #f8fafc !important; 
            font-weight: 600 !important;
        }
        button[data-testid="stBaseButton-pills"]:hover {
            background-color: #334155 !important;
            border: 1px solid #94a3b8 !important;
        }
        div[data-baseweb="popover"], div[data-baseweb="popover"] > div, div[data-baseweb="popover"] ul, div[data-baseweb="popover"] div { background-color: #1e293b !important; border-color: #334155 !important; }
        ul[data-baseweb="menu"], div[role="listbox"], div[role="listbox"] ul { background-color: #1e293b !important; }
        li[role="option"], div[role="option"], div[role="listbox"] li { color: #f8fafc !important; background-color: transparent !important; }
        li[role="option"]:hover, div[role="option"]:hover, div[role="listbox"] li:hover { background-color: #334155 !important; color: #ffffff !important; }
        li[role="option"] span, div[role="option"] span, div[role="listbox"] li span { color: #f8fafc !important; background-color: transparent !important; }

        /* Streamlit Native Dataframes & Tables */
        [data-testid="stDataFrame"], [data-testid="stTable"] { background-color: #1e293b !important; }
        [data-testid="stDataFrame"] div, [data-testid="stTable"] th, [data-testid="stTable"] td { color: #f8fafc !important; }

        /* Streamlit Dialogs / Modals */
        div[role="dialog"], [data-testid="stDialog"], [data-testid="stModal"], div[data-baseweb="modal"] > div {
            background-color: #1e293b !important;
            border: 1px solid #334155 !important;
        }
        div[role="dialog"] h1, div[role="dialog"] h2, div[role="dialog"] h3, div[role="dialog"] p, div[role="dialog"] div {
            color: #f8fafc !important;
        }
        div[role="dialog"] svg {
            fill: #f8fafc !important;
            color: #f8fafc !important;
        }

        /* Force all white/light custom HTML boxes to dark slate */
        div[style*="background: white"], div[style*="background: rgb(255, 255, 255)"],
        div[style*="background-color: white"], div[style*="background-color: rgb(255, 255, 255)"],
        div[style*="background: rgb(248, 249, 251)"], div[style*="background: rgb(248, 250, 252)"], div[style*="background: rgb(241, 245, 249)"],
        div[style*="background: #ffffff"], div[style*="background: #f8f9fb"], div[style*="background: #f8fafc"], div[style*="background: #f1f5f9"],
        div[style*="background-color: #ffffff"], div[style*="background-color: #f8f9fb"], div[style*="background-color: #f8fafc"], div[style*="background-color: #f1f5f9"],
        .glass-card, .bento-box, .summary-box {
            background: #1e293b !important;
            background-color: #1e293b !important;
            border-color: #334155 !important;
        }

        /* Fix the Dashboard Hero background */
        .dashboard-hero {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
            border: 1px solid #334155 !important;
        }

        /* Fix text colors globally across custom components */
        h1, h2, h3, h4, h5, p, span, div.card-value, div.card-label, div.metric-name, div.metric-val, 
        div[style*="color: #0f172a"], div[style*="color: #334155"] {
            color: #f8fafc !important;
            -webkit-text-fill-color: initial;
        }
        div[style*="color: #475569"], div[style*="color: #64748b"] { color: #94a3b8 !important; }

        /* Fix the gradient title at the top of the app */
        h1[style*="-webkit-text-fill-color: transparent"] {
            background: -webkit-linear-gradient(45deg, #f8fafc, #3b82f6) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
        }

        /* Sidebar Option Menu Fixes */
        .nav-link { color: #94a3b8 !important; }
        .nav-link-selected { color: #ffffff !important; background: linear-gradient(90deg, #3b82f6, #2563eb) !important; }

        /* Keep specific colored accents visible */
        .trend-up { color: #10b981 !important; background: rgba(16,185,129,0.15) !important; border: 1px solid rgba(16,185,129,0.2) !important; }
        .icon-blue, .pill-blue { background: rgba(59,130,246,0.15) !important; color: #3b82f6 !important; border-color: rgba(59,130,246,0.3) !important; }
        .icon-green, .pill-green { background: rgba(16,185,129,0.15) !important; color: #10b981 !important; border-color: rgba(16,185,129,0.3) !important; }
        .icon-purple, .pill-purple { background: rgba(139,92,246,0.15) !important; color: #8b5cf6 !important; border-color: rgba(139,92,246,0.3) !important; }
        .icon-orange { background: rgba(245,158,11,0.15) !important; color: #f59e0b !important; border-color: rgba(245,158,11,0.3) !important; }
        .skill-badge-adv { background: rgba(16,185,129,0.15) !important; color: #10b981 !important; border: none !important; }
        .skill-badge-int { background: rgba(59,130,246,0.15) !important; color: #3b82f6 !important; border: none !important; }
        .skill-badge-beg { background: rgba(139,92,246,0.15) !important; color: #8b5cf6 !important; border: none !important; }
        .skill-badge-oth { background: rgba(148,163,184,0.15) !important; color: #94a3b8 !important; border: none !important; }
        
        /* Ensure stPills text color is definitely white */
        button[data-testid="stBaseButton-pills"] *, 
        button[data-testid="stBaseButton-pills"] p,
        button[data-testid="stBaseButton-pills"] div {
            color: #f8fafc !important;
            -webkit-text-fill-color: #f8fafc !important;
        }
        </style>
        """, unsafe_allow_html=True)

# ======================================
# DATA REVIEW PAGE
# ======================================

if app_mode == "📂 Data":
    candidate_basic = candidates_df[
        ["candidate_id", "name"]
    ]

    pass

    # Candidates
    if "Candidates" in selected_data_tab:
        st.markdown("<h2 style='color: #0f172a; font-weight: 800; margin-bottom: 20px; font-size: 32px; font-family: \"Inter\", sans-serif;'>📂 Data Review Area</h2>", unsafe_allow_html=True)
        st.subheader("Candidate Data")
        st.dataframe(
            candidates_df,
            use_container_width=True
        )

    # Career
    if "Career" in selected_data_tab:
        st.subheader("Career Data")
        career_view = candidate_basic.merge(
            career_df,
            on="candidate_id",
            how="left"
        )
        st.dataframe(
            career_view,
            use_container_width=True
        )

    # Skills
    if "Skills" in selected_data_tab:
        st.subheader("Skills Data")
        skills_view = candidate_basic.merge(
            skills_df,
            on="candidate_id",
            how="left"
        )
        st.dataframe(
            skills_view,
            use_container_width=True
        )

    # Certifications
    if "Certifications" in selected_data_tab:
        st.subheader("Certification Data")
        cert_view = candidate_basic.merge(
            certifications_df,
            on="candidate_id",
            how="left"
        )
        st.dataframe(
            cert_view,
            use_container_width=True
        )

    # Education
    if "Education" in selected_data_tab:
        st.subheader("Education Data")
        edu_view = candidate_basic.merge(
            education_df,
            on="candidate_id",
            how="left"
        )
        st.dataframe(
            edu_view,
            use_container_width=True
        )

    # Languages
    if "Languages" in selected_data_tab:
        st.subheader("Languages Data")
        lang_view = candidate_basic.merge(
            languages_df,
            on="candidate_id",
            how="left"
        )
        st.dataframe(
            lang_view,
            use_container_width=True
        )

    # Signals
    if "Signals" in selected_data_tab:
        st.subheader("Signals Data")
        signal_view = candidate_basic.merge(
            signals_df,
            on="candidate_id",
            how="left"
        )
        st.dataframe(
            signal_view,
            use_container_width=True
        )

    # Assessments
    if "Assessments" in selected_data_tab:
        st.subheader("Assessment Data")
        assessment_view = candidate_basic.merge(
            assessments_df,
            on="candidate_id",
            how="left"
        )
        st.dataframe(
            assessment_view,
            use_container_width=True
        )


# ======================================
# TALENT DASHBOARD PAGE
# ======================================

if app_mode == "🤖 Dashboard":

    pass

    # WRITE DASHBOARD CODE HERE
    if "Dashboard" in selected_tab:

        st.markdown("<h2 style='color: #0f172a; font-weight: 800; margin-bottom: 20px; font-size: 32px; font-family: \"Inter\", sans-serif;'>🤖 Talent Intelligence Dashboard</h2>", unsafe_allow_html=True)

        m1 = len(master_df)
        m2 = round(master_df["years_of_experience"].mean(), 1)
        m3 = round(master_df["total_skills"].mean(), 1)
        m4 = round(master_df["companies_worked"].mean(), 1)
        
        # --- Advanced Glassmorphism KPI Dashboard ---
        html_cards = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
.dashboard-hero {{
background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
border-radius: 24px;
padding: 40px;
margin-bottom: 30px;
font-family: 'Outfit', sans-serif;
position: relative;
overflow: hidden;
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
}}
.dashboard-hero::before {{
content: '';
position: absolute;
top: -50%; left: -10%;
width: 500px; height: 500px;
background: radial-gradient(circle, rgba(59,130,246,0.15) 0%, rgba(255,255,255,0) 70%);
border-radius: 50%;
z-index: 0;
}}
.dashboard-hero::after {{
content: '';
position: absolute;
bottom: -50%; right: -10%;
width: 600px; height: 600px;
background: radial-gradient(circle, rgba(16,185,129,0.15) 0%, rgba(255,255,255,0) 70%);
border-radius: 50%;
z-index: 0;
}}
.hero-header {{
position: relative;
z-index: 1;
margin-bottom: 35px;
display: flex;
justify-content: space-between;
align-items: center;
}}
.hero-title {{
color: #0f172a;
font-size: 32px;
font-weight: 800;
margin: 0;
letter-spacing: -0.5px;
}}
.hero-subtitle {{
color: #475569;
font-size: 16px;
margin-top: 4px;
font-weight: 400;
}}
.status-badge {{
background: rgba(16, 185, 129, 0.15);
border: 1px solid rgba(16, 185, 129, 0.3);
color: #059669;
padding: 8px 16px;
border-radius: 20px;
font-size: 14px;
font-weight: 600;
display: flex;
align-items: center;
gap: 10px;
box-shadow: 0 0 20px rgba(16, 185, 129, 0.05);
}}
.pulse-dot {{
width: 8px;
height: 8px;
background-color: #10b981;
border-radius: 50%;
box-shadow: 0 0 10px #10b981;
animation: pulse 2s infinite;
}}
@keyframes pulse {{
0% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }}
70% {{ box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }}
100% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
}}
.kpi-grid {{
display: grid;
grid-template-columns: repeat(4, 1fr);
gap: 24px;
position: relative;
z-index: 1;
}}
.glass-card {{
background: rgba(255, 255, 255, 0.7);
backdrop-filter: blur(20px);
-webkit-backdrop-filter: blur(20px);
border: 1px solid rgba(255, 255, 255, 1);
border-radius: 20px;
padding: 24px;
transition: all 0.3s ease;
display: flex;
flex-direction: column;
justify-content: space-between;
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}}
.glass-card:hover {{
transform: translateY(-5px);
background: rgba(255, 255, 255, 0.95);
border-color: rgba(255, 255, 255, 1);
box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1);
}}
.card-header {{
display: flex;
justify-content: space-between;
align-items: flex-start;
margin-bottom: 24px;
}}
.icon-wrapper {{
width: 48px; height: 48px;
border-radius: 14px;
display: flex; align-items: center; justify-content: center;
font-size: 22px;
}}
.icon-blue {{ background: linear-gradient(135deg, rgba(59,130,246,0.15), rgba(37,99,235,0.15)); color: #2563eb; border: 1px solid rgba(59,130,246,0.2); }}
.icon-green {{ background: linear-gradient(135deg, rgba(16,185,129,0.15), rgba(5,150,105,0.15)); color: #059669; border: 1px solid rgba(16,185,129,0.2); }}
.icon-orange {{ background: linear-gradient(135deg, rgba(245,158,11,0.15), rgba(217,119,6,0.15)); color: #d97706; border: 1px solid rgba(245,158,11,0.2); }}
.icon-purple {{ background: linear-gradient(135deg, rgba(139,92,246,0.15), rgba(109,40,217,0.15)); color: #7c3aed; border: 1px solid rgba(139,92,246,0.2); }}
.trend-badge {{
font-size: 12px;
font-weight: 600;
background: rgba(0,0,0,0.05);
color: #475569;
padding: 4px 8px;
border-radius: 8px;
display: flex;
align-items: center;
gap: 4px;
}}
.trend-up {{ color: #059669; background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.2); }}
.card-value {{
font-size: 38px;
font-weight: 800;
color: #0f172a;
line-height: 1;
margin-bottom: 8px;
}}
.card-value span {{
font-size: 18px;
font-weight: 600;
color: #64748b;
margin-left: 4px;
}}
.card-label {{
font-size: 13px;
font-weight: 600;
color: #64748b;
text-transform: uppercase;
letter-spacing: 1px;
}}
@media (max-width: 1000px) {{
.kpi-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}
</style>
<div class="dashboard-hero">
<div class="hero-header">
<div>
<h2 class="hero-title">Platform Intelligence</h2>
<div class="hero-subtitle">Real-time metrics from your talent pool</div>
</div>
<div class="status-badge">
<div class="pulse-dot"></div> Live Analysis
</div>
</div>
<div class="kpi-grid">
<div class="glass-card">
<div class="card-header">
<div class="icon-wrapper icon-blue">👥</div>
<div class="trend-badge trend-up">↑ 12%</div>
</div>
<div>
<div class="card-value">{m1}</div>
<div class="card-label">Total Candidates</div>
</div>
</div>
<div class="glass-card">
<div class="card-header">
<div class="icon-wrapper icon-green">⚡</div>
<div class="trend-badge trend-up">↑ 4%</div>
</div>
<div>
<div class="card-value">{m2}<span>Yrs</span></div>
<div class="card-label">Avg Experience</div>
</div>
</div>
<div class="glass-card">
<div class="card-header">
<div class="icon-wrapper icon-orange">🎯</div>
<div class="trend-badge trend-up">↑ 8%</div>
</div>
<div>
<div class="card-value">{m3}</div>
<div class="card-label">Avg Skill Count</div>
</div>
</div>
<div class="glass-card">
<div class="card-header">
<div class="icon-wrapper icon-purple">🏢</div>
<div class="trend-badge" style="color:#64748b; border:1px solid rgba(0,0,0,0.1);">~ 0%</div>
</div>
<div>
<div class="card-value">{m4}</div>
<div class="card-label">Companies Worked</div>
</div>
</div>
</div>
</div>
"""
        st.markdown(html_cards, unsafe_allow_html=True)

    # WRITE PROFILE CODE HERE
    if "Profile" in selected_tab:

        st.header("Candidate 360° Profile")
        # =====================================
        # SEARCH SECTION
        # =====================================

        def update_name_from_id():
            selected_id = st.session_state.profile_candidate_id
            matching_name = candidates_df.loc[candidates_df["candidate_id"] == selected_id, "name"].iloc[0]
            st.session_state.profile_candidate_name = matching_name

        def update_id_from_name():
            selected_name = st.session_state.profile_candidate_name
            matching_id = candidates_df.loc[candidates_df["name"] == selected_name, "candidate_id"].iloc[0]
            st.session_state.profile_candidate_id = matching_id

        if "profile_candidate_id" not in st.session_state:
            st.session_state.profile_candidate_id = candidates_df["candidate_id"].iloc[0]
        if "profile_candidate_name" not in st.session_state:
            st.session_state.profile_candidate_name = candidates_df["name"].iloc[0]

        col1, col2 = st.columns(2)

        with col1:

            selected_candidate_id = st.selectbox(
                "Select Candidate ID",
                candidates_df["candidate_id"].unique(),
                key="profile_candidate_id",
                on_change=update_name_from_id
            )

        with col2:
            if st.session_state.get("blind_mode", False):
                st.text_input("Candidate Name", value="[HIDDEN IN BLIND MODE]", disabled=True)
            else:
                selected_candidate_name = st.selectbox(
                    "Select Candidate Name",
                    candidates_df["name"].unique(),
                    key="profile_candidate_name",
                    on_change=update_id_from_name
                )

        candidate = selected_candidate_id

        selected = master_df[
            master_df["candidate_id"] == candidate
        ]

        # =====================================
        # SELECTED RECORD
        # =====================================

        selected = master_df[
            master_df["candidate_id"] == candidate
        ]

        # ==========================
        # CALCULATIONS
        # ==========================

        hidden_score = st.session_state.get(
            "hidden_score",
            50
        )

        learning_velocity = round(
            (
                selected["avg_assessment_score"].iloc[0] * 0.25
                + selected["github_activity_score"].iloc[0] * 0.20
                + selected["profile_completeness_score"].iloc[0] * 0.15
                + selected["interview_completion_rate"].iloc[0] * 100 * 0.15
                + selected["certification_count"].iloc[0] * 5
            ),
            2
        )

        predicted_salary = round(
            selected["expected_salary"].iloc[0],
            2
        )

        talent_score = round(
            (
                hidden_score * 0.40
                + learning_velocity * 0.30
                + predicted_salary * 0.30
            ),
            2
        )

        # ==========================
        # TOP SECTION: BENTO BOX UI
        # ==========================

        candidate_info = candidates_df[
            candidates_df["candidate_id"] == candidate
        ].iloc[0]

        is_blind = st.session_state.get("blind_mode", False)
        display_name = f"Candidate {str(candidate_info['candidate_id'])[:5]}" if is_blind else candidate_info['name']
        display_location = "Confidential Location" if is_blind else f"{candidate_info['location']}, {candidate_info['country']}"

        if is_blind:
            initials = "🕵️"
        else:
            name_parts = str(candidate_info['name']).split()
            initials = "".join([p[0] for p in name_parts[:2]]).upper() if name_parts else "??"

        bento_html = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
.bento-container {{
font-family: 'Inter', sans-serif;
display: grid;
grid-template-columns: 2.5fr 1fr;
gap: 20px;
margin-bottom: 30px;
}}
.bento-box {{
background: #ffffff;
border: 1px solid #e2e8f0;
border-radius: 24px;
padding: 30px;
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
}}
.profile-header {{
display: flex;
gap: 24px;
align-items: center;
margin-bottom: 24px;
padding-bottom: 24px;
border-bottom: 1px solid #f1f5f9;
}}
.avatar-circle {{
width: 80px;
height: 80px;
border-radius: 50%;
background: linear-gradient(135deg, #f8fafc, #e2e8f0);
border: 1px solid #cbd5e1;
display: flex;
align-items: center;
justify-content: center;
font-size: 28px;
font-weight: 700;
color: #475569;
box-shadow: inset 0 2px 4px rgba(255,255,255,0.5);
flex-shrink: 0;
}}
.profile-title h1 {{
margin: 0;
font-size: 28px;
font-weight: 700;
color: #0f172a;
letter-spacing: -0.5px;
}}
.profile-title p {{
margin: 4px 0 0 0;
font-size: 16px;
color: #64748b;
font-weight: 500;
}}
.info-grid {{
display: grid;
grid-template-columns: repeat(2, 1fr);
gap: 20px;
}}
.info-item {{
display: flex;
flex-direction: column;
gap: 4px;
}}
.info-label {{
font-size: 12px;
text-transform: uppercase;
letter-spacing: 0.5px;
color: #94a3b8;
font-weight: 600;
}}
.info-value {{
font-size: 15px;
color: #334155;
font-weight: 500;
display: flex;
align-items: center;
gap: 8px;
}}
.summary-box {{
background: #f8fafc;
border-radius: 16px;
padding: 20px;
margin-top: 24px;
border-left: 4px solid #3b82f6;
}}
.summary-text {{
font-size: 14px;
line-height: 1.6;
color: #475569;
margin: 0;
}}
.snapshot-title {{
font-size: 18px;
font-weight: 700;
color: #0f172a;
margin-bottom: 20px;
display: flex;
align-items: center;
gap: 8px;
}}
.metric-stack {{
display: flex;
flex-direction: column;
gap: 16px;
}}
.metric-pill {{
border-radius: 16px;
padding: 16px 20px;
display: flex;
justify-content: space-between;
align-items: center;
transition: transform 0.2s, box-shadow 0.2s;
}}
.metric-pill:hover {{
transform: translateX(4px);
}}
.metric-info {{
display: flex;
flex-direction: column;
gap: 4px;
}}
.metric-name {{
font-size: 13px;
font-weight: 600;
}}
.metric-val {{
font-size: 20px;
font-weight: 700;
}}
.metric-icon {{
width: 40px; height: 40px;
border-radius: 12px;
display: flex; align-items: center; justify-content: center;
font-size: 18px;
background: rgba(255,255,255,0.2);
}}
.pill-blue {{ background: #eff6ff; box-shadow: 0 4px 12px rgba(59,130,246,0.05); border: 1px solid #dbeafe; }}
.pill-blue .metric-name {{ color: #64748b; }}
.pill-blue .metric-val {{ color: #1e3a8a; }}
.pill-blue span {{ color: #3b82f6 !important; }}
.pill-blue .metric-icon {{ background: #ffffff; box-shadow: 0 2px 4px rgba(59,130,246,0.1); }}

.pill-green {{ background: #ecfdf5; box-shadow: 0 4px 12px rgba(16,185,129,0.05); border: 1px solid #d1fae5; }}
.pill-green .metric-name {{ color: #64748b; }}
.pill-green .metric-val {{ color: #064e3b; }}
.pill-green span {{ color: #10b981 !important; }}
.pill-green .metric-icon {{ background: #ffffff; box-shadow: 0 2px 4px rgba(16,185,129,0.1); }}

.pill-purple {{ background: #f5f3ff; box-shadow: 0 4px 12px rgba(139,92,246,0.05); border: 1px solid #ede9fe; }}
.pill-purple .metric-name {{ color: #64748b; }}
.pill-purple .metric-val {{ color: #4c1d95; }}
.pill-purple span {{ color: #8b5cf6 !important; }}
.pill-purple .metric-icon {{ background: #ffffff; box-shadow: 0 2px 4px rgba(139,92,246,0.1); }}

@media (max-width: 1000px) {{
.bento-container {{ grid-template-columns: 1fr; }}
.info-grid {{ grid-template-columns: 1fr; }}
}}
</style>
<div class="bento-container">
<div class="bento-box">
<div class="profile-header">
<div class="avatar-circle">{initials}</div>
<div class="profile-title">
<h1>{display_name}</h1>
<p>{candidate_info['headline']}</p>
</div>
</div>
<div class="info-grid" style="grid-template-columns: repeat(3, 1fr);">
<div class="info-item">
<span class="info-label">Current Role</span>
<span class="info-value">💼 {candidate_info['current_title']}</span>
</div>
<div class="info-item">
<span class="info-label">Company</span>
<span class="info-value">🏢 {candidate_info['current_company']}</span>
</div>
<div class="info-item">
<span class="info-label">Company Size</span>
<span class="info-value">👥 {candidate_info['current_company_size']}</span>
</div>
<div class="info-item">
<span class="info-label">Location</span>
<span class="info-value">📍 {display_location}</span>
</div>
<div class="info-item">
<span class="info-label">Experience</span>
<span class="info-value">⏳ {candidate_info['years_of_experience']} Years</span>
</div>
<div class="info-item">
<span class="info-label">Industry</span>
<span class="info-value">🏭 {candidate_info['current_industry']}</span>
</div>
</div>
<div class="summary-box">
<p class="summary-text">{candidate_info['summary']}</p>
</div>
</div>
<div class="bento-box">
<div class="snapshot-title">🎯 Talent Snapshot</div>
<div class="metric-stack">
<div class="metric-pill pill-blue">
<div class="metric-info">
<span class="metric-name">Learning Velocity</span>
<span class="metric-val">{learning_velocity} <span style="font-size:14px;">/ 100</span></span>
</div>
<div class="metric-icon">🚀</div>
</div>
<div class="metric-pill pill-green">
<div class="metric-info">
<span class="metric-name">Predicted Salary</span>
<span class="metric-val">₹{predicted_salary} <span style="font-size:14px;">LPA</span></span>
</div>
<div class="metric-icon">💰</div>
</div>
<div class="metric-pill pill-purple">
<div class="metric-info">
<span class="metric-name">Talent Score</span>
<span class="metric-val">{talent_score}</span>
</div>
<div class="metric-icon">⭐</div>
</div>
</div>
</div>
</div>
"""
        st.markdown(bento_html, unsafe_allow_html=True)

        # ==========================
        # SKILLS
        # ==========================

        st.subheader("Skills")

        candidate_skills = skills_df[
            skills_df["candidate_id"] == candidate
        ].drop(columns=["candidate_id"], errors="ignore")

        if not candidate_skills.empty:
            html = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px;">'
            for _, row in candidate_skills.iterrows():
                skill = str(row.get("skill_name", "Skill"))
                prof = str(row.get("proficiency", "Unknown")).capitalize()
                end = int(row.get("endorsements", 0))
                dur = int(row.get("duration_months", 0))
                
                if prof.lower() == 'advanced':
                    badge_bg, badge_txt = "#dcfce7", "#166534"
                    badge_class = "skill-badge-adv"
                elif prof.lower() == 'intermediate':
                    badge_bg, badge_txt = "#dbeafe", "#1e40af"
                    badge_class = "skill-badge-int"
                elif prof.lower() == 'beginner':
                    badge_bg, badge_txt = "#f3e8ff", "#6b21a8"
                    badge_class = "skill-badge-beg"
                else:
                    badge_bg, badge_txt = "#f1f5f9", "#475569"
                    badge_class = "skill-badge-oth"

                html += f"""<div style="background: white; border: 1px solid #e2e8f0; border-radius: 20px; padding: 6px 14px; display: flex; align-items: center; gap: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
<span style="font-weight: 600; font-size: 14px; color: #1e293b;">{skill}</span>
<span class="{badge_class}" style="background: {badge_bg}; color: {badge_txt}; font-size: 11px; font-weight: bold; padding: 2px 8px; border-radius: 10px;">{prof[:3].upper()}</span>
<div style="width: 1px; height: 14px; background: #cbd5e1;"></div>
<span style="font-size: 12px; color: #64748b; font-weight: 500;">{dur}m</span>
<div style="width: 1px; height: 14px; background: #cbd5e1;"></div>
<span style="font-size: 12px; color: #64748b; font-weight: 500;">⭐ {end}</span>
</div>"""
            html += '</div>'
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.info("No skills found.")

        # ==========================
        # EDUCATION
        # ==========================

        is_dark = st.session_state.get("dark_mode", False)
        text_main = "#f8fafc" if is_dark else "#0f172a"
        text_muted = "#94a3b8" if is_dark else "#475569"
        card_bg = "#1e293b" if is_dark else "#f8f9fb"
        border_color = "#334155" if is_dark else "#e6e9ef"
        lang_card_bg = "#1e293b" if is_dark else "#ffffff"

        st.subheader("Education")

        candidate_education = education_df[
            education_df["candidate_id"] == candidate
        ].drop(columns=["candidate_id"], errors="ignore")

        if not candidate_education.empty:
            for _, row in candidate_education.iterrows():
                st.markdown(f"""
                <div style="border: 1px solid {border_color}; border-radius: 8px; padding: 16px; margin-bottom: 12px; background-color: {card_bg}; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                    <h4 style="margin: 0; color: {text_main};">🎓 {row['degree']} in {row['field_of_study']}</h4>
                    <p style="margin: 6px 0 0 0; font-size: 16px; color: {text_main};"><strong>{row['institution']}</strong> <span style="color: {text_muted};">({row.get('tier', 'N/A')})</span></p>
                    <p style="margin: 6px 0 0 0; font-size: 14px; color: {text_muted};">
                        📅 {row['start_year']} - {row['end_year']} &nbsp;|&nbsp; 🏆 Grade: <strong>{row['grade']}</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No education records found.")

        # ==========================
        # CERTIFICATIONS
        # ==========================

        st.subheader("Certifications")

        candidate_certifications = certifications_df[
            certifications_df["candidate_id"] == candidate
        ].drop(columns=["candidate_id"], errors="ignore")

        if not candidate_certifications.empty:
            for _, row in candidate_certifications.iterrows():
                st.markdown(f"""
                <div style="border: 1px solid {border_color}; border-radius: 8px; padding: 16px; margin-bottom: 12px; background-color: {card_bg}; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                    <h4 style="margin: 0; color: {text_main};">📜 {row.get('name', '')}</h4>
                    <p style="margin: 6px 0 0 0; font-size: 16px; color: {text_main};"><strong>{row.get('issuer', '')}</strong></p>
                    <p style="margin: 6px 0 0 0; font-size: 14px; color: {text_muted};">
                        📅 Year: <strong>{row.get('year', '')}</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No certifications found.")

        # ==========================
        # LANGUAGES
        # ==========================

        st.subheader("Languages")

        candidate_languages = languages_df[
            languages_df["candidate_id"] == candidate
        ].drop(columns=["candidate_id"], errors="ignore")

        if not candidate_languages.empty:
            lang_html = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px; margin-bottom: 20px;">'
            for _, row in candidate_languages.iterrows():
                lang = str(row.get('language', ''))
                prof = str(row.get('proficiency', '')).capitalize()
                prof_lower = prof.lower()
                
                if prof_lower in ['native', 'fluent', 'bilingual']: width = 100
                elif prof_lower in ['professional', 'advanced']: width = 75
                elif prof_lower in ['conversational', 'intermediate']: width = 50
                else: width = 25
                
                lang_html += f"""
<div style="background: {lang_card_bg}; border: 1px solid {border_color}; border-radius: 12px; padding: 16px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
<div style="display: flex; align-items: center; gap: 8px;">
<div style="background: linear-gradient(135deg, #e0e7ff, #c7d2fe); color: #4f46e5; width: 26px; height: 26px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 13px;">🗣️</div>
<span style="font-weight: 700; color: {text_main}; font-size: 14px;">{lang}</span>
</div>
<span style="color: {text_muted}; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">{prof}</span>
</div>
<div style="width: 100%; background: {border_color}; border-radius: 999px; height: 6px; overflow: hidden; box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);">
<div style="width: {width}%; height: 100%; background: linear-gradient(90deg, #3b82f6, #6366f1); border-radius: 999px;"></div>
</div>
</div>
"""
            lang_html += '</div>'
            st.markdown(lang_html, unsafe_allow_html=True)
        else:
            st.info("No languages found.")

        # ==========================
        # ASSESSMENTS
        # ==========================

        st.subheader("Assessments")

        candidate_assessment = assessments_df[
            assessments_df["candidate_id"] == candidate
        ].drop(columns=["candidate_id"], errors="ignore")

        if not candidate_assessment.empty:
            html = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px;">'
            for _, row in candidate_assessment.iterrows():
                score = float(row.get('score', 0))
                skill = row.get('skill', '')
                
                if score >= 80: color = "#10b981" # Green
                elif score >= 60: color = "#f59e0b" # Orange
                else: color = "#ef4444" # Red
                
                html += f"""<div style="background-color: {card_bg}; border: 1px solid {border_color}; border-radius: 8px; padding: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
<div style="display: flex; justify-content: space-between; margin-bottom: 10px; align-items: center;">
<span style="font-weight: 600; color: {text_main}; font-size: 15px;">{skill}</span>
<span style="font-weight: 700; color: {color}; font-size: 16px;">{score:.1f}%</span>
</div>
<div style="width: 100%; background-color: {border_color}; border-radius: 6px; height: 8px; overflow: hidden;">
<div style="background-color: {color}; width: {score}%; height: 100%; border-radius: 6px;"></div>
</div>
</div>"""
            html += '</div>'
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.info("No assessments found.")
        
    # with tab_profile:

    #     st.header("Candidate 360° Profile")

    #     candidate = st.selectbox(
    #         "Select Candidate",
    #         candidates_df["candidate_id"].unique(),
    #         key="profile_candidate"
    #     )

    #     selected = master_df[
    #         master_df["candidate_id"] == candidate
    #     ]

    #     # -----------------------
    #     # Candidate Info
    #     # -----------------------

    #     candidate_info = candidates_df[
    #         candidates_df["candidate_id"] == candidate
    #     ]

    #     st.subheader("Personal Information")

    #     st.dataframe(
    #         candidate_info.drop(columns=["candidate_id"]),
    #         use_container_width=True
    #     )

    #     # -----------------------
    #     # Skills
    #     # -----------------------

    #     st.subheader("Skills")

    #     candidate_skills = skills_df[
    #         skills_df["candidate_id"] == candidate
    #     ]

    #     st.dataframe(
    #         candidate_skills.drop(columns=["candidate_id"]),
    #         use_container_width=True
    #     )

    #     # -----------------------
    #     # Education
    #     # -----------------------

    #     st.subheader("Education")

    #     candidate_education = education_df[
    #         education_df["candidate_id"] == candidate
    #     ]

    #     st.dataframe(
    #         candidate_education.drop(columns=["candidate_id"]),
    #         use_container_width=True
    #     )

    #     # -----------------------
    #     # Certifications
    #     # -----------------------

    #     st.subheader("Certifications")

    #     candidate_certifications = certifications_df[
    #         certifications_df["candidate_id"] == candidate
    #     ]

    #     st.dataframe(
    #         candidate_certifications.drop(columns=["candidate_id"]),
    #         use_container_width=True
    #     )

    #     # -----------------------
    #     # Languages
    #     # -----------------------

    #     st.subheader("Languages")

    #     candidate_languages = languages_df[
    #         languages_df["candidate_id"] == candidate
    #     ]

    #     st.dataframe(
    #         candidate_languages.drop(columns=["candidate_id"]),
    #         use_container_width=True
    #     )


    #     # -----------------------
    #     # Assessments
    #     # -----------------------

    #     st.subheader("Assessments")

    #     candidate_assessment = assessments_df[
    #         assessments_df["candidate_id"] == candidate
    #     ]

    #     st.dataframe(
    #         candidate_assessment.drop(columns=["candidate_id"]),
    #         use_container_width=True
    #     )
        

    # WRITE HIDDEN TALENT CODE HERE
    if "Hidden Talent" in selected_tab:
        is_dark = st.session_state.get("dark_mode", False)
        text_main = "#f8fafc" if is_dark else "#0f172a"
        text_muted = "#94a3b8" if is_dark else "#64748b"
        card_bg = "#1e293b" if is_dark else "#f8fafc"
        border_color = "#334155" if is_dark else "#e2e8f0"
        
        st.markdown(f"""<div style="background-color: {card_bg}; border: 1px solid {border_color}; border-radius: 12px; padding: 24px; margin-bottom: 20px;">
<div style="display: flex; align-items: center; gap: 16px;">
<div style="background: #3b82f6; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 4px 6px rgba(59, 130, 246, 0.2);">🕵️‍♀️</div>
<div>
<h3 style="margin: 0; color: {text_main}; font-size: 20px; font-weight: 700;">AI Hidden Talent Scanner</h3>
<p style="margin: 4px 0 0 0; color: {text_muted}; font-size: 14px;">Uncover invisible synergies. Paste the target job description below, and our AI will calculate a hidden match score based on the candidate's latent skills.</p>
</div>
</div>
</div>""", unsafe_allow_html=True)
        options = []
        for _, r in master_df.iterrows():
            options.append(f"{r.get('name', 'Unknown')} ({r['candidate_id']})")
            
        selected_option = st.selectbox("Select Candidate to Analyze", options, key="hidden_talent_candidate")
        selected_id = selected_option.split("(")[-1].replace(")", "").strip()
        selected = master_df[master_df["candidate_id"] == selected_id]
        
        job_description = st.text_area(
            "🎯 Target Job Description",
            height=150,
            placeholder="Paste the full job description here..."
        )
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            calculate_btn = st.button("✨ Run AI Match Analysis", use_container_width=True)

        if calculate_btn:
            with st.spinner("Analyzing profile synapses..."):
                candidate_profile = (
                    str(selected["headline"].iloc[0])
                    + " "
                    + str(selected["summary"].iloc[0])
                )

                score = hidden_talent_score(
                    job_description,
                    candidate_profile
                )
                score = round(score, 2)
                
                color = "#10b981" if score >= 75 else "#f59e0b" if score >= 50 else "#ef4444"
                
                is_dark = st.session_state.get("dark_mode", False)
                empty_color = "#334155" if is_dark else "#f1f5f9"
                card_bg = "#1e293b" if is_dark else "white"
                border_color = "#334155" if is_dark else "#e2e8f0"
                text_main = "#f8fafc" if is_dark else "#334155"
                text_score = "#f8fafc" if is_dark else "#0f172a"
                
                st.markdown(f"""
<style>
.ai-match-card {{ background: {card_bg}; border: 1px solid {border_color}; border-radius: 16px; padding: 30px; text-align: center; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); width: 100%; max-width: 400px; }}
.ai-match-ring {{ position: relative; width: 150px; height: 150px; border-radius: 50%; background: conic-gradient({color} {score:.2f}%, {empty_color} 0); margin: 0 auto; display: flex; align-items: center; justify-content: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.1); }}
.ai-match-inner {{ width: 120px; height: 120px; background: {card_bg}; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}
</style>
<div style="display: flex; justify-content: center; margin-top: 30px;">
<div class="ai-match-card">
<div style="font-size: 14px; color: #94a3b8; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px;">Match Result</div>
<div class="ai-match-ring">
<div class="ai-match-inner">
<span style="font-size: 32px; font-weight: 800; color: {text_score};">{score:.2f}</span>
<span style="font-size: 12px; color: #94a3b8; font-weight: 600;">SCORE</span>
</div>
</div>
<div style="margin-top: 20px; color: {text_main}; font-size: 15px; line-height: 1.5;">
The candidate's profile has a <strong>{score:.2f}%</strong> latent synergy with the target role.
</div>
</div>
</div>""", unsafe_allow_html=True)
                
                st.session_state['hidden_score'] = score
        
    # # WRITE LEARNING CODE HERE
    # with tab_learning:
    #     st.subheader("Learning Velocity")
        
    #     learning_velocity = round(
    #         (
    #             selected["avg_assessment_score"].iloc[0] * 0.25
    #             + selected["github_activity_score"].iloc[0] * 0.20
    #             + selected["profile_completeness_score"].iloc[0] * 0.15
    #             + selected["interview_completion_rate"].iloc[0] * 100 * 0.15
    #             + selected["certification_count"].iloc[0] * 5
    #         ),
    #         2
    #     )

    #     st.metric(
    #         "Learning Velocity",
    #         f"{learning_velocity}/100"
    #     )

    # # WRITE MARKET VALUE CODE HERE
    # with tab_market:
    #     st.subheader("Market Value Prediction")
        
    #     predicted_salary = round(
    #         selected["expected_salary"].iloc[0],
    #         2
    #     )
        
    #     st.metric(
    #         "Predicted Salary",
    #         f"₹{predicted_salary} LPA"
    #     )
        
    # # WRITE TALENT SCORE CODE HERE
    # with tab_talent:
    #     st.subheader("Talent Intelligence Score")
        
    #     hidden_score = st.session_state.get('hidden_score', 50)
        
    #     # We recalculate these locally to ensure they're available even if tabs weren't fully clicked
    #     learning_velocity = round(
    #         (
    #             selected["avg_assessment_score"].iloc[0] * 0.25
    #             + selected["github_activity_score"].iloc[0] * 0.20
    #             + selected["profile_completeness_score"].iloc[0] * 0.15
    #             + selected["interview_completion_rate"].iloc[0] * 100 * 0.15
    #             + selected["certification_count"].iloc[0] * 5
    #         ),
    #         2
    #     )
        
    #     predicted_salary = round(selected["expected_salary"].iloc[0], 2)
        
    #     talent_score = round(
    #         (
    #             hidden_score * 0.40
    #             + learning_velocity * 0.30
    #             + predicted_salary * 0.30
    #         ),
    #         2
    #     )
        
    #     st.metric(
    #         "Talent Score",
    #         talent_score
    #     )        

    # WRITE TOP CANDIDATES CODE HERE
    if "Top Candidates" in selected_tab:
        st.markdown('<h2 style="color: #0f172a; margin-bottom: 20px;">🏆 Top Candidates Leaderboard</h2>', unsafe_allow_html=True)
        
        master_df["talent_score"] = (
            master_df["avg_assessment_score"].fillna(0)
            + master_df["github_activity_score"].fillna(0)
            + master_df["profile_completeness_score"].fillna(0)
        )

        ranked_df = master_df.sort_values("talent_score", ascending=False)
        ranked_top = ranked_df.head(10)
        
        # --- Functional Enterprise SaaS List View ---
        st.markdown('<p style="color: #64748b; margin-bottom: 20px; font-weight: 500; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Enterprise Leaderboard</p>', unsafe_allow_html=True)
        
        # Inject custom CSS for the Review buttons
        st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            background-color: #eff6ff;
            color: #2563eb;
            border: none;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            padding: 4px 12px;
            min-height: 32px;
        }
        div[data-testid="stButton"] > button:hover {
            background-color: #dbeafe;
            color: #1d4ed8;
            border: none;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Handle review state
        if "review_candidate" in st.session_state:
            cid = st.session_state["review_candidate"]
            cand_data = master_df[master_df["candidate_id"] == cid]
            if not cand_data.empty:
                rev_name = f"Candidate {str(cid)[:5]}" if st.session_state.get("blind_mode", False) else cand_data.iloc[0]['name']
                st.info(f"📋 **Reviewing Profile:** {rev_name} ({cid}) - Selected for next interview stage.")
                if st.button("Close Panel"):
                    del st.session_state["review_candidate"]
                    st.rerun()
            st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
            
        # Dynamic Colors
        is_dark = st.session_state.get("dark_mode", False)
        text_primary = "#f8fafc" if is_dark else "#0f172a"
        text_secondary = "#94a3b8" if is_dark else "#64748b"
        text_salary = "#e2e8f0" if is_dark else "#334155"
        bg_avatar = "#334155" if is_dark else "#e2e8f0"
        color_avatar = "#f8fafc" if is_dark else "#475569"
        border_bottom = "#334155" if is_dark else "#f1f5f9"
        border_top = "#475569" if is_dark else "#e2e8f0"

        # Header Row
        h1, h2, h3, h4 = st.columns([3, 2, 2, 1.5])
        with h1: st.markdown(f'<div style="color: {text_secondary}; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; padding-left: 10px;">Candidate Profile</div>', unsafe_allow_html=True)
        with h2: st.markdown(f'<div style="color: {text_secondary}; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Compensation</div>', unsafe_allow_html=True)
        with h3: st.markdown(f'<div style="color: {text_secondary}; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Evaluation</div>', unsafe_allow_html=True)
        with h4: st.markdown(f'<div style="color: {text_secondary}; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Action</div>', unsafe_allow_html=True)
        
        st.markdown(f"<hr style='margin: 10px 0; border-top: 2px solid {border_top};'>", unsafe_allow_html=True)
        
        for i, (_, row) in enumerate(ranked_top.iterrows()):
            rank = i + 1
            cid = row.get("candidate_id", "ID")
            
            if st.session_state.get("blind_mode", False):
                name = f"Candidate {str(cid)[:5]}"
                initials = "🕵️"
            else:
                name = row.get("name", "Unknown")
                initials = "".join([n[0] for n in str(name).split()[:2]]) if name else "??"
            cid = row.get("candidate_id", "ID")
            exp = row.get("years_of_experience", 0)
            score = float(row.get("talent_score", 0))
            salary = float(row.get("expected_salary", 0))
            
            rank_color = "#f59e0b" if rank == 1 else "#cbd5e1" if rank == 2 else "#b45309" if rank == 3 else text_secondary
            
            c1, c2, c3, c4 = st.columns([3, 2, 2, 1.5])
            
            with c1:
                st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 15px; padding: 5px 0;">
                    <div style="width: 24px; font-weight: 800; color: {rank_color}; font-size: 15px;">#{rank}</div>
                    <div style="width: 36px; height: 36px; border-radius: 50%; background: {bg_avatar}; color: {color_avatar}; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px; flex-shrink: 0;">{initials}</div>
                    <div>
                        <div style="font-weight: 600; color: {text_primary}; font-size: 14px;">{name}</div>
                        <div style="color: {text_secondary}; font-size: 12px;">{exp} Yrs Experience</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            with c2:
                st.markdown(f"""
                <div style="text-align: left; padding: 5px 0;">
                    <div style="font-weight: 600; color: {text_salary}; font-size: 14px;">₹{salary} LPA</div>
                    <div style="color: {text_secondary}; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Expected</div>
                </div>
                """, unsafe_allow_html=True)
                
            with c3:
                st.markdown(f"""
                <div style="text-align: left; padding: 5px 0;">
                    <div style="font-weight: 700; color: #3b82f6; font-size: 14px;">{score:.1f}</div>
                    <div style="color: {text_secondary}; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Talent Score</div>
                </div>
                """, unsafe_allow_html=True)
                
            with c4:
                st.markdown('<div style="padding-top: 10px;">', unsafe_allow_html=True)
                if st.button("Review", key=f"rev_{cid}_{i}"):
                    st.session_state["review_candidate"] = cid
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
                
            st.markdown(f"<hr style='margin: 5px 0; border-top: 1px solid {border_bottom};'>", unsafe_allow_html=True)
        
    # WRITE SKILLS ANALYTICS CODE HERE
    if "Skills Analytics" in selected_tab:
        is_dark = st.session_state.get("dark_mode", False)
        text_primary = "#f8fafc" if is_dark else "#0f172a"
        text_secondary = "#94a3b8" if is_dark else "#64748b"
        grid_color = "#334155" if is_dark else "#e2e8f0"
        
        st.markdown(f'<h3 style="color: {text_primary}; margin-bottom: 20px;">Skills Intelligence Center</h3>', unsafe_allow_html=True)
        
        top_skills = skills_df["skill_name"].value_counts().head(10)
        
        import plotly.express as px
        
        if not top_skills.empty:
            df_skills = top_skills.reset_index()
            df_skills.columns = ['Skill', 'Count']
            
            # Create 2x2 Grid
            row1_col1, row1_col2 = st.columns(2)
            row2_col1, row2_col2 = st.columns(2)
            
            # --- 1. PIE CHART ---
            with row1_col1:
                st.markdown(f'<strong style="color: {text_primary};">1. Pie Chart</strong>', unsafe_allow_html=True)
                fig_pie = px.pie(df_skills, values='Count', names='Skill', color_discrete_sequence=px.colors.qualitative.Pastel)
                fig_pie.update_layout(margin=dict(t=30), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=text_primary))
                st.plotly_chart(fig_pie, use_container_width=True, theme=None)

            # --- 2. BAR CHART ---
            with row1_col2:
                st.markdown(f'<strong style="color: {text_primary};">2. Bar Chart</strong>', unsafe_allow_html=True)
                fig_bar = px.bar(df_skills, x="Count", y="Skill", orientation='h', color="Count", color_continuous_scale="Tealgrn")
                fig_bar.update_layout(yaxis={'categoryorder':'total ascending'}, margin=dict(t=30), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color=text_primary))
                fig_bar.update_xaxes(showgrid=True, gridcolor=grid_color, color=text_primary)
                fig_bar.update_yaxes(showgrid=False, color=text_primary)
                fig_bar.update_coloraxes(colorbar_tickfont_color=text_primary, colorbar_title_font_color=text_primary)
                st.plotly_chart(fig_bar, use_container_width=True, theme=None)

            # --- 3. SCATTER CHART ---
            with row2_col1:
                st.markdown(f'<strong style="color: {text_primary};">3. Scatter Chart</strong>', unsafe_allow_html=True)
                fig_scatter = px.scatter(df_skills, x='Skill', y='Count', size='Count', color='Skill', size_max=40, color_discrete_sequence=px.colors.qualitative.Prism)
                fig_scatter.update_layout(margin=dict(t=30), showlegend=False, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color=text_primary))
                fig_scatter.update_xaxes(showgrid=True, gridcolor=grid_color, color=text_primary)
                fig_scatter.update_yaxes(showgrid=True, gridcolor=grid_color, color=text_primary)
                st.plotly_chart(fig_scatter, use_container_width=True, theme=None)

            # --- 4. COLUMN CHART ---
            with row2_col2:
                st.markdown(f'<strong style="color: {text_primary};">4. Column Chart</strong>', unsafe_allow_html=True)
                fig_col = px.bar(df_skills, x="Skill", y="Count", color="Count", color_continuous_scale="Purpor")
                fig_col.update_layout(xaxis={'categoryorder':'total descending'}, margin=dict(t=30), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color=text_primary))
                fig_col.update_xaxes(showgrid=False, color=text_primary)
                fig_col.update_yaxes(showgrid=True, gridcolor=grid_color, color=text_primary)
                fig_col.update_coloraxes(colorbar_tickfont_color=text_primary, colorbar_title_font_color=text_primary)
                st.plotly_chart(fig_col, use_container_width=True, theme=None)
                
        else:
            st.info("No skills data available.")
        
    # WRITE COMPARISON CODE HERE
    if "Comparison" in selected_tab:
        is_dark = st.session_state.get("dark_mode", False)
        text_primary = "#f8fafc" if is_dark else "#0f172a"
        grid_color = "#334155" if is_dark else "#e2e8f0"
        
        st.markdown(f'<h3 style="color: {text_primary}; margin-bottom: 20px;">Candidate Comparison</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        candidate1 = col1.selectbox("Select Candidate A", master_df["candidate_id"], key="cand1")
        cand2_options = master_df[master_df["candidate_id"] != candidate1]["candidate_id"]
        candidate2 = col2.selectbox("Select Candidate B", cand2_options, key="cand2")

        if candidate1 and candidate2:
            comparison = compare_candidates(master_df, candidate1, candidate2)
            
            if comparison is not None and not comparison.empty:
                st.markdown('<br>', unsafe_allow_html=True)
                
                if st.session_state.get("blind_mode", False):
                    name1 = f"Candidate {str(candidate1)[:5]}"
                    name2 = f"Candidate {str(candidate2)[:5]}"
                else:
                    name1 = master_df.loc[master_df["candidate_id"] == candidate1, "name"].iloc[0] if "name" in master_df.columns else candidate1
                    name2 = master_df.loc[master_df["candidate_id"] == candidate2, "name"].iloc[0] if "name" in master_df.columns else candidate2
                
                name1_col = f"{name1} (A)"
                name2_col = f"{name2} (B)"
                
                # --- Grouped Bar Chart ---
                import plotly.express as px
                
                df_melted = comparison.melt(id_vars=["Metric"], value_vars=[candidate1, candidate2], var_name="Candidate", value_name="Score")
                name_map = {candidate1: name1_col, candidate2: name2_col}
                df_melted["Candidate"] = df_melted["Candidate"].map(name_map)
                
                fig = px.bar(
                    df_melted, 
                    x="Score", 
                    y="Metric", 
                    color="Candidate", 
                    barmode="group", 
                    orientation='h',
                    color_discrete_sequence=["#3b82f6", "#10b981"],
                )
                
                fig.update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    font=dict(color=text_primary),
                    margin=dict(l=20, r=20, t=50, b=20),
                    height=350,
                    title=dict(text="Head-to-Head Overview", font=dict(size=18, color=text_primary)),
                    legend_title_text="",
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                )
                fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor=grid_color, title="", color=text_primary)
                fig.update_yaxes(title="", color=text_primary)
                
                # --- Create Compact Side-by-Side Layout ---
                comp_col1, comp_col2 = st.columns([1.2, 1])
                
                with comp_col1:
                    st.plotly_chart(fig, use_container_width=True, theme=None)
                
                with comp_col2:
                    st.markdown(f'<h4 style="color: {text_primary}; margin-top: 10px; margin-bottom: 25px;">Detailed Scorecard</h4>', unsafe_allow_html=True)
                    
                    display_df = comparison.copy()
                    display_df = display_df.rename(columns={candidate1: name1_col, candidate2: name2_col})
                    
                    def highlight_max(row):
                        is_max = row == row.max()
                        if is_dark:
                            return ['background-color: #064e3b; color: #6ee7b7; font-weight: 700' if v else 'color: #f8fafc;' for v in is_max]
                        else:
                            return ['background-color: #dcfce7; color: #166534; font-weight: 700' if v else 'color: #475569;' for v in is_max]
                    
                    numeric_cols = [name1_col, name2_col]
                    styled_df = display_df.style.apply(highlight_max, subset=numeric_cols, axis=1).format({c: "{:.2f}" for c in numeric_cols}).hide(axis="index")
                    
                    html_table = styled_df.to_html()
                    
                    # Safely apply custom CSS for premium enterprise look via wrapper div
                    table_class = "dark-scorecard" if is_dark else "light-scorecard"
                    
                    css = f"""
                    <style>
                    .{table_class} table {{ width: 100% !important; border-collapse: collapse !important; border-radius: 8px !important; overflow: hidden !important; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important; margin-bottom: 10px !important; }}
                    .{table_class} th {{ padding: 12px 15px !important; text-align: left !important; font-weight: 600 !important; }}
                    .{table_class} td {{ padding: 12px 15px !important; }}
                    
                    .dark-scorecard table {{ color: #f8fafc !important; background-color: #1e293b !important; }}
                    .dark-scorecard th {{ border-bottom: 1px solid #334155 !important; background-color: #0f172a !important; color: #94a3b8 !important; }}
                    .dark-scorecard td {{ border-bottom: 1px solid #334155 !important; }}
                    
                    .light-scorecard table {{ color: #0f172a !important; background-color: #ffffff !important; }}
                    .light-scorecard th {{ border-bottom: 1px solid #cbd5e1 !important; background-color: #f8fafc !important; color: #64748b !important; }}
                    .light-scorecard td {{ border-bottom: 1px solid #e2e8f0 !important; }}
                    </style>
                    <div class="{table_class}">{html_table}</div>
                    """
                        
                    st.markdown(css.replace('\n', ' '), unsafe_allow_html=True)

    # WRITE RECOMMENDATION CODE HERE
    if "Recommendation" in selected_tab:
        is_dark = st.session_state.get("dark_mode", False)
        text_primary = "#f8fafc" if is_dark else "#0f172a"
        text_secondary = "#94a3b8" if is_dark else "#64748b"
        
        # --- HERO SECTION ---
        hero_bg = "linear-gradient(135deg, #1e293b, #0f172a)" if is_dark else "linear-gradient(135deg, #f8fafc, #e2e8f0)"
        hero_border = "#334155" if is_dark else "#cbd5e1"
        st.markdown(f'''
        <div style="background: {hero_bg}; border: 1px solid {hero_border}; border-radius: 16px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); margin-bottom: 30px;">
            <div style="display: flex; align-items: center; gap: 16px;">
                <div style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 28px; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);">🎯</div>
                <div>
                    <h2 style="margin: 0; color: {text_primary}; font-family: 'Inter', sans-serif; font-size: 28px; font-weight: 800; letter-spacing: -0.5px;">AI Recommendation Engine</h2>
                    <p style="margin: 6px 0 0 0; color: {text_secondary}; font-size: 15px;">Smart-match candidates instantly by selecting required skills across technical domains.</p>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        if "recc_skills_val" not in st.session_state:
            st.session_state["recc_skills_val"] = ""
            
        def add_pill_skills(pill_key):
            selected = st.session_state.get(pill_key, [])
            if selected:
                current = st.session_state["recc_skills_val"]
                current_list = [s.strip() for s in current.split(",") if s.strip()]
                for s in selected:
                    if s not in current_list:
                        current_list.append(s)
                st.session_state["recc_skills_val"] = ", ".join(current_list)
                st.session_state[pill_key] = [] # clear pills so they act purely as buttons
        
        # Search Box
        st.markdown(f'<div style="font-size: 13px; font-weight: 700; color: {text_secondary}; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">Selected Requirements</div>', unsafe_allow_html=True)
        skills_input = st.text_input(
            "Required Skills",
            key="recc_skills_val",
            label_visibility="collapsed",
            placeholder="e.g. Python, Machine Learning, AWS..."
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Domain-specific skill groupings
        skill_categories = {
            "Data Science & Machine Learning": [
                "Python", "Machine Learning", "Deep Learning", "NLP", "Computer Vision", 
                "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "NumPy", "MLflow",
                "Keras", "XGBoost", "LightGBM", "Hugging Face", "LLMs", "OpenAI API", 
                "OpenCV", "NLTK", "SpaCy", "Matplotlib", "Seaborn", "MLOps", "Generative AI"
            ],
            "Data Analytics & BI": [
                "SQL", "Excel", "Tableau", "Power BI", "R", "Data Visualization", 
                "Looker", "Snowflake", "BigQuery", "Statistics", "Google Analytics",
                "Power Query", "Alteryx", "QlikSense", "Metabase", "dbt", "Fivetran", 
                "Data Warehousing", "Data Modeling", "A/B Testing", "SAS", "Redshift"
            ],
            "Software Engineering & Web": [
                "JavaScript", "TypeScript", "React", "Node.js", "Java", "Spring Boot", 
                "C++", "C#", ".NET", "Django", "Go", "HTML", "CSS", "Angular", "Vue.js",
                "Svelte", "Express.js", "GraphQL", "REST APIs", "PHP", "Laravel", 
                "Flask", "FastAPI", "Rust", "Kotlin", "Swift", "PostgreSQL", "MongoDB"
            ],
            "Cloud, DevOps & Data Engineering": [
                "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Terraform", "CI/CD", 
                "Jenkins", "Linux", "Apache Spark", "Kafka", "Airflow", "Hadoop", 
                "Databricks", "GitHub Actions", "GitLab CI", "Ansible", "Prometheus", 
                "Grafana", "ELK Stack", "Bash Scripting", "Redis", "Cassandra"
            ]
        }
        
        # Layout in 2x2 Grid using Multiselect
        card_bg = "#1e293b" if is_dark else "#ffffff"
        card_border = "#334155" if is_dark else "#e2e8f0"
        
        
        keys = list(skill_categories.keys())
        col1, col2 = st.columns(2)
        
        with col1:
            for cat_name in keys[:2]:
                cat_skills = skill_categories[cat_name]
                st.markdown(f"<div style='font-size: 14px; font-weight: 600; color: {text_primary}; margin-top: 5px; margin-bottom: 10px;'>{cat_name}</div>", unsafe_allow_html=True)
                st.pills(cat_name, cat_skills, selection_mode="multi", key=f"pills_{cat_name.replace(' ', '_')}", label_visibility="collapsed", on_change=add_pill_skills, args=(f"pills_{cat_name.replace(' ', '_')}",))
                st.markdown("<br>", unsafe_allow_html=True)
                
        with col2:
            for cat_name in keys[2:]:
                cat_skills = skill_categories[cat_name]
                st.markdown(f"<div style='font-size: 14px; font-weight: 600; color: {text_primary}; margin-top: 5px; margin-bottom: 10px;'>{cat_name}</div>", unsafe_allow_html=True)
                st.pills(cat_name, cat_skills, selection_mode="multi", key=f"pills_{cat_name.replace(' ', '_')}", label_visibility="collapsed", on_change=add_pill_skills, args=(f"pills_{cat_name.replace(' ', '_')}",))
                st.markdown("<br>", unsafe_allow_html=True)

        if skills_input:

            required_skills = skills_input.split(",")

            recommendations = recommend_candidates(
                master_df,
                skills_df,
                required_skills
            )
            
            # Sort intelligently
            if "talent_score" in recommendations.columns:
                recommendations = recommendations.sort_values(by=["match_score", "talent_score"], ascending=[False, False])
            elif "avg_assessment_score" in recommendations.columns:
                recommendations = recommendations.sort_values(by=["match_score", "avg_assessment_score"], ascending=[False, False])
            else:
                recommendations = recommendations.sort_values(by=["match_score"], ascending=False)
                
            top_recs = recommendations.head(6)
            
            st.markdown('<hr style="border-top: 1px dashed #cbd5e1; margin: 30px 0;">', unsafe_allow_html=True)
            st.markdown(f'<h3 style="color: {text_primary}; margin-bottom: 20px;">Top Recommended Candidates</h3>', unsafe_allow_html=True)
            
            if top_recs.empty:
                st.warning("No candidates found.")
            else:
                # Add hover CSS for candidate cards
                st.markdown("""
                <style>
                .candidate-card { transition: all 0.2s ease; }
                .candidate-card:hover { transform: translateY(-4px); box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1) !important; }
                </style>
                """, unsafe_allow_html=True)
                
                # Dark Mode Dynamic Colors for Cards
                card_bg = "#1e293b" if is_dark else "white"
                card_border = "#334155" if is_dark else "#e2e8f0"
                text_main = "#f8fafc" if is_dark else "#0f172a"
                text_muted = "#94a3b8" if is_dark else "#64748b"
                
                cols = st.columns(3)
                for i, row_data in enumerate(top_recs.iterrows()):
                    data = row_data[1]
                    col = cols[i % 3]
                    
                    match_score = data["match_score"]
                    cand_id = data["candidate_id"]
                    if st.session_state.get("blind_mode", False):
                        name = f"Candidate {str(cand_id)[:5]}"
                        initials = "🕵️"
                    else:
                        name = data["name"]
                        initials = name[0].upper() if name else "?"
                    cand_id = data["candidate_id"]
                    exp = data.get("years_of_experience", 0)
                    salary = data.get("expected_salary", 0)
                    
                    # Try to get best score metric
                    if "talent_score" in data:
                        score_label = "Talent Score"
                        score = data["talent_score"]
                    elif "avg_assessment_score" in data:
                        score_label = "Assessment"
                        score = data["avg_assessment_score"]
                    else:
                        score_label = "Score"
                        score = 0
                    
                    # Highlight logic with dynamic dark/light themes
                    if match_score == len(required_skills) and len(required_skills) > 0:
                        badge_color = "#86efac" if is_dark else "#166534" # Light Green / Dark Green
                        badge_bg = "#064e3b" if is_dark else "#dcfce7"    # Dark Green BG / Light Green BG
                    elif match_score > 0:
                        badge_color = "#fcd34d" if is_dark else "#b45309" # Yellow / Orange
                        badge_bg = "#78350f" if is_dark else "#fef3c7"    # Dark Brown / Light Orange
                    else:
                        badge_color = "#94a3b8" if is_dark else "#475569" # Gray
                        badge_bg = "#334155" if is_dark else "#f1f5f9"    # Dark Gray / Light Gray
                    
                    with col:
                        st.markdown(f"""
                        <div class="candidate-card" style="background: {card_bg}; border: 1px solid {card_border}; border-top: 4px solid {badge_color}; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); margin-bottom: 20px; cursor: pointer;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                                <div style="display: flex; align-items: center; gap: 12px;">
                                    <div style="width: 40px; height: 40px; border-radius: 50%; background: {badge_bg}; color: {badge_color}; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 18px;">
                                        {initials}
                                    </div>
                                    <div>
                                        <h3 style="margin: 0; color: {text_main}; font-size: 16px; font-weight: 700;">{name}</h3>
                                        <p style="margin: 0; color: {text_muted}; font-size: 12px;">{cand_id}</p>
                                    </div>
                                </div>
                                <div style="background: {badge_bg}; color: {badge_color}; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 800; white-space: nowrap;">
                                    🎯 {match_score} MATCH
                                </div>
                            </div>
                            <div style="display: flex; justify-content: space-between; padding-top: 15px; border-top: 1px dashed {card_border};">
                                <div style="text-align: center;">
                                    <p style="margin: 0 0 4px 0; font-size: 11px; color: {text_muted}; text-transform: uppercase; font-weight: 700;">{score_label}</p>
                                    <p style="margin: 0; font-size: 14px; font-weight: 800; color: {text_main};">⭐ {round(score, 1)}</p>
                                </div>
                                <div style="text-align: center;">
                                    <p style="margin: 0 0 4px 0; font-size: 11px; color: {text_muted}; text-transform: uppercase; font-weight: 700;">Exp.</p>
                                    <p style="margin: 0; font-size: 14px; font-weight: 800; color: {text_main};">{exp} Yrs</p>
                                </div>
                                <div style="text-align: center;">
                                    <p style="margin: 0 0 4px 0; font-size: 11px; color: {text_muted}; text-transform: uppercase; font-weight: 700;">Salary</p>
                                    <p style="margin: 0; font-size: 14px; font-weight: 800; color: {text_main};">{salary}k</p>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        
    if "Semantic Match" in selected_tab:
        
        card_bg = "#1e293b" if is_dark else "#ffffff"
        card_border = "#334155" if is_dark else "#e2e8f0"
        text_main = "#f8fafc" if is_dark else "#0f172a"
        text_muted = "#94a3b8" if is_dark else "#64748b"
        sub_bg = "#334155" if is_dark else "#f8fafc"
        
        @st.dialog("🤖 Agentic Outreach Configuration")
        def draft_pitch_modal(candidate_id, match_name, match_score, match_exp, match_salary, job_desc):
            st.markdown(f"<p style='color: {text_muted}; font-size: 14px;'>Drafting personalized pitch for <b style='color: {text_main};'>{match_name}</b></p>", unsafe_allow_html=True)
            
            t_col, f_col = st.columns(2)
            with t_col: tone = st.selectbox("Pitch Tone", ["Professional", "Casual", "Direct / Aggressive"], key=f"tone_{candidate_id}")
            with f_col: focus = st.selectbox("Pitch Focus", ["Balanced", "Salary / Compensation", "Tech Stack / Challenges", "Company Culture"], key=f"focus_{candidate_id}")
            
            email = generate_outreach_email(match_name, match_score, match_exp, match_salary, job_desc, tone=tone, focus=focus)
            
            st.markdown(f"<div style='background: {sub_bg}; padding: 15px; border-radius: 8px; border: 1px solid {card_border}; font-size: 13px; line-height: 1.6; color: {text_main}; white-space: pre-wrap; font-family: sans-serif; margin-top: 10px;'>{email}</div>", unsafe_allow_html=True)
            
            import urllib.parse
            subject = email.splitlines()[0].replace("Subject: ", "") if email.splitlines() else "Reaching Out"
            body = "\n".join(email.splitlines()[2:])
            mailto_link = f"mailto:?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
            
            st.markdown(f'''
            <a href="{mailto_link}" target="_blank" style="display: block; width: 100%; text-align: center; background-color: #3b82f6; color: white; padding: 10px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 15px; transition: opacity 0.2s;">
                🚀 Send via Email
            </a>
            ''', unsafe_allow_html=True)

        st.markdown(f'''
        <div style="background: {card_bg}; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 24px; border: 1px solid {card_border};">
        <div style="display: flex; align-items: center; gap: 16px;">
        <div style="background: linear-gradient(135deg, #8b5cf6, #3b82f6); width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 4px 6px rgba(139, 92, 246, 0.2);">🧠</div>
        <div>
        <h3 style="margin: 0; color: {text_main}; font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 800;">Semantic Job Match (RAG Engine)</h3>
        <p style="margin: 4px 0 0 0; color: {text_muted}; font-size: 14px;">Upload a Job Description to instantly rank the entire talent pool based on deep semantic meaning.</p>
        </div>
        </div>
        </div>''', unsafe_allow_html=True)
        
        job_desc = st.text_area("📋 Paste Target Job Description", height=150, placeholder="We are looking for a Senior Python Engineer...")
        
        if st.button("🚀 Find Perfect Matches", use_container_width=True):
            if job_desc:
                with st.spinner("Analyzing candidate embeddings against job requirements... (This takes a few seconds)"):
                    results = []
                    for _, row in master_df.iterrows():
                        cand_id = row['candidate_id']
                        profile_text = str(row.get('headline', '')) + " " + str(row.get('summary', ''))
                        score = hidden_talent_score(job_desc, profile_text)
                        
                        if st.session_state.get("blind_mode", False):
                            name = f"Candidate {str(cand_id)[:5]}"
                            initials = "🕵️"
                        else:
                            name = row.get('name', 'Unknown')
                            initials = "".join([n[0] for n in str(name).split()[:2]]) if name else "?"
                            
                        results.append({
                            "candidate_id": cand_id,
                            "name": name,
                            "initials": initials,
                            "score": score,
                            "experience": row.get('years_of_experience', 0),
                            "salary": row.get('expected_salary', 0)
                        })
                    
                    df_results = pd.DataFrame(results).sort_values(by="score", ascending=False).head(3)
                    st.session_state["semantic_results"] = df_results
                    st.session_state["last_job_desc"] = job_desc
                    
        if "semantic_results" in st.session_state and not st.session_state["semantic_results"].empty:
            df_results = st.session_state["semantic_results"]
            job_desc_used = st.session_state.get("last_job_desc", "")
            
            st.markdown(f"<h2 style='color: {text_main}; margin-bottom: 20px; font-family: \"Inter\", sans-serif; font-size: 24px; font-weight: 800;'>🎯 Top 3 Semantic Matches</h2>", unsafe_allow_html=True)
            
            # --- RENDER MATCH CARDS ONLY ---
            cols = st.columns(3)
            for i, (_, match) in enumerate(df_results.iterrows()):
                col = cols[i]
                color = "#10b981" if match['score'] >= 75 else "#f59e0b" if match['score'] >= 50 else "#ef4444"
                idx = i + 1
                with col:
                    st.markdown(f"""
                    <div class="glass-card" style="background: {card_bg}; border: 1px solid {card_border}; padding: 20px; border-radius: 12px; margin-bottom: 20px; text-align: center; position: relative;">
                        <div style="position: absolute; top: 10px; right: 10px; font-weight: 800; font-size: 11px; color: {text_muted};">
                            {idx}
                        </div>
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: {sub_bg}; color: {text_main}; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 20px; margin: 0 auto 15px auto;">
                            {match['initials']}
                        </div>
                        <h3 style="margin: 0; color: {text_main}; font-size: 18px; font-weight: 700;">{match['name']}</h3>
                        <p style="color: {text_muted}; font-size: 12px; margin-bottom: 15px;">{match['candidate_id']}</p>
                        <div style="background: {sub_bg}; border: 1px solid {card_border}; border-radius: 8px; padding: 10px; margin-bottom: 15px;">
                            <div style="font-size: 24px; font-weight: 800; color: {color};">{match['score']:.2f}%</div>
                            <div style="font-size: 11px; font-weight: 700; color: {text_muted}; text-transform: uppercase;">Semantic Match</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 13px;">
                            <div><span style="color:{text_muted};">Exp:</span> <b style="color:{text_main};">{match['experience']} Yrs</b></div>
                            <div><span style="color:{text_muted};">Salary:</span> <b style="color:{text_main};">₹{match['salary']}L</b></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    if st.button("✉️ Draft AI Pitch", key=f"pitch_{match['candidate_id']}", use_container_width=True):
                        draft_pitch_modal(match['candidate_id'], match['name'], match['score'], match['experience'], match['salary'], job_desc_used)

    # WRITE SEGMENTS CODE HERE
    if "Segments" in selected_tab:
        import plotly.express as px
        
        text_main = "#f8fafc" if is_dark else "#0f172a"
        text_muted = "#94a3b8" if is_dark else "#64748b"
        hover_bg = "#334155" if is_dark else "#f8fafc"
        border_color = "#334155" if is_dark else "#e2e8f0"
        row_border = "#1e293b" if is_dark else "#f1f5f9"
        
        st.markdown(f'''
        <h2 style="color: {text_main}; margin-bottom: 5px; font-weight: 800; font-family: 'Inter', sans-serif;">Candidate Segmentation Intelligence</h2>
        <p style="color: {text_muted}; margin-bottom: 30px; font-family: 'Inter', sans-serif;">A comprehensive, multi-dimensional view of your candidate clusters.</p>
        ''', unsafe_allow_html=True)
        
        segmented_df = create_segments(master_df.copy())
        segmented_df['title'] = segmented_df['current_title'].fillna('Professional')
        
        color_map = {
            "🌱 Emerging Talent": "#10b981",
            "🚀 High Potential": "#3b82f6",
            "🏆 Industry Veteran": "#8b5cf6"
        }
        
        # ---------------------------------------------------------
        # MINIMALIST ACCORDION DIRECTORY
        # ---------------------------------------------------------
        segments = sorted([s for s in segmented_df['segment'].unique() if pd.notna(s)])
        
        # 1. Top Level Distribution Metrics
        st.markdown(f'<h3 style="color: {text_main}; font-size: 14px; margin-top: 20px; margin-bottom: 20px; font-family: \'Inter\', sans-serif; text-transform: uppercase; letter-spacing: 1px;">Segment Distribution</h3>', unsafe_allow_html=True)
        
        metric_cols = st.columns(len(segments))
        for i, segment in enumerate(segments):
            count = len(segmented_df[segmented_df['segment'] == segment])
            bg_color = color_map.get(segment, "#3b82f6")
            clean_seg = segment.replace('🌱 ','').replace('🚀 ','').replace('🏆 ','')
            
            with metric_cols[i]:
                st.markdown(f'''
                <div style="border-left: 3px solid {bg_color}; padding-left: 16px; margin-bottom: 30px; font-family: 'Inter', sans-serif;">
                    <div style="font-size: 32px; font-weight: 900; color: {text_main}; line-height: 1;">{count}</div>
                    <div style="font-size: 12px; font-weight: 700; color: {text_muted}; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">{clean_seg}</div>
                </div>
                ''', unsafe_allow_html=True)
                
        # 2. Expandable Accordion Directory
        st.markdown(f'<h3 style="color: {text_main}; font-size: 14px; margin-bottom: 15px; font-family: \'Inter\', sans-serif; text-transform: uppercase; letter-spacing: 1px;">Candidate Directory</h3>', unsafe_allow_html=True)
        
        for segment in segments:
            seg_cands = segmented_df[segmented_df['segment'] == segment]
            bg_color = color_map.get(segment, "#3b82f6")
            
            with st.expander(f"{segment} ({len(seg_cands)} Candidates)", expanded=False):
                list_html = f'''
<style>
.flat-row:hover {{
    background-color: {hover_bg};
}}
</style>
<div style="font-family: 'Inter', sans-serif; padding-bottom: 10px;">
'''
                
                # Header row
                list_html += f'''
<div style="display: flex; padding: 12px 16px; border-bottom: 2px solid {border_color}; margin-bottom: 8px;">
<div style="flex: 2; font-size: 11px; font-weight: 700; color: {text_muted}; text-transform: uppercase; letter-spacing: 1px;">Candidate Name</div>
<div style="flex: 2; font-size: 11px; font-weight: 700; color: {text_muted}; text-transform: uppercase; letter-spacing: 1px;">Current Role</div>
<div style="flex: 1; font-size: 11px; font-weight: 700; color: {text_muted}; text-transform: uppercase; letter-spacing: 1px; text-align: right;">Experience</div>
<div style="flex: 1; font-size: 11px; font-weight: 700; color: {text_muted}; text-transform: uppercase; letter-spacing: 1px; text-align: right;">Score</div>
</div>
'''
                
                cands_sorted = seg_cands.sort_values('avg_assessment_score', ascending=False)
                
                for _, row in cands_sorted.iterrows():
                    name = row.get('name', 'Unknown')
                    title = row.get('title', 'Professional')
                    exp = row.get('years_of_experience', 0)
                    score = round(row.get('avg_assessment_score', 0), 1)
                    
                    list_html += f'''
<div class="flat-row" style="display: flex; padding: 14px 16px; border-bottom: 1px solid {row_border}; align-items: center; transition: background 0.2s;">
<div style="flex: 2; font-size: 14px; font-weight: 700; color: {text_main};">{name}</div>
<div style="flex: 2; font-size: 14px; font-weight: 500; color: {text_muted};">{title}</div>
<div style="flex: 1; font-size: 14px; font-weight: 600; color: {text_muted}; text-align: right;">{exp} Yrs</div>
<div style="flex: 1; font-size: 14px; font-weight: 800; color: {bg_color}; text-align: right;">{score}</div>
</div>
'''
                    
                list_html += '</div>'
                st.markdown(list_html, unsafe_allow_html=True)

    # WRITE TALENT SCORE BREAKDOWN CODE HERE
    if "Score Breakdown" in selected_tab:

        text_main = "#f8fafc" if is_dark else "#0f172a"
        text_muted = "#94a3b8" if is_dark else "#64748b"
        row_border = "#334155" if is_dark else "#f1f5f9"

        st.markdown(f'<p style="color: {text_muted}; margin-bottom: 20px; font-weight: 500; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Talent Score Composition</p>', unsafe_allow_html=True)
        
        # Enhanced Selectbox showing Name + ID
        options = []
        for _, r in master_df.iterrows():
            options.append(f"{r.get('name', 'Unknown')} ({r['candidate_id']})")
            
        selected_option = st.selectbox("Select Candidate to Analyze", options, key="breakdown_candidate")
        selected_id = selected_option.split("(")[-1].replace(")", "").strip()

        row = master_df[master_df["candidate_id"] == selected_id].iloc[0]
        breakdown_df, total_score = get_score_breakdown(row)

        col1, col2 = st.columns([1, 1.2])
        
        colors = ["#3b82f6", "#10b981", "#f59e0b", "#8b5cf6"]
        
        with col1:
            # Massive Typographic Total Score
            st.markdown(f"""
            <div style="padding: 10px 0;">
                <div style="color: {text_muted}; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px;">Overall Talent Score</div>
                <div style="color: {text_main}; font-size: 64px; font-weight: 900; line-height: 1;">{total_score:.1f}</div>
                <div style="width: 50px; height: 4px; background: #3b82f6; margin-top: 15px; margin-bottom: 30px; border-radius: 2px;"></div>
            </div>
            """, unsafe_allow_html=True)
            
            # Clean Flexbox List for Breakdown Values
            list_html = ""
            for i, (_, row_df) in enumerate(breakdown_df.iterrows()):
                comp = row_df['Component']
                score = float(row_df['Score'])
                c = colors[i % len(colors)]
                list_html += f"""
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid {row_border};">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 10px; height: 10px; border-radius: 50%; background: {c};"></div>
                        <div style="font-weight: 600; color: {text_muted}; font-size: 14px;">{comp}</div>
                    </div>
                    <div style="font-weight: 800; color: {text_main}; font-size: 16px;">{score:.1f}</div>
                </div>
                """
            st.markdown(f'<div>{list_html}</div>'.replace('\n', ''), unsafe_allow_html=True)

        with col2:
            import plotly.express as px
            # Elegant Donut Chart
            fig = px.pie(
                breakdown_df, 
                values='Score', 
                names='Component', 
                hole=0.65,
                color_discrete_sequence=colors
            )
            fig.update_traces(
                textposition='outside', 
                textinfo='percent+label', 
                marker=dict(line=dict(color='#ffffff', width=3)),
                textfont_size=13
            )
            fig.update_layout(
                showlegend=False, 
                height=400, 
                margin=dict(t=30, b=30, l=30, r=30),
                paper_bgcolor="rgba(0,0,0,0)",
                annotations=[dict(text="Composition", x=0.5, y=0.5, font_size=16, showarrow=False, font_color="#94a3b8")]
            )
            st.plotly_chart(fig, use_container_width=True)

    # WRITE AI COPILOT CODE HERE


    if "AI Copilot" in selected_tab:
        st.markdown('<h2 style="color: #0f172a; margin-bottom: 20px; font-family: \'Inter\', sans-serif; font-size: 24px; font-weight: 800;">Predictive Market Value</h2>', unsafe_allow_html=True)
        
        st.markdown('<p style="color: #64748b; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; font-family: \'Inter\', sans-serif;">Select Candidate for Analysis</p>', unsafe_allow_html=True)
        candidate = st.selectbox("Select Candidate", master_df["candidate_id"], key="copilot_cand", label_visibility="collapsed")
        
        cand_row = master_df[master_df["candidate_id"] == candidate].iloc[0]
        name = cand_row["name"] if "name" in cand_row else candidate
        exp = cand_row.get("years_of_experience", 0)
        skills = cand_row.get("total_skills", 0)
        expected_val = cand_row.get("expected_salary", 0)

        candidate_languages = languages_df[languages_df["candidate_id"] == candidate].drop(columns=["candidate_id"], errors="ignore")
        lang_html_str = ""
        if not candidate_languages.empty:
            lang_html_str += '<div style="display: flex; flex-direction: column; gap: 12px; margin-top: 10px;">'
            for _, row in candidate_languages.iterrows():
                lang = str(row.get('language', ''))
                prof = str(row.get('proficiency', '')).capitalize()
                prof_lower = prof.lower()
                
                if prof_lower in ['native', 'fluent', 'bilingual']: width = 100
                elif prof_lower in ['professional', 'advanced']: width = 75
                elif prof_lower in ['conversational', 'intermediate']: width = 50
                else: width = 25
                
                lang_html_str += f"""
<div>
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<span style="font-weight: 600; color: #0f172a; font-size: 13px;">{lang}</span>
<span style="color: #64748b; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">{prof}</span>
</div>
<div style="width: 100%; background: #f1f5f9; border-radius: 999px; height: 4px; overflow: hidden; box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);">
<div style="width: {width}%; height: 100%; background: linear-gradient(90deg, #3b82f6, #6366f1); border-radius: 999px;"></div>
</div>
</div>
"""
            lang_html_str += '</div>'
        else:
            lang_html_str = '<p style="margin: 5px 0 0 0; color: #0f172a; font-size: 14px; font-weight: 500;">Not specified</p>'

        with st.spinner("Training Random Forest model and predicting market value..."):
            features = ["years_of_experience", "total_skills", "certification_count", "avg_assessment_score", "companies_worked", "github_activity_score"]
            X_cand = master_df[master_df["candidate_id"] == candidate][features].fillna(0)
            predicted_val = market_model.predict(X_cand)[0]
            diff = expected_val - predicted_val
            
            if diff < -2:
                status = "Bargain / Undervalued"
                rec = "Hire Immediately. The candidate is asking for significantly less than their predicted market value."
                color = "#10b981"
            elif diff > 3:
                status = "Overpriced"
                rec = "Negotiate Strongly. The candidate's expectations significantly exceed their predicted market value."
                color = "#ef4444"
            else:
                status = "Fair Market Value"
                rec = "Proceed. The candidate's expected salary aligns perfectly with the current market benchmarks."
                color = "#f59e0b"
            
            diff_str = f"+{round(diff, 1)}" if diff > 0 else f"{round(diff, 1)}"
            diff_percent = max(5, min(95, 50 + (diff / 10) * 50))
            
            st.markdown(f"""
<div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; font-family: 'Inter', sans-serif; display: flex; overflow: hidden; margin-top: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">

<!-- Left Column: Profile -->
<div style="flex: 1; border-right: 1px solid #e2e8f0; padding: 30px; background: #f8fafc;">
<h3 style="margin: 0 0 25px 0; font-size: 12px; font-weight: 800; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">Candidate Profile</h3>

<div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 15px; margin-bottom: 15px;">
<p style="margin: 0; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">Name</p>
<p style="margin: 5px 0 0 0; color: #0f172a; font-size: 16px; font-weight: 600;">{name}</p>
</div>

<div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 15px; margin-bottom: 15px;">
<p style="margin: 0; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">Experience</p>
<p style="margin: 5px 0 0 0; color: #0f172a; font-size: 16px; font-weight: 600;">{exp} Years</p>
</div>

<div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 15px; margin-bottom: 15px;">
<p style="margin: 0; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">Total Skills</p>
<p style="margin: 5px 0 0 0; color: #0f172a; font-size: 16px; font-weight: 600;">{skills}</p>
</div>

<div>
<p style="margin: 0; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">Languages</p>
{lang_html_str}
</div>
</div>

<!-- Right Column: AI Analysis -->
<div style="flex: 2.5; padding: 30px;">
<h3 style="margin: 0 0 25px 0; font-size: 12px; font-weight: 800; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">Market Calibration</h3>

<div style="display: flex; gap: 40px; margin-bottom: 40px;">
<div>
<p style="margin: 0; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">Expected Salary</p>
<p style="margin: 5px 0 0 0; color: #0f172a; font-size: 36px; font-weight: 800; letter-spacing: -1px;">{expected_val}k</p>
</div>
<div>
<p style="margin: 0; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">Predicted Market</p>
<p style="margin: 5px 0 0 0; color: #0f172a; font-size: 36px; font-weight: 300; letter-spacing: -1px;">{round(predicted_val, 1)}k</p>
</div>
</div>

<!-- Minimal Flat Progress Track -->
<div style="position: relative; height: 4px; background: #e2e8f0; border-radius: 2px; margin-bottom: 50px;">
<!-- Center Line -->
<div style="position: absolute; left: 50%; top: -6px; width: 2px; height: 16px; background: #94a3b8;"></div>
<div style="position: absolute; left: 50%; top: -25px; transform: translateX(-50%); font-size: 10px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">Market Rate</div>

<!-- Expected Marker -->
<div style="position: absolute; left: {diff_percent}%; top: -4px; width: 12px; height: 12px; background: {color}; border-radius: 50%; transform: translateX(-50%);"></div>
<div style="position: absolute; left: {diff_percent}%; top: 15px; transform: translateX(-50%); font-size: 12px; font-weight: 800; color: {color};">{expected_val}k</div>
</div>

<div style="display: flex; gap: 40px; border-top: 1px solid #e2e8f0; padding-top: 25px;">
<div style="flex: 1;">
<p style="margin: 0; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">Status</p>
<p style="margin: 5px 0 0 0; color: {color}; font-size: 16px; font-weight: 700;">{status} ({diff_str}k)</p>
</div>
<div style="flex: 2;">
<p style="margin: 0; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">Recommendation</p>
<p style="margin: 5px 0 0 0; color: #0f172a; font-size: 14px; font-weight: 400; line-height: 1.5;">{rec}</p>
</div>
</div>

</div>

</div>
""", unsafe_allow_html=True)

    # WRITE JD MATCH CODE HERE
    if "JD Match" in selected_tab:
        
        text_main = "#f8fafc" if is_dark else "#0f172a"
        text_muted = "#94a3b8" if is_dark else "#64748b"
        card_bg = "#1e293b" if is_dark else "white"
        border_color = "#334155" if is_dark else "#e2e8f0"
        row_border = "#334155" if is_dark else "#f1f5f9"
        
        st.markdown(f'''
        <div style="background: {card_bg}; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 24px; border: 1px solid {border_color};">
        <div style="display: flex; align-items: center; gap: 16px;">
        <div style="background: linear-gradient(135deg, #10b981, #059669); width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px; box-shadow: 0 4px 6px rgba(16, 185, 129, 0.2);">📄</div>
        <div>
        <h3 style="margin: 0; color: {text_main}; font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 800;">JD Scoring Engine</h3>
        <p style="margin: 4px 0 0 0; color: {text_muted}; font-size: 14px;">Instantly match and rank all candidates against your custom job requirements.</p>
        </div>
        </div>
        </div>''', unsafe_allow_html=True)
        example_jds = {
            "Custom Input": "",
            "Senior React Developer": "We are looking for a Senior React Developer with 5+ years of experience in frontend UI architecture. Must have deep knowledge of React hooks, state management (Redux/Zustand), and deploying modern web applications to AWS or GCP. Experience with Tailwind CSS is a huge plus.",
            "Data Scientist (NLP)": "Seeking a Data Scientist specializing in Natural Language Processing. The ideal candidate will have strong Python skills, experience with Hugging Face transformers (BERT, Sentence-Transformers), and a solid understanding of machine learning pipelines using Scikit-Learn and Pandas. Master's degree preferred.",
            "Cloud DevOps Engineer": "We need a Cloud DevOps Engineer to manage our infrastructure. Key requirements: strong experience with Kubernetes (K8s), Docker containers, CI/CD pipelines (GitHub Actions/Jenkins), and Infrastructure as Code (Terraform). Must be comfortable in a fast-paced agile environment."
        }
        
        selected_example = st.selectbox("💡 Try an Example Job Description:", list(example_jds.keys()))
        default_jd_text = example_jds[selected_example]
        
        job_desc_input = st.text_area("📋 Paste Target Job Description", value=default_jd_text, height=150, placeholder="We are looking for...")
        
        st.markdown('<br>', unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            calc_btn = st.button("🚀 Analyze Candidates", use_container_width=True, type="primary")
        
        if calc_btn:
            if job_desc_input:
                with st.spinner("Analyzing candidate embeddings against job requirements... (This takes a few seconds)"):
                    results = []
                    for _, row in master_df.iterrows():
                        cand_id = row['candidate_id']
                        profile_text = str(row.get('headline', '')) + " " + str(row.get('summary', ''))
                        score = hidden_talent_score(job_desc_input, profile_text)
                        
                        if st.session_state.get("blind_mode", False):
                            name = f"Candidate {str(cand_id)[:5]}"
                        else:
                            name = row.get('name', 'Unknown')
                            
                        results.append({
                            "Candidate ID": cand_id,
                            "Name": name,
                            "Match Score (%)": round(score, 1),
                            "Experience (Yrs)": round(row.get('years_of_experience', 0), 1)
                        })
                    
                    df_results_full = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)
                    st.session_state["jd_match_results"] = df_results_full
            else:
                st.warning("Please enter a job description first.")
                
        if "jd_match_results" in st.session_state:
            st.markdown(f'<hr style="border-top: 2px solid {row_border}; margin: 30px 0;">', unsafe_allow_html=True)
            
            res_col1, res_col2 = st.columns([3, 1])
            with res_col1:
                st.markdown(f'<h3 style="margin: 0; color: {text_main}; font-family: \'Inter\', sans-serif; font-size: 22px; font-weight: 800; padding-top: 5px;">🎯 Match Results <span style="color: {text_muted}; font-weight: 500; font-size: 16px;">({len(st.session_state["jd_match_results"])} total)</span></h3>', unsafe_allow_html=True)
                st.markdown(f'<p style="color: {text_muted}; font-size: 14px; margin-top: 5px;">Candidates ranked by semantic similarity to your JD.</p>', unsafe_allow_html=True)
            with res_col2:
                score_filter = st.selectbox(
                    "Filter",
                    options=["All Candidates", "Score > 80", "Score > 70", "Score > 60", "Score > 50"],
                    index=0,
                    label_visibility="collapsed"
                )
                
            df_to_show = st.session_state["jd_match_results"].copy()
            
            if score_filter == "Score > 80":
                df_to_show = df_to_show[df_to_show["Match Score (%)"] > 80]
            elif score_filter == "Score > 70":
                df_to_show = df_to_show[df_to_show["Match Score (%)"] > 70]
            elif score_filter == "Score > 60":
                df_to_show = df_to_show[df_to_show["Match Score (%)"] > 60]
            elif score_filter == "Score > 50":
                df_to_show = df_to_show[df_to_show["Match Score (%)"] > 50]
            elif score_filter == "All Candidates":
                df_to_show = df_to_show.sort_values(by="Candidate ID", ascending=True)
            
            if not df_to_show.empty:
                h1, h2, h3 = st.columns([3, 1, 2])
                with h1: st.markdown(f'<div style="color: {text_muted}; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; padding-left: 10px;">Candidate Profile</div>', unsafe_allow_html=True)
                with h2: st.markdown(f'<div style="color: {text_muted}; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Experience</div>', unsafe_allow_html=True)
                with h3: st.markdown(f'<div style="color: {text_muted}; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Match Score</div>', unsafe_allow_html=True)
                
                st.markdown(f"<hr style='margin: 10px 0; border-top: 2px solid {border_color};'>", unsafe_allow_html=True)
                
                for i, (_, row) in enumerate(df_to_show.iterrows()):
                    rank = i + 1
                    cid = row["Candidate ID"]
                    name = row["Name"]
                    score = row["Match Score (%)"]
                    exp = row["Experience (Yrs)"]
                    
                    if st.session_state.get("blind_mode", False):
                        initials = "🕵️"
                    else:
                        initials = "".join([n[0] for n in str(name).split()[:2]]) if name and name != "Unknown" else "??"
                    
                    if score >= 80:
                        score_color = "#10b981"
                    elif score >= 60:
                        score_color = "#3b82f6"
                    elif score >= 40:
                        score_color = "#f59e0b"
                    else:
                        score_color = "#64748b"
                        
                    c1, c2, c3 = st.columns([3, 1, 2])
                    
                    with c1:
                        st.markdown(f"""
                        <div style="display: flex; align-items: center; gap: 15px; padding: 5px 0;">
                            <div style="width: 24px; font-weight: 800; color: {text_muted}; font-size: 13px;">#{rank}</div>
                            <div style="width: 36px; height: 36px; border-radius: 50%; background: {border_color}; color: {text_main}; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px; flex-shrink: 0;">{initials}</div>
                            <div>
                                <div style="font-weight: 600; color: {text_main}; font-size: 14px;">{name}</div>
                                <div style="color: {text_muted}; font-size: 11px;">{cid}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    with c2:
                        st.markdown(f"""
                        <div style="text-align: left; padding: 10px 0;">
                            <div style="font-weight: 600; color: {text_muted}; font-size: 14px;">{exp} Yrs</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    with c3:
                        st.markdown(f"""
                        <div style="display: flex; align-items: center; gap: 10px; padding: 8px 0;">
                            <div style="font-weight: 800; color: {score_color}; font-size: 14px; width: 45px;">{score:.2f}%</div>
                            <div style="flex-grow: 1; background: {border_color}; height: 6px; border-radius: 3px; overflow: hidden;">
                                <div style="width: {score:.2f}%; background: {score_color}; height: 100%; border-radius: 3px;"></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    with st.expander("🤖 AI Match Reasoning"):
                        if score >= 80:
                            st.write("✨ **High Semantic Overlap**: The candidate's background perfectly aligns with the core requirements of the job description. The Sentence Transformer model detected strong contextual synonym matching.")
                        elif score >= 60:
                            st.write("✅ **Moderate Semantic Overlap**: The candidate possesses many of the required concepts, but may be missing specific niche terminology mentioned in the JD.")
                        else:
                            st.write("⚠️ **Low Semantic Overlap**: The candidate's primary experience domain does not strongly align with the core context of this role.")
                            
                    st.markdown(f"<hr style='margin: 5px 0; border-top: 1px solid {row_border};'>", unsafe_allow_html=True)
            else:
                st.info("No candidates meet the selected score criteria.")
                
            st.markdown('<br>', unsafe_allow_html=True)
            csv = df_to_show.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Export Shortlist to CSV",
                data=csv,
                file_name='candidate_shortlist.csv',
                mime='text/csv',
            )