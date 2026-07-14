from agent.llm import ChapterLLM
from agent.prompts import build_prompt
from agent.middleware import TranscriptCompressionMiddleware


class ChapterAgent:
    def __init__(self):
        self.llm = ChapterLLM()
        self.middleware = TranscriptCompressionMiddleware()
        
    def run_pipeline(self, url: str, video_title: str = None):
        state = {"url": url}
        state = self.middleware.before_model(state)
        
        transcript_segments = state["transcript_segments"]
        
        prompt = build_prompt(transcript_segments, video_title)
        return self.llm.generate(prompt)