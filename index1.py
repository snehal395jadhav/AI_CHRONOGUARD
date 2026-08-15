import streamlit as st
import streamlit.components.v1 as components
import time

# ─── CONFIG ────────────────────────────────────────────────
st.set_page_config(
    page_title="Navneet AI ChronoGuard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

REDIRECT_URL = "/dashboard"
DELAY_MS = 8000


# ─── STATIC BLUE CALENDAR ICON ─────────────────────────────
logo_html = """
<div style="
    width:72px;
    height:72px;
    background:linear-gradient(145deg,#114ea8,#1976d2,#4da3ff);
    border-radius:15px;
    display:flex;
    flex-direction:column;
    overflow:hidden;
    box-shadow:0 8px 20px rgba(21,101,192,0.26);
">
  <div style="
      height:22px;
      background:rgba(0,0,0,0.16);
      display:flex;
      align-items:center;
      justify-content:space-between;
      padding:0 8px;
      flex-shrink:0;
  ">
    <div style="width:7px;height:10px;border-radius:3px;background:rgba(255,255,255,0.96);"></div>
    <span style="font-size:8px;font-weight:800;color:#fff;letter-spacing:1px;">AI</span>
    <div style="width:7px;height:10px;border-radius:3px;background:rgba(255,255,255,0.96);"></div>
  </div>

  <div style="
      flex:1;
      display:grid;
      grid-template-columns:repeat(5,1fr);
      gap:2px;
      padding:5px 6px;
  ">
    <div style="border-radius:2px;background:rgba(255,255,255,0.22);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.58);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.95);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.58);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.22);"></div>

    <div style="border-radius:2px;background:rgba(255,255,255,0.58);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.22);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.58);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.95);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.22);"></div>

    <div style="border-radius:2px;background:rgba(255,255,255,0.95);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.58);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.22);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.58);"></div>
    <div style="border-radius:2px;background:rgba(255,255,255,0.22);"></div>
  </div>
</div>
"""

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<style>
  :root {{
    --bg: #ffffff;
    --text: #0b2258;
    --muted: #6f8fb7;
    --muted-light: #9bb6d8;
    --brand: #1976d2;
    --brand-dark: #0f4ea8;
    --brand-soft: #4da3ff;
  }}

  html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    background: var(--bg);
    font-family: 'Segoe UI', system-ui, sans-serif;
    overflow-x: hidden;
    overflow-y: auto;
    cursor:
      url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28' shape-rendering='crispEdges' viewBox='0 0 28 28'>\
<rect x='2' y='2' width='4' height='4' fill='%230f4ea8'/>\
<rect x='6' y='2' width='4' height='4' fill='%231976d2'/>\
<rect x='10' y='2' width='4' height='4' fill='%234da3ff'/>\
<rect x='2' y='6' width='4' height='4' fill='%231976d2'/>\
<rect x='6' y='6' width='4' height='4' fill='%234da3ff'/>\
<rect x='10' y='10' width='4' height='4' fill='%231976d2'/>\
<rect x='14' y='14' width='4' height='4' fill='%230f4ea8'/>\
<rect x='18' y='18' width='4' height='4' fill='%234da3ff'/>\
</svg>") 4 4, auto;
    scrollbar-width: thin;
    scrollbar-color: rgba(25,118,210,0.45) rgba(227,239,252,0.7);
  }}

  body::-webkit-scrollbar {{
    width: 8px;
  }}

  body::-webkit-scrollbar-track {{
    background: rgba(227,239,252,0.7);
  }}

  body::-webkit-scrollbar-thumb {{
    background: rgba(25,118,210,0.45);
    border-radius: 999px;
  }}

  * {{
    box-sizing: border-box;
  }}

  a, button, .hover-target, .title-hover-zone {{
    cursor:
      url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' shape-rendering='crispEdges' viewBox='0 0 32 32'>\
<rect x='2' y='2' width='4' height='4' fill='%230f4ea8'/>\
<rect x='6' y='2' width='4' height='4' fill='%231976d2'/>\
<rect x='10' y='2' width='4' height='4' fill='%234da3ff'/>\
<rect x='2' y='6' width='4' height='4' fill='%231976d2'/>\
<rect x='6' y='6' width='4' height='4' fill='%234da3ff'/>\
<rect x='10' y='10' width='4' height='4' fill='%231976d2'/>\
<rect x='14' y='14' width='4' height='4' fill='%230f4ea8'/>\
<rect x='18' y='18' width='4' height='4' fill='%234da3ff'/>\
<rect x='22' y='22' width='4' height='4' fill='%231976d2'/>\
</svg>") 4 4, pointer;
  }}

  #lr {{
    position: relative;
    width: 100vw;
    min-height: 100vh;
    overflow: hidden;
    background:
      radial-gradient(circle at 20% 0%, rgba(25,118,210,0.05), transparent 28%),
      radial-gradient(circle at 100% 0%, rgba(25,118,210,0.04), transparent 26%),
      linear-gradient(180deg, #f7fbff 0%, #ffffff 32%, #ffffff 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: clamp(2px, 0.3vw, 6px);
  }}

  canvas#bgc {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
  }}

  .wave-top {{
    position: absolute;
    top: -4%;
    left: -5%;
    width: 110%;
    height: 30%;
    background: linear-gradient(180deg, rgba(25,118,210,0.07) 0%, rgba(25,118,210,0.03) 55%, transparent 100%);
    clip-path: ellipse(65% 100% at 50% 0%);
    z-index: 1;
  }}

  .wave-bot {{
    position: absolute;
    bottom: -10%;
    right: -10%;
    width: 50%;
    height: 24%;
    background: radial-gradient(circle at 100% 100%, rgba(25,118,210,0.05), transparent 70%);
    z-index: 1;
  }}

  .deco {{
    position: absolute;
    border-radius: 50%;
    border: 1px solid rgba(21,101,192,0.08);
    z-index: 1;
  }}

  .pl {{
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 2;
  }}

  .pt {{
    position: absolute;
    border-radius: 50%;
    background: rgba(15,78,168,0.15);
    animation: ptUp linear infinite;
  }}

  @keyframes ptUp {{
    from {{ transform: translateY(0) scale(1); opacity: .65; }}
    to   {{ transform: translateY(-100vh) scale(.18); opacity: 0; }}
  }}

  .spark-layer {{
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9998;
    overflow: hidden;
  }}

  .spark {{
    position: absolute;
    width: clamp(3px, 0.35vw, 5px);
    height: clamp(3px, 0.35vw, 5px);
    pointer-events: none;
    border-radius: 2px;
    background: linear-gradient(145deg, #ffffff, #4da3ff, #1976d2);
    box-shadow:
      0 0 7px rgba(77,163,255,0.40),
      0 0 12px rgba(25,118,210,0.24);
    animation: sparkFade 600ms ease-out forwards;
  }}

  @keyframes sparkFade {{
    0% {{
      transform: translate(0, 0) scale(1.02) rotate(0deg);
      opacity: 1;
    }}
    100% {{
      transform: translate(var(--dx), var(--dy)) scale(0.18) rotate(90deg);
      opacity: 0;
    }}
  }}

  .cc {{
    position: relative;
    z-index: 10;
    width: min(100%, 760px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0 clamp(14px, 1.8vw, 22px) clamp(12px, 1.2vw, 18px);
    margin-top: clamp(-260px, -15vw, -160px);
  }}

  .logo-wrap {{
    position: relative;
    width: clamp(96px, 12vw, 142px);
    height: clamp(96px, 12vw, 142px);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: clamp(4px, 0.6vw, 8px);
  }}

  .ring-svg {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
  }}

  .logo-bg {{
    width: clamp(72px, 8vw, 100px);
    height: clamp(72px, 8vw, 100px);
    border-radius: clamp(18px, 1.6vw, 22px);
    background: linear-gradient(180deg, #ffffff 0%, #f7fbff 100%);
    border: 1px solid rgba(21,101,192,0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transform: scale(.4) rotate(-8deg);
    animation: logoIn 1.05s cubic-bezier(.34,1.56,.64,1) .25s forwards;
    box-shadow:
      0 10px 24px rgba(21,101,192,0.12),
      0 2px 6px rgba(21,101,192,0.08);
  }}

  @keyframes logoIn {{
    to {{ opacity: 1; transform: scale(1) rotate(0deg); }}
  }}

  .title-block {{
    width: 100%;
    opacity: 0;
    transform: translateY(16px);
    animation: fadeUp .85s cubic-bezier(.22,1,.36,1) .95s forwards;
  }}

  .title-hover-zone {{
    position: relative;
    display: inline-block;
    padding: clamp(14px, 1.5vw, 18px) clamp(18px, 2.2vw, 30px) clamp(16px, 1.7vw, 20px);
    border-radius: clamp(18px, 1.5vw, 20px);
    min-width: min(84vw, 600px);
    transition:
      background 0.45s ease,
      box-shadow 0.45s ease,
      backdrop-filter 0.45s ease,
      transform 0.35s ease;
  }}

  .title-hover-zone::before {{
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background:
      linear-gradient(120deg,
        rgba(25,118,210,0.00) 0%,
        rgba(77,163,255,0.10) 30%,
        rgba(25,118,210,0.12) 50%,
        rgba(77,163,255,0.10) 70%,
        rgba(25,118,210,0.00) 100%);
    opacity: 0;
    transform: scale(0.985);
    transition: opacity .45s ease, transform .45s ease;
    pointer-events: none;
  }}

  .title-hover-zone::after {{
    content: "";
    position: absolute;
    left: 8%;
    right: 8%;
    bottom: 3px;
    height: 1px;
    border-radius: 999px;
    background: linear-gradient(90deg, transparent, rgba(25,118,210,.65), transparent);
    opacity: 0;
    transform: scaleX(.7);
    transition: opacity .45s ease, transform .45s ease;
    pointer-events: none;
  }}

  .title-hover-zone:hover {{
    background: rgba(255,255,255,0.18);
    box-shadow:
      0 10px 28px rgba(25,118,210,0.08),
      0 2px 10px rgba(25,118,210,0.06);
    backdrop-filter: blur(4px);
    transform: translateY(-1px);
  }}

  .title-hover-zone:hover::before {{
    opacity: 1;
    transform: scale(1);
  }}

  .title-hover-zone:hover::after {{
    opacity: 1;
    transform: scaleX(1);
  }}

  @keyframes fadeUp {{
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  .t-welcome {{
    font-size: clamp(11px, 1.15vw, 15px);
    letter-spacing: clamp(2px, .45vw, 5px);
    text-transform: uppercase;
    color: var(--brand);
    margin-bottom: clamp(5px, 0.5vw, 7px);
    font-weight: 800;
    animation: spreadIn 1s ease 1.05s both;
    transition:
      color .35s ease,
      text-shadow .35s ease,
      letter-spacing .35s ease,
      filter .35s ease;
  }}

  @keyframes spreadIn {{
    from {{ letter-spacing: 10px; opacity: 0; }}
    to   {{ letter-spacing: clamp(2px, .45vw, 5px); opacity: 1; }}
  }}

  .t-navneet {{
    font-size: clamp(30px, 5vw, 58px);
    font-weight: 900;
    line-height: 1.02;
    color: var(--text);
    letter-spacing: -1.2px;
    margin: 0;
    transition:
      color .45s ease,
      text-shadow .45s ease,
      filter .45s ease;
    position: relative;
  }}

  .t-navneet .navneet-text {{
    display: inline-block;
    background: linear-gradient(90deg, #0b2258 0%, #0b2258 45%, #1976d2 52%, #0b2258 60%, #0b2258 100%);
    background-size: 240% auto;
    background-position: 0% center;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    transition: background-position .8s ease, filter .45s ease;
  }}

  .t-ai {{
    color: var(--brand);
    display: inline-block;
    animation: aiPop .45s cubic-bezier(.34,1.56,.64,1) 1.45s both;
    position: relative;
    transition:
      transform .35s ease,
      filter .35s ease,
      text-shadow .35s ease;
  }}

  .t-ai::after {{
    content: "";
    position: absolute;
    left: -8%;
    right: -8%;
    bottom: 8%;
    height: 30%;
    background: radial-gradient(circle, rgba(77,163,255,.32) 0%, rgba(77,163,255,0) 70%);
    filter: blur(8px);
    opacity: 0;
    transition: opacity .35s ease;
    pointer-events: none;
    z-index: -1;
  }}

  @keyframes aiPop {{
    from {{ transform: scale(.55); opacity: 0; }}
    to   {{ transform: scale(1); opacity: 1; }}
  }}

  .t-chrono {{
    font-size: clamp(12px, 1.35vw, 18px);
    font-weight: 800;
    letter-spacing: clamp(3px, .55vw, 7px);
    text-transform: uppercase;
    color: var(--brand);
    margin-top: clamp(5px, 0.5vw, 7px);
    opacity: 0;
    animation: fadeUp .75s ease 1.2s forwards;
    transition:
      color .45s ease,
      text-shadow .45s ease,
      filter .45s ease;
    position: relative;
  }}

  .t-chrono .chrono-text {{
    display: inline-block;
    background: linear-gradient(90deg, #1976d2 0%, #4da3ff 45%, #0f4ea8 60%, #1976d2 100%);
    background-size: 240% auto;
    background-position: 0% center;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    transition: background-position .8s ease, filter .45s ease;
  }}

  .title-hover-zone:hover .t-welcome {{
    color: #0f4ea8;
    text-shadow: 0 0 12px rgba(77,163,255,0.15);
    filter: brightness(1.08);
  }}

  .title-hover-zone:hover .t-navneet .navneet-text {{
    background-position: 100% center;
    filter: drop-shadow(0 0 8px rgba(77,163,255,0.10));
  }}

  .title-hover-zone:hover .t-ai {{
    transform: scale(1.02);
    filter: brightness(1.08);
    text-shadow: 0 0 10px rgba(77,163,255,0.20);
  }}

  .title-hover-zone:hover .t-ai::after {{
    opacity: 1;
  }}

  .title-hover-zone:hover .t-chrono .chrono-text {{
    background-position: 100% center;
    filter: drop-shadow(0 0 8px rgba(25,118,210,0.15));
  }}

  .t-line {{
    width: min(100%, 420px);
    height: 1px;
    background: linear-gradient(
      90deg,
      transparent 0%,
      rgba(25,118,210,0.16) 20%,
      rgba(25,118,210,0.95) 50%,
      rgba(25,118,210,0.16) 80%,
      transparent 100%
    );
    margin: clamp(8px, 0.8vw, 10px) auto clamp(5px, 0.5vw, 6px);
    opacity: 0;
    animation: fadeUp .6s ease 1.35s forwards;
    transition: filter .35s ease, transform .35s ease;
  }}

  .title-hover-zone:hover .t-line {{
    filter: drop-shadow(0 0 6px rgba(77,163,255,0.22));
    transform: scaleX(1.01);
  }}

  .t-tagline {{
    font-size: clamp(9px, .92vw, 12px);
    letter-spacing: clamp(1.2px, .2vw, 2.5px);
    color: var(--muted-light);
    text-transform: uppercase;
    opacity: 0;
    animation: fadeUp .7s ease 1.5s forwards;
  }}

  .status-row {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 7px;
    margin-top: clamp(8px, .8vw, 10px);
    padding: clamp(6px, .6vw, 7px) clamp(10px, 1vw, 12px);
    border-radius: 999px;
    background: rgba(25,118,210,0.04);
    border: 1px solid rgba(25,118,210,0.08);
    opacity: 0;
    animation: fadeUp .5s ease 1.8s forwards;
  }}

  .status-dot {{
    width: clamp(5px, .45vw, 6px);
    height: clamp(5px, .45vw, 6px);
    border-radius: 50%;
    background: var(--brand);
    animation: blink 1.2s ease-in-out 1.8s infinite;
  }}

  @keyframes blink {{
    0%,100% {{ opacity: .35; }}
    50% {{ opacity: 1; box-shadow: 0 0 8px rgba(25,118,210,.35); }}
  }}

  .status-txt {{
    font-size: clamp(8px, .75vw, 9px);
    color: var(--muted);
    letter-spacing: clamp(.8px, .1vw, 1.2px);
    text-transform: uppercase;
  }}

  .pbar-wrap {{
    width: min(100%, 300px);
    margin-top: clamp(8px, .8vw, 10px);
    margin-bottom: 0;
    opacity: 0;
    animation: fadeUp .7s ease 1.7s forwards;
  }}

  .pbar-top {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 6px;
  }}

  .pbar-lbl {{
    font-size: clamp(8px, .75vw, 9px);
    letter-spacing: 1.1px;
    color: var(--muted);
    text-transform: uppercase;
  }}

  .pbar-pct {{
    font-size: clamp(8px, .75vw, 9px);
    font-weight: 700;
    color: var(--brand);
    letter-spacing: 1px;
  }}

  .pbar-track {{
    width: 100%;
    height: clamp(4px, .35vw, 4px);
    background: #eaf2fb;
    border-radius: 999px;
    overflow: hidden;
    box-shadow: inset 0 1px 2px rgba(21,101,192,0.08);
  }}

  .pbar-fill {{
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #0f4ea8 0%, #1976d2 52%, #4da3ff 100%);
    background-size: 200% auto;
    border-radius: 999px;
    animation: fillBar 4s cubic-bezier(.4,0,.2,1) 2s forwards,
               shimmer 1.4s linear 2s infinite;
  }}

  @keyframes fillBar {{
    0%   {{ width: 0%; }}
    55%  {{ width: 68%; }}
    85%  {{ width: 90%; }}
    100% {{ width: 100%; }}
  }}

  @keyframes shimmer {{
    from {{ background-position: 0% center; }}
    to   {{ background-position: 200% center; }}
  }}

  .pbar-steps {{
    display: flex;
    justify-content: space-between;
    margin-top: 6px;
    gap: 8px;
  }}

  .pbar-step {{
    font-size: clamp(7px, .62vw, 8px);
    color: #b3c7de;
    letter-spacing: .35px;
    transition: color .35s ease;
    white-space: nowrap;
  }}

  .footer {{
    position: absolute;
    left: 50%;
    bottom: clamp(5px, .7vw, 8px);
    transform: translateX(-50%);
    z-index: 15;
    width: calc(100% - 16px);
    max-width: 920px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    flex-wrap: wrap;
    text-align: center;
    color: #8ea9c7;
    font-size: clamp(7px, .75vw, 9px);
    letter-spacing: .5px;
    opacity: 0;
    animation: fadeUp .55s ease 2.3s forwards;
  }}

  .footer-sep {{
    color: #b5cbe2;
  }}

  .footer-logo {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-weight: 700;
    color: #7e9bbd;
    text-transform: uppercase;
    font-size: clamp(7px, .72vw, 8px);
    letter-spacing: 1px;
  }}

  .footer-icon {{
    width: clamp(11px, .85vw, 12px);
    height: clamp(11px, .85vw, 12px);
    border-radius: 4px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(145deg,#114ea8,#1976d2,#4da3ff);
    color: #fff;
    font-size: clamp(6px, .5vw, 7px);
    font-weight: 800;
    line-height: 1;
    box-shadow: 0 2px 6px rgba(21,101,192,0.18);
  }}

  .pixel-follower {{
    position: fixed;
    width: clamp(14px, .95vw, 16px);
    height: clamp(14px, .95vw, 16px);
    pointer-events: none;
    z-index: 9999;
    transform: translate(-50%, -50%);
    opacity: .95;
    mix-blend-mode: normal;
    filter: drop-shadow(0 0 7px rgba(77,163,255,0.18));
  }}

  .pixel-follower .px {{
    position: absolute;
    width: clamp(4px, .3vw, 5px);
    height: clamp(4px, .3vw, 5px);
    background: #1976d2;
    box-shadow: 0 0 7px rgba(77,163,255,0.18);
  }}

  .pixel-follower .p1 {{ left: 0; top: 0; background: #0f4ea8; }}
  .pixel-follower .p2 {{ left: 5px; top: 0; background: #1976d2; }}
  .pixel-follower .p3 {{ left: 0; top: 5px; background: #1976d2; }}
  .pixel-follower .p4 {{ left: 5px; top: 5px; background: #4da3ff; }}
  .pixel-follower .p5 {{ left: 10px; top: 10px; background: #1976d2; }}

  @media (max-width: 1024px) {{
    .cc {{
      width: min(100%, 700px);
    }}
  }}

  @media (max-width: 768px) {{
    html, body {{
      overflow-y: auto;
    }}

    #lr {{
      min-height: 100vh;
      padding: 8px 8px 12px;
      align-items: flex-start;
    }}

    .cc {{
      width: 100%;
      padding: 18px 12px 56px;
      margin-top: 0;
    }}

    .logo-wrap {{
      margin-bottom: 8px;
    }}

    .title-hover-zone {{
      padding: 16px 18px 18px;
      min-width: 92vw;
      border-radius: 18px;
    }}

    .t-welcome {{
      font-size: clamp(11px, 3vw, 14px);
      letter-spacing: 3px;
    }}

    .t-navneet {{
      font-size: clamp(32px, 9vw, 44px);
    }}

    .t-chrono {{
      font-size: clamp(13px, 3vw, 17px);
      letter-spacing: 3px;
    }}

    .t-tagline {{
      max-width: 92%;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.45;
      font-size: clamp(10px, 2.5vw, 12px);
    }}

    .pbar-wrap {{
      max-width: 270px;
      margin-top: 8px;
    }}

    .footer {{
      gap: 5px;
      width: calc(100% - 12px);
      bottom: 5px;
    }}

    .pixel-follower {{
      display: none;
    }}
  }}

  @media (max-width: 520px) {{
    .cc {{
      padding-bottom: 56px;
    }}

    .t-welcome {{
      margin-bottom: 6px;
    }}

    .t-line {{
      margin: 8px auto 6px;
    }}

    .status-row {{
      padding: 6px 10px;
      margin-top: 8px;
    }}

    .status-txt {{
      letter-spacing: .8px;
      font-size: 8px;
    }}

    .pbar-step {{
      font-size: 7px;
    }}

    .footer {{
      font-size: 7px;
      line-height: 1.4;
    }}

    .footer-logo {{
      font-size: 7px;
    }}
  }}

  @media (max-height: 720px) {{
    html, body {{
      overflow-y: auto;
    }}

    #lr {{
      min-height: 760px;
      align-items: flex-start;
    }}

    .cc {{
      margin-top: 0;
      padding-top: 18px;
      padding-bottom: 64px;
    }}
  }}
</style>
</head>
<body>
<div id="lr">
  <canvas id="bgc"></canvas>

  <div class="wave-top"></div>
  <div class="wave-bot"></div>

  <div class="deco" style="width:400px;height:400px;top:-140px;right:-110px;"></div>
  <div class="deco" style="width:260px;height:260px;bottom:-90px;left:-70px;"></div>

  <div class="pl" id="pl"></div>
  <div class="spark-layer" id="sparkLayer"></div>

  <div class="pixel-follower" id="pixelFollower">
    <span class="px p1"></span>
    <span class="px p2"></span>
    <span class="px p3"></span>
    <span class="px p4"></span>
    <span class="px p5"></span>
  </div>

  <div class="cc">
    <div class="logo-wrap">
      <svg class="ring-svg" viewBox="0 0 160 160" fill="none">
        <circle cx="80" cy="80" r="74" stroke="rgba(21,101,192,0.14)" stroke-width="1.5"></circle>
        <circle cx="80" cy="80" r="74" stroke="url(#rg1)" stroke-width="2.5"
          stroke-dasharray="465" stroke-dashoffset="465"
          style="animation:drawR 1.8s cubic-bezier(.4,0,.2,1) .2s forwards;
                 transform-origin:80px 80px;transform:rotate(-90deg)">
        </circle>
        <circle cx="80" cy="80" r="63" stroke="rgba(21,101,192,0.08)" stroke-width=".9"></circle>
        <circle cx="80" cy="80" r="52" stroke="rgba(21,101,192,0.05)" stroke-width=".7"></circle>

        <defs>
          <linearGradient id="rg1" x1="0" y1="0" x2="160" y2="160" gradientUnits="userSpaceOnUse">
            <stop offset="0%" stop-color="#0f4ea8"></stop>
            <stop offset="45%" stop-color="#42a5f5"></stop>
            <stop offset="100%" stop-color="#0f4ea8"></stop>
          </linearGradient>
        </defs>

        <style>
          @keyframes drawR {{
            to {{ stroke-dashoffset: 0; }}
          }}
        </style>
      </svg>

      <div class="logo-bg">
        {logo_html}
      </div>
    </div>

    <div class="title-block">
      <div class="title-hover-zone hover-target">
        <div class="t-welcome">Welcome to</div>
        <div class="t-navneet"><span class="navneet-text">Navneet</span>&nbsp;<span class="t-ai">AI</span></div>
        <div class="t-chrono"><span class="chrono-text">ChronoGuard</span></div>
        <div class="t-line"></div>
        <div class="t-tagline">Intelligent Time &nbsp;&middot;&nbsp; Protected Future</div>

        <div class="status-row">
          <div class="status-dot"></div>
          <div class="status-txt">System initializing</div>
        </div>
      </div>
    </div>

    <div class="pbar-wrap">
      <div class="pbar-top">
        <span class="pbar-lbl">Loading</span>
        <span class="pbar-pct" id="pct">0%</span>
      </div>
      <div class="pbar-track">
        <div class="pbar-fill"></div>
      </div>
      <div class="pbar-steps">
        <span class="pbar-step" id="s1">Connecting</span>
        <span class="pbar-step" id="s2">Verifying</span>
        <span class="pbar-step" id="s3">Ready</span>
      </div>
    </div>
  </div>

  <div class="footer">
    <span>© Snehal Jadhav Navneet 2026</span>
    <span class="footer-sep">•</span>
    <span class="footer-logo">
      <span class="footer-icon">N</span>
      <span>Navneet AI</span>
    </span>
  </div>
</div>

<script>
(function() {{
  const canvas = document.getElementById('bgc');
  const ctx = canvas.getContext('2d');
  const root = document.getElementById('lr');

  function resize() {{
    canvas.width = root.offsetWidth || window.innerWidth;
    canvas.height = root.offsetHeight || window.innerHeight;
  }}

  resize();
  window.addEventListener('resize', resize);

  const W = () => canvas.width;
  const H = () => canvas.height;
  const cals = [];

  function mkCal() {{
    const s = 18 + Math.random() * 34;
    return {{
      x: Math.random() * W(),
      y: Math.random() * H() + H(),
      s: s,
      spd: 0.08 + Math.random() * 0.24,
      drft: (Math.random() - 0.5) * 0.18,
      rot: (Math.random() - 0.5) * 0.42,
      rspd: (Math.random() - 0.5) * 0.006,
      a: 0.05 + Math.random() * 0.08,
      hue: 214 + Math.random() * 8
    }};
  }}

  for (let i = 0; i < 26; i++) {{
    const c = mkCal();
    c.y = Math.random() * H();
    cals.push(c);
  }}

  function drawRoundedRect(context, x, y, width, height, radius) {{
    if (typeof radius === 'number') {{
      radius = {{tl: radius, tr: radius, br: radius, bl: radius}};
    }} else {{
      radius = Object.assign({{tl: 0, tr: 0, br: 0, bl: 0}}, radius);
    }}

    context.beginPath();
    context.moveTo(x + radius.tl, y);
    context.lineTo(x + width - radius.tr, y);
    context.quadraticCurveTo(x + width, y, x + width, y + radius.tr);
    context.lineTo(x + width, y + height - radius.br);
    context.quadraticCurveTo(x + width, y + height, x + width - radius.br, y + height);
    context.lineTo(x + radius.bl, y + height);
    context.quadraticCurveTo(x, y + height, x, y + height - radius.bl);
    context.lineTo(x, y + radius.tl);
    context.quadraticCurveTo(x, y, x + radius.tl, y);
    context.closePath();
  }}

  function drawCal(context, x, y, s, a, h) {{
    context.save();
    context.globalAlpha = a;
    context.fillStyle = `hsla(${{h}},55%,96%,0.88)`;
    context.strokeStyle = `hsla(${{h}},70%,36%,0.42)`;
    context.lineWidth = 0.75;

    drawRoundedRect(context, x - s / 2, y - s / 2, s, s, s * 0.11);
    context.fill();
    context.stroke();

    const hh = s * 0.27;
    context.fillStyle = `hsla(${{h}},78%,33%,0.95)`;
    drawRoundedRect(context, x - s / 2, y - s / 2, s, hh, {{tl: s * 0.11, tr: s * 0.11, br: 0, bl: 0}});
    context.fill();

    context.strokeStyle = `hsla(${{h}},65%,36%,0.80)`;
    context.lineWidth = 0.85;
    const by = y - s / 2 - s * 0.07;

    [x - s * 0.17, x + s * 0.17].forEach((bx) => {{
      context.beginPath();
      context.moveTo(bx, by);
      context.lineTo(bx, by + s * 0.16);
      context.stroke();
    }});

    const gt = y - s / 2 + hh + s * 0.05;
    const cw = (s * 0.8) / 3;
    const ch = (s * 0.55) / 3;

    for (let r = 0; r < 3; r++) {{
      for (let c = 0; c < 3; c++) {{
        const hi = (r === 0 && c === 2);
        context.globalAlpha = a * (hi ? 1 : 0.65);
        context.fillStyle = hi
          ? `hsla(${{h}},78%,38%,0.98)`
          : `hsla(${{h}},62%,78%,0.95)`;
        context.beginPath();
        context.arc(
          x - s * 0.4 + c * cw + cw / 2,
          gt + r * ch + ch / 2,
          s * 0.038,
          0,
          Math.PI * 2
        );
        context.fill();
      }}
    }}

    context.restore();
  }}

  function tick() {{
    ctx.clearRect(0, 0, W(), H());
    for (const c of cals) {{
      ctx.save();
      ctx.translate(c.x, c.y);
      ctx.rotate(c.rot);
      drawCal(ctx, 0, 0, c.s, c.a, c.hue);
      ctx.restore();

      c.y -= c.spd;
      c.x += c.drft;
      c.rot += c.rspd;

      if (c.y < -c.s * 2) {{
        const n = mkCal();
        c.x = n.x;
        c.y = H() + n.s;
        c.s = n.s;
        c.spd = n.spd;
        c.drft = n.drft;
        c.rot = n.rot;
        c.rspd = n.rspd;
        c.a = n.a;
        c.hue = n.hue;
      }}
    }}
    requestAnimationFrame(tick);
  }}

  tick();

  const pl = document.getElementById('pl');
  for (let i = 0; i < 12; i++) {{
    const p = document.createElement('div');
    p.className = 'pt';
    const sz = 2 + Math.random() * 3.5;
    p.style.width = `${{sz}}px`;
    p.style.height = `${{sz}}px`;
    p.style.left = `${{5 + Math.random() * 90}}%`;
    p.style.bottom = `${{Math.random() * 12}}%`;
    p.style.animationDuration = `${{8 + Math.random() * 9}}s`;
    p.style.animationDelay = `${{Math.random() * 7}}s`;
    p.style.opacity = `${{0.08 + Math.random() * 0.22}}`;
    pl.appendChild(p);
  }}

  const pct = document.getElementById('pct');
  const s1 = document.getElementById('s1');
  const s2 = document.getElementById('s2');
  const s3 = document.getElementById('s3');
  const startT = Date.now() + 2000;
  const dur = 4000;

  function animPct() {{
    const t = Math.min((Date.now() - startT) / dur, 1);

    let e;
    if (t < 0.55) {{
      e = (t / 0.55) * 0.68;
    }} else if (t < 0.85) {{
      e = 0.68 + ((t - 0.55) / 0.3) * 0.22;
    }} else {{
      e = 0.9 + ((t - 0.85) / 0.15) * 0.1;
    }}

    const p = Math.round(e * 100);

    if (pct) pct.textContent = p + '%';
    if (p >= 30 && s1) s1.style.color = '#1976d2';
    if (p >= 65 && s2) s2.style.color = '#1976d2';
    if (p >= 95 && s3) s3.style.color = '#1976d2';

    if (p < 100) {{
      requestAnimationFrame(animPct);
    }} else if (pct) {{
      pct.textContent = '100%';
    }}
  }}

  setTimeout(animPct, 2000);

  const follower = document.getElementById('pixelFollower');
  let mx = window.innerWidth / 2;
  let my = window.innerHeight / 2;
  let fx = mx;
  let fy = my;

  window.addEventListener('mousemove', (e) => {{
    mx = e.clientX;
    my = e.clientY;
    createSparkBurst(e.clientX, e.clientY);
  }});

  function animateFollower() {{
    fx += (mx - fx) * 0.18;
    fy += (my - fy) * 0.18;
    if (follower) {{
      follower.style.left = fx + 'px';
      follower.style.top = fy + 'px';
    }}
    requestAnimationFrame(animateFollower);
  }}
  animateFollower();

  const sparkLayer = document.getElementById('sparkLayer');
  let lastSparkTime = 0;

  function createSparkBurst(x, y) {{
    const now = Date.now();
    if (now - lastSparkTime < 42) return;
    lastSparkTime = now;

    const count = 2;

    for (let i = 0; i < count; i++) {{
      const spark = document.createElement('div');
      spark.className = 'spark';

      const dx = (Math.random() - 0.5) * 26 + 'px';
      const dy = (Math.random() - 0.5) * 26 + 'px';

      spark.style.left = (x + (Math.random() - 0.5) * 10) + 'px';
      spark.style.top = (y + (Math.random() - 0.5) * 10) + 'px';
      spark.style.setProperty('--dx', dx);
      spark.style.setProperty('--dy', dy);
      spark.style.transform = `rotate(${{Math.random() * 45}}deg)`;

      sparkLayer.appendChild(spark);

      setTimeout(() => {{
        spark.remove();
      }}, 620);
    }}
  }}

  const hoverZone = document.querySelector('.title-hover-zone');
  if (hoverZone) {{
    hoverZone.addEventListener('mousemove', (e) => {{
      const rect = hoverZone.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
      const y = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
      hoverZone.style.boxShadow =
        `${{-x * 6}}px ${{-y * 6}}px 18px rgba(25,118,210,0.07),
         ${{x * 3}}px ${{y * 4}}px 10px rgba(77,163,255,0.08)`;
    }});

    hoverZone.addEventListener('mouseleave', () => {{
      hoverZone.style.boxShadow =
        '0 10px 28px rgba(25,118,210,0.08), 0 2px 10px rgba(25,118,210,0.06)';
    }});
  }}

  setTimeout(function() {{
    window.location.href = "{REDIRECT_URL}";
  }}, {DELAY_MS});
}})();
</script>
</body>
</html>
"""

components.html(html_code, height=820, scrolling=True)

time.sleep(DELAY_MS / 1000)
st.switch_page("pages/dashboard.py")
