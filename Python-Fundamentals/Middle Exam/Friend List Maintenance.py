friends = input().split(', ')

counter = 0
lost_counter = 0

while True:
    command = input().split()

    if command[0] == 'Report':
        print(f"Blacklisted names: {counter}")
        print(f"Lost names: {lost_counter}")
        print(f"{' '.join(friends)}")
        break

    elif command[0] == 'Blacklist':
        name = command[1]

        if name in friends:
            friends = list(map(lambda x: x.replace(name, 'Blacklisted'), friends))
            print(f"{name} was blacklisted.")
            counter += 1
        else:
            print(f"{name} was not found.")

    elif command[0] == 'Error':
        index = int(command[1])

        if 0 <= index < len(friends):
            if friends[index] != 'Blacklisted':
                if friends[index] != 'Lost':
                    print(f"{friends[index]} was lost due to an error.")
                    friends = list(map(lambda x: x.replace(friends[index], 'Lost'), friends))
                    lost_counter += 1

    elif command[0] == 'Change':
        index = int(command[1])
        new_name = command[2]

        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name
