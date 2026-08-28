<script lang="ts">
  let scrollY = $state(0);

  function handleScroll(e: Event) {
    const target = e.target as HTMLElement;
    scrollY = target.scrollTop;
  }
</script>

<div class="dior-container" onscroll={handleScroll}>
  <div class="bg-material">
    <img src="/materials/dioriviera_bg.svg" alt="Dioriviera Luxury Pattern" class="bg-img" />
  </div>

  <header class="dior-header">
    <div class="brand-house">CHRISTIAN DIOR</div>
    <div class="collection-title">DIORIVIERA BENCHMARK</div>
    <div class="sub-brand">PARIS</div>
  </header>

  <section class="dior-hero">
    <div class="hero-frame" style="transform: translateY({scrollY * 0.12}px);">
      <span class="edition-tag">LIMITED COLLECTION — 2025</span>
      <h1>LUXURY MATERIAL COMPOSITION</h1>
      <p class="tagline">Imagery used as presentation architecture, premium spacing, and restrained elegance.</p>
    </div>
  </section>

  <section class="material-showcase">
    <div class="material-card" style="transform: translateY({-scrollY * 0.04}px);">
      <div class="card-image-box">
        <div class="fake-texture gold"></div>
        <div class="card-overlay">
          <span>MAT-01</span>
          <h4>Toile de Jouy Motif</h4>
        </div>
      </div>
      <p class="desc">Subtle vector pattern layering without heavy graphics performance penalty.</p>
    </div>

    <div class="material-card" style="transform: translateY({-scrollY * 0.08}px);">
      <div class="card-image-box">
        <div class="fake-texture sand"></div>
        <div class="card-overlay">
          <span>MAT-02</span>
          <h4>Mediterranean Warmth</h4>
        </div>
      </div>
      <p class="desc">Restrained beige and champagne color palette, prioritising legibility.</p>
    </div>
  </section>
</div>

<style>
  .dior-container {
    position: relative;
    min-height: calc(100vh - 50px);
    height: calc(100vh - 50px);
    overflow-y: auto;
    background: #faf8f5;
    color: #2c251e;
    font-family: 'Times New Roman', Times, serif;
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
    opacity: 0.9;
  }

  .dior-header {
    position: relative;
    z-index: 10;
    padding: 3rem;
    text-align: center;
    border-bottom: 1px solid rgba(140, 120, 90, 0.2);
    background: rgba(250, 248, 245, 0.85);
    backdrop-filter: blur(8px);
  }

  .brand-house {
    font-size: 0.85rem;
    letter-spacing: 0.35em;
    color: #8c785a;
    font-weight: bold;
  }

  .collection-title {
    font-size: 2rem;
    letter-spacing: 0.2em;
    margin: 0.5rem 0;
    font-weight: 300;
  }

  .sub-brand {
    font-size: 0.75rem;
    letter-spacing: 0.4em;
    color: #b09e80;
  }

  .dior-hero {
    position: relative;
    z-index: 10;
    padding: 6rem 2rem 4rem 2rem;
    text-align: center;
    max-width: 900px;
    margin: 0 auto;
  }

  .edition-tag {
    font-size: 0.8rem;
    letter-spacing: 0.25em;
    color: #8c785a;
    display: block;
    margin-bottom: 1rem;
  }

  h1 {
    font-size: 3rem;
    font-weight: 300;
    letter-spacing: 0.1em;
    margin: 0 0 1.5rem 0;
    line-height: 1.2;
  }

  .tagline {
    font-size: 1.15rem;
    color: #6e5d48;
    font-style: italic;
    line-height: 1.6;
  }

  .material-showcase {
    position: relative;
    z-index: 10;
    max-width: 1100px;
    margin: 2rem auto;
    padding: 0 2rem 5rem 2rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
  }

  .material-card {
    background: #ffffff;
    border: 1px solid rgba(140, 120, 90, 0.2);
    padding: 1.5rem;
    box-shadow: 0 10px 30px rgba(140, 120, 90, 0.08);
  }

  .card-image-box {
    position: relative;
    height: 320px;
    overflow: hidden;
  }

  .fake-texture {
    width: 100%;
    height: 100%;
  }

  .fake-texture.gold {
    background: linear-gradient(135deg, #e6c894, #c49a55);
  }

  .fake-texture.sand {
    background: linear-gradient(135deg, #dfd5c6, #bfae99);
  }

  .card-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 1.5rem;
    background: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
    color: #fff;
    box-sizing: border-box;
  }

  .card-overlay span {
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    display: block;
  }

  .card-overlay h4 {
    margin: 0.25rem 0 0 0;
    font-size: 1.4rem;
    font-weight: 300;
    letter-spacing: 0.05em;
  }

  .desc {
    font-size: 0.95rem;
    color: #6e5d48;
    margin-top: 1rem;
    line-height: 1.5;
  }

  @media (max-width: 768px) {
    .material-showcase { grid-template-columns: 1fr; }
    h1 { font-size: 2rem; }
  }

  @media (prefers-reduced-motion: reduce) {
    .hero-frame, .material-card { transform: none !important; }
  }
</style>
