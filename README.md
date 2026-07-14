# Waypoint — AI Video Chapter Generator

## Overview

Waypoint is a simple AI-powered tool that automatically generates chapters for long-form videos.

Provide a video title and a publicly accessible VTT (WebVTT) transcript URL, and Waypoint analyzes the transcript to identify topic transitions and produce well-structured chapters.

Each generated chapter includes:

- Section name
- Chapter title
- Start timestamp
- End timestamp
- Duration
- Thumbnail frame timestamp

The generated chapters make long videos easier to navigate, allowing viewers to jump directly to the topics they are interested in.

---

## Why Waypoint?

Educational lectures, webinars, and training videos are often an hour or longer. Manually creating chapters requires watching the entire video and noting where topics change, making it a repetitive and time-consuming task.

Waypoint automates this process in minutes, producing consistent, meaningful chapters without manual effort.

---

## How It Works

The user provides:

- Video title
- Public VTT transcript URL
- (Optional) Preferred number of chapters

Waypoint analyzes the transcript, detects topic changes, and generates a structured list of chapters.

---

## Output

For every chapter, Waypoint returns:

- Section
- Title
- Start time
- End time
- Duration
- Frame timestamp (for thumbnail extraction)

The output can be used directly by video players to display a navigable chapter list.