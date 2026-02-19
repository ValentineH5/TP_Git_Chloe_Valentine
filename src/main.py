"""Command-line interface for the student manager application."""

import shlex

from student_service import StudentService


def print_help() -> None:
    """Prints the list of available CLI commands.

    Returns:
        None.
    """
    print("Available commands:")
    print("  list")
    print("  add <id> <name>")
    print("  remove <id>")
    print("  help")


def main() -> None:
    """Runs the interactive command-line loop.

    Returns:
        None.
    """
    service: StudentService = StudentService()

    print("Student List Manager")
    print("Type 'help' to show commands.")

    while True:
        raw_command: str = input("> ").strip()
        if not raw_command:
            continue

        # Supports quoted names such as: add 10 "Alice Martin"
        parts: list[str] = shlex.split(raw_command)
        command: str = parts[0].lower()

        if command == "help":
            print_help()

        elif command == "list":
            service.print_list()

        elif command == "add":
            if len(parts) < 3:
                print("Usage: add <id> <name>")
                continue

            student_id: str = parts[1]
            # Everything after id is treated as part of the name.
            name: str = " ".join(parts[2:])

            if service.add_student(student_id, name):
                print(f"Student '{name}' added.")
            else:
                print(f"A student with id '{student_id}' already exists.")

        elif command == "remove":
            if len(parts) != 2:
                print("Usage: remove <id>")
                continue

            student_id: str = parts[1]
            if service.remove_student(student_id):
                print(f"Student with id '{student_id}' removed.")
            else:
                print(f"No student found with id '{student_id}'.")


        else:
            print("Unknown command.")
            print_help()


if __name__ == "__main__":
    main()