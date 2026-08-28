<script lang="ts">
  import { onMount, tick } from 'svelte';
  import { fetchSession, sendSessionAction } from '../lib/api';
  import type { Session, Message, AgentStatus } from '../lib/types/session';

  let session = $state<Session | null>(null);
  let morphology = $state<'editorial' | 'tactical'>('editorial');
  let loading = $state(true);
  let scrollContainer = $state<HTMLDivElement | null>(null);
  let savedScrollTop = $state(0);
  let scrollY = $state(0);
  let inputMessage = $state('');

  onMount(async () => {
    try {
      session = await fetchSession();
    } catch (e) {
      console.error("Failed to load session from FastAPI", e);
    } finally {
      loading = false;
    }
  });

  async function toggleMorphology() {
    const nextMorph = morphology === 'editorial' ? 'tactical' : 'editorial';
    const currentScroll = scrollContainer ? scrollContainer.scrollTop : savedScrollTop;
    savedScrollTop = currentScroll;

    // Pure frontend morphology mutation
    morphology = nextMorph;

    await tick();
    if (scrollContainer) {
      scrollContainer.scrollTop = currentScroll;
    }
    setTimeout(() => {
      if (scrollContainer) scrollContainer.scrollTop = currentScroll;
    }, 50);
  }

  async function handleSendMessage() {
    if (!inputMessage.trim() || !session) return;
    const text = inputMessage;
    const tempId = `msg-temp-${Date.now()}`;
    inputMessage = '';

    const tempMsg: Message = {
      id: tempId,
      sender_id: 'user-01',
      sender_name: session.user_name,
      sender_role: 'user',
      avatar: session.user_avatar,
      content: text,
      timestamp: new Date().toLocaleTimeString(),
      tokens: Math.round(text.length / 4) + 5
    };
    session.messages = [...session.messages, tempMsg];

    await tick();
    if (scrollContainer) {
      scrollContainer.scrollTop = scrollContainer.scrollHeight;
    }

    try {
      const updated = await sendSessionAction('send_message', { text });
      if (updated) session = updated;
    } catch (e) {
      console.error("Failed sending message, rolling back optimistic message", e);
      if (session) {
        session.messages = session.messages.filter(m => m.id !== tempId);
      }
      inputMessage = text;
    }
  }

  function handleScroll(e: Event) {
    const target = e.target as HTMLDivElement;
    scrollY = target.scrollTop;
    savedScrollTop = target.scrollTop;
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

    <!-- MORPHOLOGY A: EDITORIAL -->
    <div class="editorial-layout" class:hidden={morphology !== 'editorial'}>
      <header class="editorial-header">
        <div class="header-top-bar">
          <span class="editorial-kicker">MULTIMIND EDITORIAL SURFACES</span>
          <button class="morph-btn" onclick={toggleMorphology}>
            ⚡ MUTATE TO TACTICAL MORPHOLOGY
          </button>
        </div>

        <h1 class="editorial-title">{session.title}</h1>
        <p class="editorial-subtitle">Topic: {session.topic} — {session.status} — {session.total_tokens.toLocaleString()} tokens</p>
      </header>

      <div class="editorial-body-grid">
        <aside class="editorial-sidebar">
          <h3 class="sidebar-heading">DEBATING AGENTS</h3>
          <div class="editorial-agent-list">
            {#each session.agents as ag}
              <div class="editorial-agent-item status-{ag.status.toLowerCase()}">
                <span class="ag-avatar">{ag.avatar}</span>
                <div class="ag-info">
                  <span class="ag-name">{ag.name}</span>
                  <span class="ag-role">{ag.role}</span>
                </div>
                <span class="ag-status-pill">{ag.status}</span>
              </div>
            {/each}
          </div>
        </aside>

        <main class="editorial-main-stream">
          <h2 class="stream-title">CONVERSATION NARRATIVE</h2>
          <div class="messages-list">
            {#each session.messages as msg (msg.id)}
              <article class="editorial-card role-{msg.sender_role}">
                <div class="card-meta">
                  <span class="avatar-circle">{msg.avatar}</span>
                  <span class="sender-name">{msg.sender_name}</span>
                  <span class="role-badge">{msg.sender_role}</span>
                  <span class="time-stamp">{msg.timestamp}</span>
                </div>
                <div class="card-content">
                  <p>{msg.content}</p>
                  {#if msg.thought_process}
                    <blockquote class="agent-thought-quote">
                      <span class="quote-label">Internal Trace:</span> {msg.thought_process}
                    </blockquote>
                  {/if}
                  {#if msg.code_snippet}
                    <pre class="code-box"><code>{msg.code_snippet}</code></pre>
                  {/if}
                </div>
              </article>
            {/each}
          </div>

          <form class="editorial-input-bar" onsubmit={(e) => { e.preventDefault(); handleSendMessage(); }}>
            <input type="text" bind:value={inputMessage} placeholder="Inject prompt into narrative..." class="edit-input" />
            <button type="submit" class="edit-send-btn">POST PROMPT</button>
          </form>
        </main>
      </div>
    </div>

    <!-- MORPHOLOGY B: TACTICAL -->
    <div class="tactical-layout" class:hidden={morphology !== 'tactical'}>
      <header class="tactical-hud-bar">
        <div class="hud-left">
          <span class="hud-tag">[TACTICAL MORPHOLOGY]</span>
          <span class="hud-session-id">{session.id}</span>
        </div>
        <div class="hud-center">
          <span class="hud-title">{session.title}</span>
        </div>
        <div class="hud-right">
          <span class="hud-tokens">TOKENS: {session.total_tokens}</span>
          <button class="morph-btn tactical" onclick={toggleMorphology}>
            ⚡ MUTATE TO EDITORIAL
          </button>
        </div>
      </header>

      <div class="tactical-split-surface">
        <section class="tactical-telemetry-strip">
          {#each session.agents as ag}
            <div class="telemetry-box">
              <div class="tel-top">
                <span class="tel-avatar">{ag.avatar}</span>
                <span class="tel-name">{ag.name}</span>
                <span class="tel-status">{ag.status}</span>
              </div>
              <div class="tel-metrics">
                <span>CONF: {(ag.confidence * 100).toFixed(0)}%</span>
                <span>MODEL: {ag.model}</span>
              </div>
            </div>
          {/each}
        </section>

        <section class="tactical-terminal-stream">
          <div class="terminal-messages">
            {#each session.messages as msg (msg.id)}
              <div class="terminal-row role-{msg.sender_role}">
                <span class="row-time">[{msg.timestamp}]</span>
                <span class="row-sender">&lt;{msg.sender_name}&gt;</span>
                <div class="row-content">
                  <span>{msg.content}</span>
                  {#if msg.thought_process}
                    <div class="term-thought">&gt; THOUGHT: {msg.thought_process}</div>
                  {/if}
                </div>
              </div>
            {/each}
          </div>

          <form class="tactical-command-line" onsubmit={(e) => { e.preventDefault(); handleSendMessage(); }}>
            <span class="prompt-symbol">&gt;&gt;</span>
            <input type="text" bind:value={inputMessage} placeholder="EXECUTE PROMPT..." class="cmd-input" />
            <button type="submit" class="cmd-btn">RUN</button>
          </form>
        </section>
      </div>
    </div>
  </div>
{/if}

<style>
  .multimind-app {
    width: 100%;
    min-height: calc(100vh - 50px);
    height: calc(100vh - 50px);
    overflow-y: scroll;
    box-sizing: border-box;
  }

  .hidden {
    display: none !important;
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
    height: calc(100vh - 50px);
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

  /* MORPHOLOGY A: EDITORIAL STYLES */
  .editorial-layout {
    position: relative;
    z-index: 10;
    max-width: 1300px;
    margin: 0 auto;
    padding: 2.5rem 2rem;
    font-family: Georgia, 'Times New Roman', serif;
    color: #1e293b;
    min-height: 2000px;
  }

  .editorial-header {
    border-bottom: 2px solid #cbd5e1;
    padding-bottom: 2rem;
    margin-bottom: 2.5rem;
  }

  .header-top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .editorial-kicker {
    font-family: -apple-system, sans-serif;
    font-size: 0.8rem;
    letter-spacing: 0.25em;
    font-weight: 700;
    color: #0284c7;
  }

  .editorial-title {
    font-size: 2.75rem;
    font-weight: 300;
    margin: 0.75rem 0 0.5rem 0;
    letter-spacing: -0.02em;
  }

  .editorial-subtitle {
    font-family: -apple-system, sans-serif;
    color: #64748b;
    margin: 0;
    font-size: 0.95rem;
  }

  .morph-btn {
    background: #0f172a;
    color: #fff;
    border: none;
    padding: 0.75rem 1.4rem;
    border-radius: 30px;
    font-family: -apple-system, sans-serif;
    font-weight: 700;
    font-size: 0.8rem;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    transition: all 0.2s ease;
  }

  .morph-btn:hover {
    background: #0284c7;
  }

  .editorial-body-grid {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 3rem;
  }

  .editorial-sidebar {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    height: fit-content;
    position: sticky;
    top: 2rem;
  }

  .sidebar-heading {
    font-family: -apple-system, sans-serif;
    font-size: 0.85rem;
    letter-spacing: 0.1em;
    color: #64748b;
    margin: 0 0 1rem 0;
  }

  .editorial-agent-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .editorial-agent-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.5rem;
    border-radius: 8px;
    background: #f8fafc;
  }

  .ag-avatar { font-size: 1.5rem; }
  .ag-info { display: flex; flex-direction: column; flex: 1; }
  .ag-name { font-family: -apple-system, sans-serif; font-size: 0.85rem; font-weight: bold; }
  .ag-role { font-family: -apple-system, sans-serif; font-size: 0.75rem; color: #64748b; }
  .ag-status-pill { font-family: monospace; font-size: 0.65rem; background: #e0f2fe; color: #0369a1; padding: 0.1rem 0.4rem; border-radius: 4px; }

  .editorial-main-stream {
    display: flex;
    flex-direction: column;
  }

  .stream-title {
    font-family: -apple-system, sans-serif;
    font-size: 1rem;
    letter-spacing: 0.1em;
    color: #475569;
    margin-bottom: 1.5rem;
  }

  .messages-list {
    display: flex;
    flex-direction: column;
    gap: 1.75rem;
    margin-bottom: 3rem;
  }

  .editorial-card {
    background: #ffffff;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    padding: 1.75rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
  }

  .card-meta {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
    font-family: -apple-system, sans-serif;
    font-size: 0.85rem;
  }

  .avatar-circle { font-size: 1.4rem; }
  .sender-name { font-weight: bold; color: #0f172a; }
  .role-badge { background: #f1f5f9; color: #64748b; padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.75rem; }
  .time-stamp { color: #94a3b8; margin-left: auto; font-size: 0.75rem; }

  .card-content p {
    font-size: 1.1rem;
    line-height: 1.65;
    margin: 0;
    color: #334155;
  }

  .agent-thought-quote {
    margin: 1rem 0 0 0;
    padding: 0.75rem 1rem;
    background: #f8fafc;
    border-left: 3px solid #0284c7;
    font-style: italic;
    font-size: 0.95rem;
    color: #475569;
  }

  .quote-label { font-family: -apple-system, sans-serif; font-weight: bold; font-style: normal; color: #0284c7; }

  .code-box {
    background: #0f172a;
    color: #38bdf8;
    padding: 1rem;
    border-radius: 6px;
    font-family: monospace;
    font-size: 0.85rem;
    margin-top: 1rem;
  }

  .editorial-input-bar {
    position: sticky;
    bottom: 1.5rem;
    display: flex;
    gap: 0.75rem;
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid #cbd5e1;
    padding: 0.75rem;
    border-radius: 50px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
  }

  .edit-input {
    flex: 1;
    border: none;
    outline: none;
    padding: 0.5rem 1.25rem;
    font-family: -apple-system, sans-serif;
    font-size: 0.95rem;
    background: transparent;
  }

  .edit-send-btn {
    background: #0284c7;
    color: #fff;
    border: none;
    padding: 0.6rem 1.5rem;
    border-radius: 30px;
    font-family: -apple-system, sans-serif;
    font-weight: bold;
    cursor: pointer;
  }

  /* MORPHOLOGY B: TACTICAL STYLES */
  .tactical-layout {
    position: relative;
    z-index: 10;
    padding: 1rem;
    font-family: 'Courier New', monospace;
    color: #00ffcc;
    min-height: 2000px;
  }

  .tactical-hud-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(7, 9, 14, 0.95);
    border: 1px solid #00ffcc;
    padding: 0.75rem 1.25rem;
    margin-bottom: 1rem;
  }

  .hud-tag { color: #ffaa00; font-weight: bold; margin-right: 0.75rem; }
  .hud-session-id { color: #888; font-size: 0.8rem; }
  .hud-title { color: #fff; font-weight: bold; font-size: 1.1rem; }
  .hud-tokens { color: #ffaa00; margin-right: 1rem; font-size: 0.85rem; }

  .morph-btn.tactical {
    background: transparent;
    border: 1px solid #00ffcc;
    color: #00ffcc;
    border-radius: 0;
  }

  .tactical-split-surface {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .tactical-telemetry-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }

  .telemetry-box {
    background: rgba(0, 0, 0, 0.85);
    border: 1px solid rgba(0, 255, 204, 0.4);
    padding: 0.75rem;
  }

  .tel-top { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem; }
  .tel-avatar { font-size: 1.2rem; }
  .tel-name { font-weight: bold; color: #fff; flex: 1; font-size: 0.85rem; }
  .tel-status { background: #00ffcc; color: #000; font-weight: bold; font-size: 0.65rem; padding: 0.1rem 0.3rem; }

  .tel-metrics { display: flex; justify-content: space-between; font-size: 0.75rem; color: #888; }

  .tactical-terminal-stream {
    background: rgba(5, 8, 15, 0.95);
    border: 1px solid #00ffcc;
    padding: 1rem;
  }

  .terminal-messages {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
  }

  .terminal-row {
    display: flex;
    gap: 0.75rem;
    font-size: 0.85rem;
    border-bottom: 1px dashed rgba(0, 255, 204, 0.15);
    padding-bottom: 0.5rem;
  }

  .row-time { color: #ffaa00; }
  .row-sender { color: #fff; font-weight: bold; white-space: nowrap; }
  .row-content { flex: 1; color: #00ffcc; }
  .term-thought { color: #888; font-size: 0.75rem; margin-top: 0.25rem; }

  .tactical-command-line {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    background: #000;
    border: 1px solid #00ffcc;
    padding: 0.5rem 0.75rem;
  }

  .prompt-symbol { color: #ffaa00; font-weight: bold; }

  .cmd-input {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    color: #00ffcc;
    font-family: inherit;
    font-size: 0.9rem;
  }

  .cmd-btn {
    background: #00ffcc;
    color: #000;
    border: none;
    padding: 0.4rem 1rem;
    font-family: inherit;
    font-weight: bold;
    cursor: pointer;
  }

  /* MOBILE COMPOSITIONS (390x844 HARD GATE) */
  @media (max-width: 768px) {
    .editorial-layout {
      padding: 1rem;
    }

    .editorial-title { font-size: 1.75rem; }
    .editorial-body-grid {
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }

    .editorial-sidebar {
      position: relative;
      top: 0;
      padding: 1rem;
    }

    .editorial-agent-list {
      flex-direction: row;
      overflow-x: auto;
    }

    .editorial-agent-item {
      min-width: 140px;
    }

    .editorial-card {
      padding: 1rem;
    }

    .tactical-layout {
      padding: 0.5rem;
    }

    .tactical-hud-bar {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.5rem;
    }

    .tactical-telemetry-strip {
      grid-template-columns: 1fr;
    }

    .terminal-row {
      flex-direction: column;
      gap: 0.25rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .multimind-app, .morph-btn, .loader-ring {
      transition: none !important;
      animation: none !important;
    }
  }
</style>
