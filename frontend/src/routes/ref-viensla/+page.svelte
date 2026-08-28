<script lang="ts">
  let activeSection = $state('NAVIGATION');
</script>

<div class="viensla-container">
  <div class="bg-material">
    <img src="/materials/viensla_bg.svg" alt="Viens-là Editorial Grid" class="bg-img" />
  </div>

  <header class="viensla-header">
    <div class="editorial-num">N° 04 / PROOF</div>
    <div class="editorial-brand">VIENS-LÀ / TYPOGRAPHY LED</div>
    <div class="editorial-mode">MONOSPACE MODE</div>
  </header>

  <main class="editorial-stage">
    <div class="vertical-title-strip">
      <span>ARCHITECTURE & TYPOGRAPHY BENCHMARK</span>
    </div>

    <div class="editorial-main">
      <h1 class="giant-heading">
        STRUCTURAL<br/><span class="outline-text">TYPOGRAPHY</span>
      </h1>

      <p class="editorial-lead">
        Typography as primary composition architecture. Monospaced headers, asymmetric layout rules, and microinteractions.
      </p>

      <div class="interactive-index">
        <button class="index-row" class:active={activeSection === 'NAVIGATION'} onclick={() => activeSection = 'NAVIGATION'}>
          <span class="idx-num">01.</span>
          <span class="idx-label">NON-STANDARD NAVIGATION</span>
          <span class="idx-arrow">→</span>
        </button>

        <button class="index-row" class:active={activeSection === 'MICRO'} onclick={() => activeSection = 'MICRO'}>
          <span class="idx-num">02.</span>
          <span class="idx-label">POINTER MICROINTERACTIONS</span>
          <span class="idx-arrow">→</span>
        </button>

        <button class="index-row" class:active={activeSection === 'EDITORIAL'} onclick={() => activeSection = 'EDITORIAL'}>
          <span class="idx-num">03.</span>
          <span class="idx-label">EDITORIAL LAYOUT DENSITY</span>
          <span class="idx-arrow">→</span>
        </button>
      </div>

      <div class="index-detail-box">
        {#if activeSection === 'NAVIGATION'}
          <div class="detail-content">
            <h3>[01] NON-STANDARD NAVIGATION SYSTEM</h3>
            <p>Horizontal & vertical editorial presentation behavior without standard web header patterns.</p>
          </div>
        {:else if activeSection === 'MICRO'}
          <div class="detail-content">
            <h3>[02] POINTER MICROINTERACTIONS</h3>
            <p>Monospaced cursor feedback and micro-label hover transitions native to Svelte state.</p>
          </div>
        {:else if activeSection === 'EDITORIAL'}
          <div class="detail-content">
            <h3>[03] EDITORIAL LAYOUT DENSITY</h3>
            <p>High contrast rules, poster geometry, and high readability over extreme background visuals.</p>
          </div>
        {/if}
      </div>
    </div>
  </main>
</div>

<style>
  .viensla-container {
    position: relative;
    min-height: calc(100vh - 50px);
    height: calc(100vh - 50px);
    overflow-y: auto;
    background: #0d0d0d;
    color: #f8fafc;
    font-family: 'Courier New', Courier, monospace;
  }

  .bg-material {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    pointer-events: none;
  }

  .bg-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.6;
  }

  .viensla-header {
    position: relative;
    z-index: 10;
    padding: 2rem;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 0.85rem;
    letter-spacing: 0.15em;
  }

  .editorial-brand { font-weight: bold; }
  .editorial-mode { color: #f59e0b; }

  .editorial-stage {
    position: relative;
    z-index: 10;
    display: flex;
    max-width: 1300px;
    margin: 0 auto;
    padding: 3rem 2rem;
  }

  .vertical-title-strip {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    font-size: 0.8rem;
    letter-spacing: 0.3em;
    color: #64748b;
    border-left: 1px solid rgba(255, 255, 255, 0.15);
    padding: 1rem 0.5rem;
    margin-right: 3rem;
  }

  .editorial-main {
    flex: 1;
  }

  .giant-heading {
    font-size: 5rem;
    font-weight: 900;
    line-height: 0.95;
    margin: 0 0 2rem 0;
    letter-spacing: -0.05em;
  }

  .outline-text {
    color: transparent;
    -webkit-text-stroke: 2px #ffffff;
  }

  .editorial-lead {
    font-size: 1.2rem;
    max-width: 650px;
    line-height: 1.7;
    color: #cbd5e1;
    margin-bottom: 3rem;
  }

  .interactive-index {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    max-width: 700px;
  }

  .index-row {
    background: transparent;
    border: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    padding: 1.25rem 0;
    display: flex;
    align-items: center;
    color: #94a3b8;
    font-family: inherit;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .index-row:hover, .index-row.active {
    color: #ffffff;
    padding-left: 1rem;
    border-bottom-color: #f59e0b;
  }

  .idx-num {
    color: #f59e0b;
    margin-right: 1.5rem;
    font-weight: bold;
  }

  .idx-label {
    flex: 1;
    text-align: left;
    letter-spacing: 0.05em;
  }

  .idx-arrow {
    font-size: 1.3rem;
  }

  .index-detail-box {
    margin-top: 2rem;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 1.5rem;
    max-width: 700px;
  }

  .detail-content h3 {
    margin: 0 0 0.5rem 0;
    color: #f59e0b;
    font-size: 1rem;
  }

  .detail-content p {
    margin: 0;
    color: #cbd5e1;
    line-height: 1.5;
  }

  @media (max-width: 768px) {
    .editorial-stage { flex-direction: column; }
    .vertical-title-strip { writing-mode: horizontal-tb; transform: none; margin: 0 0 1.5rem 0; border: none; }
    .giant-heading { font-size: 2.8rem; }
  }
</style>
