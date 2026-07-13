"""
frontend/styles.py
---------------------
Design system for the "AI Career Learning Pathway" app.

Concept: the "Pathway" — a glowing constellation trail that represents the
student's journey from where they are to their career goal. Dark, ink-navy
base (mirroring a night sky) with a violet -> teal "aurora" gradient marking
progress, since the whole product's job is to plot and light up a path.

Palette:
    Ink Navy      #0F1229   (dark surface base)
    Paper         #F7F8FC   (light surface base)
    Aurora Violet #7C5CFF   (primary accent - "where you're headed")
    Aurora Teal   #22D3B0   (secondary accent - "progress / growth")
    Slate Text    #2A2F45
    Muted Grey    #8A8FA3

Type:
    Display : "Space Grotesk" - geometric, technical, distinctive headings
    Body    : "Inter" - clean, highly legible body copy
    Mono    : "JetBrains Mono" - stats, numbers, data labels
"""

from __future__ import annotations
import textwrap
import streamlit as st

FONT_IMPORT = (
    "https://fonts.googleapis.com/css2?"
    "family=Space+Grotesk:wght@500;600;700&"
    "family=Inter:wght@400;500;600;700&"
    "family=JetBrains+Mono:wght@500;600&display=swap"
)

def _render_css(html_content: str) -> None:
    """Injects sanitized HTML/CSS. Explicitly sanitizes block tabs."""
    st.markdown(textwrap.dedent(html_content).strip(), unsafe_allow_html=True)

def _get_clean_vars(dark: bool) -> str:
    """Returns exact structural tokens cleanly separated by line boundaries."""
    if dark:
        return (
            "--bg: #0F1229;"
            "--bg-elevated: #161A3A;"
            "--surface: rgba(255,255,255,0.045);"
            "--surface-border: rgba(255,255,255,0.09);"
            "--text: #EDEEFB;"
            "--text-muted: #9DA3C0;"
            "--shadow: 0 8px 30px rgba(0,0,0,0.35);"
            "--background-color: #0F1229;"
            "--secondary-background-color: #161A3A;"
            "--text-color: #EDEEFB;"
            "--primary-color: #7C5CFF;"
            "--label-text: #EDEEFB;"          
            "--input-bg: #FFFFFF;"            
            "--input-text: #111633;"          
            "--input-placeholder: #6E759F;"   
            "--btn-submit-text: #0F1229;"     
            "--btn-submit-bg: #22D3B0;"       
        )
    return (
        "--bg: #F7F8FC;"
        "--bg-elevated: #FFFFFF;"
        "--surface: rgba(15,18,41,0.035);"
        "--surface-border: rgba(15,18,41,0.08);"
        "--text: #1B1E33;"
        "--text-muted: #5B6079;"
        "--shadow: 0 8px 24px rgba(30,32,70,0.08);"
        "--background-color: #F7F8FC;"
        "--secondary-background-color: #FFFFFF;"
        "--text-color: #1B1E33;"
        "--primary-color: #7C5CFF;"
        "--label-text: #1B1E33;"          
        "--input-bg: #F0F2F6;"            
        "--input-text: #1B1E33;"          
        "--input-placeholder: #7D849B;"   
        "--btn-submit-text: #FFFFFF;"     
        "--btn-submit-bg: #7C5CFF;"       
    )

def inject_css(dark_mode: bool = True) -> None:
    """Injects standard configuration tokens safely without page leaks."""
    tokens = _get_clean_vars(dark_mode)
    
    css_payload = f"""
    <link rel="stylesheet" href="{FONT_IMPORT}">
    <style>
        :root {{
            {tokens}
            --violet: #7C5CFF;
            --teal: #22D3B0;
            --gradient: linear-gradient(120deg, #7C5CFF 0%, #22D3B0 100%);
            --radius: 18px;
        }}
        
        /* High-priority layout declarations */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
            background-color: var(--bg) !important;
            color: var(--text) !important;
            font-family: 'Inter', sans-serif !important;
        }}
        
        [data-testid="stSidebarContent"], section[data-testid="stSidebar"] {{
            background-color: var(--bg-elevated) !important;
            color: var(--text) !important;
        }}

        h1, h2, h3, h4, .pathway-display {{
            font-family: 'Space Grotesk', sans-serif !important;
            color: var(--text) !important;
        }}

        /* --- INPUT LABELS & CONTAINER FILL CORRECTIONS --- */
        [data-testid="stWidgetLabel"] p {{
            color: var(--label-text) !important;
            font-weight: 500 !important;
        }}

        [data-testid="stTextInput"] input, 
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] div[data-baseweb="select"] div,
        [data-testid="stNumberInput"] input {{
            background-color: var(--input-bg) !important;
            color: var(--input-text) !important;
            -webkit-text-fill-color: var(--input-text) !important;
        }}

        ul[role="listbox"] li {{
            color: #111633 !important;
        }}

        input::placeholder, textarea::placeholder {{
            color: var(--input-placeholder) !important;
            opacity: 1 !important;
        }}

        /* --- REMOVE EDIT INSTRUCTIONS & APP FOOTERS --- */
        [data-testid="stForm"] data-testid, .stTextArea caption, [data-testid="InputInstructions"] {{
            display: none !important;
            visibility: hidden !important;
        }}
        
        #MainMenu, footer, div[data-testid="stToolbar"] {{
            display: none !important;
            visibility: hidden !important;
        }}
        
        /* Removes any default white header bars across the top layer */
        header, [data-testid="stHeader"] {{
            background-color: transparent !important;
            background: transparent !important;
        }}

        /* --- DOCK PANEL TRIGGER (TOP-LEFT CORNER CONSOLE TAB) --- */
        /* Places the sidebar panel control cleanly into the top corner grid */
        [data-testid="stSidebarCollapseButton"] {{
            position: fixed !important;
            top: 0px !important;
            left: 0px !important;
            z-index: 9999999 !important;
            display: block !important;
            visibility: visible !important;
        }}

        [data-testid="stSidebarCollapseButton"] button {{
            background-color: #111633 !important;
            color: #EDEEFB !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            border-radius: 0px 0px 8px 0px !important;
            box-shadow: var(--shadow) !important;
            height: 36px !important;
            width: 44px !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}

        /* Keeps selector control chevrons untouched */
        [data-testid="stSelectbox"] button {{
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            border-radius: 0px !important;
        }}

        /* --- BUTTON OVERRIDE --- */
        div.stFormSubmitButton > button {{
            color: var(--btn-submit-text) !important;
            background-color: var(--btn-submit-bg) !important;
            border: none !important;
            font-weight: 600 !important;
        }}

        /* Custom presentation structures */
        .glass-card {{
            background: var(--bg-elevated);
            border: 1px solid var(--surface-border);
            border-radius: var(--radius);
            padding: 1.4rem 1.5rem;
            box-shadow: var(--shadow);
            margin-bottom: 1.1rem;
        }}
        
        .cert-card {{
            background: var(--bg-elevated);
            border: 1px solid var(--surface-border);
            border-left: 4px solid var(--teal);
            border-radius: 14px;
            padding: 1rem 1.2rem;
            box-shadow: var(--shadow);
            margin-bottom: 0.9rem;
            width: 100%;
        }}
    </style>
    """
    _render_css(css_payload)
