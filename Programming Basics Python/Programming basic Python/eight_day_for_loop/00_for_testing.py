for attempt in range(1, 6):
    print(f"Attempting No {attempt}")
    print("Trying to connect to DB...")
    if attempt == 3:
        print("Success")
        break

