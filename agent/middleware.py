from vtt_pipeline import VttPipeline

class TranscriptCompressionMiddleware:
    def __init__(self):
        self.pipeline = VttPipeline()

    def before_model(self, state):
            
        transcript_segments = self.pipeline.process(state["url"], is_url=True)

        state["transcript_segments"] = transcript_segments

        return state
