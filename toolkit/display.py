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
        return

    repo1 = data["Repository"][0]
    repo2 = data["Repository"][1]
    print("\n==================================")
    print("     Github Repo Comparison       ")
    print("==================================")
    print(f"\n{'Metric':<18} {repo1:<20} {repo2:<20}")
    print("----------------------------------")
    for metric, values in data.items():
        if metric == "Repository":
            continue
        print(f"{metric:<18} {str(values[0]):<20} {str(values[1]):<20}")
    print("----------------------------------")
    stars = data["Stars"]
    if stars[0] > stars[1]:
        print(f"\nMost Stars : {repo1}")
    elif stars[1] > stars[0]:
        print(f"\nMost Stars : {repo2}")
    else:
        print("\nMost Stars : Both repo have equal stars.")

    forks = data["Forks"]
    if forks[0] > forks[1]:
        print(f"Most Forks : {repo1}")
    elif forks[1] > forks[0]:
        print(f"Most Forks : {repo2}")
    else:
        print("Most Forks : Both repo have equal forks.")
    print("----------------------------------")

def displa
    


