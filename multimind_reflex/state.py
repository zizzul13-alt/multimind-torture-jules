import reflex as rx
from pydantic import BaseModel

class Message(BaseModel):
    id: int
    sender: str
    role: str # "user" | "agent" | "system" | "critic"
    agent_name: str
    content: str
    timestamp: str

def generate_mock_conversation() -> list[Message]:
    messages = []
    sample_agents = ["Research Agent", "Critic Agent", "Synthesis Agent", "Safety Guardrail"]

    messages.append(Message(id=1, sender="User", role="user", agent_name="User", content="Execute comprehensive multi-agent analysis on Reflex framework vs FastHTML for MultiMind migration target.", timestamp="10:00:01"))

    for i in range(2, 37):
        agent = sample_agents[(i - 2) % len(sample_agents)]
        if i % 3 == 0:
            role = "user"
            sender = "User"
            agent_name = "User"
            content = f"Question/Prompt #{i//3}: Can we evaluate performance, state preservation, and custom JS escape hatch burden for iteration {i}?"
        elif agent == "Critic Agent":
            role = "critic"
            sender = "Critic Agent"
            agent_name = "Critic Agent"
            content = f"Falsification Analysis #{i}: High dependency on React component wrappers will reduce ABSTRACTION_SURVIVAL_PERCENT. Native Reflex state bindings must be verified."
        else:
            role = "agent"
            sender = agent
            agent_name = agent
            content = f"Agent Assessment Step {i}: Evaluating capability vector {i}. Reactive state synchronization across live morphology mutation preserves session data flawlessly."

        messages.append(Message(id=i, sender=sender, role=role, agent_name=agent_name, content=content, timestamp=f"10:{i//60:02d}:{i%60:02d}"))
    return messages

class MultiMindState(rx.State):
    # Session / Presentation State
    current_morphology: str = "editorial"  # "editorial" (Morphology A) or "tactical" (Morphology B)
    active_tab: str = "multimind"          # "multimind", "ref_a", "ref_b", "ref_c", "ref_d"

    # Conversation Data
    messages: list[Message] = generate_mock_conversation()
    new_message_text: str = ""

    # Scroll position preservation state across mutations
    last_scroll_top: int = 0

    # Multi-agent debate state
    agent_status: dict[str, str] = {
        "Research Agent": "RUNNING",
        "Critic Agent": "WAITING",
        "Synthesis Agent": "PENDING",
        "Safety Guardrail": "ACTIVE",
    }
    is_loading: bool = False
    loading_progress: int = 65

    def set_new_message_text(self, text: str):
        self.new_message_text = text

    def toggle_morphology(self):
        """Live Presentation Mutation - switch morphology without full page reload while keeping state"""
        if self.current_morphology == "editorial":
            self.current_morphology = "tactical"
        else:
            self.current_morphology = "editorial"

    def set_active_tab(self, tab: str):
        self.active_tab = tab

    def set_scroll_position(self, scroll_top: int):
        self.last_scroll_top = scroll_top

    def send_message(self):
        if not self.new_message_text.strip():
            return
        new_id = len(self.messages) + 1
        msg = Message(
            id=new_id,
            sender="User",
            role="user",
            agent_name="User",
            content=self.new_message_text,
            timestamp="10:45:00"
        )
        self.messages.append(msg)
        self.new_message_text = ""
