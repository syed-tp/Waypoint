from .models import Cue
from .constants import DISCOURSE_MARKERS
import spacy

def score_paragraph(cue: Cue, nlp, seen_nouns: set) -> None:
    """Assigns an information score to a single Cue."""
    doc = nlp(cue.text)
    score = 0
    
    text_lower = cue.text.lower()
    
    # + Discourse markers
    if any(dm in text_lower for dm in DISCOURSE_MARKERS):
        score += 2
        
    # + Technical terms / Nouns
    nouns = [token.text.lower() for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    if len(nouns) > 2:
        score += 1
        
    # + New concepts
    new_nouns = [n for n in nouns if n not in seen_nouns]
    if len(new_nouns) > 0:
        score += len(new_nouns)
        seen_nouns.update(new_nouns)
        
    # - Mostly fillers (short with no nouns)
    if len(doc) < 5 and len(nouns) == 0:
        score -= 2
        
    cue.score = score

def filter_low_info(cues: list[Cue], nlp) -> list[Cue]:
    """Stage 2: Score paragraphs and remove low-information ones."""
    filtered = []
    seen_nouns = set()
    
    for cue in cues:
        score_paragraph(cue, nlp, seen_nouns)
        if cue.score > 0:
            filtered.append(cue)
            
    return filtered
