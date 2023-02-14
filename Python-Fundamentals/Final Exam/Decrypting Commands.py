string = input()
command = input()

while not command == "Finish":

    command = command.split()

    if command[0] == "Replace":
        curr_char, new_char = command[1], command[2]
        string = string.replace(curr_char, new_char)
        print(string)

    elif command[0] == "Cut":
        start, end = int(command[1]), int(command[2])
        if 0 <= start < len(string) and 0 <= end < len(string):
            replacement = string[start: end + 1]
            string = string.replace(replacement, "")
            print(string)
        else:
            print("Invalid indices!")

    elif command[0] == "Make":
        if command[1] == "Upper":
            string = string.upper()
        else:
            string = string.lower()
        print(string)
    elif command[0] == "Check":
        if command[1] in string:
            print(f"Message contains {command[1]}")
        else:
            print(f"Message doesn't contain {command[1]}")
    elif command[0] == "Sum":
        start, end = int(command[1]), int(command[2])
        res = 0
        if 0 <= start < len(string) and 0 <= end < len(string):
            substring = string[start: end + 1]
            for i in substring:
                res += ord(i)
            print(res)
        else:
            print("Invalid indices!")

    command = input()