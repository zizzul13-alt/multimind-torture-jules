import reflex as rx
from multimind_reflex.state import MultiMindState
from multimind_reflex.reference_views import (
    arknights_reference,
    noomo_reference,
    dioriviera_reference,
    viensla_reference,
)
from multimind_reflex.multimind_views import (
    editorial_morphology,
    tactical_morphology,
)

def nav_tab_button(label: str, tab_id: str) -> rx.Component:
    is_active = MultiMindState.active_tab == tab_id
    button_id = f"tab-{tab_id.replace('_', '-')}"
    return rx.button(
        label,
        on_click=MultiMindState.set_active_tab(tab_id),
        variant=rx.cond(is_active, "solid", "ghost"),
        color_scheme="cyan",
        size="2",
        id=button_id,
    )

def index() -> rx.Component:
    return rx.box(
        # Top Navigation Rail across all surfaces
        rx.hstack(
            rx.hstack(
                rx.image(src="/branding/multimind_logo.svg", width="32px"),
                rx.text("MULTIMIND BENCHMARK", font_weight="bold", color="#FFF", font_size="15px"),
                spacing="3",
                align="center",
            ),
            rx.spacer(),
            rx.hstack(
                nav_tab_button("MultiMind Surface", "multimind"),
                nav_tab_button("Ref A (Arknights)", "ref_a"),
                nav_tab_button("Ref B (Noomo)", "ref_b"),
                nav_tab_button("Ref C (Dioriviera)", "ref_c"),
                nav_tab_button("Ref D (Viens-là)", "ref_d"),
                spacing="2",
                overflow_x="auto",
            ),
            width="100%",
            padding="12px 24px",
            background="#0B0F19",
            border_bottom="1px solid rgba(255,255,255,0.1)",
        ),

        # Main Surface Content Routing based on active_tab
        rx.match(
            MultiMindState.active_tab,
            ("ref_a", arknights_reference()),
            ("ref_b", noomo_reference()),
            ("ref_c", dioriviera_reference()),
            ("ref_d", viensla_reference()),
            # Default: MultiMind Surface
            rx.match(
                MultiMindState.current_morphology,
                ("tactical", tactical_morphology()),
                editorial_morphology(),
            ),
        ),

        # Client-side JavaScript snippet to preserve scroll position across morphology toggles
        rx.script("""
            window.addEventListener('DOMContentLoaded', () => {
                let currentScroll = 0;
                document.addEventListener('scroll', (e) => {
                    if (e.target && e.target.id && e.target.id.includes('scroll-area')) {
                        currentScroll = e.target.scrollTop;
                    }
                }, true);

                const observer = new MutationObserver(() => {
                    const scrollAreas = ['editorial-scroll-area', 'tactical-scroll-area', 'mobile-scroll-area'];
                    scrollAreas.forEach(id => {
                        const el = document.getElementById(id);
                        if (el && currentScroll > 0) {
                            el.scrollTop = currentScroll;
                        }
                    });
                });
                observer.observe(document.body, { childList: true, subtree: true });
            });
        """),

        width="100%",
        min_height="100vh",
        background="#090D16",
        id="app-container",
    )

app = rx.App()
app.add_page(index, route="/")
