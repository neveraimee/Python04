#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    
    filename: str = sys.argv[1] 
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None
    try:
        file = open(filename, "r")
        content: str = file.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
