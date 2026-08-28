import type { Session } from './types/session';

const API_BASE = 'http://localhost:8000';

export async function fetchSession(): Promise<Session> {
    const res = await fetch(`${API_BASE}/api/session`);
    if (!res.ok) {
        throw new Error(`Failed to fetch session: ${res.statusText}`);
    }
    return res.json();
}

export async function sendSessionAction(action_type: string, payload?: Record<string, unknown>): Promise<Session> {
    const res = await fetch(`${API_BASE}/api/session/action`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action_type, payload })
    });
    if (!res.ok) {
        throw new Error(`Failed action: ${res.statusText}`);
    }
    const data = await res.json();
    return data.updated_session;
}
