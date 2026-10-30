# Developer Utility Toolkit
Hello everyone! this is my third project and day 4 of my journey.

i dont know why the .exe file is not working right now which i will solve that issue soon

kindly support me along my jouney

# What my project does.
A Python command line interface tool that interacts with Github API to fetch repo, user info, compare repo, search for repo and export results.

# Why I made this project.
After building two project, i just wanted to explore with external api so i just thought a cli to interact with github repo like a small improvement from existing cli

# How to run this project.

```
git clone https://github.com/lucks-13/developer-utility-toolkit.git
```
```
python main.py
```

## Available commands.

1. Get repo Info.
```
python main.py repo python cpython
```
2. Get github user Info.
```
python main.py user torvalds
```
3. Compare two repo.
```
python main.py compare python cpython psf requests
```
4. Search repo.
```
python main.py search python
```
5. search by programming language
```
python main.py search django --language Python
```
6. Export results
```
python main.py repo python cpython --export json
```
```
python main.py search python cpython --export csv
```

All the exported file will be saved inside the output folder.

# What i learned.
* working with REST API
* sending HTTP request using the requests library
* receiving response as json file and interacting with it
* building cli using argparse

# Ai Disclosure

I used chatgpt as my learning assistant to understand concept, improve my code and logical thinking and to troubleshoot errors, ai guided me to build this project and explicitly told to help me only when i got stuck. 95 to 99 % of the code is Human coding. the ai just gave me instruction when i got struck.