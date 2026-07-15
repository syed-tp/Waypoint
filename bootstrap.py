import os
import sys
from dotenv import load_dotenv

def load_secrets():
    """
    Loads secrets into os.environ from two sources, in priority order:
    1. .env file (local development)
    2. st.secrets (Streamlit Cloud deployment)

    .env values take precedence — st.secrets will not overwrite them.
    After this call, the rest of the app can use os.getenv() everywhere.
    """
    load_dotenv()

    st = sys.modules.get("streamlit")
    if st is not None:
        try:
            loaded_keys = []
            for k, v in st.secrets.items():
                if k not in os.environ:  
                    val_str = str(v)
                    if isinstance(v, bool):
                        val_str = "true" if v else "false"
                    os.environ[k] = val_str
                    loaded_keys.append(k)
            
            if loaded_keys:
                print(f"[config] Loaded {len(loaded_keys)} secrets from Streamlit Cloud: {', '.join(loaded_keys)}", file=sys.stderr)
        except Exception as e:
            print(f"[config] st.secrets not loaded: {e}", file=sys.stderr)
