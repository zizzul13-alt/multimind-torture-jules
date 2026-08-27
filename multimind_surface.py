from fasthtml.common import *

# In-memory session store (Mock Session Data)
SESSION_DATA = {
    "user_id": "usr_alpha_99",
    "user_name": "Dr. Aris Thorne",
    "user_avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=Aris",
    "active_morphology": "tactical", # "tactical" (Morphology 1) or "editorial" (Morphology 2)
    "agents": [
        {"id": "agent_res", "name": "Research Agent", "role": "Fact Extraction & Intelligence", "status": "COMPLETED", "score": 0.94, "color": "#00e6c8"},
        {"id": "agent_crt", "name": "Critic Agent", "role": "Adversarial Sanity & Risk Audit", "status": "RUNNING", "score": 0.82, "color": "#ff0055"},
        {"id": "agent_syn", "name": "Synthesis Agent", "role": "Consensus & Action Formatting", "status": "WAITING", "score": 0.00, "color": "#ffb400"},
    ],
    "messages": [
        {
            "id": 1,
            "sender": "user",
            "author": "Dr. Aris Thorne",
            "timestamp": "14:20:05",
            "content": "Evaluate the architectural trade-offs of using FastHTML vs traditional SPA single-page frameworks for real-time multi-agent collaborative dashboards under extreme rendering pressure."
        },
        {
            "id": 2,
            "sender": "agent_res",
            "author": "Research Agent",
            "timestamp": "14:20:12",
            "content": "PRELIMINARY FINDINGS:\nFastHTML shifts rendering load entirely to the server using Starlette + FTFastTags while utilizing HTMX for granular hypermedia partial swaps. This eliminates heavy client JS bundles (React/Vue DOM diffing cost = zero), but transfers UI state mutation complexity into HTTP response orchestration."
        },
        {
            "id": 3,
            "sender": "agent_crt",
            "author": "Critic Agent",
            "timestamp": "14:20:19",
            "content": "ADVERSARIAL COUNTERPOINT:\nWhile server rendering reduces initial JS payload, highly dynamic spatial/3D transitions (e.g., Noomo Labs scroll-linked tilt) and complex canvas choreographies require raw browser API escape hatches. If abstraction survival drops below 60%, FastHTML becomes a backend wrapper over manual JS DOM manipulation."
        },
        {
            "id": 4,
            "sender": "user",
            "author": "Dr. Aris Thorne",
            "timestamp": "14:21:02",
            "content": "How does live presentation mutation behave during an active long conversation session without full page reloads?"
        },
        {
            "id": 5,
            "sender": "agent_syn",
            "author": "Synthesis Agent (Drafting)",
            "timestamp": "14:21:15",
            "content": "SYNTHESIS IN PROGRESS:\nBy triggering HTMX partial swaps targeting the root application morphology shell (`#multimind-morph-target`), the visual layout, typography scale, component morphology, and material backgrounds can be mutated instantly. The conversation array and active session state remain untouched in memory."
        }
    ]
}

def render_multimind_app(session: dict = SESSION_DATA):
    """
    Renders the main recomposed MultiMind application surface in the selected morphology.
    Morphology 1: Arknights x Dioriviera inspired -> Tactical Material / High-Density Glass & Layered Operations
    Morphology 2: Viens-là x Noomo Labs inspired -> Editorial Spatial / Fluid Dynamic Composition
    """
    morph = session.get("active_morphology", "tactical")
    if morph == "tactical":
        return render_tactical_morphology(session)
    else:
        return render_editorial_morphology(session)

def render_tactical_morphology(session: dict):
    """
    MORPHOLOGY 1 — Tactical Material / High-Density Operations Surface
    Derived from Arknights (layered HUD, status strips, monospace tech typography)
    and Dioriviera (material layer background, high-contrast framing).
    """
    return Div(
        # Main Header
        Header(
            Div(
                Div(
                    Span("MULTIMIND //", cls="mm-brand-prefix"),
                    Span("TACTICAL OPS SURFACE", cls="mm-brand-main"),
                    cls="mm-brand"
                ),
                Div(
                    Span(f"USER: {session['user_name']}", cls="mm-user-tag"),
                    # Live Presentation Mutation Trigger (HTMX)
                    Button(
                        "MUTATE TO MORPHOLOGY 2 (EDITORIAL SPATIAL)",
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

        # Application Body Layout
        Div(
            # Left Sidebar: Agent Debate State & Branded Loading
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
                # Agent Debate Trigger Simulation
                Div(
                    Button(
                        "ADVANCE AGENT DEBATE STEP",
                        cls="mm-action-btn",
                        hx_post="/trigger-agent-step",
                        hx_target="#multimind-app-container",
                        hx_swap="innerHTML"
                    ),
                    cls="mm-sidebar-actions"
                ),
                cls="mm-tactical-sidebar"
            ),

            # Main Conversation Area
            Main(
                # Conversation Header
                Div(
                    H3("SESSION: ARCHITECTURAL DEBATE (LONG CONVERSATION TEST)", cls="mm-chat-title"),
                    Span(f"MESSAGES RECORDED: {len(session['messages'])}", cls="mm-chat-count"),
                    cls="mm-chat-header"
                ),
                # Messages Stream
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
                # Input Console
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

        # Scoped CSS for Tactical Morphology
        Style("""
            .mm-tactical-wrapper {
                background: #080c14 url('/static/images/tactical_grid.png') repeat;
                color: #dbe4ee;
                font-family: 'Consolas', 'Courier New', monospace;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
            }
            .mm-tactical-header {
                background: rgba(10, 16, 26, 0.95);
                border-bottom: 2px solid #00e6c8;
                padding: 14px 28px;
                backdrop-filter: blur(10px);
                position: sticky;
                top: 0;
                z-index: 50;
            }
            .mm-tactical-header-inner {
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1600px;
                margin: 0 auto;
            }
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
                clip-path: polygon(0 0, 100% 0, 95% 100%, 0 100%);
                transition: background 0.2s;
            }
            .mm-mutate-btn:hover { background: #ff3377; }

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
                display: flex;
                flex-direction: column;
            }
            .mm-sidebar-head {
                font-size: 0.8rem;
                letter-spacing: 2px;
                color: #00e6c8;
                font-weight: 800;
                margin-bottom: 20px;
                padding-bottom: 8px;
                border-bottom: 1px solid #1a293d;
            }
            .mm-agent-list { display: flex; flex-direction: column; gap: 16px; flex: 1; }
            .mm-agent-card {
                background: rgba(20, 32, 48, 0.6);
                border: 1px solid #22354d;
                padding: 14px;
            }
            .agent-card-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
            .agent-name { font-weight: 700; font-size: 0.9rem; color: #fff; }
            .agent-badge { font-size: 0.65rem; padding: 2px 6px; font-weight: 800; border-radius: 2px; }
            .badge-completed { background: rgba(0,230,200,0.2); color: #00e6c8; border: 1px solid #00e6c8; }
            .badge-running { background: rgba(255,0,85,0.2); color: #ff0055; border: 1px solid #ff0055; }
            .badge-waiting { background: rgba(255,180,0,0.2); color: #ffb400; border: 1px solid #ffb400; }
            .agent-role { font-size: 0.75rem; color: #889bb0; margin-bottom: 10px; }
            .agent-bar { height: 4px; background: #162232; width: 100%; }
            .agent-bar-fill { height: 100%; transition: width 0.3s; }
            .agent-waiting-box { display: flex; align-items: center; gap: 8px; margin-top: 6px; }
            .agent-mini-loader { width: 18px; height: 18px; border-radius: 50%; }
            .agent-waiting-text { font-size: 0.7rem; color: #ffb400; font-weight: 700; letter-spacing: 1px; }

            .mm-sidebar-actions { margin-top: 20px; }
            .mm-action-btn {
                width: 100%;
                background: #1a293d;
                color: #00e6c8;
                border: 1px solid #00e6c8;
                padding: 10px;
                font-family: inherit;
                font-weight: 700;
                font-size: 0.75rem;
                letter-spacing: 1px;
                cursor: pointer;
                transition: background 0.2s;
            }
            .mm-action-btn:hover { background: rgba(0,230,200,0.15); }

            .mm-tactical-main {
                background: rgba(14, 22, 34, 0.85);
                border: 1px solid #1a293d;
                display: flex;
                flex-direction: column;
                height: 720px;
            }
            .mm-chat-header {
                padding: 16px 24px;
                border-bottom: 1px solid #1a293d;
                display: flex;
                justify-content: space-between;
                align-items: center;
                background: rgba(10, 16, 26, 0.5);
            }
            .mm-chat-title { font-size: 0.9rem; margin: 0; color: #fff; letter-spacing: 1px; }
            .mm-chat-count { font-size: 0.75rem; color: #ff0055; font-weight: 700; }
            .mm-msg-stream {
                flex: 1;
                padding: 24px;
                overflow-y: auto;
                display: flex;
                flex-direction: column;
                gap: 16px;
            }
            .mm-msg-bubble {
                padding: 16px;
                border: 1px solid #1e3047;
                max-width: 85%;
                line-height: 1.6;
                font-size: 0.88rem;
            }
            .msg-user {
                align-self: flex-end;
                background: rgba(0, 230, 200, 0.08);
                border-color: rgba(0, 230, 200, 0.4);
            }
            .msg-agent_res, .msg-agent_crt, .msg-agent_syn {
                align-self: flex-start;
                background: rgba(18, 28, 44, 0.9);
                border-left: 4px solid #ff0055;
            }
            .msg-meta { display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.75rem; }
            .msg-author { font-weight: 800; color: #00e6c8; }
            .msg-time { color: #60758c; }
            .msg-body { white-space: pre-wrap; word-break: break-word; color: #e2eaf4; }

            .mm-input-bar { padding: 16px 24px; border-top: 1px solid #1a293d; background: rgba(10, 16, 26, 0.7); }
            .mm-input-form { display: flex; gap: 12px; }
            .mm-input-field {
                flex: 1;
                background: #090e17;
                border: 1px solid #22354d;
                color: #fff;
                padding: 12px 16px;
                font-family: inherit;
                font-size: 0.85rem;
            }
            .mm-input-field:focus { outline: none; border-color: #00e6c8; }
            .mm-submit-btn {
                background: #00e6c8;
                color: #080c14;
                border: none;
                padding: 12px 24px;
                font-weight: 800;
                font-family: inherit;
                letter-spacing: 1px;
                cursor: pointer;
            }

            /* RECOMPOSED MOBILE PRESENTATION — HARD GATE SATISFACTION */
            @media (max-width: 768px) {
                .mm-tactical-grid {
                    grid-template-columns: 1fr;
                    padding: 0 12px;
                    margin: 12px 0;
                }
                .mm-tactical-sidebar {
                    order: 2;
                    border-left: none;
                    border-top: 4px solid #00e6c8;
                }
                .mm-tactical-main { height: 550px; }
                .mm-msg-bubble { max-width: 100%; }
                .mm-header-controls { display: flex; flex-direction: column; align-items: flex-end; gap: 6px; }
            }
        """),
        id="multimind-morph-target",
        cls="mm-tactical-wrapper"
    )

def render_editorial_morphology(session: dict):
    """
    MORPHOLOGY 2 — Editorial Spatial / Fluid Dynamic Composition Surface
    Derived from Viens-là (oversized serif headings, strict editorial grid, high negative space)
    and Noomo Labs (fluid spatial cards, soft floating elevation).
    """
    return Div(
        # Main Header
        Header(
            Div(
                Div(
                    Span("MULTIMIND ATELIER", cls="ed-brand-title"),
                    Span(" // EDITORIAL MORPHOLOGY", cls="ed-brand-sub"),
                    cls="ed-brand"
                ),
                Div(
                    Span(f"JOURNAL USER: {session['user_name']}", cls="ed-user-tag"),
                    # Live Presentation Mutation Trigger back to Tactical (HTMX)
                    Button(
                        "MUTATE TO MORPHOLOGY 1 (TACTICAL OPS)",
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

        # Main Surface Container
        Div(
            # Top Editorial Banner / Agent Progress Horizontal Rail
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
                cls="ed-top-banner"
            ),

            # Spatial Editorial Layout
            Div(
                # Left Editorial Statement Block
                Div(
                    Span("ISSUE N° 09 / COLLABORATION", cls="ed-issue-tag"),
                    H2("THE ART OF CONVOLUTION.", cls="ed-main-headline"),
                    P(
                        "Where synthetic reasoning evolves beyond programmatic limits into pure editorial synthesis.",
                        cls="ed-headline-sub"
                    ),
                    cls="ed-left-column"
                ),

                # Right Long Conversation Stream
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
                    # Input Field
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
            .ed-header {
                padding: 24px 48px;
                border-bottom: 1px solid rgba(34, 32, 30, 0.12);
                background: rgba(244, 241, 234, 0.9);
                backdrop-filter: blur(8px);
                position: sticky;
                top: 0;
                z-index: 50;
            }
            .ed-header-inner { display: flex; justify-content: space-between; align-items: center; max-width: 1500px; margin: 0 auto; }
            .ed-brand-title { font-size: 1.2rem; font-weight: 700; letter-spacing: 3px; color: #111; text-transform: uppercase; }
            .ed-brand-sub { font-size: 0.85rem; color: #777; letter-spacing: 1px; }
            .ed-user-tag { font-size: 0.8rem; font-style: italic; color: #666; margin-right: 16px; }
            .ed-mutate-btn {
                background: #111;
                color: #f4f1ea;
                border: 1px solid #111;
                padding: 10px 20px;
                font-size: 0.75rem;
                letter-spacing: 2px;
                text-transform: uppercase;
                cursor: pointer;
                transition: background 0.2s, color 0.2s;
            }
            .ed-mutate-btn:hover { background: #333; }

            .ed-body-container { max-width: 1500px; margin: 0 auto; padding: 32px 48px; width: 100%; flex: 1; }
            .ed-top-banner {
                background: #fff;
                border: 1px solid rgba(0,0,0,0.08);
                padding: 16px 24px;
                display: flex;
                align-items: center;
                gap: 24px;
                margin-bottom: 40px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.03);
            }
            .ed-rail-kicker { font-size: 0.7rem; letter-spacing: 3px; font-weight: 700; color: #888; text-transform: uppercase; }
            .ed-agent-rail { display: flex; gap: 16px; flex: 1; overflow-x: auto; }
            .ed-agent-chip { background: #f9f8f5; border: 1px solid #e2ded4; padding: 6px 14px; display: flex; gap: 10px; align-items: center; }
            .ed-agent-name { font-size: 0.8rem; font-weight: 700; color: #222; }
            .ed-status { font-size: 0.65rem; font-weight: 700; letter-spacing: 1px; }
            .ed-status-completed { color: #008866; }
            .ed-status-running { color: #d00030; }
            .ed-status-waiting { color: #b87000; }
            .ed-step-btn {
                background: none;
                border: 1px solid #222;
                color: #222;
                padding: 6px 14px;
                font-size: 0.75rem;
                letter-spacing: 1px;
                cursor: pointer;
            }

            .ed-spatial-layout { display: grid; grid-template-columns: 380px 1fr; gap: 60px; }
            .ed-issue-tag { font-size: 0.75rem; letter-spacing: 4px; color: #d00030; display: block; margin-bottom: 16px; font-weight: 700; }
            .ed-main-headline { font-size: 3.2rem; font-weight: 300; line-height: 1.05; margin: 0 0 24px 0; color: #111; text-transform: uppercase; }
            .ed-headline-sub { font-size: 1.1rem; line-height: 1.7; color: #555; font-style: italic; }

            .ed-right-column { display: flex; flex-direction: column; height: 700px; }
            .ed-stream-inner { flex: 1; overflow-y: auto; padding-right: 16px; display: flex; flex-direction: column; gap: 24px; }
            .ed-msg-card {
                background: #fff;
                border: 1px solid rgba(0,0,0,0.08);
                padding: 24px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.02);
                transition: transform 0.2s;
            }
            .ed-msg-card:hover { transform: translateY(-2px); }
            .ed-msg-user { border-left: 4px solid #111; }
            .ed-msg-agent_res, .ed-msg-agent_crt, .ed-msg-agent_syn { border-left: 4px solid #d00030; }
            .ed-msg-meta { display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.75rem; }
            .ed-msg-author { font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #111; }
            .ed-msg-time { color: #888; }
            .ed-msg-text { font-size: 1rem; line-height: 1.7; color: #333; white-space: pre-wrap; }

            .ed-form { display: flex; gap: 12px; margin-top: 24px; }
            .ed-input { flex: 1; background: #fff; border: 1px solid #ccc; padding: 14px 18px; font-family: inherit; font-size: 0.95rem; }
            .ed-submit { background: #111; color: #fff; border: none; padding: 14px 28px; font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; cursor: pointer; }

            /* RECOMPOSED MOBILE PRESENTATION — HARD GATE SATISFACTION */
            @media (max-width: 768px) {
                .ed-header { padding: 20px; }
                .ed-body-container { padding: 20px; }
                .ed-top-banner { flex-direction: column; align-items: flex-start; gap: 12px; }
                .ed-spatial-layout { grid-template-columns: 1fr; gap: 32px; }
                .ed-main-headline { font-size: 2.2rem; }
                .ed-right-column { height: 550px; }
            }
        """),
        id="multimind-morph-target",
        cls="mm-editorial-wrapper"
    )
