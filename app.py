import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

from config import (
    APP_TITLE,
    APP_SUBTITLE,
    PAGE_ICON,
    MODEL_NAME,
    APP_VERSION,
    MAX_CONTEXT_WINDOW
)

from prompts import PERSONALITIES

from utils import (
    initialize_session,
    add_user_message,
    add_ai_message,
    display_chat,
    clear_chat,
    update_statistics,
    build_conversation
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================================================
# INITIALIZE SESSION
# ==========================================================

initialize_session()
if "selected_personality" not in st.session_state:
    st.session_state.selected_personality = "Ethical Hacker"
# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("AI Multiverse")

    st.caption("Explore Multiple AI Personalities")

    

    st.divider()

    
    

    st.subheader("Session Statistics")

    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

    st.metric(
        "Characters",
        st.session_state.total_characters
    )

    st.metric(
        "Estimated Tokens",
        st.session_state.total_tokens
    )

    st.metric(
        "Context Window",
        f"{MAX_CONTEXT_WINDOW}"
    )

    st.divider()

    if st.button(
        "🗑 Clear Conversation",
        use_container_width=True
    ):
        clear_chat()
        st.rerun()

    

    st.divider()

  
    st.markdown(
    "<h4 style='text-align: center;'>Powered by Gemini</h4>",
    unsafe_allow_html=True
)

st.markdown("""
<style>

/* Main */

.block-container{

    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:3rem;
    padding-right:3rem;

}

/* Sidebar */

section[data-testid="stSidebar"]{

    border-right:1px solid rgba(120,120,120,.15);

}

/* Buttons */

.stButton button{

    width:100%;

    height:48px;

    border-radius:12px;

    font-weight:600;

    transition:.25s;

}

.stButton button:hover{

    transform:translateY(-2px);

}

/* Selectbox */

.stSelectbox > div{

    border-radius:12px;

}

/* Metrics */

[data-testid="stMetric"]{

    border:1px solid rgba(120,120,120,.15);

    border-radius:16px;

    padding:12px;

    box-shadow:0 6px 18px rgba(0,0,0,.05);

}

/* Chat */

[data-testid="stChatMessage"]{

    border-radius:16px;

    padding:10px;

}

/* Mobile */

@media (max-width:768px){

.block-container{

padding-left:1rem;
padding-right:1rem;

}

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

header_left, header_right = st.columns([6, 1])

with header_left:

    st.title(APP_TITLE)

    st.caption(APP_SUBTITLE)

with header_right:

    st.success("● Online")

st.markdown("---")

st.subheader("Choose Your AI Universe")

universes = [
    {
        "key": "Tech Guru",
        "title": "Tech Guru",
        "subtitle": "Programming & AI",
        "icon": "💠"
    },
    {
        "key": "Teacher",
        "title": "Teacher",
        "subtitle": "Step-by-Step Learning",
        "icon": "📘"
    },
    {
        "key": "Startup Mentor",
        "title": "Startup Mentor",
        "subtitle": "Business Strategy",
        "icon": "📊"
    },
    {
        "key": "Ethical Hacker",
        "title": "Ethical Hacker",
        "subtitle": "Cyber Security",
        "icon": "🛡️"
    },
    {
        "key": "Motivational Coach",
        "title": "Coach",
        "subtitle": "Growth Mindset",
        "icon": "🎯"
    },
    {
        "key": "Philosopher",
        "title": "Philosopher",
        "subtitle": "Critical Thinking",
        "icon": "🧠"
    },
    {
        "key": "Scientist",
        "title": "Scientist",
        "subtitle": "Evidence Based",
        "icon": "⚗️"
    },
    {
        "key": "Comedian",
        "title": "Comedian",
        "subtitle": "Humor & Fun",
        "icon": "✨"
    }
]

for row in range(0, len(universes), 4):

    cols = st.columns(4, gap="small")

    for col, universe in zip(cols, universes[row:row+4]):

        with col:

            active = (
                st.session_state.selected_personality
                == universe["key"]
            )

            with st.container(border=True):

                st.markdown(
                    f"""
<div style="text-align:center;padding:6px">

<div style="
font-size:34px;
margin-bottom:8px;">
{universe["icon"]}
</div>

<div style="
font-size:18px;
font-weight:700;">
{universe["title"]}
</div>

<div style="
font-size:13px;
color:#9ca3af;
margin-top:4px;
margin-bottom:10px;">
{universe["subtitle"]}
</div>

</div>
""",
                    unsafe_allow_html=True
                )

                label = "✓ Active" if active else "Activate"

                if st.button(
                    label,
                    key=universe["key"],
                    use_container_width=True,
                    disabled=active
                ):
                    st.session_state.selected_personality = universe["key"]
                    st.rerun()

UNIVERSE_INFO = {

    "Friendly AI Assistant": {
        "description": "Helpful & General Purpose AI",
        "skills": "Conversation • Writing • Coding • Research • Daily Tasks"
    },

    "Tech Guru": {
        "description": "Programming & Artificial Intelligence",
        "skills": "Python • Java • Web Development • AI • System Design"
    },

    "Teacher": {
        "description": "Step-by-Step Learning Assistant",
        "skills": "Concept Explanation • Examples • Practice Questions • Revision"
    },

    "Startup Mentor": {
        "description": "Business & Innovation Advisor",
        "skills": "Startup Ideas • Business Models • Marketing • Pitch Decks"
    },

    "Ethical Hacker": {
        "description": "Cybersecurity Specialist",
        "skills": "Network Security • Ethical Hacking • Secure Coding • Best Practices"
    },

    "Motivational Coach": {
        "description": "Personal Growth & Productivity",
        "skills": "Goal Setting • Confidence • Interview Motivation • Discipline"
    },

    "Philosopher": {
        "description": "Critical Thinker & Wise Guide",
        "skills": "Deep Discussions • Logic • Ethics • Life Advice"
    },

    "Scientist": {
        "description": "Research & Scientific Analysis",
        "skills": "Scientific Reasoning • Experiments • Data Analysis • Evidence-Based Answers"
    },

    "Comedian": {
        "description": "Humor & Entertainment",
        "skills": "Jokes • Funny Stories • Lighthearted Conversations • Wordplay"
    }

}
with st.container(border=True):

    st.subheader("Current Universe")

    info = UNIVERSE_INFO[st.session_state.selected_personality]

    st.markdown(f"### {st.session_state.selected_personality}")

    st.caption(info["description"])

    st.write(info["skills"])
st.divider()

# ==========================================================
# DISPLAY CHAT HISTORY
# ==========================================================

display_chat()
if not st.session_state.messages:
    st.info(
        "💡 Select an AI Universe and ask your first question to begin the conversation."
    )
# ==========================================================
# CHAT INPUT
# ==========================================================

user_prompt = st.chat_input(
    "Type your message here..."
)

# ==========================================================
# PROCESS USER INPUT
# ==========================================================

if user_prompt:

    # Store user message
    add_user_message(user_prompt)

    # Display user message immediately
    with st.chat_message("user"):
        st.write(user_prompt)

    # Build AI prompt

    conversation = build_conversation()

    ai_prompt = f"""
{PERSONALITIES[st.session_state.
selected_personality]}

The following is the conversation history.

{conversation}

Continue naturally while staying completely in character.

Assistant:
"""

    # Generate AI Response
    with st.chat_message("assistant"):

        with st.spinner("Connecting to the Multiverse..."):

            try:

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=ai_prompt
                )

                ai_response = response.text

            except Exception as e:

                ai_response = (
                    "Unable to connect to Gemini API.\n\n"
                    f"Error: {e}"
                )

        st.write(ai_response)

    # Save AI response
    add_ai_message(ai_response)

    # Update Statistics
    update_statistics(user_prompt)
    update_statistics(ai_response)

    # Refresh page to show updated sidebar statistics
    st.rerun()