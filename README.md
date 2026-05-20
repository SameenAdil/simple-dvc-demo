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


