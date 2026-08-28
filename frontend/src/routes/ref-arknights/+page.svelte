<script lang="ts">
  import { onMount } from 'svelte';

  let scrollY = $state(0);
  let activeTab = $state('OPERATIVES');

  function handleScroll(e: Event) {
    const target = e.target as HTMLElement;
    scrollY = target.scrollTop;
  }
</script>

<div class="arknights-container" onscroll={handleScroll}>
  <!-- Background Layered Material -->
  <div class="bg-material" style="transform: translateY({scrollY * 0.15}px);">
    <img src="/materials/arknights_bg.svg" alt="Arknights Tactical Background" class="bg-img" />
  </div>

  <div class="overlay-grid"></div>

  <!-- Header Surface -->
  <header class="ark-header">
    <div class="rhodes-logo">
      <span class="amber-badge">RHODES ISLAND</span>
      <h1>TACTICAL OPERATIVE TERMINAL</h1>
    </div>
    <div class="status-strip">
      <div class="status-item"><span class="label">SEC-LEVEL:</span> <span class="val amber">ALPHA-0</span></div>
      <div class="status-item"><span class="label">TACTICAL LINK:</span> <span class="val active">SYNCHRONIZED</span></div>
    </div>
  </header>

  <!-- Interactive Scroll Choreography & Layered Content -->
  <section class="viewport-hero">
    <div class="hero-card" style="transform: perspective(1000px) rotateX({Math.min(15, scrollY * 0.05)}deg) translateY({-scrollY * 0.1}px);">
      <div class="card-accent"></div>
      <div class="card-content">
        <h2>DEBATE ENGINE :: AGENT AMBER-09</h2>
        <p class="sub">Layered visual composition + scroll-linked HUD transform</p>
        <div class="operatives-bar">
          <button class="op-btn" class:active={activeTab === 'OPERATIVES'} onclick={() => activeTab = 'OPERATIVES'}>[01] OPERATIVES</button>
          <button class="op-btn" class:active={activeTab === 'DEBATE'} onclick={() => activeTab = 'DEBATE'}>[02] DEBATE MATRIX</button>
          <button class="op-btn" class:active={activeTab === 'TELEMETRY'} onclick={() => activeTab = 'TELEMETRY'}>[03] TELEMETRY</button>
        </div>
      </div>
    </div>
  </section>

  <section class="tactical-body">
    <div class="panel-left">
      <h3>TACTICAL PROTOCOL STATE</h3>
      <div class="hud-box">
        <div class="hud-line"><span>ACTIVE DEBATE:</span> <strong>SvelteKit vs FastAPI Boundary</strong></div>
        <div class="hud-line"><span>AGENTS ONLINE:</span> <strong class="amber">3 OPERATIVES</strong></div>
        <div class="hud-line"><span>LATENCY:</span> <span>1.2ms (REST API)</span></div>
      </div>
      <div class="ambient-pulse">
        <div class="pulse-ring"></div>
        <span>MONITORING STREAM</span>
      </div>
    </div>

    <div class="panel-right">
      <h3>OPERATIVE DEPLOYMENT TIMELINE</h3>
      <div class="timeline-list">
        {#each Array(8) as _, i}
          <div class="timeline-item">
            <div class="time-stamp">10:{10 + i}:00</div>
            <div class="op-info">
              <span class="op-title">OPERATIVE-{i + 1} // DISPATCHED</span>
              <p>State message trace evaluation #{i + 1}. Tactical scroll sync active.</p>
            </div>
          </div>
        {/each}
      </div>
    </div>
  </section>
</div>

<style>
  .arknights-container {
    position: relative;
    min-height: calc(100vh - 50px);
    height: calc(100vh - 50px);
    overflow-y: auto;
    background: #080a0f;
    color: #f1f5f9;
    font-family: 'Rajdhani', -apple-system, sans-serif;
  }

  .bg-material {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 120%;
    z-index: 1;
    pointer-events: none;
  }

  .bg-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.7;
  }

  .overlay-grid {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: radial-gradient(rgba(245, 158, 11, 0.1) 1px, transparent 0);
    background-size: 24px 24px;
    z-index: 2;
    pointer-events: none;
  }

  .ark-header {
    position: relative;
    z-index: 10;
    padding: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(245, 158, 11, 0.3);
    background: rgba(8, 10, 15, 0.85);
    backdrop-filter: blur(10px);
  }

  .amber-badge {
    background: #f59e0b;
    color: #000;
    font-weight: 900;
    padding: 0.2rem 0.6rem;
    font-size: 0.75rem;
    letter-spacing: 0.15em;
  }

  h1 {
    margin: 0.5rem 0 0 0;
    font-size: 1.75rem;
    letter-spacing: 0.1em;
    color: #fff;
    text-transform: uppercase;
  }

  .status-strip {
    display: flex;
    gap: 1.5rem;
    font-size: 0.85rem;
    font-family: monospace;
  }

  .val.amber { color: #f59e0b; }
  .val.active { color: #10b981; }

  .viewport-hero {
    position: relative;
    z-index: 10;
    padding: 3rem 2rem;
    display: flex;
    justify-content: center;
  }

  .hero-card {
    width: 100%;
    max-width: 900px;
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(245, 158, 11, 0.4);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(245, 158, 11, 0.15);
    position: relative;
    transition: transform 0.1s ease-out;
  }

  .card-accent {
    position: absolute;
    top: 0;
    left: 0;
    width: 6px;
    height: 100%;
    background: #f59e0b;
  }

  .card-content {
    padding: 2.5rem;
  }

  .hero-card h2 {
    margin: 0;
    font-size: 1.8rem;
    color: #f59e0b;
    letter-spacing: 0.05em;
  }

  .sub {
    color: #94a3b8;
    margin-bottom: 2rem;
  }

  .operatives-bar {
    display: flex;
    gap: 1rem;
  }

  .op-btn {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #cbd5e1;
    padding: 0.75rem 1.5rem;
    font-weight: 700;
    font-family: monospace;
    cursor: pointer;
    transition: all 0.2s;
  }

  .op-btn.active, .op-btn:hover {
    background: #f59e0b;
    color: #000;
    border-color: #f59e0b;
  }

  .tactical-body {
    position: relative;
    z-index: 10;
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 2rem;
  }

  .panel-left, .panel-right {
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 1.5rem;
  }

  .hud-box {
    background: rgba(0, 0, 0, 0.4);
    padding: 1rem;
    border-left: 3px solid #f59e0b;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    font-family: monospace;
    font-size: 0.85rem;
  }

  .ambient-pulse {
    margin-top: 2rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 0.8rem;
    color: #f59e0b;
    font-family: monospace;
  }

  .pulse-ring {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #f59e0b;
    box-shadow: 0 0 10px #f59e0b;
    animation: pulse 1.5s infinite;
  }

  @keyframes pulse {
    0% { transform: scale(0.95); opacity: 0.8; }
    50% { transform: scale(1.3); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.8; }
  }

  .timeline-item {
    display: flex;
    gap: 1.5rem;
    padding: 1rem 0;
    border-bottom: 1px dashed rgba(255, 255, 255, 0.1);
  }

  .time-stamp {
    font-family: monospace;
    color: #f59e0b;
    font-size: 0.85rem;
  }

  .op-title {
    font-weight: 700;
    font-size: 0.95rem;
  }

  .op-info p {
    margin: 0.25rem 0 0 0;
    font-size: 0.85rem;
    color: #94a3b8;
  }

  @media (max-width: 768px) {
    .tactical-body {
      grid-template-columns: 1fr;
    }
    .ark-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 1rem;
    }
    .operatives-bar {
      flex-direction: column;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .hero-card, .pulse-ring, .bg-material {
      transition: none !important;
      animation: none !important;
      transform: none !important;
    }
  }
</style>
