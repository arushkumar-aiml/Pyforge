<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PyForge — Lightweight PyTorch Training Framework</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --bg: #0a0a0f;
    --surface: #111118;
    --card: #16161f;
    --border: #2a2a3a;
    --fire1: #ff6b00;
    --fire2: #ff9500;
    --fire3: #ffcc00;
    --text: #e8e8f0;
    --muted: #7070a0;
    --green: #00e5a0;
    --red: #ff4466;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
    cursor: none;
  }

  /* Custom cursor */
  #cursor {
    position: fixed;
    width: 12px; height: 12px;
    background: var(--fire1);
    border-radius: 50%;
    pointer-events: none;
    z-index: 9999;
    transition: transform 0.1s ease;
    mix-blend-mode: screen;
  }
  #cursor-ring {
    position: fixed;
    width: 36px; height: 36px;
    border: 1.5px solid var(--fire2);
    border-radius: 50%;
    pointer-events: none;
    z-index: 9998;
    transition: left 0.12s ease, top 0.12s ease;
    opacity: 0.5;
  }

  /* Noise overlay */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 1;
    opacity: 0.3;
  }

  /* Hero */
  #hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem;
    position: relative;
    overflow: hidden;
  }

  .grid-bg {
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(255,107,0,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,107,0,0.04) 1px, transparent 1px);
    background-size: 60px 60px;
    animation: gridPulse 8s ease-in-out infinite;
  }

  @keyframes gridPulse {
    0%, 100% { opacity: 0.4; }
    50% { opacity: 1; }
  }

  .glow-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    pointer-events: none;
  }
  .orb1 { width: 500px; height: 500px; background: rgba(255,107,0,0.12); top: -100px; left: -100px; animation: drift1 12s ease-in-out infinite; }
  .orb2 { width: 400px; height: 400px; background: rgba(255,149,0,0.08); bottom: -80px; right: -80px; animation: drift2 10s ease-in-out infinite; }

  @keyframes drift1 { 0%,100%{transform:translate(0,0)} 50%{transform:translate(60px,40px)} }
  @keyframes drift2 { 0%,100%{transform:translate(0,0)} 50%{transform:translate(-50px,-30px)} }

  .flame-icon {
    font-size: 5rem;
    margin-bottom: 1.5rem;
    display: inline-block;
    animation: flamePulse 2s ease-in-out infinite;
    position: relative;
    z-index: 2;
    filter: drop-shadow(0 0 30px rgba(255,107,0,0.8));
  }
  @keyframes flamePulse {
    0%,100%{transform:scale(1) rotate(-2deg);filter:drop-shadow(0 0 30px rgba(255,107,0,0.8))}
    50%{transform:scale(1.08) rotate(2deg);filter:drop-shadow(0 0 50px rgba(255,200,0,1))}
  }

  h1 {
    font-size: clamp(4rem, 12vw, 9rem);
    font-weight: 800;
    line-height: 0.9;
    letter-spacing: -0.03em;
    position: relative;
    z-index: 2;
  }

  .title-py { color: var(--text); }
  .title-forge {
    background: linear-gradient(135deg, var(--fire1), var(--fire2), var(--fire3));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    position: relative;
  }
  .title-forge::after {
    content: 'FORGE';
    position: absolute;
    left: 0; top: 4px;
    background: linear-gradient(135deg, var(--fire1), var(--fire2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: blur(8px);
    opacity: 0.4;
    z-index: -1;
  }

  .tagline {
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    color: var(--muted);
    margin-top: 1.5rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    position: relative;
    z-index: 2;
  }

  .badges {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 2rem;
    position: relative;
    z-index: 2;
  }

  .badge {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    border: 1px solid;
    letter-spacing: 0.05em;
  }
  .badge-blue { border-color: #4488ff; color: #4488ff; background: rgba(68,136,255,0.08); }
  .badge-orange { border-color: var(--fire1); color: var(--fire2); background: rgba(255,107,0,0.08); }
  .badge-green { border-color: var(--green); color: var(--green); background: rgba(0,229,160,0.08); }

  /* Scroll arrow */
  .scroll-hint {
    position: absolute;
    bottom: 2.5rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    z-index: 2;
    opacity: 0.5;
    animation: bounceArrow 2s ease-in-out infinite;
  }
  .scroll-hint span { font-size: 0.7rem; font-family: 'Space Mono', monospace; letter-spacing: 0.15em; color: var(--muted); }
  @keyframes bounceArrow { 0%,100%{transform:translateX(-50%) translateY(0)} 50%{transform:translateX(-50%) translateY(8px)} }

  /* Section layout */
  section {
    max-width: 1100px;
    margin: 0 auto;
    padding: 5rem 2rem;
    position: relative;
    z-index: 2;
  }

  .section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--fire1);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }
  .section-label::before {
    content: '';
    display: block;
    width: 30px;
    height: 1px;
    background: var(--fire1);
  }

  h2 {
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    letter-spacing: -0.02em;
    margin-bottom: 2.5rem;
    line-height: 1.1;
  }

  /* Flow diagram */
  .flow {
    display: flex;
    align-items: center;
    gap: 0;
    flex-wrap: wrap;
    margin: 3rem 0;
    justify-content: center;
  }

  .flow-step {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem 1.5rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    text-align: center;
    position: relative;
    transition: all 0.3s ease;
    cursor: default;
    min-width: 140px;
  }

  .flow-step:hover {
    border-color: var(--fire1);
    background: rgba(255,107,0,0.06);
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(255,107,0,0.15);
  }

  .flow-step .step-num {
    font-size: 0.6rem;
    color: var(--fire2);
    letter-spacing: 0.15em;
    margin-bottom: 0.4rem;
  }

  .flow-arrow {
    color: var(--fire1);
    font-size: 1.5rem;
    padding: 0 0.5rem;
    opacity: 0.6;
    flex-shrink: 0;
  }

  /* Terminal */
  .terminal {
    background: #0d0d14;
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    margin: 2rem 0;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,107,0,0.05);
  }

  .terminal-bar {
    background: #18182a;
    padding: 0.85rem 1.2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    border-bottom: 1px solid var(--border);
  }

  .t-dots { display: flex; gap: 7px; }
  .t-dot { width: 12px; height: 12px; border-radius: 50%; }
  .t-dot.r { background: #ff5f56; }
  .t-dot.y { background: #ffbd2e; }
  .t-dot.g { background: #27c93f; }

  .t-title { color: var(--muted); font-size: 0.75rem; letter-spacing: 0.08em; }

  .terminal-body {
    padding: 1.5rem 1.8rem;
    line-height: 2;
  }

  .t-line { display: flex; align-items: baseline; gap: 0.75rem; }
  .t-prompt { color: var(--fire1); }
  .t-cmd { color: var(--text); }
  .t-out { color: var(--muted); }
  .t-success { color: var(--green); }
  .t-loss { color: var(--fire2); }

  /* Typewriter */
  .typewriter { overflow: hidden; white-space: nowrap; border-right: 2px solid var(--fire1); animation: typing 2s steps(30) forwards, blink 0.7s step-end infinite 2s; width: 0; }
  @keyframes typing { to { width: 100%; } }
  @keyframes blink { 50% { border-color: transparent; } }

  /* Cards grid */
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
  }

  .card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
  }

  .card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,107,0,0.04), transparent);
    opacity: 0;
    transition: opacity 0.35s ease;
  }

  .card:hover {
    border-color: rgba(255,107,0,0.4);
    transform: translateY(-5px);
    box-shadow: 0 20px 50px rgba(255,107,0,0.1);
  }

  .card:hover::before { opacity: 1; }

  .card-icon { font-size: 2.2rem; margin-bottom: 1rem; }
  .card-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }
  .card-desc { font-size: 0.9rem; color: var(--muted); line-height: 1.6; }

  /* Feature table */
  .feature-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    margin: 2rem 0;
  }

  .feature-table th {
    text-align: left;
    padding: 1rem 1.5rem;
    background: var(--card);
    border-bottom: 1px solid var(--border);
    color: var(--muted);
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    font-weight: 400;
  }

  .feature-table td {
    padding: 1rem 1.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    transition: background 0.2s;
  }

  .feature-table tr:hover td { background: rgba(255,107,0,0.03); }

  .status-done {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: var(--green);
  }

  .status-coming {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: var(--muted);
  }

  /* Timeline */
  .timeline {
    position: relative;
    padding-left: 2rem;
    margin: 2rem 0;
  }

  .timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0; bottom: 0;
    width: 1px;
    background: linear-gradient(to bottom, var(--fire1), transparent);
  }

  .timeline-item {
    position: relative;
    margin-bottom: 2.5rem;
    padding-left: 1.5rem;
    opacity: 0;
    transform: translateX(-20px);
    transition: all 0.5s ease;
  }

  .timeline-item.visible {
    opacity: 1;
    transform: translateX(0);
  }

  .timeline-item::before {
    content: '';
    position: absolute;
    left: -2rem;
    top: 0.4rem;
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--fire1);
    box-shadow: 0 0 10px var(--fire1);
  }

  .timeline-day {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--fire2);
    margin-bottom: 0.3rem;
  }

  .timeline-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }
  .timeline-topics { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.75rem; }

  .topic-tag {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
    background: rgba(255,107,0,0.08);
    border: 1px solid rgba(255,107,0,0.2);
    color: var(--fire2);
  }

  /* Roadmap */
  .roadmap {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin: 2rem 0;
  }

  .roadmap-item {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    padding: 1.2rem 1.5rem;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }

  .roadmap-item.done {
    border-color: rgba(0,229,160,0.2);
  }

  .roadmap-item.done::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: var(--green);
  }

  .roadmap-item:not(.done)::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: var(--border);
  }

  .roadmap-item:hover { transform: translateX(6px); }

  .roadmap-version {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: var(--fire2);
    min-width: 50px;
    font-weight: 700;
  }

  .roadmap-desc { flex: 1; font-size: 0.95rem; }
  .roadmap-status { font-size: 1.1rem; }

  /* Authors */
  .authors {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
  }

  .author-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
  }

  .author-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--fire1), var(--fire3));
    transform: scaleX(0);
    transition: transform 0.35s ease;
  }

  .author-card:hover { border-color: rgba(255,107,0,0.4); transform: translateY(-8px); }
  .author-card:hover::after { transform: scaleX(1); }

  .author-avatar {
    width: 72px; height: 72px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--fire1), var(--fire3));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    margin: 0 auto 1.2rem;
    box-shadow: 0 0 30px rgba(255,107,0,0.3);
  }

  .author-name { font-size: 1.15rem; font-weight: 700; margin-bottom: 0.3rem; }
  .author-role { font-family: 'Space Mono', monospace; font-size: 0.7rem; color: var(--muted); letter-spacing: 0.1em; text-transform: uppercase; }

  /* Footer */
  footer {
    border-top: 1px solid var(--border);
    text-align: center;
    padding: 3rem 2rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: var(--muted);
    position: relative;
    z-index: 2;
  }

  footer .logo { font-size: 1.5rem; font-weight: 800; font-family: 'Syne', sans-serif; margin-bottom: 0.75rem; }
  footer .logo span { background: linear-gradient(135deg, var(--fire1), var(--fire3)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }

  /* Divider */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 0 2rem;
    position: relative;
    z-index: 2;
  }

  /* Fade-in on scroll */
  .fade-in {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.7s ease, transform 0.7s ease;
  }
  .fade-in.visible { opacity: 1; transform: translateY(0); }

  /* Loss chart animation */
  .loss-chart {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2rem;
    margin: 2rem 0;
  }

  .loss-chart-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: var(--muted);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
  }

  .chart-area {
    position: relative;
    height: 120px;
  }

  svg.loss-svg { width: 100%; height: 100%; overflow: visible; }

  .chart-label {
    display: flex;
    justify-content: space-between;
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    color: var(--muted);
    margin-top: 0.75rem;
  }

  @media (max-width: 600px) {
    .flow { gap: 0.5rem; }
    .flow-arrow { display: none; }
    h1 { font-size: 3.5rem; }
  }
</style>
</head>
<body>

<div id="cursor"></div>
<div id="cursor-ring"></div>

<!-- HERO -->
<div id="hero">
  <div class="grid-bg"></div>
  <div class="glow-orb orb1"></div>
  <div class="glow-orb orb2"></div>

  <div class="flame-icon">🔥</div>
  <h1>
    <span class="title-py">Py</span><span class="title-forge">Forge</span>
  </h1>
  <p class="tagline">A lightweight PyTorch training framework — built from scratch</p>
  <div class="badges">
    <span class="badge badge-blue">Python 3.11</span>
    <span class="badge badge-orange">PyTorch 2.0</span>
    <span class="badge badge-green">MIT License</span>
  </div>

  <div class="scroll-hint">
    <span>Scroll</span>
    <svg width="16" height="24" viewBox="0 0 16 24" fill="none">
      <path d="M8 2v20M2 16l6 6 6-6" stroke="#ff6b00" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
  </div>
</div>

<div class="divider"></div>

<!-- WHAT IS PYFORGE -->
<section class="fade-in">
  <div class="section-label">Overview</div>
  <h2>What is PyForge?</h2>
  <p style="color:var(--muted);font-size:1.05rem;max-width:600px;line-height:1.8;">
    PyForge is a minimal PyTorch training framework that handles the repetitive parts of the ML training loop — so you can focus on building smarter models.
  </p>

  <div class="cards" style="margin-top:2.5rem;">
    <div class="card">
      <div class="card-icon">⚡</div>
      <div class="card-title">Auto Hardware Detection</div>
      <div class="card-desc">Detects CUDA, MPS (Apple Silicon), or CPU automatically. No config needed.</div>
    </div>
    <div class="card">
      <div class="card-icon">🔁</div>
      <div class="card-title">Auto Training Loop</div>
      <div class="card-desc">Pass any PyTorch model and PyForge handles the forward pass, backprop, and optimization.</div>
    </div>
    <div class="card">
      <div class="card-icon">📊</div>
      <div class="card-title">Validation & Reporting</div>
      <div class="card-desc">Automatic validation loop with loss reporting after every epoch — no boilerplate.</div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- HOW IT WORKS -->
<section class="fade-in">
  <div class="section-label">Architecture</div>
  <h2>How it Works</h2>

  <div class="flow">
    <div class="flow-step"><div class="step-num">01</div>Your Model</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">02</div>PyForge(model)</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">03</div>Hardware Detection</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">04</div>Auto Training</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">05</div>Loss Report</div>
  </div>

  <div class="terminal">
    <div class="terminal-bar">
      <div class="t-dots">
        <div class="t-dot r"></div>
        <div class="t-dot y"></div>
        <div class="t-dot g"></div>
      </div>
      <span class="t-title">terminal — python main.py</span>
    </div>
    <div class="terminal-body">
      <div class="t-line"><span class="t-prompt">$</span><span class="t-cmd">python main.py</span></div>
      <div class="t-line" style="margin-top:0.5rem;"><span class="t-out">[PyForge] Device: cpu</span></div>
      <div class="t-line"><span class="t-out">[PyForge] Running on cpu</span></div>
      <div class="t-line"><span class="t-out">[PyForge] Supported: ['cuda', 'mps', 'cpu']</span></div>
      <div class="t-line" style="margin-top:0.5rem;"><span class="t-loss" id="e1">[PyForge] Epoch 1 Loss: 0.8921</span></div>
      <div class="t-line"><span class="t-loss" id="e2" style="opacity:0">[PyForge] Epoch 2 Loss: 0.6543</span></div>
      <div class="t-line"><span class="t-loss"

