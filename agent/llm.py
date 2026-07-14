# agent/llm.py

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agent.models import ChapterList

load_dotenv()


class ChapterLLM:
    def __init__(
        self,
        model: str = "gemini-2.5-flash",
        temperature: float = 0.2,
    ):
        llm = ChatGoogleGenerativeAI(
            model=model,
            temperature=temperature,
        )

        self._llm = llm.with_structured_output(ChapterList)

    def generate(self, prompt: str) -> ChapterList:
        """
        Generate YouTube chapters from a prompt.

        Args:
            prompt: The fully constructed prompt containing the system prompt
                    and topic boundaries.

        Returns:
            ChapterList
        """
        return self._llm.invoke(prompt)