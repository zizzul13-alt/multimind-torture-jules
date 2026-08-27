from fasthtml.common import *

def render_arknights_proof():
    """
    Reference A — Arknights Global Benchmark Slice
    Key characteristics:
    - Tactical layered visual materials (background texture, angled masks, overlay status strips)
    - Strong art direction & non-generic typography (monospace technical headers, high-contrast badges)
    - Interactive loading & scroll-linked motion choreography
    - Responsive identity
    """
    return Div(
        # Top Navigation Bar with tactical HUD aesthetic
        Header(
            Div(
                Span("RHODES // MM-SYSTEM", cls="tactical-logo"),
                Span("STATUS: ONLINE [SECURE_NODE_09]", cls="tactical-status"),
                Nav(
                    A("OPERATIONS", href="#ops", cls="hud-link active"),
                    A("INTEL", href="#intel", cls="hud-link"),
                    A("ARCHIVE", href="#archive", cls="hud-link"),
                    cls="hud-nav"
                ),
                cls="hud-header-inner"
            ),
            cls="hud-header"
        ),

        # Hero Section with layered background, angled hazard accents, and interactive state trigger
        Section(
            Div(cls="ark-bg-layer"),
            Div(cls="ark-grid-overlay"),
            Div(
                Div(
                    Span("CLASSIFIED ACCESS // LEVEL 4", cls="ark-tag"),
                    H1("PROJECT ARK-MULTIMIND", cls="ark-title"),
                    P("AUTONOMOUS DEBATE & SYNTHESIS PROTOCOL — TACTICAL INTERFACE", cls="ark-subtitle"),
                    Div(
                        Button(
                            "INITIALIZE PROTOCOL",
                            cls="ark-btn-primary",
                            hx_post="/ref/arknights/deploy",
                            hx_target="#ark-deploy-status",
                            hx_swap="innerHTML"
                        ),
                        A("EXPLORE INTEL", href="#scroll-target", cls="ark-btn-secondary"),
                        cls="ark-btn-group"
                    ),
                    Div(id="ark-deploy-status", cls="ark-status-output"),
                    cls="ark-hero-content"
                ),
                Div(
                    Div(
                        Img(src="/static/images/ambient_loader.gif", cls="ark-loader-img", alt="Loading Core"),
                        Div("CORE ENGINE INITIALIZING...", cls="ark-loader-text"),
                        cls="ark-loader-box"
                    ),
                    cls="ark-hero-visual"
                ),
                cls="ark-hero-grid"
            ),
            cls="ark-hero-section"
        ),

        # Scroll Choreography Section: Layered Tactical Cards & Parallax Strips
        Section(
            H2("SYSTEM ARCHITECTURE & LAYERED RECONNAISSANCE", cls="ark-sec-title"),
            Div(
                Div(
                    Div("01 // TACTICAL SYNTHESIS", cls="card-code"),
                    H3("Multi-Agent Debate Matrix", cls="card-head"),
                    P("Real-time consensus scoring across divergent LLM agent personas under adverse conditions."),
                    cls="ark-card"
                ),
                Div(
                    Div("02 // PARALLAX RECON", cls="card-code"),
                    H3("Spatial Stream Isolation", cls="card-head"),
                    P("Dynamic material layering isolates high-priority alerts from background log telemetry."),
                    cls="ark-card"
                ),
                Div(
                    Div("03 // FAULT TOLERANCE", cls="card-code"),
                    H3("Zero-Refresh Mutation", cls="card-head"),
                    P("Presentation state morphs in place without terminating the live tactical stream."),
                    cls="ark-card"
                ),
                cls="ark-cards-grid"
            ),
            id="scroll-target",
            cls="ark-body-section"
        ),

        # Embedded Scoped CSS for Arknights Reference
        Style("""
            .arknights-wrapper {
                background: #090d14;
                color: #e0e6ed;
                font-family: 'Courier New', Courier, monospace, sans-serif;
                min-height: 100vh;
                position: relative;
                overflow-x: hidden;
            }
            .hud-header {
                background: rgba(10, 15, 24, 0.95);
                border-bottom: 2px solid #00e6c8;
                padding: 12px 24px;
                position: sticky;
                top: 0;
                z-index: 100;
                backdrop-filter: blur(8px);
            }
            .hud-header-inner {
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1400px;
                margin: 0 auto;
            }
            .tactical-logo {
                font-weight: 900;
                letter-spacing: 2px;
                color: #00e6c8;
                font-size: 1.1rem;
            }
            .tactical-status {
                font-size: 0.8rem;
                color: #ffb400;
                background: rgba(255, 180, 0, 0.1);
                padding: 4px 8px;
                border: 1px solid #ffb400;
            }
            .hud-nav { display: flex; gap: 16px; }
            .hud-link {
                color: #8a9ba8;
                text-decoration: none;
                font-size: 0.85rem;
                letter-spacing: 1px;
                transition: color 0.2s;
            }
            .hud-link:hover, .hud-link.active { color: #00e6c8; }

            .ark-hero-section {
                position: relative;
                padding: 80px 24px;
                min-height: 80vh;
                display: flex;
                align-items: center;
                background: url('/static/images/tactical_grid.png') repeat;
            }
            .ark-hero-grid {
                max-width: 1400px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 48px;
                align-items: center;
                width: 100%;
                z-index: 2;
                position: relative;
            }
            .ark-tag {
                background: #ff0055;
                color: #fff;
                font-size: 0.75rem;
                font-weight: 700;
                padding: 4px 10px;
                letter-spacing: 2px;
                display: inline-block;
                margin-bottom: 16px;
                clip-path: polygon(0 0, 100% 0, 92% 100%, 0 100%);
            }
            .ark-title {
                font-size: 3rem;
                font-weight: 900;
                letter-spacing: 2px;
                line-height: 1.1;
                color: #ffffff;
                margin: 0 0 16px 0;
                text-shadow: 0 0 20px rgba(0, 230, 200, 0.3);
            }
            .ark-subtitle {
                font-size: 1rem;
                color: #9aaec4;
                margin-bottom: 32px;
                line-height: 1.6;
            }
            .ark-btn-group { display: flex; gap: 16px; flex-wrap: wrap; }
            .ark-btn-primary {
                background: #00e6c8;
                color: #090d14;
                border: none;
                padding: 14px 28px;
                font-weight: 800;
                letter-spacing: 1.5px;
                cursor: pointer;
                clip-path: polygon(0 0, 100% 0, 90% 100%, 0 100%);
                transition: transform 0.15s, background 0.15s;
            }
            .ark-btn-primary:hover {
                background: #00ffd5;
                transform: translateY(-2px);
            }
            .ark-btn-secondary {
                border: 1px solid #30455c;
                color: #e0e6ed;
                padding: 14px 28px;
                text-decoration: none;
                font-weight: 700;
                letter-spacing: 1px;
                display: inline-block;
            }
            .ark-status-output {
                margin-top: 20px;
                font-size: 0.9rem;
                color: #00e6c8;
                min-height: 24px;
            }
            .ark-loader-box {
                background: rgba(15, 23, 36, 0.85);
                border: 1px solid #1e2d42;
                border-left: 4px solid #00e6c8;
                padding: 32px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }
            .ark-loader-img {
                width: 120px;
                height: 120px;
                border-radius: 50%;
                margin-bottom: 16px;
            }
            .ark-loader-text {
                font-weight: 700;
                color: #ffb400;
                letter-spacing: 2px;
                font-size: 0.85rem;
            }
            .ark-body-section {
                padding: 80px 24px;
                max-width: 1400px;
                margin: 0 auto;
            }
            .ark-sec-title {
                font-size: 1.8rem;
                border-left: 4px solid #ff0055;
                padding-left: 16px;
                margin-bottom: 40px;
                letter-spacing: 1px;
            }
            .ark-cards-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 24px;
            }
            .ark-card {
                background: rgba(16, 25, 40, 0.7);
                border: 1px solid #1e2d42;
                padding: 28px;
                position: relative;
                transition: border-color 0.2s, transform 0.2s;
            }
            .ark-card:hover {
                border-color: #00e6c8;
                transform: translateY(-4px);
            }
            .card-code {
                color: #ff0055;
                font-size: 0.8rem;
                font-weight: 700;
                margin-bottom: 12px;
            }
            .card-head { font-size: 1.3rem; margin: 0 0 12px 0; color: #fff; }

            @media (max-width: 768px) {
                .ark-hero-grid { grid-template-columns: 1fr; gap: 32px; }
                .ark-title { font-size: 2rem; }
                .hud-status { display: none; }
            }
        """),
        cls="arknights-wrapper"
    )

def handle_arknights_deploy():
    return Div(
        Span("✔ PROTOCOL ARK-9 ACTIVATED — ALL AGENTS SYNCED TO MESH", style="color: #00e6c8; font-weight: bold;")
    )
