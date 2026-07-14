from dataclasses import dataclass

@dataclass
class Cue:
    start: str
    end: str
    text: str
    score: float = 0.0
