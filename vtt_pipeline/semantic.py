from sklearn.metrics.pairwise import cosine_similarity
from .models import Cue
from .constants import SEMANTIC_DEDUP_THRESHOLD, TOPIC_SHIFT_THRESHOLD, DISCOURSE_MARKERS

def generate_embeddings(cues: list[Cue], embedder) -> list:
    """Generate vector embeddings for each cue's text."""
    texts = [cue.text for cue in cues]
    return embedder.encode(texts)

def deduplicate_semantics(cues: list[Cue], embeddings: list) -> tuple[list[Cue], list]:
    """Remove conceptually identical adjacent paragraphs."""
    concept_cues = []
    concept_embeddings = []
    
    for i, (cue, emb) in enumerate(zip(cues, embeddings)):
        if i == 0:
            concept_cues.append(cue)
            concept_embeddings.append(emb)
            continue
            
        sim = cosine_similarity([emb], [concept_embeddings[-1]])[0][0]
        if sim < SEMANTIC_DEDUP_THRESHOLD:
            concept_cues.append(cue)
            concept_embeddings.append(emb)
            
    return concept_cues, concept_embeddings

def detect_shifts(concept_cues: list[Cue], concept_embeddings: list) -> list[int]:
    """Identify indices where the topic shifts."""
    boundaries = [0]
    
    for i in range(1, len(concept_cues)):
        sim = cosine_similarity([concept_embeddings[i]], [concept_embeddings[i-1]])[0][0]
        
        is_new_topic = sim < TOPIC_SHIFT_THRESHOLD
        has_marker = any(concept_cues[i].text.lower().startswith(dm) for dm in DISCOURSE_MARKERS)
        
        if is_new_topic or has_marker:
            boundaries.append(i)
            
    return boundaries

def perform_semantic_analysis(cues: list[Cue], embedder) -> tuple[list[int], list[Cue]]:
    """Stage 3: Embeddings, semantic dedup, and shift detection."""
    if not cues:
        return [], []
        
    embeddings = generate_embeddings(cues, embedder)
    concept_cues, concept_embeddings = deduplicate_semantics(cues, embeddings)
    boundaries = detect_shifts(concept_cues, concept_embeddings)
    
    return boundaries, concept_cues
