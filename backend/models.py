from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Literal

AgentStatusType = Literal["ACTIVE", "WAITING", "RUNNING", "PENDING", "THINKING", "COMPLETED"]
SenderRoleType = Literal["user", "assistant", "agent", "system"]
SessionStatusType = Literal["ACTIVE_DEBATE", "PAUSED", "COMPLETED"]
ActionType = Literal["send_message", "trigger_debate", "reset_session"]

class AgentStatus(BaseModel):
    id: str
    name: str
    role: str
    avatar: str
    status: AgentStatusType
    model: str
    tokens_used: int
    confidence: float
    current_thought: Optional[str] = None

class Message(BaseModel):
    id: str
    sender_id: str
    sender_name: str
    sender_role: SenderRoleType
    avatar: str
    content: str
    timestamp: str
    thought_process: Optional[str] = None
    code_snippet: Optional[str] = None
    tokens: int = 0
    agent_status: Optional[AgentStatusType] = None

class Session(BaseModel):
    id: str
    title: str
    topic: str
    created_at: str
    status: SessionStatusType
    total_tokens: int
    user_name: str
    user_avatar: str
    agents: List[AgentStatus]
    messages: List[Message]

class ActionPayloadSendMessage(BaseModel):
    text: str

class ActionRequest(BaseModel):
    action_type: ActionType
    payload: Optional[Dict[str, Any]] = None

class ActionResponse(BaseModel):
    success: bool
    message: str
    updated_session: Optional[Session] = None
