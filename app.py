# import argparse
# from agent.agent import ChapterAgent

# def main():
#     parser = argparse.ArgumentParser(description="Generate YouTube Chapters from a VTT URL")
#     parser.add_argument("url", help="The HTTP URL of the VTT file")
#     parser.add_argument("--title", "-t", help="The title of the video to provide better context to the AI", default=None)
#     args = parser.parse_args()

#     print(f"Initializing AI Agent and VTT Pipeline for URL: {args.url}")
#     if args.title:
#         print(f"Using Video Title Context: '{args.title}'")
        
#     agent = ChapterAgent()
    
#     print("Processing VTT and analyzing topics...")
#     chapters_context = agent.run_pipeline(args.url, video_title=args.title)
    
#     print("\n--- FINAL YOUTUBE CHAPTERS ---")
#     for chapter in chapters_context.chapters:
#         print(f"[{chapter.start_time}] {chapter.title}")

# if __name__ == "__main__":
#     main()



