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
            "--label-text: #EDEEFB;"          # Crisp bright labels on dark canvas
            "--input-bg: #FFFFFF;"            # White box background
            "--input-text: #111633;"          # Deep dark text inside white boxes
            "--input-placeholder: #6E759F;"   # Readable placeholder text
            "--btn-submit-text: #0F1229;"     # Force deep dark text for the button
            "--btn-submit-bg: #22D3B0;"       # Keep button bright accent
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
        "--label-text: #1B1E33;"          # Dark labels for light mode canvas
        "--input-bg: #F0F2F6;"            # Standard light input box
        "--input-text: #1B1E33;"          # Dark text inside boxes
        "--input-placeholder: #7D849B;"   # Muted placeholder
        "--btn-submit-text: #FFFFFF;"     # White text for light mode button
        "--btn-submit-bg: #7C5CFF;"       # Violet background for light mode
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
        /* Forces the field names above the boxes to stay legible */
        [data-testid="stWidgetLabel"] p {{
            color: var(--label-text) !important;
            font-weight: 500 !important;
        }}

        /* Targets text inputs, textareas, number controls, and drop-down fields */
        [data-testid="stTextInput"] input, 
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] div[data-baseweb="select"] div,
        [data-testid="stNumberInput"] input {{
            background-color: var(--input-bg) !important;
            color: var(--input-text) !important;
            -webkit-text-fill-color: var(--input-text) !important;
        }}

        /* Fixes native dropdown selection lists matching structural background values */
        ul[role="listbox"] li {{
            color: #111633 !important;
        }}

        /* Forces input placeholders to be visible and distinct */
        input::placeholder, textarea::placeholder {{
            color: var(--input-placeholder) !important;
            opacity: 1 !important;
        }}

        /* --- REMOVE EDIT INSTRUCTIONS & APP FOOTERS --- */
        /* Hides the "Press Ctrl+Enter to submit form" helper text label completely */
        [data-testid="stForm"] data-testid, .stTextArea caption, [data-testid="InputInstructions"] {{
            display: none !important;
            visibility: hidden !important;
        }}
        
        /* Hides Streamlit main header toolbar menu and footer branding lines */
        #MainMenu, header, footer {{
            display: none !important;
            visibility: hidden !important;
        }}
        
        div[data-testid="stToolbar"] {{
            display: none !important;
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
