#!/usr/bin/env python3


def secure_archive(filename: str, mode: str = "r", content: str = "") -> tuple[bool, str]: 
    try:
        if mode in "r" or "read":
            with open(filename, "r") as file:
                data = file.read()
            return (True, data)
        elif mode in "w" or "write":
            with open(filename, "w") as file: 
                file.write(content) 
            return (True, "Content successfully written to file")
        else: 
            return (False, "Invalid mode specified") 
    except Exception as e:
        return (False, str(e)) 


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    result: tuple[bool, str] = secure_archive("/not/existing/file", "r")
    print(result)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/master.passwd", "r")
    print(result)

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "r")
    print(result)

    if result[0]: 
        print("\nUsing 'secure_archive' to write previous content to a new file:")
        write_result: tuple[bool, str] = secure_archive("vault_backup.txt", "w", result[1])
        print(write_result)


if __name__ == "__main__":
    main()