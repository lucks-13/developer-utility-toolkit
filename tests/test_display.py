from toolkit.display import display_repo

def test_display_repo(capsys):
    data = {
        "Repository" : "cpython",
        "Owner" : "python",
        "Description" : "Python programming language",
        "Language" : "Python",
        "Stars" : 100,
        "Forks" : 20,
        "Watchers" : 100,
        "Open Issues" : 50,
        "Default Branch" : "main",
        "License" : "MIT",
        "Size (KB)" : 50000,
        "Topics" : "python, programming",
        "Archived" : False,
        "Is Fork" : False,
        "URL" : "https://github.com/python/cpython"
    }

    display_repo(data)
    captured = capsys.readouterr()
    assert "Github Repository" in captured.out
    assert
    assert "Repository : cpython" in captured.out
    assert "Owner : python" in captured.out
    assert "Stars : 100" in captured.out

def test_display_repo_no_data(capsys):
    display_repo(None)
    captured = capsys.readouterr()
    assert "No Data." in captured.out