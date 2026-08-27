from fasthtml.common import *

def render_dioriviera_proof():
    """
    Reference C — Dioriviera Luxury/Material Benchmark Slice
    Key characteristics:
    - Imagery as layout composition, not card decoration
    - Premium spacing, material layering & textures (sand/paper grain overlay)
    - Strong serif typography (Baskerville / Bodoni feel)
    - Restrained, highly polished presentation
    - Proof that visual sophistication does not require visual clutter
    """
    return Div(
        Header(
            Div("DIORIVIERA // MULTIMIND EDITION", cls="dior-brand"),
            Nav(
                A("COLLECTION", href="#", cls="dior-link"),
                A("MAISON DEBATE", href="#", cls="dior-link active"),
                A("ATELIER", href="#", cls="dior-link"),
                cls="dior-nav"
            ),
            cls="dior-header"
        ),

        # Hero Section with full-bleed material background & editorial text placement
        Section(
            Div(cls="dior-texture-overlay"),
            Div(
                Span("LA MAISON DE DIORIVIERA", cls="dior-kicker"),
                H1("SOPHISTICATED SYNTHESIS", cls="dior-title"),
                P(
                    "An architectural composition of intellect and refinement. "
                    "Where artificial intelligence meets pure material elegance.",
                    cls="dior-lead"
                ),
                Div(
                    A("DISCOVER THE DEBATE", href="#atelier", cls="dior-btn-luxury"),
                    cls="dior-cta-wrap"
                ),
                cls="dior-hero-content"
            ),
            cls="dior-hero"
        ),

        # Luxury Composition Showcase
        Section(
            Div(
                Div(
                    Div(
                        Span("FIGURE I", cls="dior-fig-num"),
                        H2("Harmonious Proportions", cls="dior-fig-title"),
                        P(
                            "Each panel is sculpted with generous negative space, ensuring "
                            "that complex reasoning reads with effortless grace and tranquility.",
                            cls="dior-fig-body"
                        ),
                        cls="dior-text-block"
                    ),
                    Div(
                        Div(
                            Img(src="/static/images/luxury_paper.png", cls="dior-mat-img", alt="Material Texture"),
                            Div("RAW MATERIAL LAYER", cls="dior-mat-label"),
                            cls="dior-mat-frame"
                        ),
                        cls="dior-visual-block"
                    ),
                    cls="dior-editorial-split"
                ),
                id="atelier",
                cls="dior-container"
            ),
            cls="dior-editorial-sec"
        ),

        # Embedded Scoped CSS for Dioriviera luxury aesthetic
        Style("""
            .dior-wrapper {
                background: #f6f4ee;
                color: #2c2a29;
                font-family: 'Georgia', 'Times New Roman', serif;
                min-height: 100vh;
                position: relative;
            }
            .dior-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 32px 64px;
                border-bottom: 1px solid rgba(44, 42, 41, 0.12);
                background: #f6f4ee;
            }
            .dior-brand {
                font-size: 1.1rem;
                letter-spacing: 4px;
                font-weight: 400;
                color: #1a1918;
                text-transform: uppercase;
            }
            .dior-nav { display: flex; gap: 36px; }
            .dior-link {
                color: #666360;
                text-decoration: none;
                font-size: 0.8rem;
                letter-spacing: 3px;
                text-transform: uppercase;
                transition: color 0.3s;
            }
            .dior-link.active, .dior-link:hover { color: #1a1918; }

            .dior-hero {
                position: relative;
                padding: 120px 64px;
                text-align: center;
                background: url('/static/images/luxury_paper.png') repeat;
                border-bottom: 1px solid rgba(44, 42, 41, 0.1);
            }
            .dior-hero-content {
                max-width: 800px;
                margin: 0 auto;
            }
            .dior-kicker {
                font-size: 0.75rem;
                letter-spacing: 5px;
                color: #8c857b;
                text-transform: uppercase;
                display: block;
                margin-bottom: 24px;
            }
            .dior-title {
                font-size: 3.8rem;
                font-weight: 300;
                letter-spacing: 2px;
                line-height: 1.15;
                margin: 0 0 24px 0;
                color: #1a1918;
            }
            .dior-lead {
                font-size: 1.25rem;
                color: #55514e;
                line-height: 1.8;
                font-style: italic;
                margin-bottom: 48px;
            }
            .dior-btn-luxury {
                display: inline-block;
                padding: 16px 40px;
                border: 1px solid #1a1918;
                color: #1a1918;
                text-decoration: none;
                font-size: 0.75rem;
                letter-spacing: 4px;
                text-transform: uppercase;
                transition: background 0.3s, color 0.3s;
            }
            .dior-btn-luxury:hover {
                background: #1a1918;
                color: #f6f4ee;
            }

            .dior-editorial-sec { padding: 100px 64px; }
            .dior-container { max-width: 1200px; margin: 0 auto; }
            .dior-editorial-split {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 80px;
                align-items: center;
            }
            .dior-fig-num {
                font-size: 0.75rem;
                letter-spacing: 4px;
                color: #a0988e;
                display: block;
                margin-bottom: 16px;
            }
            .dior-fig-title {
                font-size: 2.4rem;
                font-weight: 300;
                margin: 0 0 24px 0;
                color: #1a1918;
            }
            .dior-fig-body {
                font-size: 1.1rem;
                line-height: 1.8;
                color: #55514e;
                margin: 0;
            }
            .dior-mat-frame {
                position: relative;
                padding: 20px;
                border: 1px solid rgba(44, 42, 41, 0.15);
                background: #fff;
                box-shadow: 0 30px 60px rgba(0,0,0,0.05);
            }
            .dior-mat-img {
                width: 100%;
                height: 320px;
                object-fit: cover;
                display: block;
            }
            .dior-mat-label {
                position: absolute;
                bottom: -12px;
                right: 24px;
                background: #1a1918;
                color: #fff;
                font-size: 0.65rem;
                letter-spacing: 3px;
                padding: 6px 14px;
            }

            @media (max-width: 768px) {
                .dior-header { padding: 24px 20px; }
                .dior-hero { padding: 60px 20px; }
                .dior-title { font-size: 2.4rem; }
                .dior-editorial-split { grid-template-columns: 1fr; gap: 40px; }
            }
        """),
        cls="dior-wrapper"
    )
