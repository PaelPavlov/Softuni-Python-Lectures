license_plate_by_username = {}

count = int(input())
for _ in range(count):
    command_args = input().split()
    command = command_args[0]
    username = command_args[1]

    if command == 'register':
        license_plate = command_args[2]
        if username in license_plate_by_username:
            print(f"ERROR: already registered with plate number {license_plate_by_username[username]}")
        else:
            license_plate_by_username[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
    else:
        if username in license_plate_by_username:
            license_plate_by_username.pop(username)
            print(f'{username} unregistered successfully')
        else:
            print(f'ERROR: user {username} not found')
for username, license_plate in license_plate_by_username.items():
    print(f'{username} => {license_plate}')