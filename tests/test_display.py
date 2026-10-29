from toolkit.display import display_repo

def test_display_repo(capsys):
    data = {
        "Repository" : "cpython",
        "Owner" : "python",
        "Stars" : 100
    }

    display_repo(data)
    captured = capsys.