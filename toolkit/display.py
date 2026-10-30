def display_repo(data):
    if data is None:
        print("No Data.")
        return
    print("\n=============================")
    print("     Github Repository       ")
    print("=============================")
    print("\n------ Basic Information ------")
    b_fields = [
        "Repository",
        "Owner",
        "Description",
        "Language"
    ]

    for field in b_fields:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print("\n------ Statistics ------")
    stats = [
        "Stars",
        "Forks",
        "Watchers",
        "Open Issues"
    ]

    for field in stats:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print("\n------ Repo Details ------")
    details = [
        "Default Branch",
        "License",
        "Size (KB)",
        "Topics",
        "Archived",
        "Is Fork"
    ]

    for field in details:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print(f"\n{'URL' :<16} : {data.get('URL','Not Available')}")
    print("\n=============================")

def display_user(data):
    if data is None:
        print("No Data.")
        return
    print("\n=============================")
    print("     Github User Profile       ")
    print("=============================")
    print("\n------ Basic Information ------")
    b_fields = [
        "Username",
        "Owner",
        "Description",
        "Language"
    ]

    for field in b_fields:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print("\n------ Statistics ------")
    stats = [
        "Stars",
        "Forks",
        "Watchers",
        "Open Issues"
    ]

    for field in stats:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print("\n------ Repo Details ------")
    details = [
        "Default Branch",
        "License",
        "Size (KB)",
        "Topics",
        "Archived",
        "Is Fork"
    ]

    for field in details:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print(f"\n{'URL' :<16} : {data.get('URL','Not Available')}")
    print("\n=============================")
