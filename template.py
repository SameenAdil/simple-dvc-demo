import os
#os.path.join

dirs = [
    os.path.join("data", "raw"),      #data/raw,
    os.path.join("data","processed"),
    "notebook",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:  #with open("example.py", "w") as file:
        pass


files = [       #these files not push on github 
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"),
]

for file_ in files:
    #os.makedirs(file_, exist_ok=True)
    with open(file_, "w") as f:
        pass