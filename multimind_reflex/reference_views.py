import reflex as rx

# --- State for Reference Interactive Demos ---
class ReferenceState(rx.State):
    # Arknights Interactive State
    arknights_loading_progress: int = 42
    arknights_selected_agent: str = "ALPHA"
    is_deploying: bool = False

    # Noomo Interactive State - Driven by scroll position
    noomo_scroll_progress: int = 0  # 0 to 100 percentage
    noomo_depth_scale: float = 1.0
    noomo_rotation: int = 0

    # Viens-là Interactive State
    viensla_layout_mode: str = "vertical"  # "vertical" or "horizontal"

    def set_arknights_agent(self, agent: str):
        self.arknights_selected_agent = agent

    def trigger_deployment(self):
        self.is_deploying = True
        self.arknights_loading_progress = 95

    def reset_deployment(self):
        self.is_deploying = False
        self.arknights_loading_progress = 42

    def set_noomo_scroll_progress(self, val: int):
        self.noomo_scroll_progress = min(max(val, 0), 100)
        # Compute dynamic scroll-linked scale and rotation
        self.noomo_depth_scale = round(1.0 + (self.noomo_scroll_progress / 100.0) * 0.8, 2)
        self.noomo_rotation = int((self.noomo_scroll_progress / 100.0) * 45)

    def toggle_viensla_layout(self):
        if self.viensla_layout_mode == "vertical":
            self.viensla_layout_mode = "horizontal"
        else:
            self.viensla_layout_mode = "vertical"


# --- Reference A: Arknights Global (Tactical / Interactive / Layered) ---
def arknights_reference() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Top Bar
            rx.hstack(
                rx.text("PRTS // ARKNIGHTS REFERENCE SLICE", font_family="monospace", font_weight="bold", color="#00F0FF", font_size="14px"),
                rx.spacer(),
                rx.badge("SYSTEM: ONLINE", color_scheme="cyan", variant="solid"),
                width="100%",
                padding="16px 24px",
                border_bottom="1px solid rgba(0, 240, 255, 0.2)",
                background="rgba(13, 17, 23, 0.9)",
            ),
            # Main Tactical Hero with Interactive Loading State
            rx.box(
                rx.vstack(
                    rx.image(src="/reference_a/hud_badge.svg", width="220px"),
                    rx.heading("TACTICAL OPERATIVE DEPLOYMENT", font_family="monospace", font_size=rx.breakpoints(initial="22px", md="32px"), color="#FFFFFF", letter_spacing="2px"),

                    # Branded Interactive Progress / Loading Rail
                    rx.vstack(
                        rx.hstack(
                            rx.text("DEBATE CORE SYNCHRONIZATION", font_family="monospace", font_size="11px", color="#00F0FF"),
                            rx.spacer(),
                            rx.text(f"{ReferenceState.arknights_loading_progress}%", font_family="monospace", font_size="11px", color="#FFB800", font_weight="bold"),
                            width="100%",
                        ),
                        rx.box(
                            rx.box(
                                width=f"{ReferenceState.arknights_loading_progress}%",
                                height="100%",
                                background="linear-gradient(90deg, #00F0FF 0%, #FFB800 100%)",
                                transition="width 0.4s ease-in-out",
                            ),
                            width="100%",
                            height="8px",
                            background="rgba(255, 255, 255, 0.1)",
                            border_radius="4px",
                            overflow="hidden",
                            border="1px solid rgba(0, 240, 255, 0.3)",
                        ),
                        width="100%",
                        max_width="500px",
                        margin_y="12px",
                    ),

                    rx.hstack(
                        rx.button(
                            "TRIGGER HIGH-SPEED DEPLOYMENT",
                            on_click=ReferenceState.trigger_deployment,
                            color_scheme="cyan",
                            variant="solid",
                            size="3",
                            id="btn-arknights-deploy",
                        ),
                        rx.button(
                            "RESET SYSTEM",
                            on_click=ReferenceState.reset_deployment,
                            color_scheme="amber",
                            variant="outline",
                            size="3",
                            id="btn-arknights-reset",
                        ),
                        spacing="4",
                        margin_top="12px",
                    ),
                    spacing="4",
                    align="center",
                ),
                padding="40px 24px",
                background="radial-gradient(circle at center, rgba(0, 240, 255, 0.15) 0%, rgba(13, 17, 23, 0.95) 70%)",
                width="100%",
                border_radius="12px",
                box_shadow="0 8px 32px rgba(0, 240, 255, 0.1)",
            ),

            # Interactive Agent Selector Grid
            rx.grid(
                rx.box(
                    rx.hstack(
                        rx.text("OPERATOR ALPHA", font_family="monospace", font_size="12px", color="#00F0FF"),
                        rx.spacer(),
                        rx.button("SELECT", on_click=ReferenceState.set_arknights_agent("ALPHA"), size="1", color_scheme="cyan"),
                    ),
                    rx.heading("REASONING ENGINE", font_size="18px", color="#FFF", margin_top="8px"),
                    rx.text("Active multi-hop debate and verification pass.", font_size="13px", color="#8B949E"),
                    padding="20px",
                    background=rx.cond(ReferenceState.arknights_selected_agent == "ALPHA", "rgba(0, 240, 255, 0.15)", "rgba(22, 27, 34, 0.8)"),
                    border="1px solid rgba(0, 240, 255, 0.4)",
                    border_left="4px solid #00F0FF",
                ),
                rx.box(
                    rx.hstack(
                        rx.text("OPERATOR BETA", font_family="monospace", font_size="12px", color="#FFB800"),
                        rx.spacer(),
                        rx.button("SELECT", on_click=ReferenceState.set_arknights_agent("BETA"), size="1", color_scheme="amber"),
                    ),
                    rx.heading("CRITIC REASONING", font_size="18px", color="#FFF", margin_top="8px"),
                    rx.text("Falsification check and logical consistency review.", font_size="13px", color="#8B949E"),
                    padding="20px",
                    background=rx.cond(ReferenceState.arknights_selected_agent == "BETA", "rgba(255, 184, 0, 0.15)", "rgba(22, 27, 34, 0.8)"),
                    border="1px solid rgba(255, 184, 0, 0.4)",
                    border_left="4px solid #FFB800",
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="4",
                width="100%",
            ),
            width="100%",
            max_width="1200px",
            spacing="6",
        ),
        padding="20px",
        background_color="#0D1117",
        min_height="100vh",
        background_image="url('/textures/grid_pattern.svg')",
        width="100%",
        id="reference-arknights",
    )


# --- Reference B: Noomo Labs (Interactive / Kinetic / Actual Scroll-Linked Choreography) ---
def noomo_reference() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("NOOMO LABS // SPATIAL BENCHMARK", font_family="sans-serif", font_weight="bold", color="#FFF", font_size="16px", letter_spacing="1px"),
                rx.spacer(),
                rx.text("ACTUAL SCROLL-LINKED CHOREOGRAPHY", font_family="monospace", color="#FF3366", font_size="12px"),
                width="100%",
                padding="24px 0px",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("KINETIC SPATIAL INTERACTION", font_size=rx.breakpoints(initial="28px", md="52px"), color="#FFFFFF", font_weight="900", line_height="1.1"),
                    rx.text("Actual scroll-linked motion: scroll progress dynamically drives 3D depth scale and spatial rotation in real time.", color="#A0A0A0", font_size="16px", max_width="700px"),

                    # Scroll Simulation Slider / Observer for Proof
                    rx.hstack(
                        rx.text("SIMULATED SCROLL POSITION:", font_family="monospace", color="#00E5FF", font_size="12px"),
                        rx.slider(
                            value=[ReferenceState.noomo_scroll_progress],
                            on_value_commit=lambda val: ReferenceState.set_noomo_scroll_progress(val[0]),
                            min=0,
                            max=100,
                            width="240px",
                            id="slider-noomo-scroll",
                        ),
                        rx.text(f"{ReferenceState.noomo_scroll_progress}%", font_family="monospace", color="#FF3366", font_weight="bold"),
                        spacing="3",
                        align="center",
                        margin_y="16px",
                    ),

                    # Kinetic Scroll-Driven Spatial Canvas
                    rx.box(
                        rx.vstack(
                            rx.text("SCROLL-LINKED SPATIAL CANVAS", font_family="monospace", color="#00E5FF", font_size="12px"),
                            rx.text(f"SCALE: {ReferenceState.noomo_depth_scale}x  |  ROTATION: {ReferenceState.noomo_rotation}°", color="#FFF", font_weight="bold"),
                            rx.box(
                                rx.text("3D SPATIAL LAYER", font_weight="bold", color="#FF3366"),
                                padding="20px",
                                background="rgba(255, 51, 102, 0.1)",
                                border="1px dashed #FF3366",
                                border_radius="8px",
                                margin_top="12px",
                            ),
                            align="center",
                            spacing="2",
                        ),
                        padding="40px",
                        background="rgba(26, 26, 36, 0.9)",
                        border="2px solid #FF3366",
                        border_radius="16px",
                        transform=f"scale({ReferenceState.noomo_depth_scale}) rotate({ReferenceState.noomo_rotation}deg)",
                        transition="transform 0.2s cubic-bezier(0.1, 0.8, 0.3, 1.0)",
                        margin_y="30px",
                        width="100%",
                        max_width="600px",
                        id="noomo-kinetic-canvas",
                    ),
                    spacing="5",
                    align="start",
                ),
                padding="40px 0px",
                width="100%",
            ),
            width="100%",
            max_width="1200px",
        ),

        # Web-layer scroll observer script to drive Noomo kinetic spatial transform on window scroll
        rx.script("""
            window.addEventListener('scroll', () => {
                const noomoCanvas = document.getElementById('noomo-kinetic-canvas');
                if (noomoCanvas) {
                    const scrollY = window.scrollY;
                    const maxScroll = document.body.scrollHeight - window.innerHeight || 1;
                    const progress = Math.min(Math.max(scrollY / maxScroll, 0), 1);
                    const scale = (1.0 + progress * 0.5).toFixed(2);
                    const rotation = Math.round(progress * 30);
                    noomoCanvas.style.transform = `scale(${scale}) rotate(${rotation}deg)`;
                }
            });
        """),

        padding="20px 40px",
        background_color="#0A0A0F",
        min_height="100vh",
        width="100%",
        id="reference-noomo",
    )


# --- Reference C: Dioriviera (Full-Bleed Luxury Composition / Material) ---
def dioriviera_reference() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Full-bleed Luxury Hero Canvas with Layered Crest
            rx.box(
                rx.vstack(
                    rx.image(src="/reference_c/luxury_crest.svg", width="160px"),
                    rx.text("DIORIVIERA BENCHMARK", font_family="serif", font_size="12px", letter_spacing="6px", color="#8C733E", margin_top="16px"),
                    rx.heading("ESTHÉTIQUE & MATIÈRE", font_family="serif", font_size=rx.breakpoints(initial="32px", md="56px"), font_weight="300", color="#1A1A1A", text_align="center", margin_y="16px"),
                    rx.text("Full-bleed material composition where imagery is structural rather than decorative.", font_family="serif", font_size="18px", color="#444", text_align="center", max_width="650px", font_style="italic"),
                    align="center",
                    spacing="2",
                ),
                width="100%",
                padding="80px 20px",
                background="radial-gradient(ellipse at top, #FAF6EE 0%, #EFE8D8 100%)",
                border_bottom="1px solid #D1C7BD",
            ),

            # Compositional Layered Split Surface
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.text("MATIÈRE NATIVE I", font_family="serif", font_size="14px", letter_spacing="3px", color="#8C733E"),
                        rx.heading("ORGANIC TYPOGRAPHY", font_family="serif", font_size="24px", color="#1A1A1A"),
                        rx.text("High-contrast editorial layout utilizing generous negative space and gold subtle accents.", font_family="serif", font_size="14px", color="#666"),
                        align="start",
                        spacing="3",
                    ),
                    width="50%",
                    padding="40px",
                ),
                rx.box(
                    rx.image(src="/textures/noise_pattern.svg", width="100%", height="240px", object_fit="cover", border_radius="2px"),
                    width="50%",
                    padding="20px",
                ),
                width="100%",
                max_width="1200px",
                padding_y="40px",
            ),
            width="100%",
            align="center",
        ),
        background_color="#F7F5F0",
        min_height="100vh",
        width="100%",
        id="reference-dioriviera",
    )


# --- Reference D: Viens-là (Unconventional Typography / Dynamic Layout) ---
def viensla_reference() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading("VIENS-LÀ", font_family="sans-serif", font_weight="900", font_size="28px", color="#111"),
                rx.spacer(),
                rx.button(
                    f"TOGGLE LAYOUT: {ReferenceState.viensla_layout_mode.upper()}",
                    on_click=ReferenceState.toggle_viensla_layout,
                    size="2",
                    color_scheme="gray",
                    variant="solid",
                    id="btn-viensla-toggle",
                ),
                width="100%",
                padding_bottom="20px",
                border_bottom="3px solid #111",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("TYPOGRAPHY AS ARCHITECTURE", font_size=rx.breakpoints(initial="32px", md="68px"), font_weight="900", line_height="0.95", color="#111", letter_spacing="-2px"),

                    # Unconventional Layout Shift Container
                    rx.cond(
                        ReferenceState.viensla_layout_mode == "vertical",
                        rx.vstack(
                            rx.box("01 // EDITORIAL DIRECTION", font_weight="bold", font_size="14px", padding="20px", border="2px solid #111", width="100%"),
                            rx.box("02 // DIGITAL EXPERIENCE", font_weight="bold", font_size="14px", padding="20px", border="2px solid #111", width="100%", background="#111", color="#FFF"),
                            spacing="3",
                            width="100%",
                            margin_top="24px",
                        ),
                        rx.hstack(
                            rx.box("01 // EDITORIAL DIRECTION", font_weight="bold", font_size="14px", padding="30px", border="2px solid #111", width="100%"),
                            rx.box("02 // DIGITAL EXPERIENCE", font_weight="bold", font_size="14px", padding="30px", border="2px solid #111", width="100%", background="#111", color="#FFF"),
                            spacing="4",
                            width="100%",
                            margin_top="24px",
                        ),
                    ),
                    spacing="4",
                    align="start",
                ),
                padding="40px 0px",
                width="100%",
            ),
            width="100%",
            max_width="1200px",
        ),
        padding="40px 30px",
        background_color="#EFEFEF",
        min_height="100vh",
        width="100%",
        id="reference-viensla",
    )
