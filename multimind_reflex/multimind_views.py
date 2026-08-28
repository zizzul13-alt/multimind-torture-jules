import reflex as rx
from multimind_reflex.state import MultiMindState, Message

def render_message_editorial(msg: Message) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    msg.agent_name,
                    font_family="serif",
                    font_weight="bold",
                    font_size="13px",
                    color=rx.cond(
                        msg.role == "user",
                        "#8C733E",
                        rx.cond(msg.role == "critic", "#DC2626", "#2563EB")
                    ),
                    letter_spacing="1px"
                ),
                rx.spacer(),
                rx.text(msg.timestamp, font_family="monospace", font_size="10px", color="#9CA3AF"),
                width="100%",
            ),
            rx.text(msg.content, font_family="serif", font_size="15px", color="#1F2937", line_height="1.6"),
            spacing="2",
            align="start",
        ),
        padding="18px 22px",
        background=rx.cond(
            msg.role == "user",
            "rgba(240, 238, 233, 0.8)",
            rx.cond(msg.role == "critic", "rgba(254, 242, 242, 0.8)", "rgba(255, 255, 255, 0.9)")
        ),
        border=rx.cond(
            msg.role == "user",
            "1px solid #D1C7BD",
            rx.cond(msg.role == "critic", "1px solid #FECACA", "1px solid #E5E0D8")
        ),
        border_radius="6px",
        margin_y="8px",
        box_shadow="0 2px 8px rgba(0,0,0,0.02)",
        width="100%",
    )

def render_message_tactical(msg: Message) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.badge(
                    msg.agent_name,
                    color_scheme=rx.cond(msg.role == "critic", "amber", "cyan"),
                    variant="solid",
                    font_size="10px"
                ),
                rx.spacer(),
                rx.text(msg.timestamp, font_family="monospace", font_size="10px", color="#6B7280"),
                width="100%",
            ),
            rx.text(msg.content, font_family="monospace", font_size="13px", color="#E5E7EB", line_height="1.5"),
            spacing="2",
            align="start",
        ),
        padding="14px 18px",
        background="rgba(17, 24, 39, 0.85)",
        border="1px solid rgba(75, 85, 99, 0.4)",
        border_left=rx.cond(
            msg.role == "critic",
            "4px solid #FFB800",
            rx.cond(msg.role == "user", "4px solid #38BDF8", "4px solid #00F0FF")
        ),
        border_radius="2px",
        margin_y="6px",
        width="100%",
    )

# Desktop Morphology A: Editorial / Spatial
def editorial_morphology() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Top Editorial Bar
            rx.hstack(
                rx.hstack(
                    rx.image(src="/reference_c/luxury_crest.svg", width="36px"),
                    rx.heading("MULTIMIND", font_family="serif", font_size="20px", letter_spacing="3px", color="#1A1A1A"),
                    spacing="3",
                    align="center",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.badge("MORPHOLOGY A: EDITORIAL", variant="outline", color_scheme="gold"),
                    rx.button(
                        "SWITCH TO TACTICAL HUD",
                        on_click=MultiMindState.toggle_morphology,
                        variant="solid",
                        color_scheme="gray",
                        size="2",
                        id="btn-morphology-switch",
                    ),
                    spacing="3",
                ),
                width="100%",
                padding="16px 24px",
                border_bottom="1px solid #EAE5D9",
                background="#FBF9F5",
            ),

            # Agent Status Rail
            rx.hstack(
                rx.foreach(
                    MultiMindState.agent_status,
                    lambda item: rx.box(
                        rx.hstack(
                            rx.text(item[0], font_family="serif", font_size="12px", font_weight="bold", color="#1A1A1A"),
                            rx.badge(item[1], size="1", variant="soft", color_scheme=rx.cond(item[1] == "RUNNING", "green", "gray")),
                            spacing="2",
                        ),
                        padding="8px 16px",
                        background="#FFF",
                        border="1px solid #E5E0D8",
                        border_radius="20px",
                    )
                ),
                spacing="3",
                padding="12px 24px",
                width="100%",
                overflow_x="auto",
                background="#F7F5F0",
            ),

            # Main Editorial Chat Surface
            rx.box(
                rx.vstack(
                    rx.foreach(
                        MultiMindState.messages,
                        render_message_editorial
                    ),
                    width="100%",
                    id="chat-messages-container",
                ),
                padding="24px",
                height="65vh",
                overflow_y="auto",
                width="100%",
                background="#FAF8F5",
                id="editorial-scroll-area",
            ),

            # Input Control Box
            rx.hstack(
                rx.input(
                    placeholder="Type a message or instruction...",
                    value=MultiMindState.new_message_text,
                    on_change=MultiMindState.set_new_message_text,
                    width="100%",
                    size="3",
                    variant="surface",
                    id="input-message",
                ),
                rx.button("SEND", on_click=MultiMindState.send_message, size="3", color_scheme="amber", id="btn-send"),
                padding="16px 24px",
                width="100%",
                background="#FBF9F5",
                border_top="1px solid #EAE5D9",
            ),
            width="100%",
            spacing="0",
        ),
        width="100%",
        background="#FBF9F5",
        id="morphology-editorial",
    )

# Desktop Morphology B: Tactical / Layered
def tactical_morphology() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Top Tactical Bar
            rx.hstack(
                rx.hstack(
                    rx.image(src="/reference_a/hud_badge.svg", width="120px"),
                    rx.text("MULTIMIND // TACTICAL HUD", font_family="monospace", font_weight="bold", color="#00F0FF", font_size="16px"),
                    spacing="3",
                    align="center",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.badge("MORPHOLOGY B: TACTICAL", color_scheme="cyan", variant="solid"),
                    rx.button(
                        "SWITCH TO EDITORIAL",
                        on_click=MultiMindState.toggle_morphology,
                        variant="outline",
                        color_scheme="cyan",
                        size="2",
                        id="btn-morphology-switch-tactical",
                    ),
                    spacing="3",
                ),
                width="100%",
                padding="12px 20px",
                border_bottom="1px solid rgba(0, 240, 255, 0.3)",
                background="rgba(10, 15, 26, 0.95)",
            ),

            # Agent Status Rail
            rx.grid(
                rx.foreach(
                    MultiMindState.agent_status,
                    lambda item: rx.box(
                        rx.hstack(
                            rx.text(item[0], font_family="monospace", font_size="11px", color="#00F0FF"),
                            rx.spacer(),
                            rx.text(
                                item[1],
                                font_family="monospace",
                                font_size="11px",
                                font_weight="bold",
                                color=rx.cond(item[1] == "RUNNING", "#FFB800", "#9CA3AF")
                            ),
                        ),
                        padding="8px 12px",
                        background="rgba(17, 24, 39, 0.8)",
                        border="1px solid rgba(0, 240, 255, 0.2)",
                    )
                ),
                columns=rx.breakpoints(initial="2", md="4"),
                spacing="2",
                padding="12px 20px",
                width="100%",
                background="#0B0F19",
            ),

            # Main Tactical Chat Surface
            rx.box(
                rx.vstack(
                    rx.foreach(
                        MultiMindState.messages,
                        render_message_tactical
                    ),
                    width="100%",
                    id="chat-messages-container-tactical",
                ),
                padding="20px",
                height="65vh",
                overflow_y="auto",
                width="100%",
                background="#0D1117",
                id="tactical-scroll-area",
            ),

            # Tactical Input Control Box
            rx.hstack(
                rx.input(
                    placeholder="ENTER COMMAND OR MULTI-AGENT PROMPT...",
                    value=MultiMindState.new_message_text,
                    on_change=MultiMindState.set_new_message_text,
                    width="100%",
                    size="3",
                    id="input-message-tactical",
                ),
                rx.button("EXECUTE", on_click=MultiMindState.send_message, size="3", color_scheme="cyan", id="btn-send-tactical"),
                padding="16px 20px",
                width="100%",
                background="rgba(10, 15, 26, 0.95)",
                border_top="1px solid rgba(0, 240, 255, 0.3)",
            ),
            width="100%",
            spacing="0",
        ),
        width="100%",
        background="#0D1117",
        background_image="url('/textures/grid_pattern.svg')",
        id="morphology-tactical",
    )


# --- PURPOSE-BUILT MOBILE MORPHOLOGIES (HARD GATE) ---

# Mobile Morphology A: Editorial / Spatial
def mobile_editorial_view() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Editorial Mobile Header
            rx.hstack(
                rx.image(src="/reference_c/luxury_crest.svg", width="28px"),
                rx.text("MULTIMIND MAISON", font_family="serif", font_weight="bold", font_size="14px", color="#1A1A1A", letter_spacing="2px"),
                rx.spacer(),
                rx.button("TACTICAL MODE", on_click=MultiMindState.toggle_morphology, size="1", color_scheme="gold", variant="solid", id="btn-mobile-toggle-a"),
                width="100%",
                padding="12px 16px",
                background="#FBF9F5",
                border_bottom="1px solid #EAE5D9",
            ),

            # Floating Circular Status Pill
            rx.box(
                rx.hstack(
                    rx.text("4 AGENTS SYNTHESIZING", font_family="serif", font_size="11px", color="#8C733E", font_style="italic"),
                    rx.spacer(),
                    rx.badge("RUNNING", color_scheme="green", variant="soft", size="1"),
                    width="100%",
                ),
                padding="8px 16px",
                background="#FAF8F5",
                border_bottom="1px solid #E5E0D8",
                width="100%",
            ),

            # Mobile Conversation Flow (Editorial)
            rx.box(
                rx.vstack(
                    rx.foreach(
                        MultiMindState.messages,
                        render_message_editorial
                    ),
                    width="100%",
                ),
                padding="12px",
                height="68vh",
                overflow_y="auto",
                width="100%",
                id="mobile-scroll-area-a",
            ),

            # Floating Rounded Control Surface
            rx.box(
                rx.hstack(
                    rx.input(
                        placeholder="Editorial prompt...",
                        value=MultiMindState.new_message_text,
                        on_change=MultiMindState.set_new_message_text,
                        width="100%",
                        size="2",
                        variant="surface",
                        id="input-mobile-msg-a",
                    ),
                    rx.button("SEND", on_click=MultiMindState.send_message, size="2", color_scheme="amber", id="btn-mobile-send-a"),
                    spacing="2",
                    width="100%",
                ),
                padding="12px 16px",
                background="#FBF9F5",
                border_top="1px solid #EAE5D9",
                position="sticky",
                bottom="0",
                width="100%",
            ),
            width="100%",
            spacing="0",
        ),
        width="100%",
        min_height="100vh",
        background="#FAF8F5",
        id="mobile-editorial-surface",
    )

# Mobile Morphology B: Tactical HUD
def mobile_tactical_view() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Tactical Sci-Fi Mobile Header
            rx.hstack(
                rx.image(src="/reference_a/hud_badge.svg", width="80px"),
                rx.text("PRTS // MOBILE HUD", font_family="monospace", font_weight="bold", font_size="13px", color="#00F0FF"),
                rx.spacer(),
                rx.button("EDITORIAL MODE", on_click=MultiMindState.toggle_morphology, size="1", color_scheme="cyan", variant="outline", id="btn-mobile-toggle-b"),
                width="100%",
                padding="10px 14px",
                background="rgba(10, 15, 26, 0.98)",
                border_bottom="1px solid rgba(0, 240, 255, 0.3)",
            ),

            # Dense Monospace Status Rail
            rx.box(
                rx.hstack(
                    rx.text("DEBATE CORE: ONLINE", font_family="monospace", font_size="10px", color="#FFB800"),
                    rx.spacer(),
                    rx.badge("TACTICAL PASS 04", color_scheme="cyan", size="1"),
                    width="100%",
                ),
                padding="6px 14px",
                background="#0B0F19",
                border_bottom="1px solid rgba(75, 85, 99, 0.4)",
                width="100%",
            ),

            # Mobile Conversation Flow (Tactical)
            rx.box(
                rx.vstack(
                    rx.foreach(
                        MultiMindState.messages,
                        render_message_tactical
                    ),
                    width="100%",
                ),
                padding="10px",
                height="68vh",
                overflow_y="auto",
                width="100%",
                id="mobile-scroll-area-b",
            ),

            # Segmented Mobile Command Console
            rx.box(
                rx.hstack(
                    rx.input(
                        placeholder="ENTER CMD...",
                        value=MultiMindState.new_message_text,
                        on_change=MultiMindState.set_new_message_text,
                        width="100%",
                        size="2",
                        id="input-mobile-msg-b",
                    ),
                    rx.button("EXEC", on_click=MultiMindState.send_message, size="2", color_scheme="cyan", id="btn-mobile-send-b"),
                    spacing="2",
                    width="100%",
                ),
                padding="10px 14px",
                background="rgba(10, 15, 26, 0.98)",
                border_top="1px solid rgba(0, 240, 255, 0.3)",
                position="sticky",
                bottom="0",
                width="100%",
            ),
            width="100%",
            spacing="0",
        ),
        width="100%",
        min_height="100vh",
        background="#0D1117",
        background_image="url('/textures/grid_pattern.svg')",
        id="mobile-tactical-surface",
    )

# Router for Mobile Surface based on state
def mobile_multimind_view() -> rx.Component:
    return rx.match(
        MultiMindState.current_morphology,
        ("tactical", mobile_tactical_view()),
        mobile_editorial_view(),
    )
