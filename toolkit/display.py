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
        "Name",
        "Bio",
        "Location",
        "Company"
    ]

    for field in b_fields:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print("\n------ Statistics ------")
    stats = [
        "Public Repos",
        "Followers",
        "Following"
    ]

    for field in stats:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print("\n------ Account Details ------")
    details = [
        "Account Type",
        "Created At",
        "Profile URL"
    ]

    for field in details:
        print(f"{field:<16} : {data.get(field, 'Not Available')}")

    print("\n=============================")

def display_comparison(data):
    if data is None:
        print("No comparison data is available.")
0