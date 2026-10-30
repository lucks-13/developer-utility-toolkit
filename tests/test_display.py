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
    assert "Basic Information" in captured.out
    assert "Statistics" in captured.out
    assert "Repository Details" in captured.out
    assert "cpython" in captured.out
    assert "python" in captured.out
    assert "Stars" in captured.out
    assert "100" in captured.out
    assert "MIT" in captured.out

def test_display_repo_no_data(capsys):
    display_repo(None)
    captured = capsys.readouterr()
    assert "No Data." in captured.out