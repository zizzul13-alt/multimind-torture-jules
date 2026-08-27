from fasthtml.common import *

# Expanded deterministic mock conversation (35+ multi-turn messages for Long-Use Usability Test)
MOCK_MESSAGES = [
    {"id": 1, "sender": "user", "author": "Dr. Aris Thorne", "timestamp": "14:00:01", "content": "Initiating system audit on presentation platform target candidates for MultiMind architecture v2."},
    {"id": 2, "sender": "agent_res", "author": "Research Agent", "timestamp": "14:00:05", "content": "OPERATIONAL INDEX:\nCandidate 1: FastHTML (Python Starlette + HTMX hypermedia)\nCandidate 2: Reflex (Python React wrapper)\nCandidate 3: SvelteKit + FastAPI\n\nFastHTML evaluation active."},
    {"id": 3, "sender": "agent_crt", "author": "Critic Agent", "timestamp": "14:00:12", "content": "CRITICAL RISK IDENTIFIED:\nFramework default visual identity (PicoCSS / standard cards) must be stripped. MultiMind demands bespoke material composition and zero-refresh presentation mutation."},
    {"id": 4, "sender": "agent_syn", "author": "Synthesis Agent", "timestamp": "14:00:20", "content": "PROPOSED PROTOCOL:\nImplement two radically distinct visual morphologies (Tactical Operations vs. Editorial Spatial Atelier) and test live hypermedia partial swaps while preserving in-memory conversation state."},
    {"id": 5, "sender": "user", "author": "Dr. Aris Thorne", "timestamp": "14:01:00", "content": "How does FastHTML handle material layering such as tactical grid backgrounds, animated WebP/GIF loaders, and luxury paper grain overlays?"},
    {"id": 6, "sender": "agent_res", "author": "Research Agent", "timestamp": "14:01:08", "content": "MATERIAL EFFICIENCY REPORT:\nBy using static image assets (PNG grid textures, GIF ambient loaders) combined with CSS backdrop filters, material-over-code efficiency reaches 90%. Avoided writing complex custom JS particle loops."},
    {"id": 7, "sender": "agent_crt", "author": "Critic Agent", "timestamp": "14:01:15", "content": "ESCAPE HATCH AUDIT:\nNotice that while image assets are static, applying them requires embedding custom CSS styles and JS event listeners directly into FastHTML FT `Style` and `Script` tags, reducing abstraction survival."},
    {"id": 8, "sender": "user", "author": "Dr. Aris Thorne", "timestamp": "14:01:30", "content": "What is the exact mobile recomposition strategy? Stacking desktop columns vertically is explicitly a hard failure gate."},
    {"id": 9, "sender": "agent_syn", "author": "Synthesis Agent", "timestamp": "14:01:42", "content": "MOBILE ARCHITECTURE:\n1. Tactical Morphology on mobile uses a floating agent status bar, sticky bottom command bar, and modal agent matrix drawer.\n2. Editorial Morphology on mobile uses a top journal rail and full-screen conversation stream with floating action controls."},
    {"id": 10, "sender": "user", "author": "Dr. Aris Thorne", "timestamp": "14:02:10", "content": "Let us stress test long-use readability. Generate long multi-paragraph reasoning outputs to evaluate typography density under deep scroll conditions."},
]

# Generate additional realistic long debate messages (up to 35 messages)
for i in range(11, 36):
    sender_type = ["user", "agent_res", "agent_crt", "agent_syn"][i % 4]
    author_name = {
        "user": "Dr. Aris Thorne",
        "agent_res": "Research Agent",
        "agent_crt": "Critic Agent",
        "agent_syn": "Synthesis Agent"
    }[sender_type]

    if sender_type == "user":
        content = f"Query {i}: Deep inspection of typography scale and line height in long conversation thread item #{i}. Verify sticky headers do not obscure text."
    elif sender_type == "agent_res":
        content = f"ANALYSIS LOG #{i}:\nVerified font hierarchy at index {i}. Line height set to 1.65 for high long-session readability. Server-rendered FastTags maintain zero layout shift during continuous message insertion."
    elif sender_type == "agent_crt":
        content = f"ADVERSARIAL TEST #{i}:\nEvaluating scroll position retention and DOM node pressure at message count {i}. HTMX partial swapping of target container retains scroll anchors."
    else:
        content = f"SYNTHESIS SUMMARY #{i}:\nConsensus score stabilized at 0.{85 + (i%10)}. All agents confirm state preservation across live morphology switches."

    MOCK_MESSAGES.append({
        "id": i,
        "sender": sender_type,
        "author": author_name,
        "timestamp": f"14:{i//2:02d}:{i*2%60:02d}",
        "content": content
    })

SESSION_DATA = {
    "user_id": "usr_alpha_99",
    "user_name": "Dr. Aris Thorne",
    "active_morphology": "tactical", # "tactical" or "editorial"
    "show_mobile_drawer": False,
    "agents": [
        {"id": "agent_res", "name": "Research Agent", "role": "Fact Extraction & Intelligence", "status": "COMPLETED", "score": 0.94, "color": "#00e6c8"},
        {"id": "agent_crt", "name": "Critic Agent", "role": "Adversarial Sanity & Risk Audit", "status": "RUNNING", "score": 0.82, "color": "#ff0055"},
        {"id": "agent_syn", "name": "Synthesis Agent", "role": "Consensus & Action Formatting", "status": "WAITING", "score": 0.00, "color": "#ffb400"},
    ],
    "messages": MOCK_MESSAGES
}

def render_multimind_app(session: dict = SESSION_DATA):
    morph = session.get("active_morphology", "tactical")
    if morph == "tactical":
        return render_tactical_morphology(session)
    else:
        return render_editorial_morphology(session)

def render_tactical_morphology(session: dict):
    return Div(
        # Top Header HUD
        Header(
            Div(
                Div(
                    Span("MULTIMIND //", cls="mm-brand-prefix"),
                    Span("TACTICAL OPS SURFACE", cls="mm-brand-main"),
                    cls="mm-brand"
                ),
                Div(
                    Span(f"USER: {session['user_name']}", cls="mm-user-tag desktop-only"),
                    Button(
                        "MUTATE TO EDITORIAL MORPHOLOGY",
                        cls="mm-mutate-btn",
                        hx_post="/mutate-presentation?to=editorial",
                        hx_target="#multimind-app-container",
                        hx_swap="innerHTML"
                    ),
                    cls="mm-header-controls"
                ),
                cls="mm-tactical-header-inner"
            ),
            cls="mm-tactical-header"
        ),

        # Mobile Floating Status Bar (Mobile-specific Recomposition)
        Div(
            Span("ACTIVE AGENTS: 3", cls="mob-status-label"),
            Span("RUNNING: CRITIC AGENT", cls="mob-status-active"),
            Button(
                "AGENT MATRIX ☰",
                cls="mob-drawer-toggle",
                onclick="document.getElementById('mob-tactical-drawer').classList.toggle('active')"
            ),
            cls="mm-tactical-mobile-bar mobile-only"
        ),

        # Mobile Modal Drawer for Agent Matrix (Satisfies Mobile Recomposition Gate)
        Div(
            Div(
                Div(
                    H4("TACTICAL AGENT MATRIX", cls="drawer-title"),
                    Button("✕", cls="drawer-close", onclick="document.getElementById('mob-tactical-drawer').classList.remove('active')"),
                    cls="drawer-header"
                ),
                Div(
                    *[
                        Div(
                            Div(agent["name"], cls="agent-name"),
                            Div(agent["status"], cls=f"agent-badge badge-{agent['status'].lower()}"),
                            Div(agent["role"], cls="agent-role"),
                            cls="drawer-agent-card"
                        )
                        for agent in session["agents"]
                    ],
                    cls="drawer-body"
                ),
                cls="drawer-content"
            ),
            id="mob-tactical-drawer",
            cls="mm-mobile-drawer mobile-only"
        ),

        # Desktop Grid Layout (Sidebar + Main Chat)
        Div(
            # Sidebar Desktop Only
            Aside(
                Div("DEBATE AGENT STATUS MATRIX", cls="mm-sidebar-head"),
                Div(
                    *[
                        Div(
                            Div(
                                Span(agent["name"], cls="agent-name"),
                                Span(agent["status"], cls=f"agent-badge badge-{agent['status'].lower()}"),
                                cls="agent-card-top"
                            ),
                            Div(agent["role"], cls="agent-role"),
                            Div(
                                Div(style=f"width: {int(agent['score']*100)}%; background: {agent['color']};", cls="agent-bar-fill"),
                                cls="agent-bar"
                            ) if agent["status"] != "WAITING" else Div(
                                Img(src="/static/images/ambient_loader.gif", cls="agent-mini-loader", alt="Loading"),
                                Span("PONDERINGS IN PROGRESS...", cls="agent-waiting-text"),
                                cls="agent-waiting-box"
                            ),
                            cls="mm-agent-card"
                        )
                        for agent in session["agents"]
                    ],
                    cls="mm-agent-list"
                ),
                Div(
                    Button(
                        "ADVANCE DEBATE STEP",
                        cls="mm-action-btn",
                        hx_post="/trigger-agent-step",
                        hx_target="#multimind-app-container",
                        hx_swap="innerHTML"
                    ),
                    cls="mm-sidebar-actions"
                ),
                cls="mm-tactical-sidebar desktop-only"
            ),

            # Main Chat Surface (Desktop & Mobile)
            Main(
                Div(
                    H3("SESSION: ARCHITECTURAL DEBATE (LONG-USE TEST)", cls="mm-chat-title"),
                    Span(f"MESSAGES RECORDED: {len(session['messages'])}", cls="mm-chat-count"),
                    cls="mm-chat-header"
                ),
                Div(
                    *[
                        Div(
                            Div(
                                Span(msg["author"], cls="msg-author"),
                                Span(msg["timestamp"], cls="msg-time"),
                                cls="msg-meta"
                            ),
                            Div(msg["content"], cls="msg-body"),
                            cls=f"mm-msg-bubble msg-{msg['sender']}"
                        )
                        for msg in session["messages"]
                    ],
                    id="mm-msg-container",
                    cls="mm-msg-stream"
                ),
                # Input Console (Sticky Desktop & Bottom Mobile)
                Div(
                    Form(
                        Input(type="text", name="message", placeholder="Transmit instruction to multi-agent swarm...", cls="mm-input-field", required=True),
                        Button("TRANSMIT", type="submit", cls="mm-submit-btn"),
                        hx_post="/send-message",
                        hx_target="#multimind-app-container",
                        hx_swap="innerHTML",
                        cls="mm-input-form"
                    ),
                    cls="mm-input-bar"
                ),
                cls="mm-tactical-main"
            ),
            cls="mm-tactical-grid"
        ),

        # Scoped CSS for Tactical Morphology (Desktop & Mobile Recomposition)
        Style("""
            .mm-tactical-wrapper {
                background: #080c14 url('/static/images/tactical_grid.png') repeat;
                color: #dbe4ee;
                font-family: 'Consolas', 'Courier New', monospace;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
            }
            .desktop-only { display: block; }
            .mobile-only { display: none; }

            .mm-tactical-header {
                background: rgba(10, 16, 26, 0.95);
                border-bottom: 2px solid #00e6c8;
                padding: 14px 28px;
                backdrop-filter: blur(10px);
                position: sticky;
                top: 0;
                z-index: 50;
            }
            .mm-tactical-header-inner { display: flex; justify-content: space-between; align-items: center; max-width: 1600px; margin: 0 auto; }
            .mm-brand-prefix { color: #ff0055; font-weight: 900; letter-spacing: 2px; }
            .mm-brand-main { color: #00e6c8; font-weight: 800; letter-spacing: 1px; margin-left: 6px; }
            .mm-user-tag { font-size: 0.8rem; color: #ffb400; margin-right: 16px; }
            .mm-mutate-btn {
                background: #ff0055;
                color: #fff;
                border: none;
                padding: 8px 16px;
                font-weight: 700;
                font-size: 0.75rem;
                letter-spacing: 1px;
                cursor: pointer;
            }

            .mm-tactical-grid {
                display: grid;
                grid-template-columns: 320px 1fr;
                gap: 24px;
                max-width: 1600px;
                margin: 24px auto;
                padding: 0 24px;
                width: 100%;
                flex: 1;
            }
            .mm-tactical-sidebar {
                background: rgba(14, 22, 34, 0.85);
                border: 1px solid #1a293d;
                border-left: 4px solid #00e6c8;
                padding: 20px;
            }
            .mm-sidebar-head { font-size: 0.8rem; letter-spacing: 2px; color: #00e6c8; font-weight: 800; margin-bottom: 20px; border-bottom: 1px solid #1a293d; padding-bottom: 8px; }
            .mm-agent-list { display: flex; flex-direction: column; gap: 16px; }
            .mm-agent-card { background: rgba(20, 32, 48, 0.6); border: 1px solid #22354d; padding: 14px; }
            .agent-card-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
            .agent-name { font-weight: 700; font-size: 0.9rem; color: #fff; }
            .agent-badge { font-size: 0.65rem; padding: 2px 6px; font-weight: 800; }
            .badge-completed { background: rgba(0,230,200,0.2); color: #00e6c8; border: 1px solid #00e6c8; }
            .badge-running { background: rgba(255,0,85,0.2); color: #ff0055; border: 1px solid #ff0055; }
            .badge-waiting { background: rgba(255,180,0,0.2); color: #ffb400; border: 1px solid #ffb400; }
            .agent-role { font-size: 0.75rem; color: #889bb0; margin-bottom: 10px; }
            .agent-bar { height: 4px; background: #162232; width: 100%; }
            .agent-bar-fill { height: 100%; }
            .agent-waiting-box { display: flex; align-items: center; gap: 8px; }
            .agent-mini-loader { width: 18px; height: 18px; border-radius: 50%; }
            .agent-waiting-text { font-size: 0.7rem; color: #ffb400; font-weight: 700; }
            .mm-sidebar-actions { margin-top: 20px; }
            .mm-action-btn { width: 100%; background: #1a293d; color: #00e6c8; border: 1px solid #00e6c8; padding: 10px; font-family: inherit; font-weight: 700; font-size: 0.75rem; cursor: pointer; }

            .mm-tactical-main { background: rgba(14, 22, 34, 0.85); border: 1px solid #1a293d; display: flex; flex-direction: column; height: 750px; }
            .mm-chat-header { padding: 16px 24px; border-bottom: 1px solid #1a293d; display: flex; justify-content: space-between; align-items: center; background: rgba(10, 16, 26, 0.5); }
            .mm-chat-title { font-size: 0.9rem; margin: 0; color: #fff; }
            .mm-chat-count { font-size: 0.75rem; color: #ff0055; font-weight: 700; }
            .mm-msg-stream { flex: 1; padding: 24px; overflow-y: auto; display: flex; flex-direction: column; gap: 16px; }
            .mm-msg-bubble { padding: 16px; border: 1px solid #1e3047; max-width: 85%; line-height: 1.65; font-size: 0.88rem; }
            .msg-user { align-self: flex-end; background: rgba(0, 230, 200, 0.08); border-color: rgba(0, 230, 200, 0.4); }
            .msg-agent_res, .msg-agent_crt, .msg-agent_syn { align-self: flex-start; background: rgba(18, 28, 44, 0.9); border-left: 4px solid #ff0055; }
            .msg-meta { display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.75rem; }
            .msg-author { font-weight: 800; color: #00e6c8; }
            .msg-time { color: #60758c; }
            .msg-body { white-space: pre-wrap; word-break: break-word; color: #e2eaf4; }

            .mm-input-bar { padding: 16px 24px; border-top: 1px solid #1a293d; background: rgba(10, 16, 26, 0.7); }
            .mm-input-form { display: flex; gap: 12px; }
            .mm-input-field { flex: 1; background: #090e17; border: 1px solid #22354d; color: #fff; padding: 12px 16px; font-family: inherit; font-size: 0.85rem; }
            .mm-submit-btn { background: #00e6c8; color: #080c14; border: none; padding: 12px 24px; font-weight: 800; font-family: inherit; cursor: pointer; }

            /* GENUINE MOBILE RECOMPOSITION — SATISFIES DESKTOP_STACKED_VERTICALLY HARD GATE */
            @media (max-width: 768px) {
                .desktop-only { display: none !important; }
                .mobile-only { display: flex !important; }

                .mm-tactical-header { padding: 10px 16px; }
                .mm-tactical-grid { display: block; padding: 0 10px; margin: 10px 0; }
                .mm-tactical-main { height: calc(100vh - 180px); min-height: 520px; }

                .mm-tactical-mobile-bar {
                    background: #0f172a;
                    border-bottom: 1px solid #00e6c8;
                    padding: 8px 16px;
                    justify-content: space-between;
                    align-items: center;
                    font-size: 0.75rem;
                }
                .mob-status-label { color: #889bb0; }
                .mob-status-active { color: #ff0055; font-weight: 800; }
                .mob-drawer-toggle { background: #00e6c8; color: #000; border: none; padding: 4px 10px; font-weight: 800; font-size: 0.7rem; border-radius: 4px; }

                .mm-mobile-drawer {
                    display: none !important;
                    position: fixed;
                    top: 0; left: 0; right: 0; bottom: 0;
                    background: rgba(0,0,0,0.85);
                    backdrop-filter: blur(8px);
                    z-index: 200;
                    display: none;
                    justify-content: flex-end;
                }
                .mm-mobile-drawer.active { display: flex !important; }
                .drawer-content {
                    width: 80%;
                    max-width: 300px;
                    background: #0d1522;
                    border-left: 2px solid #00e6c8;
                    padding: 20px;
                    display: flex;
                    flex-direction: column;
                }
                .drawer-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e2d42; padding-bottom: 12px; margin-bottom: 16px; }
                .drawer-title { font-size: 0.85rem; color: #00e6c8; margin: 0; }
                .drawer-close { background: none; border: none; color: #fff; font-size: 1.2rem; cursor: pointer; }
                .drawer-agent-card { background: #142032; padding: 12px; margin-bottom: 12px; border-radius: 4px; }

                .mm-msg-bubble { max-width: 100%; }
                .mm-input-bar { position: sticky; bottom: 0; z-index: 40; }
            }
        """),
        id="multimind-morph-target",
        cls="mm-tactical-wrapper"
    )

def render_editorial_morphology(session: dict):
    return Div(
        # Main Header
        Header(
            Div(
                Div(
                    Span("MULTIMIND ATELIER", cls="ed-brand-title"),
                    Span(" // EDITORIAL MORPHOLOGY", cls="ed-brand-sub desktop-only"),
                    cls="ed-brand"
                ),
                Div(
                    Button(
                        "MUTATE TO TACTICAL MORPHOLOGY",
                        cls="ed-mutate-btn",
                        hx_post="/mutate-presentation?to=tactical",
                        hx_target="#multimind-app-container",
                        hx_swap="innerHTML"
                    ),
                    cls="ed-header-controls"
                ),
                cls="ed-header-inner"
            ),
            cls="ed-header"
        ),

        # Mobile Floating Journal Rail (Mobile-specific Recomposition)
        Div(
            Span("JOURNAL ISSUE N° 09", cls="ed-mob-tag"),
            Span("DEBATE ACTIVE", cls="ed-mob-status"),
            cls="ed-mobile-top-rail mobile-only"
        ),

        # Surface Container
        Div(
            # Top Banner (Desktop Only)
            Div(
                Span("ACTIVE AGENT SWARM DEBATE", cls="ed-rail-kicker"),
                Div(
                    *[
                        Div(
                            Div(agent["name"], cls="ed-agent-name"),
                            Div(agent["status"], cls=f"ed-status ed-status-{agent['status'].lower()}"),
                            cls="ed-agent-chip"
                        )
                        for agent in session["agents"]
                    ],
                    cls="ed-agent-rail"
                ),
                Button(
                    "ADVANCE DEBATE STEP →",
                    cls="ed-step-btn",
                    hx_post="/trigger-agent-step",
                    hx_target="#multimind-app-container",
                    hx_swap="innerHTML"
                ),
                cls="ed-top-banner desktop-only"
            ),

            # Spatial Editorial Layout
            Div(
                # Left Column (Desktop Only)
                Div(
                    Span("ISSUE N° 09 / COLLABORATION", cls="ed-issue-tag"),
                    H2("THE ART OF CONVOLUTION.", cls="ed-main-headline"),
                    P("Where synthetic reasoning evolves beyond programmatic limits into pure editorial synthesis.", cls="ed-headline-sub"),
                    cls="ed-left-column desktop-only"
                ),

                # Right Column Chat Stream (Desktop & Mobile)
                Div(
                    Div(
                        *[
                            Div(
                                Div(
                                    Span(msg["author"], cls="ed-msg-author"),
                                    Span(msg["timestamp"], cls="ed-msg-time"),
                                    cls="ed-msg-meta"
                                ),
                                Div(msg["content"], cls="ed-msg-text"),
                                cls=f"ed-msg-card ed-msg-{msg['sender']}"
                            )
                            for msg in session["messages"]
                        ],
                        cls="ed-stream-inner"
                    ),
                    Form(
                        Input(type="text", name="message", placeholder="Type editorial reflection...", cls="ed-input", required=True),
                        Button("PUBLISH", type="submit", cls="ed-submit"),
                        hx_post="/send-message",
                        hx_target="#multimind-app-container",
                        hx_swap="innerHTML",
                        cls="ed-form"
                    ),
                    cls="ed-right-column"
                ),
                cls="ed-spatial-layout"
            ),
            cls="ed-body-container"
        ),

        # Scoped CSS for Editorial Morphology
        Style("""
            .mm-editorial-wrapper {
                background: #f4f1ea url('/static/images/luxury_paper.png') repeat;
                color: #22201e;
                font-family: 'Georgia', 'Times New Roman', serif;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
            }
            .ed-header { padding: 24px 48px; border-bottom: 1px solid rgba(34, 32, 30, 0.12); background: rgba(244, 241, 234, 0.9); backdrop-filter: blur(8px); position: sticky; top: 0; z-index: 50; }
            .ed-header-inner { display: flex; justify-content: space-between; align-items: center; max-width: 1500px; margin: 0 auto; }
            .ed-brand-title { font-size: 1.2rem; font-weight: 700; letter-spacing: 3px; color: #111; text-transform: uppercase; }
            .ed-brand-sub { font-size: 0.85rem; color: #777; letter-spacing: 1px; }
            .ed-mutate-btn { background: #111; color: #f4f1ea; border: 1px solid #111; padding: 10px 20px; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; cursor: pointer; }

            .ed-body-container { max-width: 1500px; margin: 0 auto; padding: 32px 48px; width: 100%; flex: 1; }
            .ed-top-banner { background: #fff; border: 1px solid rgba(0,0,0,0.08); padding: 16px 24px; display: flex; align-items: center; gap: 24px; margin-bottom: 40px; }
            .ed-rail-kicker { font-size: 0.7rem; letter-spacing: 3px; font-weight: 700; color: #888; text-transform: uppercase; }
            .ed-agent-rail { display: flex; gap: 16px; flex: 1; overflow-x: auto; }
            .ed-agent-chip { background: #f9f8f5; border: 1px solid #e2ded4; padding: 6px 14px; display: flex; gap: 10px; align-items: center; }
            .ed-agent-name { font-size: 0.8rem; font-weight: 700; color: #222; }
            .ed-status { font-size: 0.65rem; font-weight: 700; }
            .ed-status-completed { color: #008866; }
            .ed-status-running { color: #d00030; }
            .ed-status-waiting { color: #b87000; }
            .ed-step-btn { background: none; border: 1px solid #222; color: #222; padding: 6px 14px; font-size: 0.75rem; cursor: pointer; }

            .ed-spatial-layout { display: grid; grid-template-columns: 380px 1fr; gap: 60px; }
            .ed-issue-tag { font-size: 0.75rem; letter-spacing: 4px; color: #d00030; display: block; margin-bottom: 16px; font-weight: 700; }
            .ed-main-headline { font-size: 3.2rem; font-weight: 300; line-height: 1.05; margin: 0 0 24px 0; color: #111; text-transform: uppercase; }
            .ed-headline-sub { font-size: 1.1rem; line-height: 1.7; color: #555; font-style: italic; }

            .ed-right-column { display: flex; flex-direction: column; height: 750px; }
            .ed-stream-inner { flex: 1; overflow-y: auto; padding-right: 16px; display: flex; flex-direction: column; gap: 24px; }
            .ed-msg-card { background: #fff; border: 1px solid rgba(0,0,0,0.08); padding: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.02); }
            .ed-msg-user { border-left: 4px solid #111; }
            .ed-msg-agent_res, .ed-msg-agent_crt, .ed-msg-agent_syn { border-left: 4px solid #d00030; }
            .ed-msg-meta { display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.75rem; }
            .ed-msg-author { font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #111; }
            .ed-msg-time { color: #888; }
            .ed-msg-text { font-size: 1rem; line-height: 1.7; color: #333; white-space: pre-wrap; }

            .ed-form { display: flex; gap: 12px; margin-top: 24px; }
            .ed-input { flex: 1; background: #fff; border: 1px solid #ccc; padding: 14px 18px; font-family: inherit; font-size: 0.95rem; }
            .ed-submit { background: #111; color: #fff; border: none; padding: 14px 28px; font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; cursor: pointer; }

            /* EDITORIAL MOBILE RECOMPOSITION */
            @media (max-width: 768px) {
                .ed-header { padding: 16px 20px; }
                .ed-body-container { padding: 16px 20px; }
                .ed-mobile-top-rail {
                    background: #111;
                    color: #fff;
                    padding: 8px 16px;
                    display: flex;
                    justify-content: space-between;
                    font-size: 0.75rem;
                    letter-spacing: 2px;
                }
                .ed-mob-tag { color: #d00030; font-weight: 700; }
                .ed-mob-status { color: #aaa; }
                .ed-spatial-layout { grid-template-columns: 1fr; gap: 20px; }
                .ed-right-column { height: calc(100vh - 200px); min-height: 520px; }
                .ed-msg-card { padding: 16px; }
                .ed-form { position: sticky; bottom: 0; background: #f4f1ea; padding: 10px 0; }
            }
        """),
        id="multimind-morph-target",
        cls="mm-editorial-wrapper"
    )
