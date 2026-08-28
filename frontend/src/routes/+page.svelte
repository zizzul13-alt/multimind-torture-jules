<script lang="ts">
  import { onMount, tick } from 'svelte';
  import { fetchSession, sendSessionAction } from '../lib/api';
  import type { Session, Message, AgentStatus } from '../lib/types/session';

  let session = $state<Session | null>(null);
  let morphology = $state<'editorial' | 'tactical'>('editorial');
  let loading = $state(true);
  let scrollContainer = $state<HTMLDivElement | null>(null);
  let scrollY = $state(0);
  let inputMessage = $state('');

  onMount(async () => {
    try {
      session = await fetchSession();
      morphology = session.active_morphology || 'editorial';
    } catch (e) {
      console.error("Failed to load session from FastAPI", e);
    } finally {
      loading = false;
    }
  });

  async function toggleMorphology() {
    const nextMorph = morphology === 'editorial' ? 'tactical' : 'editorial';
    const currentScroll = scrollContainer ? scrollContainer.scrollTop : 0;

    // Update local state and backend state asynchronously without page refresh
    morphology = nextMorph;

    // Preserve scroll position deterministically after DOM updates
    await tick();
    setTimeout(() => {
      if (scrollContainer) {
        scrollContainer.scrollTop = currentScroll;
      }
    }, 50);

    try {
      await sendSessionAction('change_morphology', { morphology: nextMorph });
    } catch (e) {
      console.error("Failed sync action", e);
    }
  }

  async function handleSendMessage() {
    if (!inputMessage.trim() || !session) return;
    const text = inputMessage;
    inputMessage = '';

    // Optimistic UI append
    const tempMsg: Message = {
      id: `msg-temp-${Date.now()}`,
      sender_id: 'user-01',
      sender_name: session.user_name,
      sender_role: 'user',
      avatar: session.user_avatar,
      content: text,
      timestamp: new Date().toLocaleTimeString(),
      tokens: Math.round(text.length / 4) + 5
    };
    session.messages = [...session.messages, tempMsg];

    try {
      const updated = await sendSessionAction('send_message', { text });
      if (updated) session = updated;
    } catch (e) {
      console.error("Failed sending message", e);
    }

    await tick();
    if (scrollContainer) {
      scrollContainer.scrollTop = scrollContainer.scrollHeight;
    }
  }

  function handleScroll(e: Event) {
    const target = e.target as HTMLDivElement;
    scrollY = target.scrollTop;
  }
</script>

{#if loading}
  <div class="branded-loader">
    <div class="loader-ring"></div>
    <div class="loader-text">INITIALIZING MULTIMIND CORE...</div>
  </div>
{:else if session}
  <div
    class="multimind-app {morphology}"
    bind:this={scrollContainer}
    onscroll={handleScroll}
    data-morphology={morphology}
    data-scroll-y={scrollY}
  >
    <!-- Background Material -->
    <div class="bg-material-layer">
      {#if morphology === 'editorial'}
        <img src="/materials/dioriviera_bg.svg" alt="Editorial Texture" class="bg-material-img opacity-40" />
      {:else}
        <img src="/materials/arknights_bg.svg" alt="Tactical HUD Grid" class="bg-material-img opacity-60" />
      {/if}
    </div>

    <!-- MultiMind Header & Control Bar -->
    <header class="app-header">
      <div class="session-meta">
        <span class="morphology-badge">{morphology.toUpperCase()} MORPHOLOGY</span>
        <h1 class="session-title">{session.title}</h1>
        <div class="session-sub">Topic: {session.topic} • Created: {session.created_at}</div>
      </div>

      <div class="morphology-toggle-box">
        <button class="morph-btn" onclick={toggleMorphology}>
          <span class="btn-icon">⚡</span>
          <span class="btn-text">MUTATE MORPHOLOGY [{morphology === 'editorial' ? 'TACTICAL' : 'EDITORIAL'}]</span>
        </button>
        <div class="token-tracker">TOKENS: {session.total_tokens.toLocaleString()}</div>
      </div>
    </header>

    <!-- Agent Debate & Progress Surface -->
    <section class="agents-surface">
      <div class="agents-header">
        <h2>ACTIVE AGENT MATRIX ({session.agents.length})</h2>
        <span class="debate-status"><span class="pulse-dot"></span> {session.status}</span>
      </div>
      <div class="agents-grid">
        {#each session.agents as ag}
          <div class="agent-card status-{ag.status.toLowerCase()}">
            <div class="ag-top">
              <span class="ag-avatar">{ag.avatar}</span>
              <div class="ag-name-block">
                <span class="ag-name">{ag.name}</span>
                <span class="ag-role">{ag.role}</span>
              </div>
              <span class="ag-status-pill">{ag.status}</span>
            </div>
            <div class="ag-body">
              <div class="ag-model">Model: {ag.model}</div>
              <div class="ag-confidence">Confidence: {(ag.confidence * 100).toFixed(0)}%</div>
              {#if ag.current_thought}
                <div class="ag-thought">"{ag.current_thought}"</div>
              {/if}
            </div>
          </div>
        {/each}
      </div>
    </section>

    <!-- Main Conversation Torture Surface -->
    <section class="conversation-torture-surface">
      <div class="conv-header">
        <h2>SESSION CONVERSATION TRACE ({session.messages.length} MESSAGES)</h2>
        <span class="scroll-pos-indicator">SCROLL Y: {Math.round(scrollY)}px</span>
      </div>

      <div class="messages-container" id="messages-list">
        {#each session.messages as msg, i (msg.id)}
          <article class="message-item role-{msg.sender_role}">
            <div class="msg-avatar">{msg.avatar}</div>
            <div class="msg-content-wrapper">
              <div class="msg-meta">
                <span class="msg-sender">{msg.sender_name}</span>
                <span class="msg-role-tag">{msg.sender_role}</span>
                <span class="msg-time">{msg.timestamp}</span>
                <span class="msg-tokens">{msg.tokens} tokens</span>
              </div>

              <div class="msg-body">
                <p>{msg.content}</p>
                {#if msg.thought_process}
                  <details class="thought-accordion">
                    <summary>Internal Agent Reasoning Trace</summary>
                    <p class="thought-text">{msg.thought_process}</p>
                  </details>
                {/if}
                {#if msg.code_snippet}
                  <pre class="code-block"><code>{msg.code_snippet}</code></pre>
                {/if}
              </div>
            </div>
          </article>
        {/each}
      </div>

      <!-- Chat Input Surface -->
      <form class="input-surface" onsubmit={(e) => { e.preventDefault(); handleSendMessage(); }}>
        <input
          type="text"
          bind:value={inputMessage}
          placeholder="Inject prompt message into active debate session..."
          class="chat-input"
        />
        <button type="submit" class="send-btn">SEND PROMPT</button>
      </form>
    </section>
  </div>
{/if}

<style>
  /* Base Container */
  .multimind-app {
    position: relative;
    min-height: calc(100vh - 50px);
    height: calc(100vh - 50px);
    overflow-y: auto;
    transition: background 0.3s ease, color 0.3s ease;
  }

  .bg-material-layer {
    position: fixed;
    top: 50px;
    left: 0;
    width: 100%;
    height: calc(100vh - 50px);
    z-index: 0;
    pointer-events: none;
  }

  .bg-material-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .opacity-40 { opacity: 0.4; }
  .opacity-60 { opacity: 0.6; }

  .branded-loader {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: calc(100vh - 50px);
    background: #0b0f17;
    color: #38bdf8;
    font-family: monospace;
  }

  .loader-ring {
    width: 48px;
    height: 48px;
    border: 3px solid rgba(56, 189, 248, 0.2);
    border-top-color: #38bdf8;
    border-radius: 50%;
    animation: spin 1s infinite linear;
    margin-bottom: 1.5rem;
  }

  @keyframes spin { 100% { transform: rotate(360deg); } }

  /* ========================================================= */
  /* MORPHOLOGY A: EDITORIAL / SPATIAL                          */
  /* ========================================================= */
  .multimind-app.editorial {
    background: #faf8f5;
    color: #1e293b;
    font-family: Georgia, 'Times New Roman', serif;
    padding: 2rem 4rem;
  }

  .editorial .app-header {
    position: relative;
    z-index: 10;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 2rem;
    margin-bottom: 3rem;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }

  .editorial .morphology-badge {
    font-family: -apple-system, sans-serif;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    font-weight: 700;
    color: #0284c7;
    background: #e0f2fe;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
  }

  .editorial .session-title {
    font-size: 2.5rem;
    font-weight: 300;
    margin: 0.5rem 0 0.25rem 0;
  }

  .editorial .session-sub {
    font-family: -apple-system, sans-serif;
    color: #64748b;
    font-size: 0.9rem;
  }

  .editorial .morph-btn {
    background: #0f172a;
    color: #fff;
    border: none;
    padding: 0.8rem 1.6rem;
    border-radius: 30px;
    font-family: -apple-system, sans-serif;
    font-weight: 600;
    font-size: 0.85rem;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    transition: transform 0.2s ease;
  }

  .editorial .morph-btn:hover {
    transform: translateY(-2px);
  }

  .editorial .token-tracker {
    font-family: monospace;
    font-size: 0.85rem;
    color: #64748b;
    margin-top: 0.5rem;
    text-align: right;
  }

  .editorial .agents-surface {
    position: relative;
    z-index: 10;
    margin-bottom: 4rem;
  }

  .editorial .agents-header h2 {
    font-size: 1.25rem;
    font-weight: 400;
    letter-spacing: 0.05em;
    margin-bottom: 1.5rem;
    color: #334155;
  }

  .editorial .agents-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
  }

  .editorial .agent-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    border: 1px solid #cbd5e1;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.03);
  }

  .editorial .ag-top {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .editorial .ag-avatar { font-size: 1.8rem; }
  .editorial .ag-name { font-weight: bold; font-family: -apple-system, sans-serif; display: block; }
  .editorial .ag-role { font-size: 0.8rem; color: #64748b; font-family: -apple-system, sans-serif; }
  .editorial .ag-status-pill {
    margin-left: auto;
    font-family: monospace;
    font-size: 0.7rem;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    background: #e2e8f0;
  }

  .editorial .ag-thought {
    font-style: italic;
    font-size: 0.9rem;
    color: #475569;
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-top: 1px solid #f1f5f9;
  }

  .editorial .conversation-torture-surface {
    position: relative;
    z-index: 10;
    max-width: 900px;
    margin: 0 auto;
  }

  .editorial .messages-container {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-bottom: 3rem;
  }

  .editorial .message-item {
    display: flex;
    gap: 1.5rem;
    background: #ffffff;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    border: 1px solid #e2e8f0;
  }

  .editorial .msg-avatar { font-size: 2rem; }
  .editorial .msg-sender { font-family: -apple-system, sans-serif; font-weight: bold; }
  .editorial .msg-meta { font-size: 0.8rem; color: #94a3b8; font-family: -apple-system, sans-serif; display: flex; gap: 0.75rem; align-items: center; }
  .editorial .msg-body { font-size: 1.05rem; line-height: 1.6; margin-top: 0.5rem; }

  /* ========================================================= */
  /* MORPHOLOGY B: TACTICAL / DENSE                            */
  /* ========================================================= */
  .multimind-app.tactical {
    background: #07090e;
    color: #00ffcc;
    font-family: 'Courier New', monospace;
    padding: 1rem 1.5rem;
  }

  .tactical .app-header {
    position: relative;
    z-index: 10;
    border: 1px solid #00ffcc;
    background: rgba(7, 9, 14, 0.9);
    padding: 1rem;
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .tactical .morphology-badge {
    background: #00ffcc;
    color: #000;
    font-weight: 900;
    padding: 0.1rem 0.5rem;
    font-size: 0.7rem;
  }

  .tactical .session-title {
    font-size: 1.4rem;
    margin: 0.25rem 0;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .tactical .session-sub { color: #00ffcc; opacity: 0.7; font-size: 0.75rem; }

  .tactical .morph-btn {
    background: transparent;
    border: 1px solid #00ffcc;
    color: #00ffcc;
    padding: 0.5rem 1rem;
    font-family: monospace;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s;
  }

  .tactical .morph-btn:hover {
    background: #00ffcc;
    color: #000;
  }

  .tactical .token-tracker { font-size: 0.75rem; color: #ffaa00; margin-top: 0.25rem; text-align: right; }

  .tactical .agents-surface {
    position: relative;
    z-index: 10;
    margin-bottom: 2rem;
  }

  .tactical .agents-header h2 {
    font-size: 0.9rem;
    color: #ffaa00;
    margin-bottom: 0.75rem;
    letter-spacing: 0.1em;
  }

  .tactical .agents-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }

  .tactical .agent-card {
    background: rgba(0, 0, 0, 0.8);
    border: 1px solid rgba(0, 255, 204, 0.3);
    padding: 0.75rem;
    font-size: 0.8rem;
  }

  .tactical .ag-top { display: flex; justify-content: space-between; align-items: center; }
  .tactical .ag-name { font-weight: bold; color: #fff; }
  .tactical .ag-status-pill { background: #00ffcc; color: #000; font-weight: bold; padding: 0.1rem 0.3rem; font-size: 0.65rem; }
  .tactical .ag-thought { color: #888; font-size: 0.75rem; margin-top: 0.5rem; }

  .tactical .conversation-torture-surface {
    position: relative;
    z-index: 10;
  }

  .tactical .messages-container {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-bottom: 2rem;
  }

  .tactical .message-item {
    background: rgba(10, 15, 25, 0.9);
    border-left: 3px solid #00ffcc;
    padding: 0.75rem 1rem;
    display: flex;
    gap: 1rem;
  }

  .tactical .msg-avatar { font-size: 1.2rem; }
  .tactical .msg-sender { font-weight: bold; color: #fff; }
  .tactical .msg-meta { font-size: 0.7rem; color: #666; display: flex; gap: 0.75rem; }
  .tactical .msg-body { font-size: 0.85rem; color: #00ffcc; margin-top: 0.25rem; }

  /* Shared Form Input */
  .input-surface {
    position: sticky;
    bottom: 1rem;
    z-index: 50;
    display: flex;
    gap: 0.5rem;
    background: rgba(15, 23, 42, 0.95);
    padding: 0.75rem;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
  }

  .chat-input {
    flex: 1;
    background: rgba(0, 0, 0, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #fff;
    padding: 0.75rem 1rem;
    border-radius: 6px;
    font-family: inherit;
    font-size: 0.9rem;
  }

  .send-btn {
    background: #38bdf8;
    color: #000;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    font-weight: bold;
    cursor: pointer;
  }

  .code-block {
    background: #000;
    color: #00ffcc;
    padding: 0.75rem;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 0.8rem;
    margin-top: 0.5rem;
  }

  .thought-accordion {
    margin-top: 0.5rem;
    font-size: 0.8rem;
    color: #94a3b8;
  }

  .pulse-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    background: #10b981;
    border-radius: 50%;
    margin-right: 0.4rem;
    box-shadow: 0 0 8px #10b981;
  }

  /* ========================================================= */
  /* MOBILE HARD GATE (390x844) RECOMPOSITION                  */
  /* ========================================================= */
  @media (max-width: 768px) {
    .multimind-app.editorial, .multimind-app.tactical {
      padding: 0.75rem;
    }

    .app-header {
      flex-direction: column;
      align-items: flex-start !important;
      gap: 0.75rem;
    }

    .session-title { font-size: 1.3rem !important; }
    .agents-grid { grid-template-columns: 1fr !important; }
    .editorial .message-item, .tactical .message-item {
      padding: 0.75rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .multimind-app, .morph-btn, .loader-ring {
      transition: none !important;
      animation: none !important;
    }
  }
</style>
