import re

pattern = r"\|(?P<boss>[A-Z]{4,})\|\:\#(?P<title>[A-Za-z]+ [A-Za-z]+)\#"

n = int(input())
for i in range(n):
    text = input()
    match = [i.groupdict() for i in re.finditer(pattern, text)]

    if match:
        for j in match:
            print(f"{j['boss']}, The {j['title']}")
            print(f">> Strength: {len(j['boss'])}")
            print(f">> Armor: {len(j['title'])}")
    else:
        print("Access denied!")
