import streamlit as st
from groq import Groq

# ── Groq Client ───────────────────────────────────────────────────────────────
client = Groq(api_key=st.secrets["GROQ_API_CHATBOT"])

# ── System Context ────────────────────────────────────────────────────────────
SYSTEM_CONTEXT = (
    """
You are the professional AI assistant representing Shivam Verma on his portfolio. Always respond in English unless the user explicitly writes in Hindi — in that case, use Hinglish. Be mature, composed, and articulate. Sound like a real professional assistant, not a chatbot. No filler phrases, no excessive emojis, no robotic sign-offs. Use emojis sparingly and only when naturally fitting. Be concise — 2–4 sentences for simple answers. Use Markdown formatting: **bold** for key terms, bullet lists for multiple items, ### headings only for structured multi-part answers.

CORE RULES:
- You are Shivam's ASSISTANT, not Shivam himself. Clarify this if asked who you are.
- Reveal links/details only when relevant or explicitly asked — never dump everything at once.
- If a question is in Hindi, reply in Hinglish (Hindi + English mix).
- For anything outside your context: "I'm not aware of that — feel free to ask Shivam directly!"
- For anything only Shivam should answer personally: "Ask Shivam directly for this one!"
- Use the link emoji when sharing links. Make all links clickable Markdown.
- Do NOT proactively share: gym stats, YouTube channel, chess ID, physical stats — only reveal if asked.
- NEVER dump all links or info at once.

WHO IS SHIVAM:
- Full Name: Shivam Verma
- 3rd year B.Tech CSE student at MSIT (Maharaja Surajmal Institute of Technology), GGSIPU, New Delhi.
  Currently in 6th Semester. Expected graduation: August 2027. GPA: 8.66/10
- Lives in Paschim Vihar, West Delhi, India.
- Roles: Social Media & Content Lead @ GDG on Campus MSIT | Project Administrator @ GSSoC | Freelancer | Open-Source Contributor
- Hackathons: Competed in 6+ hackathons — 1 win, 2 top-5 placements.
  Secured 3rd place at HackWithMAIT 6.0 (2025) by Microsoft & MAIT, among 200+ teams.
- Mentored 30+ students at BuildUp Ideathon (organized by GDG MSIT, Geekroom MSIT, ISTE MSIT).

EXPERIENCE:
1. IT Intern Trainee — Airports Authority of India (AAI), Regional HQ, New Delhi (Jan 2026 - Feb 2026)
   - Selected for 4-week IT operations training at AAI Regional HQ.
   - Led development & deployment of AERISK predictive maintenance platform (ML + FastAPI + React).

2. Project Administrator — GirlScript Summer of Code / GSSoC (July 2025 - Nov 2025)
   - Managed open-source project with 50+ contributors, reviewed 100+ PRs, reduced bug reports by 60%.
   - Improved onboarding efficiency by 40%.

3. Social Media & Content Lead — Google Developer Groups on Campus, MSIT (Oct 2024 - Present)
   - Directed social media strategy for 2,000+ member developer community.
   - Drove 150% engagement growth; expanded network by 200+ industry connections.

4. Open Source Contributor — GSSoC (May 2024 - Aug 2024)
   - Contributed to 5+ open-source projects (UI/UX focus), 100% PR approval rate.

CONTACT:
- Primary Email (preferred): sv35215@gmail.com -> [sv35215@gmail.com](mailto:sv35215@gmail.com)
- Secondary Email: shivam.verma256@outlook.com -> [shivam.verma256@outlook.com](mailto:shivam.verma256@outlook.com)
- Discord: [shivamm-verma](https://discord.com/@shivamm-verma) (prefers email over Discord)
- Phone: Ask Shivam directly.
- For pricing/project timelines: reach out via email — depends on scope.

SOCIAL HANDLES:
- GitHub: [github.com/shivamm-verma](https://github.com/shivamm-verma)
- LinkedIn: [linkedin.com/in/shivamm-verma](https://www.linkedin.com/in/shivam-verma-332710237/)
- Twitter/X: [@shivamm_verm](https://x.com/shivamm_verm)
- Portfolio: [shivamm-vermaportfolio.vercel.app](https://shivamm-vermaportfolio.vercel.app)
- GitHub Sponsors: [github.com/sponsors/shivamm-verma](https://github.com/sponsors/shivamm-verma)
- PayPal: [paypal.me/shivammvermaa](https://www.paypal.com/paypalme/shivammvermaa)

TECHNICAL SKILLS:
- Languages: Python, C++, JavaScript, Java, SQL, C, Go
- Frameworks & Libraries: React.js, Next.js, Node.js, Express.js, FastAPI, TensorFlow, Scikit-learn, Streamlit
- Databases & Tools: MongoDB, Redis, Docker, Git, GitHub, GitHub Actions
- Web: Full-Stack Dev, RESTful APIs, MERN Stack, Tailwind CSS, Responsive Design
- ML/AI: Deep Learning, LSTM Networks, Random Forest, Predictive Analytics, Feature Engineering, Model Deployment
- Cloud & DevOps: Vercel, Render, CI/CD Pipelines, Cloud Deployment
- Video Editing: DaVinci Resolve (solid level), CapCut, Canva — also does voiceovers.
  Work samples: [Shivam's Video Editing Drive](https://drive.google.com/drive/folders/1Ci85K0yqmFaTwASd-VTgcC5OAgFX9X2N?usp=sharing)
- Currently learning: Go, DSA with C++, AI/ML deepening
- Freelancing: Open to web dev, video editing, and related work. Flexible. Reach out to confirm availability.

PROJECTS:
1. AERISK - Aviation Risk Analysis System -> [risk-analysis-fault-prediction.vercel.app](https://risk-analysis-fault-prediction.vercel.app)
   - Predictive maintenance for aircraft fault detection using LSTM + Random Forest. 92% accuracy.
   - FastAPI backend + React frontend. Automated CSV pipeline, feature engineering, real-time risk dashboard.
   - Built for Airports Authority of India.

2. AbyssAI - Marine Biodiversity Detection Platform -> [abyss-ai.vercel.app](https://abyss-ai.vercel.app)
   - AI platform for marine eDNA analysis using deep learning + K-Means Clustering. 85% better detection.
   - Won 3rd place at HackWithMAIT 6.0 (Microsoft & MAIT) among 200+ teams.

3. MyAI ChatBot - Conversational AI Assistant -> [github.com/shivamm-verma](https://github.com/shivamm-verma)
   - This very bot! Built with Streamlit + Llama 3.3 70B via Groq API. 92% response accuracy.

PRIVATE (reveal ONLY if explicitly asked):
- YouTube: [More of Shivam](https://www.youtube.com/@shivamm-) — talks coding, editing, tech. Just started, ~20 subs. Only mention if asked about hobbies or YouTube.
- Gym PRs (bodybuilding, not powerlifting): Bench 65kg/143lbs | Deadlift 130kg/287lbs | Squat 80kg/176lbs. Only share if asked.
- Physical: 6ft, 69kg. Do NOT mention BMI. Only share if asked.
- Chess: [chess.com/member/shivamisthatyou](https://www.chess.com/member/shivamisthatyou) — only share if asked about hobbies or chess.
- Hobbies: Content creation, gym, chess.
"""
    + st.secrets.get("SHIVAM_CONTEXT", "")
)


# ── API Call (BUG FIXED) ──────────────────────────────────────────────────────
# ROOT CAUSE FIX: Previously context + question were jammed into a single "user" message.
# This caused BadRequestError when context grew too large (no token budget left) and also
# confused the model about who is speaking. Now correctly split into system + user roles.
def get_completion(user_question: str) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": SYSTEM_CONTEXT},
            {"role": "user",   "content": user_question},
        ],
        model="llama-3.3-70b-versatile",   # upgraded from deprecated llama3-8b-8192
        max_tokens=1024,
        temperature=0.7,
    )
    return chat_completion.choices[0].message.content


# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Shivam Verma · AI Assistant",
    layout="centered",
    page_icon="🤖",
)

# ── Apple-style CSS ───────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --bg:        #000000;
    --surface:   #111111;
    --surface2:  #1c1c1e;
    --text:      #f5f5f7;
    --border:    rgba(255,255,255,0.08);
    --accent:    #0a84ff;
    --accent-glow: rgba(10,132,255,0.18);
    --muted:     #86868b;
    --radius:    16px;
    --radius-sm: 10px;
}

html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    -webkit-font-smoothing: antialiased;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2.5rem !important; max-width: 760px !important; }

/* ─── Hero ─── */
.hero-badge {
    display: inline-block;
    background: var(--accent-glow);
    border: 1px solid rgba(10,132,255,0.35);
    color: var(--accent);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 4px 13px;
    border-radius: 100px;
    margin-bottom: 18px;
}
.hero-title {
    font-size: clamp(30px, 5vw, 44px);
    font-weight: 700;
    letter-spacing: -0.03em;
    line-height: 1.1;
    color: var(--text);
    margin: 0 0 12px 0;
}
.hero-sub {
    font-size: 16px;
    color: var(--muted);
    line-height: 1.6;
    font-weight: 400;
    margin-bottom: 0;
}

/* ─── Pills ─── */
.pill-row { display: flex; flex-wrap: wrap; gap: 8px; margin: 20px 0 28px 0; }
.pill {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: 12px;
    font-weight: 500;
    padding: 5px 13px;
    border-radius: 100px;
}

/* ─── Divider ─── */
.divider { border: none; border-top: 1px solid var(--border); margin: 28px 0; }

/* ─── Chat Bubbles ─── */
.bubble-row {
    display: flex;
    margin: 6px 0;
    align-items: flex-end;
    gap: 10px;
    animation: fadeSlide 0.2s ease;
}
.user-row { justify-content: flex-end; }
.bot-row  { justify-content: flex-start; }

.bubble { max-width: 72%; word-wrap: break-word; font-size: 14.5px; line-height: 1.65; }

.user-bubble {
    background: var(--accent);
    color: #fff;
    padding: 10px 15px;
    border-radius: 18px 18px 4px 18px;
    font-weight: 450;
}
.bot-bubble {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 13px 16px;
    border-radius: 18px 18px 18px 4px;
    max-width: 76%;
    font-size: 14.5px;
    line-height: 1.7;
}
.bot-bubble p { margin: 0 0 7px !important; }
.bot-bubble p:last-child { margin-bottom: 0 !important; }
.bot-bubble h3 { font-size:14px !important; font-weight:600 !important; margin:10px 0 3px !important; color:var(--text) !important; }
.bot-bubble h3:first-child { margin-top:0 !important; }
.bot-bubble ul, .bot-bubble ol { margin: 5px 0 7px 16px !important; }
.bot-bubble li { margin-bottom: 3px !important; }
.bot-bubble a { color: var(--accent) !important; text-decoration: none !important; }
.bot-bubble a:hover { text-decoration: underline !important; }
.bot-bubble strong { font-weight: 600 !important; }
.bot-bubble code { background: rgba(255,255,255,0.07) !important; padding: 2px 6px !important; border-radius: 4px !important; font-size: 13px !important; }
.bot-avatar { font-size: 20px; flex-shrink: 0; }

/* ─── Form ─── */
[data-testid="stForm"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 10px 14px !important;
    margin-top: 14px !important;
}
[data-testid="stFormSubmitButton"] > button {
    background: var(--accent) !important;
    color: #fff !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 10px 14px !important;
    width: 100% !important;
    margin-top: 0 !important;
    transition: background 0.18s !important;
}
[data-testid="stFormSubmitButton"] > button:hover {
    background: #0071e3 !important;
    box-shadow: 0 4px 16px rgba(10,132,255,0.28) !important;
}

/* ─── Text Input ─── */
.stTextInput > div > div > input {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text) !important;
    font-size: 15px !important;
    padding: 12px 16px !important;
    transition: border-color 0.2s, box-shadow 0.2s;
    font-family: 'Inter', sans-serif !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px var(--accent-glow) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder { color: var(--muted) !important; }

/* ─── Button ─── */
.stButton > button {
    background: var(--accent) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 11px 28px !important;
    letter-spacing: 0.01em !important;
    transition: background 0.18s, transform 0.15s, box-shadow 0.18s !important;
    width: 100% !important;
    margin-top: 10px !important;
}
.stButton > button:hover {
    background: #0071e3 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 28px rgba(10,132,255,0.32) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ─── Response Card ─── */
.response-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 24px 26px;
    margin-top: 12px;
    animation: fadeSlide 0.3s ease;
    line-height: 1.75;
    font-size: 15px;
}
.response-label {
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 14px;
}

/* ─── Markdown inside response ─── */
.response-card h3 { font-size: 16px !important; font-weight: 600 !important; color: var(--text) !important; margin: 16px 0 6px !important; }
.response-card a  { color: var(--accent) !important; text-decoration: none !important; }
.response-card a:hover { text-decoration: underline !important; }
.response-card code {
    background: var(--surface2) !important;
    border-radius: 5px !important;
    padding: 2px 7px !important;
    font-size: 13px !important;
    color: #ff6b6b !important;
}
.response-card p { margin: 0 0 10px !important; }

/* ─── Animation ─── */
@keyframes fadeSlide {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ─── Spinner ─── */
.stSpinner > div { border-top-color: var(--accent) !important; }

/* ─── Alerts ─── */
.stAlert { border-radius: var(--radius-sm) !important; }

/* ─── Sidebar ─── */
section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }
section[data-testid="stSidebar"] img { border-radius: 14px !important; }
section[data-testid="stSidebar"] h3 {
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.07em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    margin: 16px 0 8px !important;
}

/* ─── Scrollbar ─── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 99px; }
</style>
""", unsafe_allow_html=True)

# ── Hero Section ──────────────────────────────────────────────────────────────
st.markdown('<div class="hero-badge">🤖 llama3-based Personal Assistant</div>', unsafe_allow_html=True)
st.markdown("<h1 class='hero-title'>Hey, I'm Shivam's Bot.</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='hero-sub'>Ask me anything about Shivam — his work, skills, projects, or how to hire him.</p>",
    unsafe_allow_html=True,
)
st.markdown("""
<div class="pill-row">
  <span class="pill">✈️ AAI Intern '26</span>
  <span class="pill">🏆 HackWithMAIT 3rd Place</span>
  <span class="pill">🌍 GSSoC Project Admin</span>
  <span class="pill">🎓 MSIT'27 · 8.66 GPA</span>
  <span class="pill">⚡ GDG MSIT</span>
  <span class="pill">🔗 Open Source</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Chat History State ─────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ── Render Chat Messages ───────────────────────────────────────────────────────
chat_container = st.container()
with chat_container:
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="bubble-row user-row">'
                f'<div class="bubble user-bubble">{msg["content"]}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown('<div class="bubble-row bot-row"><div class="bot-avatar">🤖</div><div class="bot-bubble">', unsafe_allow_html=True)
            st.markdown(msg["content"])
            st.markdown('</div></div>', unsafe_allow_html=True)

# ── Auto-scroll to bottom ──────────────────────────────────────────────────────
st.markdown("""
<script>
    window.scrollTo(0, document.body.scrollHeight);
</script>
""", unsafe_allow_html=True)

# ── Input Form (Enter key works) ───────────────────────────────────────────────
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_question = st.text_input(
            "msg",
            placeholder="Ask anything about Shivam...",
            label_visibility="collapsed",
        )
    with col2:
        clicked = st.form_submit_button("Send →")

# ── Handle send ────────────────────────────────────────────────────────────────
if clicked and user_question.strip():
    st.session_state.chat_history.append({"role": "user", "content": user_question})
    with st.spinner(""):
        try:
            messages = [{"role": "system", "content": SYSTEM_CONTEXT}]
            for m in st.session_state.chat_history:
                role = "assistant" if m["role"] == "bot" else "user"
                messages.append({"role": role, "content": m["content"]})
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama-3.3-70b-versatile",
                max_tokens=1024,
                temperature=0.7,
            )
            response = chat_completion.choices[0].message.content
            st.session_state.chat_history.append({"role": "bot", "content": response})
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.image("Images/shivam_pfp.jpg", use_container_width=True)
st.sidebar.markdown("## Shivam Verma")
st.sidebar.markdown(
    '<p style="font-size:13px;color:#86868b;margin-top:-10px;margin-bottom:4px;">B.Tech CSE · MSIT · 6th Sem · GGSIPU</p>',
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    '<p style="font-size:13px;color:#86868b;">GPA: 8.66 &nbsp;·&nbsp; Grad: 2027</p>',
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Socials")
st.sidebar.html("""
<div style="display:flex;flex-direction:column;gap:8px;padding-bottom:6px;">
  <a href="https://github.com/shivamm-verma"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://cdn.simpleicons.org/github/ffffff" height="18">GitHub
  </a>
  <a href="https://www.linkedin.com/in/shivam-verma-332710237/"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/3840px-LinkedIn_icon.svg.png" height="18">LinkedIn
  </a>
  <a href="https://shivamm-vermaportfolio.vercel.app"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    🌐&nbsp;Portfolio
  </a>
  <a href="https://leetcode.com/u/shivamm-verma/"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png" height="18">Leetcode
  </a>
  </a>
  <a href="https://x.com/shivamm_verm"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://cdn.simpleicons.org/x/ffffff" height="18">Twitter / X
  </a>
</div>
""")

st.sidebar.markdown("### Contact")
st.sidebar.html("""
<div style="display:flex;flex-direction:column;gap:8px;padding-bottom:6px;">
  <a href="mailto:sv35215@gmail.com"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://cdn.simpleicons.org/gmail/ea4335" height="18">
    Gmail&nbsp;<span style="color:#0a84ff;font-size:11px;margin-left:auto;font-weight:600;">Primary</span>
  </a>
  <a href="mailto:shivam.verma256@outlook.com"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Microsoft_Outlook_Icon_%282025%E2%80%93present%29.svg/960px-Microsoft_Outlook_Icon_%282025%E2%80%93present%29.svg.png" height="18">Outlook
  </a>
  <a href="mailto:sv35215@gmail.com"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://files.raycast.com/x100jg3t6b29czgpdggvf3smrl29" height="18">
    CalCom Meeting&nbsp;<span style="color:#0a84ff;font-size:11px;margin-left:auto;font-weight:600;">Instant</span>
  </a>
</div>
""")

st.sidebar.markdown("### Sponsor")
st.sidebar.html("""
<div style="display:flex;flex-direction:column;gap:8px;padding-bottom:6px;">
  <a href="https://github.com/sponsors/shivamm-verma"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://cdn.simpleicons.org/githubsponsors/ea4aaa" height="18">GitHub Sponsors
  </a>
  <a href="https://www.paypal.com/paypalme/shivammvermaa"
     style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;
            background:#1c1c1e;border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:9px 13px;font-size:13px;color:#f5f5f7;font-weight:500;">
    <img src="https://cdn.simpleicons.org/paypal/003087" height="18">PayPal
  </a>
</div>
""")

# st.sidebar.markdown("---")
# st.sidebar.markdown("### GitHub Stats")
# st.sidebar.markdown("""
# ![GitHub Stats](https://github-readme-stats.vercel.app/api?username=shivamm-verma&show=prs_merged,prs_merged_percentage&theme=dark&hide_border=true&bg_color=111111)

# ![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=shivamm-verma&layout=pie&theme=dark&hide_border=true&bg_color=111111)
# """)