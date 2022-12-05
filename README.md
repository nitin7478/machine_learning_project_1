# machine_learning_project_1
My First project upload 

Create conda environment
```
conda init
conda create -p venv python== 3.10 -y 
conda activate venv/
```
if gives error  then enter following command
```
eval "$(conda shell.bash hook)"
conda activate venv/
```

or create python environment
```
python -m venv .venv
shift + p select python interpreter 
```
create requirements.txt file and put libraries in it
```
pip install -r requirements.txt
```
To add files 
```
git add <file_name>
```

Note : To ignore file or folder we can add filename or folder name to .gitingnore file
To check git status
```
git status
```
To check all versions
````
git log
````

To create version/commit all changes by git
```
git commit -m "message"
```
To send changes/version to github 
```
git push origin main
```
To check remote url
```
git remote -v
```
To check your branch
```
git branch
```