#!/usr/bin/env python3
import sys
import typing


def transform_content(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed: list[str] = [f"{x}#" for x in lines]
    return "\n".join(transformed) + ("\n" if lines else "")


def save_archive(new_filename: str, content: str) -> None:
    print(f"Saving data to '{new_filename}'")
    file: typing.IO[str] | None = None
    try:
        file = open(new_filename, "w")
        file.write(content)
        print(f"Data saved in file '{new_filename}'")
    except OSError as e:
        print(f"[STDERR] Error opening file"
              f"'{new_filename}': {e}", file=sys.stderr, flush=True)
        print("Data not saved.")
    finally:
        if file is not None and not file.closed:
            file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print(
            "Usage: ft_stream_management.py <file>",
            file=sys.stderr, flush=True
        )
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None
    content: str = ""
    try:
        file = open(filename, "r")
        content = file.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
    except OSError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr, flush=True)
        return
    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{filename}' closed.")

    print("\nTransform data:")
    print("---\n")
    transformed: str = transform_content(content)
    print(transformed, end="" if transformed.endswith("\n") else "\n")
    print("\n---")

    print(
            "Enter new file name (or empty): ",
            end="", file=sys.stdout, flush=True
    )

    new_filename: str = sys.stdin.readline().strip()
    if not new_filename:
        print("Not saving data.")
    else:
        save_archive(new_filename, transformed)


if __name__ == "__main__":
    main()
