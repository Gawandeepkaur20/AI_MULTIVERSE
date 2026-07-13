import streamlit as st
from io import BytesIO

from config import MODEL_NAME
from image_generator import generate_image


def render_image_studio(client):


    st.title("🎨 AI Image Studio")

    st.caption(
        "Create stunning AI-generated images using Pollinations AI."
    )

    st.divider()

    

    prompt = st.text_area(
        "Describe your image",
        height=180,
        placeholder="""
Example:

A futuristic cyberpunk city at sunset with flying vehicles,
neon skyscrapers,
volumetric lighting,
ultra realistic,
8K,
cinematic.
"""
    )

    

    characters = len(prompt)
    words = len(prompt.split())
    tokens = round(characters / 4)

   



    with st.sidebar:

        st.title("🎨 Image Studio")

        st.caption("AI Image Generation Workspace")

        st.divider()

        st.subheader("Navigation")

        if st.button(
            "🏠 Home",
            use_container_width=True
        ):
            st.session_state.page = "home"
            st.rerun()

        if st.button(
            "🤖 Chat AI",
            use_container_width=True
        ):
            st.session_state.page = "chat"
            st.rerun()

        st.divider()

        st.subheader("Image Engine")

        st.success("🟢 Pollinations AI")

        st.caption("Fast • Free • Unlimited")

        st.divider()

        style = st.selectbox(
            "🎨 Art Style",
            [
                "Realistic",
                "Anime",
                "Cyberpunk",
                "Fantasy",
                "Watercolor",
                "Oil Painting",
                "Pixar"
            ]
        )

        resolution = st.selectbox(
            "📐 Resolution",
            [
                "512 × 512",
                "768 × 768",
                "1024 × 1024"
            ]
        )

        st.divider()

        st.subheader("Prompt Statistics")

        st.metric(
            "Characters",
            characters
        )

        st.metric(
            "Words",
            words
        )

        st.metric(
            "Estimated Tokens",
            tokens
        )

        st.divider()

        if st.button(
            "🧹 Clear Prompt",
            use_container_width=True
        ):
            st.session_state.pop("enhanced_prompt", None)
            st.rerun()

        st.divider()

        st.info("Powered by Pollinations AI")


    col1, col2 = st.columns(2)

    with col1:

        enhance = st.button(
            "✨ Enhance Prompt",
            use_container_width=True
        )

    with col2:

        generate = st.button(
            "🎨 Generate Image",
            use_container_width=True
        )

  
    if enhance:

        if not prompt.strip():

            st.warning("Please enter a prompt first.")

        else:

            with st.spinner("Enhancing Prompt..."):

                improve = f"""
You are an expert AI prompt engineer.

Rewrite the prompt into a highly detailed image generation prompt.

Requirements:

- Keep original meaning
- Add cinematic lighting
- Add composition
- Add atmosphere
- Add camera angle
- Add rendering quality
- Return ONLY the improved prompt

Prompt:

{prompt}
"""

                try:

                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=improve
                    )

                    st.session_state.enhanced_prompt = response.text

                except Exception as e:

                    st.error(e)

  

    if "enhanced_prompt" in st.session_state:

        st.divider()

        st.subheader("✨ Enhanced Prompt")

        st.text_area(
            "",
            value=st.session_state.enhanced_prompt,
            height=180
        )

  

    if generate:

        final_prompt = st.session_state.get(
            "enhanced_prompt",
            prompt
        )

        if not final_prompt.strip():

            st.warning("Please enter a prompt.")

        else:

            with st.spinner("Generating Image..."):

           

                final_prompt = (
                    f"{final_prompt}, "
                    f"{style} style, "
                    f"{resolution} resolution"
                )

                image = generate_image(final_prompt)

                if image:

                    st.divider()

                    st.subheader("🖼 Generated Image")

                    st.image(
                        image,
                        use_container_width=True
                    )

                    buffer = BytesIO()

                    image.save(
                        buffer,
                        format="PNG"
                    )

                    st.download_button(
                        "⬇ Download Image",
                        buffer.getvalue(),
                        "generated_image.png",
                        "image/png",
                        use_container_width=True
                    )

                else:

                    st.error(
                        "Unable to generate image."
                    )