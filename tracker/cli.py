import argparse
from .tasks import add_task, list_tasks, mark_done, delete_task


def main():
    parser = argparse.ArgumentParser(
        description="CLI Productivity Tracker"
    )

    subparsers = parser.add_subparsers(dest="command")

    # add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    # list command
    subparsers.add_parser("list")

    # done command
    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)

    # delete command
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)

    elif args.command == "list":
        list_tasks()

    elif args.command == "done":
        mark_done(args.id)

    elif args.command == "delete":
        delete_task(args.id)

    else:
        print("No command given")


if __name__ == "__main__":
    main()
