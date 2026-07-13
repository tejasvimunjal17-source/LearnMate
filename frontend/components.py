"""
frontend/components.py
-------------------------
Reusable, presentation-only Streamlit UI components. Keeping these separate
from app.py keeps the main entrypoint thin and makes components testable /
reusable across pages.

All HTML-emitting helpers route through `_md()`, which dedents the string
before handing it to st.markdown(). Without this, any triple-quoted HTML
string written inside an indented function body carries 4+ spaces of
leading whitespace on every line - which CommonMark (Streamlit's markdown
parser) treats as an "indented code block" and renders as literal visible
text instead of parsing as HTML. See frontend/styles.py for the full
explanation; the same bug class applies to every component here, so the
fix is centralized in one helper rather than patched call-by-call.
"""

from __future__ import annotations

import textwrap
from typing import Any

import streamlit as st

PRIORITY_CLASS = {"High": "pill-high", "Medium": "pill-medium", "Low": "pill-low"}


def _md(html: str, target: Any = None) -> None:
    """Dedent + render raw HTML. `target` lets callers pass a column/container."""
    renderer = target if target is not None else st
    renderer.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


def hero(eyebrow: str, title: str, subtitle: str = "") -> None:
    _md(f"""
        <div class="hero">
            <span class="hero-eyebrow">{eyebrow}</span>
            <h1>{title}</h1>
            <p class="muted" style="max-width:640px;">{subtitle}</p>
        </div>
        """)


def metric_card(label: str, value: str, col=None) -> None:
    _md(f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, target=col)


def cert_card(text: str, col=None, icon: str = "🏅") -> None:
    """
    Certification/course-name card.

    Deliberately NOT metric_card: certification names are full sentences
    ("Professional Certificate in Business Analytics (Coursera/edX)"), not
    short numeric stats. Reusing metric_card's large centered display font
    for that kind of text is what made the Courses & Certifications page
    look cramped/messy - long strings either overflowed the card or forced
    an oversized, awkwardly wrapped heading. This uses a compact, left
    aligned, properly wrapping layout instead.
    """
    _md(f"""
        <div class="cert-card">
            <div class="cert-icon">{icon}</div>
            <div class="cert-text">{text}</div>
        </div>
        """, target=col)


def glass_card_open(title: str = "") -> None:
    heading = f"<h3 style='margin-top:0'>{title}</h3>" if title else ""
    _md(f"<div class='glass-card'>{heading}")


def glass_card_close() -> None:
    _md("</div>")


def progress_bar(percent: int, label: str = "") -> None:
    percent = max(0, min(100, percent))
    label_html = f"<div class='muted' style='font-size:0.8rem;margin-bottom:4px;'>{label}</div>" if label else ""
    _md(f"""
        {label_html}
        <div class="progress-track">
            <div class="progress-fill" style="width:{percent}%;"></div>
        </div>
        <div class="mono muted" style="font-size:0.75rem;margin-top:3px;">{percent}% complete</div>
        """)


def pill(text: str, variant: str = "") -> str:
    cls = f"pill {variant}".strip()
    return f"<span class='{cls}'>{text}</span>"


def pill_row(items: list[str], variant: str = "") -> None:
    _md("".join(pill(i, variant) for i in items))


def milestone_node(milestone: dict[str, Any]) -> None:
    week = milestone.get("week", "?")
    title = milestone.get("title", "")
    skills = milestone.get("key_skills", [])
    courses = milestone.get("recommended_courses", [])
    project = milestone.get("mini_project", "")
    tasks = milestone.get("practice_tasks", [])

    with st.container():
        _md(f"""
            <div class="pathway-node">
                <span class="week-chip">WEEK {week}</span>
                <h4 style="margin:0 0 6px 0;">{title}</h4>
            </div>
            """)
        c1, c2 = st.columns(2)
        with c1:
            if skills:
                st.markdown("**🎯 Key Skills**")
                pill_row(skills)
            if project:
                st.markdown(f"**🛠️ Mini Project**  \n{project}")
        with c2:
            if courses:
                st.markdown("**📚 Recommended Courses**")
                for c in courses:
                    st.markdown(f"- {c}")
            if tasks:
                st.markdown("**✅ Practice Tasks**")
                for t in tasks:
                    st.markdown(f"- {t}")
        _md("<div style='height:6px'></div>")


def skill_gap_row(gap: dict[str, Any]) -> None:
    priority = gap.get("priority", "Medium")
    cls = PRIORITY_CLASS.get(priority, "")
    c1, c2, c3, c4 = st.columns([3, 2, 2, 1.4])
    c1.markdown(f"**{gap.get('skill', '-')}**")
    _md(f"<span class='mono muted'>{gap.get('current_level', '-')}</span>", target=c2)
    _md(f"<span class='mono muted'>&rarr; {gap.get('required_level', '-')}</span>", target=c3)
    _md(pill(priority, cls), target=c4)


def empty_state(icon: str, message: str) -> None:
    _md(f"""
        <div class="glass-card" style="text-align:center; padding:2.4rem;">
            <div style="font-size:2.2rem;">{icon}</div>
            <p class="muted" style="margin-top:0.6rem;">{message}</p>
        </div>
        """)
