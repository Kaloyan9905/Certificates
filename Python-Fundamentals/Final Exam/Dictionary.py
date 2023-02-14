text = input().split(" | ")
my_dict = {}

for line in text:
    word, description = line.split(": ")
    if word not in my_dict:
        my_dict[word] = []
    my_dict[word].append(description)

words = input().split(" | ")
command = input()

if command == "Test":
    for word in words:
        if word in my_dict:
            print(f"{word}:")
            for value in my_dict[word]:
                print(f" -{value}")
else:
    for key in my_dict:
        print(key, end=" ")
