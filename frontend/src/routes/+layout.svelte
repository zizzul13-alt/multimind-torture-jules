<script lang="ts">
  import { page } from '$app/stores';
  let { children } = $props();
</script>

<div class="app-container">
  <nav class="top-nav" aria-label="Benchmark Navigation Matrix">
    <div class="brand">
      <span class="logo-icon">⚡</span>
      <span class="logo-text">MULTIMIND <small>SvelteKit + FastAPI</small></span>
    </div>

    <div class="nav-links">
      <a href="/" class:active={$page.url.pathname === '/'}>MultiMind App</a>
      <a href="/ref-arknights" class:active={$page.url.pathname === '/ref-arknights'}>Ref A: Arknights</a>
      <a href="/ref-noomo" class:active={$page.url.pathname === '/ref-noomo'}>Ref B: Noomo</a>
      <a href="/ref-dioriviera" class:active={$page.url.pathname === '/ref-dioriviera'}>Ref C: Dioriviera</a>
      <a href="/ref-viensla" class:active={$page.url.pathname === '/ref-viensla'}>Ref D: Viens-là</a>
    </div>
  </nav>

  <main class="content-body">
    {@render children()}
  </main>
</div>

<style>
  :global(html, body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: #0b0f17;
    color: #e2e8f0;
    overflow-x: hidden;
  }

  .app-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  .top-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem 1.5rem;
    background: rgba(15, 23, 42, 0.95);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(8px);
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 800;
    letter-spacing: 0.05em;
  }

  .logo-text small {
    font-weight: 400;
    color: #94a3b8;
    font-size: 0.75rem;
    margin-left: 0.25rem;
  }

  .nav-links {
    display: flex;
    gap: 0.5rem;
    overflow-x: auto;
  }

  .nav-links a {
    color: #94a3b8;
    text-decoration: none;
    padding: 0.4rem 0.8rem;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    transition: all 0.2s ease;
  }

  .nav-links a:hover {
    color: #f8fafc;
    background: rgba(255, 255, 255, 0.05);
  }

  .nav-links a.active {
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.3);
  }

  .content-body {
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  @media (max-width: 768px) {
    .top-nav {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.5rem;
      padding: 0.5rem 1rem;
    }
    .nav-links {
      width: 100%;
      padding-bottom: 0.25rem;
    }
  }
</style>
