# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ContentCalendar
python
import argparse

def main():
    parser = argparse.ArgumentParser(description="ContentCalendar CLI")
    sub = parser.add_subparsers(dest="command")
    pub = sub.add_parser("publish", help="Publish a post")
    pub.add_argument("--title", required=True)
    pub.add_argument("--channel", required=True)
    pub.add_argument("--theme", required=True)
    pub.add_argument("--status", default="draft")
    pub.add_argument("--deadline", default=None)
    idea = sub.add_parser("idea", help="Add an idea")
    idea.add_argument("--text", required=True)
    idea.add_argument("--channel", default=None)
    idea.add_argument("--theme", default=None)
    idea.add_argument("--status", default="idea")
    status = sub.add_parser("status", help="Show status summary")
    status.add_argument("--channel", default=None)
    theme = sub.add_parser("theme", help="Show themes")
    theme.add_argument("--channel", default=None)
    args = parser.parse_args()
    if args.command == "publish":
        post = Post(args.title, args.channel, args.theme, args.status, args.deadline)
        post.save()
    elif args.command == "idea":
        idea = Idea(args.text, args.channel, args.theme, args.status)
        idea.save()
    elif args.command == "status":
        show_status(args.channel)
    elif args.command == "theme":
        show_themes(args.channel)

if __name__ == "__main__":
    main()
