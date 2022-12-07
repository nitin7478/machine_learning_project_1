# machine_learning_project_1
My First project upload 

Create conda environment(Use command prompt terminal inside vscode)
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

Note: To ignore file or folder we can add filename or folder name to .gitingnore file
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
 

 Heroku email : nitin7478@gmail.com
 api_key : 92bb0b61-afc3-4cd5-8918-8483f824de77
 heroku_app_name : ml-first-p

 BUILD DOCKER IMAGE
 ```
 docker build -t <image_name>:<tagname> .
 ```

* Note: Image name mustbe in lowercase

To list docker images
```
docker images
```
To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <docker_image_id> 
```

To check running container in docker
```
docker ps
```
To stop docker image 
```
docker stop <container_id>
```
To install setup on cmd in vscode
```
python setup.py install
```



