def display_repo(data):
    if data is not None:
    print("\n=============================")
    print("     Github Repository       ")
    print("=============================")
    for key,value in data.items():
        print(f"{key} : {value}")
    else:
        print