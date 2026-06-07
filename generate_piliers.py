

/* ============================================================
   ÉCONOMIE-CARBURANT.FR — Design System 2026
   Aesthetic: Premium French Editorial × Financial Tool
   Fonts: Space Grotesk (headings) + Inter (body)
   ============================================================ */

/* ── CSS VARIABLES ── */
:root {
  --green:       #27AE60;
  --green-dark:  #1E8449;
  --green-light: #EAFAF1;
  --green-mid:   #A9DFBF;
  --blue:        #3498DB;
  --blue-dark:   #217DBB;
  --blue-light:  #EBF5FB;
  --orange:      #F39C12;
  --orange-light:#FEF9E7;
  --purple:      #9B59B6;
  --purple-light:#F5EEF8;
  --red:         #E74C3C;
  --red-light:   #FDEDEC;
  --teal:        #1ABC9C;
  --teal-light:  #E8F8F5;
  --dark:        #1A252F;
  --dark-2:      #2C3E50;
  --dark-3:      #34495E;
  --gray:        #7F8C8D;
  --gray-light:  #BDC3C7;
  --bg:          #F4F6F8;
  --bg-2:        #FAFBFC;
  --white:       #FFFFFF;
  --card-shadow: 0 2px 12px rgba(26,37,47,0.08);
  --card-hover:  0 12px 40px rgba(26,37,47,0.16);
  --radius:      12px;
  --radius-lg:   20px;
  --radius-xl:   28px;
  --transition:  0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --font-head:   'Space Grotesk', sans-serif;
  --font-body:   'Inter', sans-serif;
  --max-w:       1200px;
  --header-h:    68px;
}

/* ── RESET & BASE ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; font-size: 16px; }
body {
  font-family: var(--font-body);
  font-size: 1rem;
  color: var(--dark-2);
  background: var(--bg-2);
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}
img { max-width: 100%; height: auto; display: block; }
a { color: var(--green); text-decoration: none; transition: color var(--transition); }
a:hover { color: var(--green-dark); }
button { cursor: pointer; font-family: var(--font-body); border: none; outline: none; }
input, select { font-family: var(--font-body); }

/* ── TYPOGRAPHY ── */
h1, h2, h3, h4, h5 {
  font-family: var(--font-head);
  font-weight: 700;
  line-height: 1.2;
  color: var(--dark);
}
h1 { font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; letter-spacing: -0.03em; }
h2 { font-size: clamp(1.5rem, 3vw, 2.2rem); letter-spacing: -0.02em; }
h3 { font-size: clamp(1.1rem, 2vw, 1.4rem); }
h4 { font-size: 1.1rem; }
p { line-height: 1.7; }

/* ── LAYOUT ── */
.container { max-width: var(--max-w); margin: 0 auto; padding: 0 20px; }
.section { padding: 80px 0; }
.section--sm { padding: 48px 0; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.grid-6 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.flex { display: flex; }
.flex-center { display: flex; align-items: center; justify-content: center; }
.flex-between { display: flex; align-items: center; justify-content: space-between; }

/* ── STICKY HEADER ── */
.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  height: var(--header-h);
  background: rgba(255,255,255,0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(44,62,80,0.08);
  transition: box-shadow var(--transition);
}
.site-header.scrolled { box-shadow: 0 4px 24px rgba(26,37,47,0.12); }
.header-inner { height: 100%; display: flex; align-items: center; justify-content: space-between; }
.logo { display: flex; align-items: center; gap: 10px; text-decoration: none; }
.logo-icon {
  width: 36px; height: 36px;
  background: linear-gradient(135deg, var(--green), #1A8A4A);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem;
}
.logo-text {
  font-family: var(--font-head);
  font-weight: 800;
  font-size: 1.05rem;
  color: var(--dark);
  letter-spacing: -0.02em;
}
.logo-text span { color: var(--green); }
.nav { display: flex; align-items: center; gap: 4px; }
.nav a {
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--dark-3);
  transition: all var(--transition);
}
.nav a:hover, .nav a.active {
  background: var(--green-light);
  color: var(--green-dark);
}
.nav-cta {
  margin-left: 12px;
  padding: 9px 20px !important;
  background: var(--green) !important;
  color: var(--white) !important;
  border-radius: 8px !important;
  font-weight: 600 !important;
  box-shadow: 0 2px 12px rgba(39,174,96,0.3);
}
.nav-cta:hover { background: var(--green-dark) !important; transform: translateY(-1px); box-shadow: 0 4px 20px rgba(39,174,96,0.4) !important; }
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
}
.hamburger span { display: block; width: 22px; height: 2px; background: var(--dark-2); border-radius: 2px; transition: all var(--transition); }

/* ── HERO ── */
.hero {
  position: relative;
  background: linear-gradient(135deg, #0D1B2A 0%, #1A2E22 50%, #0F2017 100%);
  min-height: calc(100vh - var(--header-h));
  display: flex;
  align-items: center;
  overflow: hidden;
  padding: 60px 0;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 800px 600px at 70% 50%, rgba(39,174,96,0.12) 0%, transparent 70%),
    radial-gradient(ellipse 400px 400px at 20% 80%, rgba(52,152,219,0.08) 0%, transparent 60%);
  pointer-events: none;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1fr 1.1fr;
  gap: 48px;
  align-items: center;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(39,174,96,0.15);
  border: 1px solid rgba(39,174,96,0.3);
  color: #5DE89B;
  padding: 6px 14px;
  border-radius: 100px;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-bottom: 20px;
}
.hero-badge::before { content: '●'; font-size: 0.6rem; animation: blink 1.5s infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }
.hero h1 {
  font-size: clamp(2.2rem, 4.5vw, 3.4rem);
  color: #FFFFFF;
  margin-bottom: 16px;
  line-height: 1.1;
}
.hero h1 .accent { color: #4ADE80; }
.hero-tldr {
  font-size: 1.05rem;
  color: rgba(255,255,255,0.7);
  margin-bottom: 28px;
  line-height: 1.6;
  max-width: 480px;
}
.hero-stats {
  display: flex;
  gap: 24px;
  margin-top: 32px;
}
.hero-stat { text-align: center; }
.hero-stat .val {
  font-family: var(--font-head);
  font-size: 1.8rem;
  font-weight: 800;
  color: #4ADE80;
  display: block;
}
.hero-stat .lbl {
  font-size: 0.78rem;
  color: rgba(255,255,255,0.5);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.hero-divider { width: 1px; background: rgba(255,255,255,0.12); height: 40px; align-self: center; }

/* ── CALCULATOR CARD (Hero) ── */
.calc-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: var(--radius-xl);
  padding: 32px;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
}
.calc-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--green), #4ADE80, var(--blue));
}
.calc-title {
  font-family: var(--font-head);
  font-size: 1rem;
  font-weight: 700;
  color: rgba(255,255,255,0.9);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ── YEAR TABS ── */
.year-tabs {
  display: flex;
  gap: 6px;
  margin-bottom: 20px;
  background: rgba(0,0,0,0.2);
  border-radius: 10px;
  padding: 4px;
}
.year-tab {
  flex: 1;
  padding: 8px 0;
  border-radius: 7px;
  background: transparent;
  color: rgba(255,255,255,0.5);
  font-size: 0.85rem;
  font-weight: 600;
  font-family: var(--font-head);
  transition: all var(--transition);
  border: none;
}
.year-tab.active {
  background: var(--green);
  color: #fff;
  box-shadow: 0 2px 12px rgba(39,174,96,0.4);
}
.year-tab:hover:not(.active) { color: rgba(255,255,255,0.8); background: rgba(255,255,255,0.06); }

/* ── FORM ELEMENTS ── */
.form-group { margin-bottom: 16px; }
.form-label {
  display: block;
  font-size: 0.82rem;
  font-weight: 600;
  color: rgba(255,255,255,0.6);
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.form-label.dark { color: var(--dark-3); }
.form-input, .form-select {
  width: 100%;
  padding: 13px 16px;
  background: rgba(255,255,255,0.07);
  border: 1.5px solid rgba(255,255,255,0.12);
  border-radius: var(--radius);
  color: #fff;
  font-size: 1rem;
  font-family: var(--font-body);
  transition: all var(--transition);
  appearance: none;
}
.form-input:focus, .form-select:focus {
  outline: none;
  border-color: var(--green);
  background: rgba(39,174,96,0.08);
  box-shadow: 0 0 0 3px rgba(39,174,96,0.15);
}
.form-input::placeholder { color: rgba(255,255,255,0.3); }
.form-select option { background: var(--dark-2); color: #fff; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }

/* Light form variants */
.form-input.light, .form-select.light {
  background: var(--bg);
  border-color: rgba(44,62,80,0.15);
  color: var(--dark-2);
}
.form-input.light:focus, .form-select.light:focus {
  border-color: var(--green);
  background: var(--green-light);
  box-shadow: 0 0 0 3px rgba(39,174,96,0.1);
}
.form-input.light::placeholder { color: var(--gray-light); }

/* ── BUTTONS ── */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 28px;
  border-radius: var(--radius);
  font-family: var(--font-head);
  font-weight: 700;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  transition: all var(--transition);
  letter-spacing: -0.01em;
  position: relative;
  overflow: hidden;
}
.btn::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(255,255,255,0);
  transition: background var(--transition);
}
.btn:hover::after { background: rgba(255,255,255,0.08); }
.btn-green {
  background: linear-gradient(135deg, #27AE60, #1E8449);
  color: #fff;
  box-shadow: 0 4px 20px rgba(39,174,96,0.35);
}
.btn-green:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(39,174,96,0.5); }
.btn-full { width: 100%; }
.btn-calculer {
  animation: pulse 2.4s ease-in-out infinite;
  background: linear-gradient(135deg, #27AE60, #1ABC9C);
  color: #fff;
  box-shadow: 0 4px 20px rgba(39,174,96,0.4);
}
.btn-calculer:hover { animation-play-state: paused; transform: translateY(-3px); box-shadow: 0 12px 40px rgba(39,174,96,0.55); }
@keyframes pulse {
  0%   { box-shadow: 0 4px 20px rgba(39,174,96,0.4); transform: scale(1); }
  50%  { box-shadow: 0 6px 30px rgba(39,174,96,0.6); transform: scale(1.02); }
  100% { box-shadow: 0 4px 20px rgba(39,174,96,0.4); transform: scale(1); }
}
.btn-blue { background: linear-gradient(135deg, #3498DB, #2471A3); color: #fff; box-shadow: 0 4px 20px rgba(52,152,219,0.35); }
.btn-blue:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(52,152,219,0.5); }
.btn-orange { background: linear-gradient(135deg, #F39C12, #D68910); color: #fff; box-shadow: 0 4px 20px rgba(243,156,18,0.35); }
.btn-outline {
  background: transparent;
  border: 2px solid var(--green);
  color: var(--green);
}
.btn-outline:hover { background: var(--green); color: #fff; }
.btn-sm { padding: 9px 18px; font-size: 0.88rem; }
.btn-lg { padding: 18px 36px; font-size: 1.1rem; border-radius: var(--radius-lg); }
.btn-icon { font-size: 1.1em; }

/* ── RESULT BOX ── */
.result-box {
  margin-top: 20px;
  padding: 24px;
  background: linear-gradient(135deg, rgba(39,174,96,0.12), rgba(26,188,156,0.08));
  border: 1px solid rgba(39,174,96,0.25);
  border-radius: var(--radius-lg);
  display: none;
  animation: resultReveal 0.5s cubic-bezier(0.34,1.56,0.64,1) forwards;
}
.result-box.show { display: block; }
@keyframes resultReveal {
  from { opacity: 0; transform: scale(0.95) translateY(10px); }
  to   { opacity: 1; transform: scale(1)   translateY(0); }
}
.result-label {
  font-size: 0.78rem;
  color: rgba(255,255,255,0.5);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 8px;
}
.result-label.dark { color: var(--gray); }
.result-amount {
  font-family: var(--font-head);
  font-size: 2.8rem;
  font-weight: 800;
  color: #4ADE80;
  line-height: 1;
  margin-bottom: 6px;
}
.result-amount.dark { color: var(--green); }
.result-detail {
  font-size: 0.88rem;
  color: rgba(255,255,255,0.6);
  margin-top: 8px;
}
.result-detail.dark { color: var(--dark-3); }
.result-box-light {
  background: var(--green-light);
  border: 1px solid var(--green-mid);
}

/* ── PROGRESS BAR ── */
.progress-wrap { margin-top: 12px; }
.progress-bar {
  height: 4px;
  background: rgba(255,255,255,0.1);
  border-radius: 4px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--green), #4ADE80);
  border-radius: 4px;
  width: 0%;
  transition: width 0.4s ease;
}
.progress-fill.done { width: 100%; }

/* ── TOOL CARDS GRID ── */
.tools-section { background: var(--bg); }
.section-title-wrap { text-align: center; margin-bottom: 48px; }
.section-eyebrow {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--green);
  background: var(--green-light);
  padding: 4px 12px;
  border-radius: 100px;
  margin-bottom: 12px;
}
.section-title { color: var(--dark); margin-bottom: 12px; }
.section-sub { color: var(--gray); font-size: 1.05rem; max-width: 560px; margin: 0 auto; }

.tool-card {
  background: var(--white);
  border-radius: var(--radius-lg);
  padding: 28px 24px;
  box-shadow: var(--card-shadow);
  border: 1px solid rgba(44,62,80,0.06);
  transition: all var(--transition);
  cursor: pointer;
  display: block;
  text-decoration: none;
  position: relative;
  overflow: hidden;
}
.tool-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 0;
  background: linear-gradient(135deg, var(--card-color, #27AE60), transparent);
  opacity: 0.06;
  transition: height var(--transition);
}
.tool-card:hover { transform: translateY(-6px); box-shadow: var(--card-hover); border-color: var(--card-color, var(--green)); }
.tool-card:hover::before { height: 100%; }
.tool-icon {
  width: 52px; height: 52px;
  border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 16px;
  transition: transform var(--transition);
}
.tool-card:hover .tool-icon { transform: scale(1.1) rotate(-4deg); }
.tool-card h3 {
  font-size: 1.05rem;
  color: var(--dark);
  margin-bottom: 8px;
}
.tool-card p { font-size: 0.88rem; color: var(--gray); line-height: 1.5; margin-bottom: 16px; }
.tool-vol {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--card-color, var(--green));
}
.tool-arrow {
  position: absolute;
  top: 24px; right: 24px;
  width: 28px; height: 28px;
  border-radius: 50%;
  background: var(--bg);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.8rem;
  color: var(--gray);
  transition: all var(--transition);
}
.tool-card:hover .tool-arrow {
  background: var(--card-color, var(--green));
  color: #fff;
  transform: translateX(4px);
}

/* Color variants */
.color-green  { --card-color: #27AE60; }
.color-blue   { --card-color: #3498DB; }
.color-orange { --card-color: #F39C12; }
.color-purple { --card-color: #9B59B6; }
.color-red    { --card-color: #E74C3C; }
.color-teal   { --card-color: #1ABC9C; }

.icon-green  { background: #EAFAF1; color: #27AE60; }
.icon-blue   { background: #EBF5FB; color: #3498DB; }
.icon-orange { background: #FEF9E7; color: #F39C12; }
.icon-purple { background: #F5EEF8; color: #9B59B6; }
.icon-red    { background: #FDEDEC; color: #E74C3C; }
.icon-teal   { background: #E8F8F5; color: #1ABC9C; }

/* ── TOOL PAGE LAYOUT ── */
.tool-page { padding-top: 40px; padding-bottom: 80px; }
.tool-hero {
  background: linear-gradient(135deg, #0D1B2A, #152A1E);
  padding: 60px 0 80px;
  position: relative;
  overflow: hidden;
}
.tool-hero::after {
  content: '';
  position: absolute;
  bottom: -1px; left: 0; right: 0;
  height: 40px;
  background: var(--bg-2);
  border-radius: 40px 40px 0 0;
}
.tool-hero-inner { position: relative; z-index: 1; max-width: 700px; }
.tool-hero h1 { color: #fff; margin-bottom: 12px; }
.tool-tldr {
  color: rgba(255,255,255,0.7);
  font-size: 1.05rem;
  margin-bottom: 20px;
}
.tool-content { max-width: var(--max-w); margin: 0 auto; padding: 0 20px; }

/* Main calc panel */
.calc-panel {
  background: var(--white);
  border-radius: var(--radius-xl);
  padding: 40px;
  box-shadow: 0 4px 40px rgba(26,37,47,0.1);
  border: 1px solid rgba(44,62,80,0.06);
  margin-top: -40px;
  position: relative;
  z-index: 2;
}
.calc-panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--bg);
}
.calc-panel-title {
  font-family: var(--font-head);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--dark);
  display: flex;
  align-items: center;
  gap: 10px;
}
.calc-panel-title .icon {
  width: 36px; height: 36px;
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem;
}
.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px; }

/* ── YEAR TABS (page outil) ── */
.year-tabs-light {
  display: flex;
  gap: 6px;
  background: var(--bg);
  border-radius: 10px;
  padding: 4px;
  margin-bottom: 24px;
  width: fit-content;
}
.year-tab-light {
  padding: 8px 16px;
  border-radius: 7px;
  background: transparent;
  color: var(--gray);
  font-size: 0.88rem;
  font-weight: 700;
  font-family: var(--font-head);
  border: none;
  cursor: pointer;
  transition: all var(--transition);
}
.year-tab-light.active { background: var(--green); color: #fff; box-shadow: 0 2px 12px rgba(39,174,96,0.35); }
.year-tab-light:hover:not(.active) { background: var(--white); color: var(--dark-2); }

/* ── RESULT PANEL ── */
.result-panel {
  display: none;
  margin-top: 28px;
  padding: 32px;
  background: linear-gradient(135deg, #F0FDF6, #E8F8F5);
  border: 1px solid #A9DFBF;
  border-radius: var(--radius-lg);
  animation: resultReveal 0.6s cubic-bezier(0.34,1.56,0.64,1) forwards;
}
.result-panel.show { display: block; }
.result-main {
  display: flex;
  align-items: flex-end;
  gap: 16px;
  margin-bottom: 20px;
}
.result-num {
  font-family: var(--font-head);
  font-size: 3.5rem;
  font-weight: 800;
  color: var(--green-dark);
  line-height: 1;
  letter-spacing: -0.04em;
}
.result-unit {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--green);
  padding-bottom: 8px;
}
.result-breakdown {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid rgba(39,174,96,0.2);
}
.result-breakdown-item { text-align: center; }
.result-breakdown-val {
  font-family: var(--font-head);
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--dark-2);
  display: block;
}
.result-breakdown-lbl { font-size: 0.78rem; color: var(--gray); margin-top: 2px; }
.result-actions { display: flex; gap: 12px; margin-top: 20px; flex-wrap: wrap; }

/* ── ACCORDION ── */
.accordion { margin: 40px 0; }
.accordion-item {
  background: var(--white);
  border-radius: var(--radius);
  border: 1px solid rgba(44,62,80,0.08);
  margin-bottom: 12px;
  overflow: hidden;
  transition: border-color var(--transition);
}
.accordion-item.open { border-color: var(--green); }
.accordion-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px;
  cursor: pointer;
  user-select: none;
  transition: background var(--transition);
}
.accordion-header:hover { background: var(--bg); }
.accordion-item.open .accordion-header { background: var(--green-light); }
.accordion-q {
  font-family: var(--font-head);
  font-weight: 600;
  font-size: 1rem;
  color: var(--dark);
}
.accordion-icon {
  width: 28px; height: 28px;
  border-radius: 50%;
  background: var(--bg);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.8rem;
  color: var(--gray);
  transition: all var(--transition);
  flex-shrink: 0;
}
.accordion-item.open .accordion-icon {
  background: var(--green);
  color: #fff;
  transform: rotate(180deg);
}
.accordion-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease, padding 0.3s ease;
  padding: 0 24px;
}
.accordion-item.open .accordion-body { max-height: 600px; padding: 4px 24px 24px; }
.accordion-body p { color: var(--dark-3); line-height: 1.7; }
.accordion-body ul { color: var(--dark-3); padding-left: 20px; margin-top: 8px; }
.accordion-body li { margin-bottom: 6px; }

/* ── FORMULA BOX ── */
.formula-box {
  background: var(--dark);
  border-radius: var(--radius);
  padding: 20px 24px;
  font-family: 'Courier New', monospace;
  color: #4ADE80;
  font-size: 0.9rem;
  line-height: 1.8;
  margin: 12px 0;
  position: relative;
  overflow: hidden;
}
.formula-box::before {
  content: 'FORMULE';
  position: absolute;
  top: 8px; right: 12px;
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  color: rgba(255,255,255,0.2);
  font-family: var(--font-body);
}

/* ── TABLE ── */
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  margin: 20px 0;
}
.data-table th {
  background: var(--dark);
  color: rgba(255,255,255,0.9);
  padding: 12px 16px;
  font-family: var(--font-head);
  font-size: 0.8rem;
  font-weight: 600;
  text-align: left;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.data-table th:first-child { border-radius: 8px 0 0 0; }
.data-table th:last-child  { border-radius: 0 8px 0 0; }
.data-table td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--bg);
  color: var(--dark-2);
}
.data-table tr:last-child td { border-bottom: none; }
.data-table tr:nth-child(even) td { background: var(--bg-2); }
.data-table tr:hover td { background: var(--green-light); }
.data-table .highlight td {
  background: linear-gradient(90deg, var(--green-light), transparent);
  font-weight: 600;
  color: var(--green-dark);
}

/* ── INFO CARDS ── */
.info-card {
  background: var(--white);
  border-radius: var(--radius-lg);
  padding: 28px;
  box-shadow: var(--card-shadow);
  border: 1px solid rgba(44,62,80,0.06);
  margin: 20px 0;
}
.info-card-header {
  display: flex; align-items: center; gap: 12px; margin-bottom: 16px;
}
.info-card-icon {
  width: 40px; height: 40px;
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem;
}
.info-card-title { font-family: var(--font-head); font-weight: 700; font-size: 1.05rem; }

/* ── EXAMPLE CARD ── */
.example-card {
  background: linear-gradient(135deg, #E8F6F3, #D5F5E3);
  border: 1px solid var(--green-mid);
  border-radius: var(--radius-lg);
  padding: 24px 28px;
  margin: 24px 0;
}
.example-title {
  font-family: var(--font-head);
  font-weight: 700;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--green-dark);
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.example-val {
  font-family: var(--font-head);
  font-size: 2rem;
  font-weight: 800;
  color: var(--green-dark);
}

/* ── SOURCES ── */
.sources-section {
  background: var(--bg);
  border-radius: var(--radius-lg);
  padding: 24px 28px;
  margin-top: 32px;
}
.sources-title {
  font-family: var(--font-head);
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--gray);
  margin-bottom: 12px;
}
.sources-list { display: flex; flex-wrap: wrap; gap: 10px; }
.source-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  background: var(--white);
  border: 1px solid rgba(44,62,80,0.1);
  border-radius: 100px;
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--blue);
  transition: all var(--transition);
}
.source-link:hover { border-color: var(--blue); box-shadow: 0 2px 8px rgba(52,152,219,0.15); color: var(--blue-dark); }

/* ── PDF BANNER ── */
.pdf-banner {
  background: linear-gradient(135deg, #1A252F, #1E3A28);
  border-radius: var(--radius-xl);
  padding: 40px 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 32px;
  margin: 40px 0;
  position: relative;
  overflow: hidden;
}
.pdf-banner::before {
  content: '📄';
  position: absolute;
  right: -20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 8rem;
  opacity: 0.05;
}
.pdf-banner-badge {
  display: inline-block;
  background: rgba(243,156,18,0.2);
  border: 1px solid rgba(243,156,18,0.4);
  color: #F6C142;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 10px;
}
.pdf-banner h3 {
  color: #fff;
  font-size: 1.5rem;
  margin-bottom: 8px;
}
.pdf-banner p { color: rgba(255,255,255,0.65); font-size: 0.95rem; }
.pdf-banner-price {
  text-align: center;
  flex-shrink: 0;
}
.pdf-price-val {
  font-family: var(--font-head);
  font-size: 3rem;
  font-weight: 800;
  color: #4ADE80;
  line-height: 1;
  display: block;
  margin-bottom: 4px;
}
.pdf-price-lbl { font-size: 0.82rem; color: rgba(255,255,255,0.5); margin-bottom: 16px; display: block; }

/* ── NEWS BANNER ── */
.news-banner {
  background: linear-gradient(90deg, var(--orange) 0%, #E67E22 100%);
  padding: 14px 0;
  position: relative;
  overflow: hidden;
}
.news-banner-inner {
  display: flex;
  align-items: center;
  gap: 12px;
}
.news-badge {
  background: rgba(255,255,255,0.25);
  color: #fff;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 4px;
  white-space: nowrap;
}
.news-text { color: #fff; font-size: 0.9rem; font-weight: 500; }
.news-link { color: rgba(255,255,255,0.85); text-decoration: underline; font-weight: 600; }

/* ── FOOTER ── */
.site-footer {
  background: var(--dark);
  color: rgba(255,255,255,0.7);
  padding: 60px 0 32px;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 48px;
}
.footer-brand .logo-text { color: rgba(255,255,255,0.9); }
.footer-desc {
  font-size: 0.88rem;
  color: rgba(255,255,255,0.5);
  margin: 16px 0;
  line-height: 1.7;
}
.footer-title {
  font-family: var(--font-head);
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: rgba(255,255,255,0.35);
  margin-bottom: 16px;
}
.footer-links { list-style: none; }
.footer-links li { margin-bottom: 10px; }
.footer-links a {
  font-size: 0.9rem;
  color: rgba(255,255,255,0.6);
  transition: color var(--transition);
}
.footer-links a:hover { color: #4ADE80; }
.footer-bottom {
  padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}
.footer-copy { font-size: 0.82rem; color: rgba(255,255,255,0.35); }
.trust-badges { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
.trust-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 6px;
  font-size: 0.78rem;
  color: rgba(255,255,255,0.5);
  transition: all var(--transition);
}
.trust-badge:hover { border-color: rgba(255,255,255,0.2); color: rgba(255,255,255,0.8); }
.trust-badge .icon { font-size: 0.9rem; }

/* ── COOKIES BANNER ── */
.cookies-banner {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%) translateY(120px);
  z-index: 9999;
  background: var(--dark);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  max-width: 580px;
  width: calc(100% - 40px);
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.4);
  backdrop-filter: blur(12px);
  transition: transform 0.5s cubic-bezier(0.34,1.56,0.64,1);
}
.cookies-banner.show { transform: translateX(-50%) translateY(0); }
.cookies-text { font-size: 0.85rem; color: rgba(255,255,255,0.7); flex: 1; line-height: 1.5; }
.cookies-text a { color: #4ADE80; }
.cookies-actions { display: flex; gap: 8px; flex-shrink: 0; flex-wrap: wrap; }
.btn-cookies-accept { padding: 9px 16px; background: var(--green); color: #fff; border-radius: 8px; font-size: 0.85rem; font-weight: 600; font-family: var(--font-body); border: none; cursor: pointer; white-space: nowrap; transition: all var(--transition); }
.btn-cookies-accept:hover { background: var(--green-dark); }
.btn-cookies-refuse { padding: 9px 16px; background: transparent; color: rgba(255,255,255,0.5); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; font-size: 0.85rem; font-family: var(--font-body); cursor: pointer; white-space: nowrap; transition: all var(--transition); }
.btn-cookies-refuse:hover { color: rgba(255,255,255,0.8); }

/* ── AOS (custom, 0 dependency) ── */
[data-aos] { opacity: 0; transform: translateY(24px); transition: opacity 0.6s ease, transform 0.6s ease; }
[data-aos].aos-in { opacity: 1; transform: translateY(0); }
[data-aos="fade-left"]  { transform: translateX(-24px); }
[data-aos="fade-left"].aos-in  { transform: translateX(0); }
[data-aos="fade-right"] { transform: translateX(24px); }
[data-aos="fade-right"].aos-in { transform: translateX(0); }
[data-aos="zoom-in"]    { transform: scale(0.9); }
[data-aos="zoom-in"].aos-in    { transform: scale(1); }
.delay-1 { transition-delay: 0.1s !important; }
.delay-2 { transition-delay: 0.2s !important; }
.delay-3 { transition-delay: 0.3s !important; }
.delay-4 { transition-delay: 0.4s !important; }
.delay-5 { transition-delay: 0.5s !important; }

/* ── ALERT / NOTICE ── */
.alert {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 18px;
  border-radius: var(--radius);
  font-size: 0.9rem;
  margin: 16px 0;
}
.alert-green  { background: var(--green-light);  border: 1px solid var(--green-mid);   color: var(--green-dark); }
.alert-blue   { background: var(--blue-light);   border: 1px solid #A9D0F5;            color: var(--blue-dark); }
.alert-orange { background: var(--orange-light); border: 1px solid #F9E4B7;            color: #9A6A04; }
.alert-icon   { font-size: 1.1rem; flex-shrink: 0; margin-top: 1px; }

/* ── STAT COUNTER ── */
.stat-grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 20px;
  margin: 40px 0;
}
.stat-item {
  text-align: center;
  padding: 24px 16px;
  background: var(--white);
  border-radius: var(--radius-lg);
  box-shadow: var(--card-shadow);
  border: 1px solid rgba(44,62,80,0.05);
}
.stat-val {
  font-family: var(--font-head);
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--green);
  display: block;
  line-height: 1;
  margin-bottom: 8px;
}
.stat-lbl { font-size: 0.82rem; color: var(--gray); text-transform: uppercase; letter-spacing: 0.05em; }

/* ── NEWSLETTER ── */
.newsletter-section {
  background: linear-gradient(135deg, var(--green) 0%, #1ABC9C 100%);
  padding: 60px 0;
  position: relative;
  overflow: hidden;
}
.newsletter-section::before {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.newsletter-inner {
  text-align: center;
  position: relative;
  z-index: 1;
}
.newsletter-inner h2 { color: #fff; margin-bottom: 8px; }
.newsletter-inner p { color: rgba(255,255,255,0.8); margin-bottom: 28px; }
.newsletter-form {
  display: flex;
  gap: 12px;
  max-width: 480px;
  margin: 0 auto;
}
.newsletter-form input {
  flex: 1;
  padding: 14px 18px;
  border-radius: var(--radius);
  border: none;
  font-size: 1rem;
  font-family: var(--font-body);
  background: rgba(255,255,255,0.95);
  color: var(--dark-2);
}
.newsletter-form input::placeholder { color: var(--gray); }
.newsletter-form button {
  padding: 14px 24px;
  background: var(--dark);
  color: #fff;
  border-radius: var(--radius);
  border: none;
  font-weight: 700;
  font-family: var(--font-head);
  cursor: pointer;
  white-space: nowrap;
  transition: all var(--transition);
}
.newsletter-form button:hover { background: var(--dark-3); transform: translateY(-1px); }

/* ── EXIT INTENT MODAL ── */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.6);
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  backdrop-filter: blur(4px);
  transition: opacity 0.3s ease;
}
.modal-overlay.show { opacity: 1; pointer-events: all; }
.modal-box {
  background: var(--white);
  border-radius: var(--radius-xl);
  padding: 40px;
  max-width: 480px;
  width: calc(100% - 40px);
  position: relative;
  transform: scale(0.9);
  transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
.modal-overlay.show .modal-box { transform: scale(1); }
.modal-close {
  position: absolute;
  top: 16px; right: 16px;
  width: 32px; height: 32px;
  border-radius: 50%;
  background: var(--bg);
  display: flex; align-items: center; justify-content: center;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  color: var(--gray);
  transition: all var(--transition);
}
.modal-close:hover { background: var(--red-light); color: var(--red); }

/* ── RELATED TOOLS ── */
.related-tools {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  margin: 24px 0;
}
.related-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: var(--white);
  border-radius: var(--radius);
  border: 1px solid rgba(44,62,80,0.08);
  text-decoration: none;
  transition: all var(--transition);
}
.related-card:hover { border-color: var(--green); transform: translateY(-2px); box-shadow: 0 4px 20px rgba(39,174,96,0.12); }
.related-icon { width: 36px; height: 36px; border-radius: 9px; display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0; }
.related-text { font-size: 0.88rem; font-weight: 600; color: var(--dark-2); }

/* ── BLOG / ARTICLE ── */
.article-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; }
.article-card {
  background: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--card-shadow);
  border: 1px solid rgba(44,62,80,0.06);
  transition: all var(--transition);
  text-decoration: none;
}
.article-card:hover { transform: translateY(-4px); box-shadow: var(--card-hover); }
.article-thumb {
  height: 160px;
  background: linear-gradient(135deg, var(--green-light), #D5F5E3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
}
.article-body { padding: 20px; }
.article-tag {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--green);
  background: var(--green-light);
  padding: 3px 8px;
  border-radius: 4px;
  margin-bottom: 10px;
}
.article-title { font-size: 0.95rem; font-weight: 700; color: var(--dark); line-height: 1.4; margin-bottom: 8px; }
.article-meta { font-size: 0.78rem; color: var(--gray); }

/* ── ADENSE ZONES ── */
.ad-zone {
  background: var(--bg);
  border: 2px dashed rgba(44,62,80,0.1);
  border-radius: var(--radius);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--gray-light);
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.05em;
}
.ad-leaderboard { height: 90px; }
.ad-rectangle  { height: 250px; width: 300px; }
.ad-half-page  { height: 600px; width: 300px; }
.sidebar { position: sticky; top: calc(var(--header-h) + 24px); }

/* ── BREADCRUMB ── */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
  color: rgba(255,255,255,0.5);
  margin-bottom: 20px;
}
.breadcrumb a { color: rgba(255,255,255,0.6); text-decoration: none; }
.breadcrumb a:hover { color: #4ADE80; }
.breadcrumb-sep { color: rgba(255,255,255,0.25); }

/* ── TAG / BADGE ── */
.tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 10px;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 600;
}
.tag-green  { background: var(--green-light);  color: var(--green-dark); }
.tag-blue   { background: var(--blue-light);   color: var(--blue-dark); }
.tag-orange { background: var(--orange-light); color: #9A6A04; }
.new-badge {
  background: var(--orange);
  color: #fff;
  font-size: 0.68rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* ── HISTORY BOX ── */
.history-box {
  margin-top: 24px;
  padding: 20px;
  background: var(--bg);
  border-radius: var(--radius);
  display: none;
}
.history-box.show { display: block; }
.history-title {
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--gray);
  margin-bottom: 12px;
}
.history-list { list-style: none; }
.history-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid rgba(44,62,80,0.08);
  font-size: 0.88rem;
  color: var(--dark-3);
}
.history-item:last-child { border-bottom: none; }
.history-val { font-weight: 600; color: var(--green-dark); }

/* ── PRINT ── */
@media print {
  .site-header, .site-footer, .ad-zone, .cookies-banner, .modal-overlay { display: none !important; }
}

/* ── RESPONSIVE ── */
@media (max-width: 1024px) {
  .footer-grid { grid-template-columns: 1fr 1fr; }
  .stat-grid { grid-template-columns: repeat(2,1fr); }
  .grid-3 { grid-template-columns: repeat(2,1fr); }
  .pdf-banner { flex-direction: column; text-align: center; }
}
@media (max-width: 768px) {
  :root { --header-h: 60px; }
  .nav { display: none; }
  .hamburger { display: flex; }
  .nav.open {
    display: flex;
    flex-direction: column;
    position: fixed;
    top: 60px; left: 0; right: 0;
    background: var(--white);
    padding: 16px;
    gap: 4px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.12);
    z-index: 999;
  }
  .hero-grid { grid-template-columns: 1fr; gap: 32px; }
  .calc-card { order: 2; }
  .hero-stats { flex-wrap: wrap; gap: 16px; }
  .grid-6 { grid-template-columns: 1fr 1fr; }
  .grid-2, .grid-3 { grid-template-columns: 1fr; }
  .form-grid { grid-template-columns: 1fr; }
  .form-row { grid-template-columns: 1fr; }
  .result-breakdown { grid-template-columns: 1fr 1fr; }
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 24px; }
  .stat-grid { grid-template-columns: repeat(2,1fr); }
  .related-tools { grid-template-columns: 1fr; }
  .article-grid { grid-template-columns: 1fr; }
  .calc-panel { padding: 24px 20px; margin-top: -30px; }
  .newsletter-form { flex-direction: column; }
  .hero-divider { display: none; }
  .section { padding: 56px 0; }
  h1 { font-size: clamp(1.8rem, 7vw, 2.4rem); }
}
@media (max-width: 480px) {
  .grid-6 { grid-template-columns: 1fr; }
  .footer-grid { grid-template-columns: 1fr; }
  .pdf-banner { padding: 28px 20px; }
  .year-tabs-light { width: 100%; }
  .year-tab-light { flex: 1; padding: 8px 8px; font-size: 0.82rem; }
  .result-breakdown { grid-template-columns: 1fr; }
  .trust-badges { flex-wrap: wrap; gap: 8px; }
}


