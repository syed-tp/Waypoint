import urllib.parse
import streamlit as st

COMPOSER_CSS = """
<style>
.st-key-composer_card,
.st-key-composer_card > div,
.st-key-composer_card > div > div {
    background-color: #ffffff !important;
    background: #ffffff !important;
}

.st-key-composer_card {
    border: 1px solid #E5E7EB !important;
    border-radius: 16px !important;
    box-shadow:
        0 1px 3px  rgba(0,0,0,.06),
        0 8px 24px rgba(0,0,0,.09) !important;
    padding: 1.5rem !important;
}

/* Center the generate button */
.st-key-composer_card [data-testid="stElementContainer"]:has([data-testid="stButton"]) {
    width: 100%;
    display: flex;
    justify-content: center;
}

.st-key-composer_card [data-testid="stButton"],
.st-key-composer_card [data-testid="stButton"] button {
    width: fit-content !important;
}

/* Style for disabled generate button */
.st-key-composer_card [data-testid="stButton"] button:disabled {
    background-color: #f3f4f6 !important;
    color: #9ca3af !important;
    border-color: #e5e7eb !important;
    opacity: 1 !important;
}
</style>
"""


def render_composer():
    st.markdown(COMPOSER_CSS, unsafe_allow_html=True)

    _, col, _ = st.columns([1, 2, 1])
    with col:
        with st.container(key="composer_card"):
            st.markdown("#### Generate chapters")

            st.text_input(
                "VTT file URL",
                placeholder="https://example.com/captions.vtt",
                key="composer_url",
            )

            st.text_input(
                "Video title (optional)",
                placeholder="My awesome tutorial",
                key="composer_title",
            )

            if st.button(
                ":material/auto_awesome: Generate chapters",
                type="primary",
                disabled=st.session_state.get("is_generating", False),
            ):
                url = st.session_state.get("composer_url", "").strip()
                parsed = urllib.parse.urlparse(url)
                
                if not url or not all([parsed.scheme, parsed.netloc]):
                    st.error("please provide the valid url")
                else:
                    st.session_state.is_generating = True
                    st.session_state.current_url = url
                    st.session_state.pop("generation_success", None)
                    st.session_state.pop("generation_error", None)
                    st.rerun()

            if st.session_state.get("is_generating", False):
                from agent.agent import ChapterAgent
                try:
                    with st.spinner("Analyzing transcript and generating chapters..."):
                        agent = ChapterAgent()
                        url = st.session_state.current_url
                        title = st.session_state.get("composer_title", "").strip()
                        chapters_data = agent.run_pipeline(url, video_title=title if title else None)
                        st.session_state.chapters_data = chapters_data
                        st.session_state.generation_success = True
                except Exception as e:
                    st.session_state.generation_error = str(e)
                finally:
                    st.session_state.is_generating = False
                    st.rerun()

            if st.session_state.get("generation_success"):
                chapters_data = st.session_state.chapters_data
                st.success("Successfully generated chapters!")
                
                st.markdown("### Generated Chapters")
                tab1, tab2 = st.tabs(["List", "JSON"])
                
                with tab1:
                    for chapter in chapters_data.chapters:
                        st.markdown(f"- **`{chapter.start_time}`** : {chapter.title}")
                        
                with tab2:
                    import json
                    data_dict = chapters_data.model_dump() if hasattr(chapters_data, "model_dump") else chapters_data.dict()
                    st.code(json.dumps(data_dict, indent=2), language="json")

                # Auto-scroll to the generated chapters
                import streamlit.components.v1 as components
                components.html(
                    """
                    <script>
                    const tabs = window.parent.document.querySelector('[data-testid="stTabs"]');
                    if (tabs) {
                        tabs.scrollIntoView({behavior: 'smooth', block: 'center'});
                    }
                    </script>
                    """,
                    height=0,
                )
            elif st.session_state.get("generation_error"):
                error_str = st.session_state.generation_error
                if "429" in error_str or "ResourceExhausted" in error_str:
                    st.error("Hold your horses! Rate limit exceeded. Please wait a moment and try again.")
                else:
                    st.error(f"Oops! Something went wrong while generating chapters:\n\n`{error_str}`")
