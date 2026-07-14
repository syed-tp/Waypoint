from langchain_core.messages import SystemMessage, HumanMessage
from .constants import SYSTEM_PROMPT


def build_prompt(transcript_segments: list[dict], video_title: str = None) -> list:
    """
    Combines the SYSTEM_PROMPT and the highly-compressed transcript_segments 
    into a format that LangChain can send to LLM.
    """
    context_lines = []
    for segment in transcript_segments:
        context_lines.append(f"Timestamp: {segment['timestamp']}\nContext: {segment['context']}\n")
    
    formatted_context = "\n".join(context_lines)
    
    # Dynamically calculate the ideal number of chapters based on video length
    target_chapters = 8 # Default
    if transcript_segments:
        last_timestamp = transcript_segments[-1]['timestamp']
        # Format is usually HH:MM:SS or HH:MM:SS.mmm
        time_parts = last_timestamp.split('.')[0].split(':')
        if len(time_parts) >= 2:
            try:
                # Calculate total minutes (Hours * 60 + Minutes)
                hours = int(time_parts[0]) if len(time_parts) == 3 else 0
                minutes = int(time_parts[1]) if len(time_parts) == 3 else int(time_parts[0])
                total_minutes = (hours * 60) + minutes
                
                # Rule of thumb: 1 chapter every ~10 minutes, min 5, max 25
                target_chapters = max(5, min(25, total_minutes // 10))
            except ValueError:
                pass

    human_text = ""
    if video_title:
        human_text += f"Video Title: {video_title}\n\n"
        
    human_text += f"CRITICAL INSTRUCTION: Based on the video length, you must aggressively filter the timestamps down and output exactly {target_chapters} to {target_chapters + 3} major chapters. Do NOT output more than {target_chapters + 3} chapters.\n\n"
    human_text += f"Here are the Topic Boundaries. Group them and generate the chapters:\n\n{formatted_context}"

    return [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=human_text)
    ]
