from pydantic import BaseModel, Field


class Chapter(BaseModel):
    title: str = Field(description="A concise, descriptive title for the chapter")
    start_time: str = Field(description="The exact start timestamp (e.g. 00:15:00)")


class ChapterList(BaseModel):
    chapters: list[Chapter]