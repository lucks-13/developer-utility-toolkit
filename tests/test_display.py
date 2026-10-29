from toolkit.display import display_repo

def test_display_repo(capsys):
    data = {
        "Repository" : "cpython",
        "Owner" : "python",
        "Stars" : 100
    }

    display_repo(data)
    captured = capsys.readouterr()
    assert "Github Repository" in captured.out
    assert "Repository : cpython" in captured.out
    assert "Owner : python" in captured.out
    assert "Stars : 100" in captured.out

def test_display_repo_no_data(capsys):
    display_repo(None)
    captured = capsys.readouterr()
    assert "No Data." in captured.out