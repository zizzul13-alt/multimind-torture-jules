from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class AgentStatus(BaseModel):
    id: str
    name: str
    role: str
    avatar: str
    status: str # "ACTIVE", "WAITING", "RUNNING", "PENDING", "THINKING", "COMPLETED"
    model: str
    tokens_used: int
    confidence: float
    current_thought: Optional[str] = None

class Message(BaseModel):
    id: str
    sender_id: str
    sender_name: str
    sender_role: str # "user", "assistant", "agent", "system"
    avatar: str
    content: str
    timestamp: str
    thought_process: Optional[str] = None
    code_snippet: Optional[str] = None
    tokens: int = 0
    agent_status: Optional[str] = None

class Session(BaseModel):
    id: str
    title: str
    topic: str
    created_at: str
    status: str # "ACTIVE_DEBATE", "PAUSED", "COMPLETED"
    total_tokens: int
    active_morphology: str # "editorial" or "tactical"
    user_name: str
    user_avatar: str
    agents: List[AgentStatus]
    messages: List[Message]

class ActionRequest(BaseModel):
    action_type: str # "send_message", "trigger_debate", "change_morphology", "reset_session"
    payload: Optional[Dict[str, Any]] = None

class ActionResponse(BaseModel):
    success: bool
    message: str
    updated_session: Optional[Session] = None
