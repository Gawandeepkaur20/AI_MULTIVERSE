import streamlit as st


def render_home():

   

    st.markdown("""
    <style>

    .block-container{
        padding-top:2rem;
        padding-left:3rem;
        padding-right:3rem;
    }

    .card{

        border:1px solid rgba(255,255,255,.12);
        border-radius:18px;
        padding:30px;
        background:#111827;
        text-align:center;
        height:250px;

    }

    .title{

        font-size:28px;
        font-weight:700;
        margin-bottom:10px;

    }

    .subtitle{

        color:#9ca3af;
        font-size:16px;

    }

    </style>
    """, unsafe_allow_html=True)

  
    with st.sidebar:

        st.title("🌌 AI Multiverse")

        st.caption("One Platform • Multiple AI Experiences")

        st.divider()

        st.subheader("Applications")

        if st.button(
            "🤖 Multiverse Chat",
            use_container_width=True
        ):

            st.session_state.page = "chat"
            st.rerun()

        if st.button(
            "🎨 Image Studio",
            use_container_width=True
        ):

            st.session_state.page = "image"
            st.rerun()

        st.divider()

        st.info(
            """
**Version 1.0**

Powered by

• Gemini

• Pollinations AI
"""
        )


    

  
    st.markdown(
        """
## Welcome

AI Multiverse combines multiple AI tools into one modern workspace.

Choose an application below to get started.
"""
    )

    st.write("")

   

    col1, col2 = st.columns(2)


    with col1:

        with st.container(border=True):

            st.markdown(
                "<h2 style='text-align:center;'>🤖 Multiverse Chat</h2>",
                unsafe_allow_html=True
            )

            st.write("")

            st.markdown(
                """
Interact with multiple AI personalities including:

- 👨‍💻 Tech Guru
- 👨‍🏫 Teacher
- 🛡 Ethical Hacker
- 🚀 Startup Mentor
- 🔬 Scientist

"""
            )

            st.write("")

            if st.button(
                "Launch Multiverse Chat",
                use_container_width=True
            ):

                st.session_state.page = "chat"
                st.rerun()



    with col2:

        with st.container(border=True):

            st.markdown(
                "<h2 style='text-align:center;'>🎨 Image Studio</h2>",
                unsafe_allow_html=True
            )

            st.write("")

            st.markdown(
                """
Create professional AI artwork with:

- ✨ Prompt Enhancement
- 🎭 Art Styles
- 📐 Multiple Resolutions
- 🖼 Instant Download
- ⚡ Pollinations AI
"""
            )

            st.write("")

            if st.button(
                "Launch Image Studio",
                use_container_width=True
            ):

                st.session_state.page = "image"
                st.rerun()

    st.write("")
    st.write("")

   

    st.subheader("🚀 Coming Soon")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info(
            """
🎙 Voice AI

Talk naturally with AI
"""
        )

    with c2:

        st.info(
            """
📄 PDF Assistant

Chat with documents
"""
        )

    with c3:

        st.info(
            """
👁 Vision AI

Analyze images
"""
        )