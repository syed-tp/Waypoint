import os
import requests
import tempfile
import spacy
from sentence_transformers import SentenceTransformer

from .cleanup import clean_transcript
from .filtering import filter_low_info
from .semantic import perform_semantic_analysis
from .context import build_representative_context

class VttPipeline:
    def __init__(self, embedding_model="all-MiniLM-L6-v2", spacy_model="en_core_web_sm"):
        self.embedder = SentenceTransformer(embedding_model)
        self.nlp = spacy.load(spacy_model)

    def process(self, source: str, is_url: bool = False) -> list[dict]:
        vtt_file = source
        if is_url:
            vtt_file = self._download_vtt(source)
            
        cues = clean_transcript(vtt_file)
        filtered_cues = filter_low_info(cues, self.nlp)
        boundaries, concept_cues = perform_semantic_analysis(filtered_cues, self.embedder)
        final_context = build_representative_context(concept_cues, boundaries)
        
        if is_url and os.path.exists(vtt_file):
            os.remove(vtt_file)
            
        return final_context

    def _download_vtt(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        fd, temp_path = tempfile.mkstemp(suffix=".vtt")
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(response.text)
        return temp_path
