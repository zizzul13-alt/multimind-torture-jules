from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from backend.models import Session, AgentStatus, Message, ActionRequest, ActionResponse
from typing import List

app = FastAPI(title="MultiMind FastAPI Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock initial session state with long conversation messages
def generate_mock_session() -> Session:
    agents = [
        AgentStatus(
            id="agent-arch",
            name="Architect-Prime",
            role="System Architect",
            avatar="🏛️",
            status="RUNNING",
            model="Claude-3.5-Sonnet",
            tokens_used=14200,
            confidence=0.96,
            current_thought="Evaluating asynchronous state hydration versus SvelteKit SSR hydrators..."
        ),
        AgentStatus(
            id="agent-sec",
            name="Sentinel-Sec",
            role="Security Analyst",
            avatar="🛡️",
            status="ACTIVE",
            model="GPT-4o",
            tokens_used=9850,
            confidence=0.92,
            current_thought="Auditing API boundary parameter sanitization and CORS security policies."
        ),
        AgentStatus(
            id="agent-perf",
            name="Hyper-V",
            role="Performance Engineer",
            avatar="⚡",
            status="WAITING",
            model="DeepSeek-R1",
            tokens_used=18400,
            confidence=0.98,
            current_thought="Analyzing paint lifecycle cost and initial bundle JS payload budget."
        )
    ]

    # Generate multi-turn long conversation
    messages = []

    # Message 1
    messages.append(Message(
        id="msg-001",
        sender_id="user-01",
        sender_name="Jules Lead",
        sender_role="user",
        avatar="👤",
        content="Welcome team. We are conducting the MultiMind Torture Benchmark evaluating SvelteKit + FastAPI vs Python-first frameworks. Please present your preliminary architecture assessments.",
        timestamp="10:00:15",
        tokens=34
    ))

    # Message 2
    messages.append(Message(
        id="msg-002",
        sender_id="agent-arch",
        sender_name="Architect-Prime",
        sender_role="agent",
        avatar="🏛️",
        content="Initial telemetry indicates SvelteKit provides standard DOM ownership while FastAPI handles structured validation with Pydantic. Unlike Reflex or FastHTML, presentation logic is completely decoupled from backend Python models.",
        timestamp="10:00:42",
        thought_process="Analysis complete: Zero python-to-JS compilation escape hatches required for core DOM manipulation.",
        code_snippet="""// SvelteKit state contract
export let sessionState = writable<SessionData>();
""",
        tokens=180,
        agent_status="RUNNING"
    ))

    # Message 3
    messages.append(Message(
        id="msg-003",
        sender_id="agent-sec",
        sender_name="Sentinel-Sec",
        sender_role="agent",
        avatar="🛡️",
        content="The security boundary is strictly enforced via FastAPI OpenAPI definitions. The SvelteKit frontend consumes typed JSON payloads without ambient server session leakages.",
        timestamp="10:01:10",
        thought_process="CORS verification completed across standard dev ports.",
        tokens=120,
        agent_status="ACTIVE"
    ))

    # Message 4
    messages.append(Message(
        id="msg-004",
        sender_id="agent-perf",
        sender_name="Hyper-V",
        sender_role="agent",
        avatar="⚡",
        content="Performance audit update: Svelte compiler output contains zero heavy virtual-DOM runtime overhead. Page load initial JS stays lightweight while preserving smooth 60fps presentation switching.",
        timestamp="10:01:45",
        thought_process="Hydrated bundle benchmark target: < 150KB total payload.",
        tokens=145,
        agent_status="WAITING"
    ))

    # Generate 20 additional long conversation entries for torture testing
    for i in range(5, 26):
        agent_idx = (i % 3)
        ag = agents[agent_idx]
        messages.append(Message(
            id=f"msg-0{i:02d}",
            sender_id=ag.id,
            sender_name=ag.name,
            sender_role="agent",
            avatar=ag.avatar,
            content=f"[Torture Message Turn #{i}] Evaluating multi-turn debate item #{i}. The agent consensus matrix is dynamically validating session continuity, scroll preservation, and presentation switching without full page reload across both desktop and 390x844 viewports.",
            timestamp=f"10:{i:02d}:30",
            thought_process=f"Agent internal trace #{i}: Validating layout stability, DOM tree depth, and CSS transform efficiency.",
            tokens=110 + i * 5,
            agent_status=ag.status
        ))

    return Session(
        id="session-multimind-torture-01",
        title="Candidate 3 — SvelteKit + FastAPI Architecture Benchmark",
        topic="Full-Stack Ceiling & Performance Evaluation",
        created_at="2025-08-28 10:00:00",
        status="ACTIVE_DEBATE",
        total_tokens=42450,
        active_morphology="editorial",
        user_name="Jules Lead",
        user_avatar="👤",
        agents=agents,
        messages=messages
    )

CURRENT_SESSION = generate_mock_session()

@app.get("/api/health")
def get_health():
    return {"status": "ok", "backend": "FastAPI", "version": "1.0.0"}

@app.get("/api/session", response_model=Session)
def get_session():
    return CURRENT_SESSION

@app.get("/api/session/messages", response_model=List[Message])
def get_messages():
    return CURRENT_SESSION.messages

@app.get("/api/session/agents", response_model=List[AgentStatus])
def get_agents():
    return CURRENT_SESSION.agents

@app.post("/api/session/action", response_model=ActionResponse)
def handle_action(req: ActionRequest):
    global CURRENT_SESSION
    if req.action_type == "change_morphology":
        new_morph = req.payload.get("morphology", "editorial") if req.payload else "editorial"
        CURRENT_SESSION.active_morphology = new_morph
        return ActionResponse(
            success=True,
            message=f"Morphology updated to {new_morph}",
            updated_session=CURRENT_SESSION
        )
    elif req.action_type == "send_message":
        text = req.payload.get("text", "") if req.payload else ""
        if text:
            new_msg = Message(
                id=f"msg-{len(CURRENT_SESSION.messages)+1:03d}",
                sender_id="user-01",
                sender_name="Jules Lead",
                sender_role="user",
                avatar="👤",
                content=text,
                timestamp="10:30:00",
                tokens=len(text) // 4 + 5
            )
            CURRENT_SESSION.messages.append(new_msg)
            return ActionResponse(
                success=True,
                message="Message added successfully",
                updated_session=CURRENT_SESSION
            )
    elif req.action_type == "trigger_debate":
        # Simulate active agent debate update
        for ag in CURRENT_SESSION.agents:
            ag.tokens_used += 120
        return ActionResponse(
            success=True,
            message="Debate round triggered across active agents",
            updated_session=CURRENT_SESSION
        )

    return ActionResponse(success=True, message="Action processed", updated_session=CURRENT_SESSION)
