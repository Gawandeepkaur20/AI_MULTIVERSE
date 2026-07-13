import streamlit as st

from config import (
    APP_TITLE,
    APP_SUBTITLE,
    MAX_CONTEXT_WINDOW,
    MODEL_NAME,
)

from utils import (
    initialize_session,
    clear_chat,
    display_chat,
    add_user_message,
    add_ai_message,
    update_statistics,
    build_conversation,
)
from prompts import PERSONALITIES



def render_chat(client):

    initialize_session()

    if "selected_personality" not in st.session_state:
        st.session_state.selected_personality = "Ethical Hacker"

   

    st.markdown("""
    <style>

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        padding-left:3rem;
        padding-right:3rem;
    }

    section[data-testid="stSidebar"]{
        border-right:1px solid rgba(120,120,120,.15);
    }

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

    .stSelectbox > div{
        border-radius:12px;
    }

    [data-testid="stMetric"]{
        border:1px solid rgba(120,120,120,.15);
        border-radius:16px;
        padding:12px;
        box-shadow:0 6px 18px rgba(0,0,0,.05);
    }

    [data-testid="stChatMessage"]{
        border-radius:16px;
        padding:10px;
    }

    @media (max-width:768px){

        .block-container{
            padding-left:1rem;
            padding-right:1rem;
        }

    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        st.title("🤖 Multiverse Chat")

        st.caption("Multiple AI Personalities")

        st.divider()

        st.subheader("Navigation")

        if st.button(
        "🏠 Home",
        use_container_width=True
        ):
           st.session_state.page = "home"
           st.rerun()

        if st.button(
        "🎨 Image Studio",
        use_container_width=True
        ):
           st.session_state.page = "image"
           st.rerun()

       

        

        st.divider()
        st.subheader("Response")

        st.session_state.response_length = st.select_slider(
        "Response Length",
    options=["Short", "Medium", "Long"],
    value=st.session_state.get("response_length", "Medium")
        )

        st.divider()
        
        

        with st.expander("Conversation History"):

            if not st.session_state.conversation_log:

               st.info("No conversation yet.")

            else:

               for msg in st.session_state.conversation_log:

                    if msg["role"] == "user":

                        st.markdown(f"👤 {msg['content']}")

                    else:

                        st.markdown(
                            f"🤖 {msg['personality']}"
                        )

                        st.write(msg["content"])
        st.divider()               
        st.subheader("Statistics")

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
        MAX_CONTEXT_WINDOW
        )

        st.divider()
                        
        if st.button(
        "🗑 Clear Conversation",
        use_container_width=True
        ):
           clear_chat()
           st.rerun()

        st.divider()

        st.info("Powered by Gemini 2.5")

  
   

    left, right = st.columns([6,1])

    with left:

        st.title(APP_TITLE)

        st.caption(APP_SUBTITLE)

    with right:

        st.success("● Online")

    st.divider()


    st.subheader("Choose Your AI Universe")

    universes = [

        {
            "key":"Tech Guru",
            "title":"Tech Guru",
            "subtitle":"Programming & AI",
            "icon":"💠"
        },

        {
            "key":"Teacher",
            "title":"Teacher",
            "subtitle":"Step-by-Step Learning",
            "icon":"📘"
        },

        {
            "key":"Startup Mentor",
            "title":"Startup Mentor",
            "subtitle":"Business Strategy",
            "icon":"📊"
        },

        {
            "key":"Ethical Hacker",
            "title":"Ethical Hacker",
            "subtitle":"Cyber Security",
            "icon":"🛡️"
        },

        {
            "key":"Motivational Coach",
            "title":"Coach",
            "subtitle":"Growth Mindset",
            "icon":"🎯"
        },

        {
            "key":"Philosopher",
            "title":"Philosopher",
            "subtitle":"Critical Thinking",
            "icon":"🧠"
        },

        {
            "key":"Scientist",
            "title":"Scientist",
            "subtitle":"Evidence Based",
            "icon":"⚗️"
        },

        {
            "key":"Comedian",
            "title":"Comedian",
            "subtitle":"Humor & Fun",
            "icon":"✨"
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

<div style="font-size:34px;margin-bottom:8px;">
{universe["icon"]}
</div>

<div style="font-size:18px;font-weight:700;">
{universe["title"]}
</div>

<div style="font-size:13px;color:#9ca3af;margin-top:4px;margin-bottom:10px;">
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
            "skills": "Goal Setting • Confidence • Discipline • Confidence Building"
        },

        "Philosopher": {
            "description": "Critical Thinker",
            "skills": "Logic • Ethics • Deep Thinking • Wisdom"
        },

        "Scientist": {
            "description": "Research & Scientific Analysis",
            "skills": "Evidence Based Answers • Experiments • Research"
        },

        "Comedian": {
            "description": "Humor & Entertainment",
            "skills": "Funny Replies • Jokes • Memes • Light Conversation"
        }

    }

    with st.container(border=True):

        st.subheader("Current Universe")

        info = UNIVERSE_INFO[
            st.session_state.selected_personality
        ]

        st.markdown(
            f"### {st.session_state.selected_personality}"
        )

        st.caption(info["description"])

        st.write(info["skills"])

    st.divider()

   

    display_chat()

    if not st.session_state.messages:

        st.info(
            "💡 Select an AI Universe and ask your first question to begin the conversation."
        )

   

    user_prompt = st.chat_input(
        "Type your message here..."
    )

    if not user_prompt:
        return

   

    add_user_message(user_prompt)
    
    

    with st.chat_message("user"):

        st.write(user_prompt)

   

    conversation = build_conversation()

    response_rules = {
    "Short": """
- Reply in ONLY 2-4 sentences.
- Maximum 80 words.
- Be concise.
""",

    "Medium": """
- Reply in 1-2 paragraphs.
- Maximum 180 words.
""",

    "Long": """
- Give a detailed explanation.
- Use headings or bullet points when appropriate.
- Up to 500 words.
"""
}

    ai_prompt = f"""
You MUST behave ONLY as the following personality.

{PERSONALITIES[st.session_state.selected_personality]}

STRICT RESPONSE RULES

{response_rules[st.session_state.response_length]}

Additional Rules

- Never say you are an AI.
- Never break character.
- Remember previous conversation.
- Continue naturally.

Conversation

{conversation}

Assistant:
"""
   

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
                    "Unable to connect.\n\n"
                    f"{e}"
                )

        st.write(ai_response)

    

    add_ai_message(ai_response)
    
  

    update_statistics(user_prompt)

    update_statistics(ai_response)

    st.rerun()                        
                        