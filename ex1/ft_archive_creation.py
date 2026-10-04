#!/usr/bin/env python3
import sys
import typing


def transform_content(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed: list[str] = [f"{line}#" for line in lines]
    return "\n".join(transformed) + ("\n" if lines else "")


def save_archive(new_filename: str, content: str) -> None:
    print(f"Saving data to '{new_filename}'")
    file: typing.IO[str] | None = None
    try:
        file = open(new_filename, "w")
        file.write(content)
        print(f"Data saved in file '{new_filename}.'")
    except OSError as e:
        print(f"Error writing to file '{new_filename}': {e}")
    finally:
        if file is not None and not file.closed:
            file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Presentation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None
    try:
        file = open(filename, "r")
        content: str = file.read()
        print("---\n")
        print(content, end="" if content.endswith("\n") else "\n")
        print("\n---")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
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
    new_filename: str = input("Enter new file name (or empty): ").strip()
    if not new_filename:
        print("Not saving data.")
    else:
        save_archive(new_filename, transformed)


if __name__ == "__main__":
    main()
