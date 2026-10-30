from toolkit.compare import compare_repos

def test_compare_repos_success():
    repo1 = {
        "Repository" : "cpython",
        "Owner" : "python",
        "Language" : "Python",
        "Stars" : 100,
        "Forks" : 20,
        "Watchers" : 100,
        "Open Issues" : 50,
        "License" : "MIT"
    }

    repo2 = {
        "Repository" : "requests",
        "Owner" : "psf",
        "Language" : "Python",
        "Stars" : 80,
        "Forks" : 10,
        "Watchers" : 80,
        "Open Issues" : 30,
        "License" : "Apache-2.0"
    }

    result = compare_repos(repo1, repo2)
    assert result["Repository"] == ["cpython", "requests"]
    assert result["Stars"] == [100, 80]
    assert result["Forks"] == [20, 10] 