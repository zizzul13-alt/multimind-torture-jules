export interface AgentStatus {
    id: string;
    name: string;
    role: string;
    avatar: string;
    status: string; // "ACTIVE", "WAITING", "RUNNING", "PENDING", "THINKING", "COMPLETED"
    model: string;
    tokens_used: number;
    confidence: number;
    current_thought?: string;
}

export interface Message {
    id: string;
    sender_id: string;
    sender_name: string;
    sender_role: string; // "user" | "assistant" | "agent" | "system"
    avatar: string;
    content: string;
    timestamp: string;
    thought_process?: string;
    code_snippet?: string;
    tokens: number;
    agent_status?: string;
}

export interface Session {
    id: string;
    title: string;
    topic: string;
    created_at: string;
    status: string;
    total_tokens: number;
    active_morphology: 'editorial' | 'tactical';
    user_name: string;
    user_avatar: string;
    agents: AgentStatus[];
    messages: Message[];
}
