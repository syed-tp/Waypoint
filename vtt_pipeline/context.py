from .models import Cue

def build_representative_context(concept_cues: list[Cue], boundaries: list[int]) -> list[dict]:
    """Stage 4: Take the first few cues around each boundary as representative context."""
    final_output = []
    
    for idx, bound_idx in enumerate(boundaries):
        start_cue = concept_cues[bound_idx]
        timestamp = start_cue.start
        
        end_idx = boundaries[idx+1] if idx + 1 < len(boundaries) else len(concept_cues)
        # Take the first 3 concept blocks for the topic
        chunk_cues = concept_cues[bound_idx : min(bound_idx + 3, end_idx)]
        
        context_text = " ".join([c.text for c in chunk_cues])
        
        final_output.append({
            "timestamp": timestamp,
            "context": context_text
        })
        
    return final_output
