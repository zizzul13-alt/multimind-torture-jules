from fasthtml.common import *
import sys
sys.path.append('.')

from references.ref_arknights import render_arknights_proof, handle_arknights_deploy
from references.ref_noomo import render_noomo_proof
from references.ref_dioriviera import render_dioriviera_proof
from references.ref_viensla import render_viensla_proof
from multimind_surface import render_multimind_app, SESSION_DATA

app, rt = fast_app(
    pico=False,
    hdrs=(
        Link(rel="stylesheet", href="/static/css/global.css", type="text/css"),
        Meta(name="viewport", content="width=device-width, initial-scale=1, viewport-fit=cover")
    )
)

# Global layout shell for reference switcher navigation
def with_shell(content, current_route="/"):
    return Title("MultiMind Platform Torture Benchmark — FastHTML"), Div(
        Header(
            Div(
                Span("MULTIMIND BENCHMARK", cls="shell-title"),
                Nav(
                    A("PARITY: ARKNIGHTS", href="/ref/arknights", cls=f"shell-link {'active' if current_route=='/ref/arknights' else ''}"),
                    A("PARITY: NOOMO LABS", href="/ref/noomo", cls=f"shell-link {'active' if current_route=='/ref/noomo' else ''}"),
                    A("PARITY: DIORIVIERA", href="/ref/dioriviera", cls=f"shell-link {'active' if current_route=='/ref/dioriviera' else ''}"),
                    A("PARITY: VIENS-LÀ", href="/ref/viensla", cls=f"shell-link {'active' if current_route=='/ref/viensla' else ''}"),
                    A("MULTIMIND SURFACE", href="/multimind", cls=f"shell-link highlight {'active' if current_route=='/multimind' else ''}"),
                    cls="shell-nav"
                ),
                cls="shell-header-inner"
            ),
            cls="shell-header"
        ),
        Main(content, id="app-content-root"),
        Style("""
            body { margin: 0; padding: 0; background: #000; font-family: system-ui, sans-serif; }
            .shell-header { background: #0a0c10; border-bottom: 1px solid #1f2937; padding: 10px 20px; color: #fff; }
            .shell-header-inner { display: flex; justify-content: space-between; align-items: center; max-width: 1600px; margin: 0 auto; }
            .shell-title { font-weight: 900; letter-spacing: 2px; font-size: 0.85rem; color: #ff0055; }
            .shell-nav { display: flex; gap: 12px; }
            .shell-link { color: #9ca3af; text-decoration: none; font-size: 0.75rem; padding: 6px 12px; border-radius: 4px; border: 1px solid transparent; transition: all 0.2s; }
            .shell-link:hover, .shell-link.active { color: #fff; border-color: #374151; background: #111827; }
            .shell-link.highlight { background: #00e6c8; color: #000; font-weight: bold; }
            .shell-link.highlight:hover { background: #00ffd5; }
        """)
    )

@rt("/")
def get_home():
    return with_shell(render_multimind_app(SESSION_DATA), current_route="/multimind")

@rt("/ref/arknights")
def get_ark():
    return with_shell(render_arknights_proof(), current_route="/ref/arknights")

@rt("/ref/arknights/deploy", methods=["POST"])
def post_ark_deploy():
    return handle_arknights_deploy()

@rt("/ref/noomo")
def get_noomo():
    return with_shell(render_noomo_proof(), current_route="/ref/noomo")

@rt("/ref/dioriviera")
def get_dior():
    return with_shell(render_dioriviera_proof(), current_route="/ref/dioriviera")

@rt("/ref/viensla")
def get_viensla():
    return with_shell(render_viensla_proof(), current_route="/ref/viensla")

@rt("/multimind")
def get_multimind():
    return with_shell(
        Div(render_multimind_app(SESSION_DATA), id="multimind-app-container"),
        current_route="/multimind"
    )

# HTMX Mutation Route — Swaps Morphology Live without full page reload or session loss
@rt("/mutate-presentation", methods=["POST"])
def post_mutate(to: str = "tactical"):
    SESSION_DATA["active_morphology"] = to
    # Returns only the inner app HTML partial for HTMX swap
    return render_multimind_app(SESSION_DATA)

# HTMX Agent Step Trigger Route
@rt("/trigger-agent-step", methods=["POST"])
def post_agent_step():
    # Advance agent state sequentially
    if SESSION_DATA["agents"][1]["status"] == "RUNNING":
        SESSION_DATA["agents"][1]["status"] = "COMPLETED"
        SESSION_DATA["agents"][1]["score"] = 0.91
        SESSION_DATA["agents"][2]["status"] = "RUNNING"
        SESSION_DATA["messages"].append({
            "id": len(SESSION_DATA["messages"]) + 1,
            "sender": "agent_syn",
            "author": "Synthesis Agent",
            "timestamp": "14:22:01",
            "content": "FINAL VERDICT:\nFastHTML successfully maintains zero-refresh live morphology swaps, preserving all in-memory multi-agent debate history and active user context."
        })
    return render_multimind_app(SESSION_DATA)

# HTMX Chat Message Submit Route
@rt("/send-message", methods=["POST"])
def post_message(message: str = ""):
    if message.strip():
        SESSION_DATA["messages"].append({
            "id": len(SESSION_DATA["messages"]) + 1,
            "sender": "user",
            "author": SESSION_DATA["user_name"],
            "timestamp": "14:22:45",
            "content": message
        })
    return render_multimind_app(SESSION_DATA)

if __name__ == "__main__":
    serve()
