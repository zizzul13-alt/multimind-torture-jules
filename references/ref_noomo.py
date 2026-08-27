from fasthtml.common import *

def render_noomo_proof():
    """
    Reference B — Noomo Labs / Agency-Style Interaction Benchmark Slice
    Key characteristics:
    - Unusual interaction & scroll-linked fluid motion
    - 3D spatial card depth & dynamic cursor-aware tilt state
    - Interactive composition & non-standard navigation behavior
    - Mobile-specific choreography
    """
    return Div(
        Header(
            Div("NOOMO // AGENCY EXPERIMENTAL", cls="noomo-brand"),
            Nav(
                Span("01 EXPERIMENTS", cls="noomo-nav-item active"),
                Span("02 LABS", cls="noomo-nav-item"),
                Span("03 SPATIAL", cls="noomo-nav-item"),
                cls="noomo-nav"
            ),
            cls="noomo-header"
        ),

        # Hero Section with scroll-linked 3D transform visual
        Section(
            Div(
                H1(
                    Span("FLUID", cls="word-accent"),
                    Span(" INTERACTION "),
                    Span("MATRIX", cls="word-accent-alt"),
                    cls="noomo-hero-title"
                ),
                P("Exploring multi-agent spatial topologies with scroll-synchronized gesture controls.", cls="noomo-sub"),
                cls="noomo-hero-text"
            ),
            # Interactive 3D Spatial Canvas Simulation
            Div(
                Div(
                    Div(
                        Div("NODE_01", cls="node-badge"),
                        H4("SYNAPTIC FLOW"),
                        P("Real-time vector interpolation"),
                        cls="spatial-card card-a"
                    ),
                    Div(
                        Div("NODE_02", cls="node-badge-alt"),
                        H4("DEBATE WAVE"),
                        P("Harmonic consensus oscillation"),
                        cls="spatial-card card-b"
                    ),
                    Div(
                        Div("NODE_03", cls="node-badge"),
                        H4("LATENT SPACE"),
                        P("Non-Euclidean agent mapping"),
                        cls="spatial-card card-c"
                    ),
                    id="spatial-container",
                    cls="spatial-container"
                ),
                cls="noomo-stage"
            ),
            cls="noomo-hero"
        ),

        # Scroll Interactive Showcase Section
        Section(
            H2("SCROLL-LINKED CHOREOGRAPHY", cls="noomo-sec-title"),
            Div(
                Div("SCROLL TO ROTATE & INTERPOLATE SPATIAL LAYERS", cls="noomo-instruction"),
                Div(
                    Div(
                        H3("01 / Dynamic Tilt"),
                        P("Spatial perspective reacts dynamically to scroll velocity and viewport offset."),
                        cls="noomo-feature"
                    ),
                    Div(
                        H3("02 / Non-Standard Layout"),
                        P("Elements break traditional grid boundaries to create memorable visual momentum."),
                        cls="noomo-feature"
                    ),
                    Div(
                        H3("03 / Responsive Fluidity"),
                        P("Mobile viewports recompose spatial cards into a horizontal snap-scroll carousels."),
                        cls="noomo-feature"
                    ),
                    cls="noomo-features-grid"
                ),
                cls="noomo-scroll-wrapper"
            ),
            cls="noomo-body"
        ),

        # Embedded Scoped CSS & JS for Noomo Labs scroll-linked behavior
        Style("""
            .noomo-wrapper {
                background: #050508;
                color: #f0f0f5;
                font-family: 'Helvetica Neue', Arial, sans-serif;
                min-height: 100vh;
                overflow-x: hidden;
            }
            .noomo-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 24px 40px;
                border-bottom: 1px solid rgba(255,255,255,0.08);
            }
            .noomo-brand {
                font-weight: 800;
                letter-spacing: 3px;
                font-size: 0.9rem;
                color: #fff;
            }
            .noomo-nav { display: flex; gap: 24px; }
            .noomo-nav-item {
                font-size: 0.8rem;
                letter-spacing: 2px;
                color: #666677;
                cursor: pointer;
                transition: color 0.2s;
            }
            .noomo-nav-item.active, .noomo-nav-item:hover { color: #7000ff; }

            .noomo-hero {
                padding: 60px 40px;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 40px;
                align-items: center;
                min-height: 75vh;
            }
            .noomo-hero-title {
                font-size: 3.5rem;
                font-weight: 900;
                line-height: 1.05;
                letter-spacing: -1px;
                margin: 0 0 24px 0;
            }
            .word-accent { color: #7000ff; }
            .word-accent-alt { color: #00f0ff; }
            .noomo-sub {
                font-size: 1.1rem;
                color: #9999aa;
                line-height: 1.6;
                max-width: 480px;
            }

            .noomo-stage {
                perspective: 1000px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 400px;
            }
            .spatial-container {
                position: relative;
                width: 320px;
                height: 320px;
                transform-style: preserve-3d;
                transition: transform 0.1s ease-out;
            }
            .spatial-card {
                position: absolute;
                width: 240px;
                padding: 24px;
                border-radius: 16px;
                background: rgba(20, 20, 32, 0.8);
                border: 1px solid rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(12px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.6);
                transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
            }
            .card-a { top: 0; left: 0; transform: translateZ(40px) rotate(-6deg); }
            .card-b { top: 60px; left: 80px; transform: translateZ(80px) rotate(4deg); border-color: rgba(112, 0, 255, 0.5); }
            .card-c { top: 140px; left: 20px; transform: translateZ(120px) rotate(-2deg); border-color: rgba(0, 240, 255, 0.5); }

            .node-badge {
                font-size: 0.65rem;
                font-weight: 800;
                color: #00f0ff;
                letter-spacing: 2px;
                margin-bottom: 8px;
            }
            .node-badge-alt {
                font-size: 0.65rem;
                font-weight: 800;
                color: #7000ff;
                letter-spacing: 2px;
                margin-bottom: 8px;
            }
            .spatial-card h4 { margin: 0 0 6px 0; font-size: 1.1rem; color: #fff; }
            .spatial-card p { margin: 0; font-size: 0.85rem; color: #aaa; }

            .noomo-body { padding: 80px 40px; }
            .noomo-sec-title {
                font-size: 2rem;
                letter-spacing: 2px;
                margin-bottom: 8px;
            }
            .noomo-instruction {
                font-size: 0.75rem;
                letter-spacing: 3px;
                color: #00f0ff;
                margin-bottom: 40px;
            }
            .noomo-features-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 32px;
            }
            .noomo-feature {
                background: rgba(15, 15, 24, 0.6);
                border: 1px solid rgba(255,255,255,0.08);
                padding: 32px;
                border-radius: 12px;
            }
            .noomo-feature h3 { font-size: 1.2rem; color: #fff; margin-0 0 12px 0; }
            .noomo-feature p { color: #888899; line-height: 1.6; margin: 0; font-size: 0.95rem; }

            @media (max-width: 768px) {
                .noomo-hero { grid-template-columns: 1fr; padding: 40px 20px; }
                .noomo-hero-title { font-size: 2.2rem; }
                .noomo-features-grid { grid-template-columns: 1fr; }
                .spatial-container { width: 100%; }
            }
        """),
        Script("""
            window.addEventListener('scroll', () => {
                const scrolled = window.scrollY;
                const container = document.getElementById('spatial-container');
                if (container) {
                    const rotX = (scrolled * 0.05) % 20;
                    const rotY = (scrolled * 0.08) % 30;
                    container.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg)`;
                }
            });
        """),
        cls="noomo-wrapper"
    )
