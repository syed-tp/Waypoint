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
            ):
                url = st.session_state.get("composer_url", "").strip()
                parsed = urllib.parse.urlparse(url)
                
                if not url or not all([parsed.scheme, parsed.netloc]):
                    st.error("please provide the valid url")
                else:
                    from agent.models import Chapter, ChapterList
                    
                    dummy_data = ChapterList(chapters=[
                        Chapter(start_time="00:00:00", title="Introduction"),
                        Chapter(start_time="00:02:15", title="Setting up the Environment"),
                        Chapter(start_time="00:08:42", title="Core Concepts & Architecture"),
                        Chapter(start_time="00:15:30", title="Advanced Implementation"),
                        Chapter(start_time="00:28:10", title="Summary and Q&A")
                    ])
                    
                    st.success("Successfully generated chapters!")
                    
                    st.markdown("### Generated Chapters")
                    tab1, tab2 = st.tabs(["List", "JSON"])
                    
                    with tab1:
                        for chapter in dummy_data.chapters:
                            st.markdown(f"- **`{chapter.start_time}`** : {chapter.title}")
                            
                    with tab2:
                        import json
                        data_dict = dummy_data.model_dump() if hasattr(dummy_data, "model_dump") else dummy_data.dict()
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

