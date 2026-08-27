import reflex as rx

# --- Reference A: Arknights Global (Tactical / Layered / Industrial) ---
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
            # Main Hero
            rx.box(
                rx.vstack(
                    rx.image(src="/reference_a/hud_badge.svg", width="200px"),
                    rx.heading("TACTICAL OPERATIVE DEPLOYMENT", font_family="monospace", font_size="32px", color="#FFFFFF", letter_spacing="2px"),
                    rx.text("Layered industrial interface with dynamic HUD status rails, scroll choreography, and responsive identity.", color="#8B949E", max_width="600px", text_align="center"),
                    rx.hstack(
                        rx.button("INITIALIZE CORE", color_scheme="cyan", variant="outline", size="3"),
                        rx.button("VIEW TACTICAL DATA", color_scheme="amber", variant="solid", size="3"),
                        spacing="4",
                        margin_top="16px",
                    ),
                    spacing="4",
                    align="center",
                ),
                padding="60px 24px",
                background="radial-gradient(circle at center, rgba(0, 240, 255, 0.15) 0%, rgba(13, 17, 23, 0.95) 70%)",
                width="100%",
                border_radius="12px",
                margin_y="20px",
                box_shadow="0 8px 32px rgba(0, 240, 255, 0.1)",
            ),
            # Status Grid
            rx.grid(
                rx.box(
                    rx.text("AGENT ALPHA", font_family="monospace", font_size="12px", color="#00F0FF"),
                    rx.heading("REASONING ENGINE", font_size="18px", color="#FFF"),
                    rx.text("Active multi-hop debate and verification pass.", font_size="13px", color="#8B949E"),
                    padding="20px",
                    background="rgba(22, 27, 34, 0.8)",
                    border="1px solid rgba(0, 240, 255, 0.2)",
                    border_left="4px solid #00F0FF",
                ),
                rx.box(
                    rx.text("AGENT BETA", font_family="monospace", font_size="12px", color="#FFB800"),
                    rx.heading("CRITIC REASONING", font_size="18px", color="#FFF"),
                    rx.text("Falsification check and logical consistency review.", font_size="13px", color="#8B949E"),
                    padding="20px",
                    background="rgba(22, 27, 34, 0.8)",
                    border="1px solid rgba(255, 184, 0, 0.2)",
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

# --- Reference B: Noomo Labs (Interactive / Kinetic / Spatial) ---
def noomo_reference() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("NOOMO LABS // INTERACTIVE BENCHMARK", font_family="sans-serif", font_weight="bold", color="#FFF", font_size="16px", letter_spacing="1px"),
                rx.spacer(),
                rx.text("EXPERIMENT 04", font_family="monospace", color="#FF3366", font_size="12px"),
                width="100%",
                padding="24px 0px",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("KINETIC SPATIAL INTERACTION", font_size=rx.breakpoints(initial="32px", md="56px"), color="#FFFFFF", font_weight="900", line_height="1.1"),
                    rx.text("Scroll-linked motion, interactive layer composition, and non-standard fluid layout hierarchy.", color="#A0A0A0", font_size="18px", max_width="700px"),
                    rx.box(
                        rx.hstack(
                            rx.box(rx.text("01 / MOTION", color="#FF3366", font_weight="bold"), rx.text("Smooth kinetic transitions", color="#FFF", font_size="14px"), padding="16px", background="#1A1A24", border_radius="8px", width="100%"),
                            rx.box(rx.text("02 / SPATIAL", color="#00E5FF", font_weight="bold"), rx.text("3D visual depth layers", color="#FFF", font_size="14px"), padding="16px", background="#1A1A24", border_radius="8px", width="100%"),
                            spacing="4",
                            width="100%",
                        ),
                        margin_top="32px",
                        width="100%",
                    ),
                    spacing="5",
                    align="start",
                ),
                padding="60px 0px",
                width="100%",
            ),
            width="100%",
            max_width="1200px",
        ),
        padding="20px 40px",
        background_color="#0A0A0F",
        min_height="100vh",
        width="100%",
        id="reference-noomo",
    )

# --- Reference C: Dioriviera (Luxury / Material / Editorial) ---
def dioriviera_reference() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.center(
                rx.image(src="/reference_c/luxury_crest.svg", width="140px"),
                padding="30px 0",
            ),
            rx.text("DIORIVIERA BENCHMARK", font_family="serif", font_size="12px", letter_spacing="4px", color="#8C733E"),
            rx.heading("ESTHÉTIQUE & MATIÈRE", font_family="serif", font_size=rx.breakpoints(initial="28px", md="48px"), font_weight="300", color="#1A1A1A", text_align="center", margin_y="16px"),
            rx.text("A restrained luxury presentation with full-bleed materials, generous negative space, and refined typography control.", font_family="serif", font_size="16px", color="#555", text_align="center", max_width="600px", font_style="italic"),
            rx.grid(
                rx.box(
                    rx.image(src="/textures/noise_pattern.svg", width="100%", height="260px", object_fit="cover", border_radius="4px"),
                    rx.text("COLLECTION I", font_family="serif", font_size="14px", letter_spacing="2px", color="#1A1A1A", margin_top="12px"),
                    rx.text("Material Synthesis & Spatial Flow", font_family="serif", font_size="12px", color="#777"),
                    padding="16px",
                    background="#FBF9F5",
                    border="1px solid #EAE5D9",
                ),
                rx.box(
                    rx.image(src="/textures/grid_pattern.svg", width="100%", height="260px", object_fit="cover", border_radius="4px", background="#222"),
                    rx.text("COLLECTION II", font_family="serif", font_size="14px", letter_spacing="2px", color="#1A1A1A", margin_top="12px"),
                    rx.text("Tactical Geometry in Fine Detail", font_family="serif", font_size="12px", color="#777"),
                    padding="16px",
                    background="#FBF9F5",
                    border="1px solid #EAE5D9",
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="6",
                width="100%",
                margin_top="40px",
            ),
            width="100%",
            max_width="1100px",
            align="center",
        ),
        padding="40px 20px",
        background_color="#F7F5F0",
        min_height="100vh",
        width="100%",
        id="reference-dioriviera",
    )

# --- Reference D: Viens-là (Typography / Unconventional Layout) ---
def viensla_reference() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading("VIENS-LÀ", font_family="sans-serif", font_weight="900", font_size="24px", color="#111"),
                rx.spacer(),
                rx.text("EDITORIAL BENCHMARK '26", font_family="monospace", font_size="12px", color="#666"),
                width="100%",
                padding_bottom="20px",
                border_bottom="2px solid #111",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("TYPOGRAPHY AS ARCHITECTURE", font_size=rx.breakpoints(initial="36px", md="72px"), font_weight="900", line_height="0.95", color="#111", letter_spacing="-2px"),
                    rx.hstack(
                        rx.text("(01)", font_family="monospace", font_weight="bold", color="#111"),
                        rx.text("Unconventional layout structures, horizontal/vertical behavior shifts, microinteractions, and deliberate editorial hierarchy.", color="#444", font_size="16px", max_width="650px"),
                        spacing="4",
                        align="start",
                        margin_top="24px",
                    ),
                    spacing="4",
                    align="start",
                ),
                padding="60px 0px",
                width="100%",
            ),
            rx.hstack(
                rx.box("01 // CREATIVE DIRECTION", font_weight="bold", font_size="13px", padding="16px 24px", border="1px solid #111", width="100%"),
                rx.box("02 // DIGITAL EXPERIENCE", font_weight="bold", font_size="13px", padding="16px 24px", border="1px solid #111", width="100%", background="#111", color="#FFF"),
                spacing="0",
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
