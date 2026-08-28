<script lang="ts">
  import { onMount } from 'svelte';

  let mouseX = $state(0);
  let mouseY = $state(0);
  let scrollY = $state(0);

  function handleMouseMove(e: MouseEvent) {
    const target = e.currentTarget as HTMLElement;
    const rect = target.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    mouseX = Math.round((x / rect.width - 0.5) * 40);
    mouseY = Math.round((y / rect.height - 0.5) * 40);
  }

  function handleScroll(e: Event) {
    const target = e.target as HTMLElement;
    scrollY = target.scrollTop;
  }
</script>

<div
  class="noomo-container"
  onmousemove={handleMouseMove}
  onscroll={handleScroll}
  role="region"
  aria-label="Noomo Interactive Workspace"
  data-mouse-x={mouseX}
  data-mouse-y={mouseY}
>
  <div class="bg-material" style="transform: translate({mouseX * 0.2}px, {mouseY * 0.2}px);">
    <img src="/materials/noomo_bg.svg" alt="Noomo Interactive Spatial Background" class="bg-img" />
  </div>

  <div class="floating-orb orb-1" style="transform: translate({mouseX * 0.8}px, {mouseY * 0.8 + scrollY * 0.1}px);"></div>
  <div class="floating-orb orb-2" style="transform: translate({-mouseX * 0.6}px, {-mouseY * 0.6 + scrollY * 0.2}px);"></div>

  <header class="noomo-header">
    <div class="brand-tag">NOOMO LABS / SPATIAL AGENCY</div>
    <div class="interactive-coord">POS: [{mouseX}, {mouseY}]</div>
  </header>

  <section class="spatial-hero">
    <h1 style="transform: perspective(800px) rotateY({mouseX * 0.3}deg) rotateX({-mouseY * 0.3}deg);">
      INTERACTIVE<br/><span class="gradient-text">SPATIAL AGENCY</span>
    </h1>
    <p class="hero-sub">Dynamic cursor parallax + non-standard motion architecture proof</p>
  </section>

  <section class="cards-grid">
    <div class="spatial-card" style="transform: translateY({-scrollY * 0.05}px) rotate({mouseX * 0.05}deg);">
      <div class="card-num">01</div>
      <h3>Dynamic Canvas Transformation</h3>
      <p>Scroll-linked CSS 3D transforms with spring responsiveness natively compiled by Svelte.</p>
    </div>

    <div class="spatial-card highlighted" style="transform: translateY({-scrollY * 0.1}px) rotate({-mouseX * 0.05}deg);">
      <div class="card-num">02</div>
      <h3>Spatial Interaction Boundary</h3>
      <p>Seamless spatial rhythm without bloated external JS animation engines.</p>
    </div>

    <div class="spatial-card" style="transform: translateY({-scrollY * 0.15}px) rotate({mouseX * 0.08}deg);">
      <div class="card-num">03</div>
      <h3>Asymmetric Navigation</h3>
      <p>Non-grid visual compositions reacting directly to pointer micro-inputs.</p>
    </div>
  </section>
</div>

<style>
  .noomo-container {
    position: relative;
    min-height: calc(100vh - 50px);
    height: calc(100vh - 50px);
    overflow-y: auto;
    background: #05030a;
    color: #fff;
    font-family: 'Space Grotesk', -apple-system, sans-serif;
  }

  .bg-material {
    position: absolute;
    top: -5%;
    left: -5%;
    width: 110%;
    height: 110%;
    z-index: 1;
    pointer-events: none;
    transition: transform 0.1s ease-out;
  }

  .bg-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.85;
  }

  .floating-orb {
    position: absolute;
    border-radius: 50%;
    pointer-events: none;
    z-index: 2;
    filter: blur(40px);
    transition: transform 0.1s ease-out;
  }

  .orb-1 {
    top: 20%;
    right: 15%;
    width: 300px;
    height: 300px;
    background: rgba(168, 85, 247, 0.25);
  }

  .orb-2 {
    bottom: 20%;
    left: 10%;
    width: 400px;
    height: 400px;
    background: rgba(236, 72, 153, 0.2);
  }

  .noomo-header {
    position: relative;
    z-index: 10;
    padding: 2.5rem;
    display: flex;
    justify-content: space-between;
    font-family: monospace;
    font-size: 0.9rem;
    letter-spacing: 0.1em;
  }

  .interactive-coord {
    color: #a855f7;
  }

  .spatial-hero {
    position: relative;
    z-index: 10;
    padding: 4rem 2.5rem;
    text-align: center;
  }

  h1 {
    font-size: 4.5rem;
    font-weight: 900;
    line-height: 0.95;
    margin: 0;
    letter-spacing: -0.03em;
    transition: transform 0.1s ease-out;
  }

  .gradient-text {
    background: linear-gradient(135deg, #a855f7, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .hero-sub {
    font-size: 1.25rem;
    color: #94a3b8;
    margin-top: 1.5rem;
  }

  .cards-grid {
    position: relative;
    z-index: 10;
    max-width: 1200px;
    margin: 3rem auto;
    padding: 0 2rem 5rem 2rem;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }

  .spatial-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 2.5rem;
    transition: transform 0.1s ease-out, border-color 0.3s ease;
  }

  .spatial-card.highlighted {
    background: rgba(168, 85, 247, 0.08);
    border-color: rgba(168, 85, 247, 0.4);
  }

  .card-num {
    font-family: monospace;
    font-size: 1.2rem;
    color: #ec4899;
    margin-bottom: 1rem;
  }

  .spatial-card h3 {
    font-size: 1.5rem;
    margin: 0 0 1rem 0;
  }

  .spatial-card p {
    color: #cbd5e1;
    line-height: 1.6;
    margin: 0;
  }

  @media (max-width: 768px) {
    h1 { font-size: 2.5rem; }
    .cards-grid { grid-template-columns: 1fr; }
  }

  @media (prefers-reduced-motion: reduce) {
    .bg-material, .floating-orb, h1, .spatial-card {
      transform: none !important;
      transition: none !important;
    }
  }
</style>
