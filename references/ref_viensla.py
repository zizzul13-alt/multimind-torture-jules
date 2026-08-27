from fasthtml.common import *

def render_viensla_proof():
    """
    Reference D — Viens-là Typography / Editorial Navigation Benchmark Slice
    Key characteristics:
    - Typography-led composition (oversized headline scale, strict editorial grid)
    - Unusual navigation & layout alignment (vertical/horizontal editorial axis)
    - Microinteractions & interactive hover pointer state
    - High contrast, restrained editorial elegance
    """
    return Div(
        Header(
            Div("VIENS-LÀ // EDITORIAL MULTIMIND", cls="vl-brand"),
            Nav(
                A("JOURNAL", href="#", cls="vl-nav-link active"),
                A("INDEX", href="#", cls="vl-nav-link"),
                A("ABOUT", href="#", cls="vl-nav-link"),
                cls="vl-nav"
            ),
            cls="vl-header"
        ),

        # Oversized Editorial Typography Hero Section
        Section(
            Div(
                Div("ISSUE N° 04 / SYNTHESIS", cls="vl-issue-tag"),
                H1("TYPOGRAPHY AS ARCHITECTURE.", cls="vl-title-hero"),
                Div(
                    P(
                        "Exploring editorial layouts where typographic scale establishes hierarchy "
                        "and structural rhythm without administrative visual clutter.",
                        cls="vl-hero-lead"
                    ),
                    Div("SCROLL FOR EDITORIAL GRID →", cls="vl-hero-scroll-prompt"),
                    cls="vl-hero-meta"
                ),
                cls="vl-hero-grid"
            ),
            cls="vl-hero-section"
        ),

        # Editorial Horizontal / Vertical Asymmetric Grid Showcase
        Section(
            Div(
                Div(
                    Span("01 / DEBATE MORPHOLOGY", cls="vl-col-num"),
                    H3("ASYMMETRIC COLUMNS", cls="vl-col-title"),
                    P("Text blocks aligned along rigorous vertical axes create tension and structural clarity."),
                    cls="vl-col"
                ),
                Div(
                    Span("02 / MICROINTERACTIONS", cls="vl-col-num"),
                    H3("POINTER FEEDBACK", cls="vl-col-title"),
                    P("Subtle kinetic feedback on typography highlights active thought streams."),
                    cls="vl-col"
                ),
                Div(
                    Span("03 / EDITORIAL CONTRAST", cls="vl-col-num"),
                    H3("MONOCHROME DENSITY", cls="vl-col-title"),
                    P("Strict black and white composition emphasizes pure textual substance."),
                    cls="vl-col"
                ),
                cls="vl-editorial-grid"
            ),
            cls="vl-body-section"
        ),

        # Embedded Scoped CSS & Pointer Microinteraction for Viens-là
        Style("""
            .vl-wrapper {
                background: #0d0d0d;
                color: #f5f5f5;
                font-family: 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif;
                min-height: 100vh;
            }
            .vl-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 32px 48px;
                border-bottom: 1px solid rgba(255,255,255,0.12);
            }
            .vl-brand {
                font-size: 0.9rem;
                font-weight: 800;
                letter-spacing: 3px;
                color: #fff;
            }
            .vl-nav { display: flex; gap: 32px; }
            .vl-nav-link {
                color: #777;
                text-decoration: none;
                font-size: 0.8rem;
                letter-spacing: 2px;
                text-transform: uppercase;
                transition: color 0.2s;
            }
            .vl-nav-link:hover, .vl-nav-link.active { color: #fff; }

            .vl-hero-section {
                padding: 100px 48px 80px 48px;
                border-bottom: 1px solid rgba(255,255,255,0.1);
            }
            .vl-hero-grid { max-width: 1300px; margin: 0 auto; }
            .vl-issue-tag {
                font-size: 0.75rem;
                letter-spacing: 4px;
                color: #ff3333;
                font-weight: 700;
                margin-bottom: 24px;
            }
            .vl-title-hero {
                font-size: 4.8rem;
                font-weight: 900;
                line-height: 0.95;
                letter-spacing: -2px;
                margin: 0 0 40px 0;
                color: #ffffff;
                text-transform: uppercase;
            }
            .vl-hero-meta {
                display: flex;
                justify-content: space-between;
                align-items: flex-end;
                gap: 40px;
            }
            .vl-hero-lead {
                font-size: 1.25rem;
                color: #aaa;
                max-width: 600px;
                line-height: 1.6;
                margin: 0;
            }
            .vl-hero-scroll-prompt {
                font-size: 0.75rem;
                letter-spacing: 3px;
                color: #666;
            }

            .vl-body-section { padding: 100px 48px; max-width: 1300px; margin: 0 auto; }
            .vl-editorial-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 48px;
            }
            .vl-col {
                border-top: 2px solid #fff;
                padding-top: 24px;
                transition: border-color 0.3s, transform 0.3s;
            }
            .vl-col:hover {
                border-color: #ff3333;
                transform: translateY(-4px);
            }
            .vl-col-num {
                font-size: 0.75rem;
                letter-spacing: 3px;
                color: #ff3333;
                font-weight: 700;
                display: block;
                margin-bottom: 16px;
            }
            .vl-col-title {
                font-size: 1.5rem;
                font-weight: 800;
                margin: 0 0 16px 0;
                color: #fff;
            }
            .vl-col p {
                font-size: 0.95rem;
                color: #888;
                line-height: 1.7;
                margin: 0;
            }

            @media (max-width: 768px) {
                .vl-header { padding: 24px 20px; }
                .vl-hero-section { padding: 60px 20px; }
                .vl-title-hero { font-size: 2.8rem; }
                .vl-hero-meta { flex-direction: column; align-items: flex-start; gap: 20px; }
                .vl-editorial-grid { grid-template-columns: 1fr; gap: 32px; }
            }
        """),
        cls="vl-wrapper"
    )
