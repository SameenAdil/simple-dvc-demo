create env
```bash
python -m virtualenv wineq 
```

activate env   in git bash
```bash
source wineq/Scripts/activate
 or 
. wineq/Scripts/activate
```

create requirements.txt file and install req
```bash
pip install -r requirements.txt
```
download the data from 

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

```bash
git init
```
```bash 
dvc init
```
```bash
dvc add data_given/winequality.csv
```
use (dvc push) when u add remote loc but here i didnt add any location. That's why we would not use dvc push



```bash
git add .
```
```bash
git commit -m "first commit"
```
onliner updates for readme    
 ```bash  
git add . && git commit -m "update readme.md"
```
```bash
https://github.com/SameenAdil/simple-dvc-demo.git
git branch -M main
git push -u origin main
```
excecute(rerun/reproduce) pipeline and update results 
```bash
dvc repro
```

Show the current experiment results.
```bash
dvc metrics show
```

Compare metrics between versions head/old, workspace/new
```bash
dvc metrics diff
```
tox command -
```bash
tox
```

for rebuilding
```bash
tox -r
```

pytest command
```bash
pytest -v
```
setup commands - 
```bash
pip install -e .
or 
python setup.py install
```

build your own package on PYPI, command-
```bash
python setup.py sdist bdist_wheel
``` 

