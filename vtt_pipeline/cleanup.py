import webvtt
import re
import difflib
from .models import Cue
from .constants import FILLERS, DEDUP_SIMILARITY_THRESHOLD

def parse_cues(vtt_path: str) -> list[Cue]:
    """Parse a VTT file into a list of Cue objects."""
    captions = webvtt.read(vtt_path)
    cues = []
    for cap in captions:
        text = cap.text.strip().replace('\n', ' ')
        if text:
            cues.append(Cue(start=cap.start, end=cap.end, text=text))
    return cues

def merge_into_sentences(cues: list[Cue]) -> list[Cue]:
    """Merge short fragments into sentence-level Cues."""
    merged = []
    current_text = []
    current_start = None
    
    for cue in cues:
        if current_start is None:
            current_start = cue.start
            
        current_text.append(cue.text)
        
        # Merge until end of sentence or long enough block
        if cue.text.endswith(('.', '?', '!')) or len(" ".join(current_text)) > 150:
            merged.append(Cue(
                start=current_start,
                end=cue.end,
                text=" ".join(current_text)
            ))
            current_text = []
            current_start = None
            
    # Add any remaining
    if current_text:
        merged.append(Cue(
            start=current_start,
            end=cues[-1].end if cues else current_start,
            text=" ".join(current_text)
        ))
        
    return merged

def strip_fillers(cues: list[Cue]) -> list[Cue]:
    """Remove non-grammatical fillers from cue text."""
    cleaned_cues = []
    for cue in cues:
        words = cue.text.split()
        cleaned_words = []
        for w in words:
            w_lower = re.sub(r'[^a-z]', '', w.lower())
            if w_lower not in FILLERS:
                cleaned_words.append(w)
        
        cleaned_text = " ".join(cleaned_words)
        if cleaned_text.strip():
            cue.text = cleaned_text.strip()
            cleaned_cues.append(cue)
            
    return cleaned_cues

def drop_repeats(cues: list[Cue]) -> list[Cue]:
    """Deduplicate back-to-back phrases that say the same thing."""
    deduped = []
    for i, cue in enumerate(cues):
        if i == 0:
            deduped.append(cue)
            continue
            
        similarity = difflib.SequenceMatcher(None, cue.text, deduped[-1].text).ratio()
        if similarity > DEDUP_SIMILARITY_THRESHOLD:
            # Conceptually identical repetition, update end time of previous
            deduped[-1].end = cue.end
        else:
            deduped.append(cue)
            
    return deduped

def clean_transcript(vtt_path: str) -> list[Cue]:
    """Stage 1: Execute all cleanup operations."""
    cues = parse_cues(vtt_path)
    cues = merge_into_sentences(cues)
    cues = strip_fillers(cues)
    cues = drop_repeats(cues)
    return cues
