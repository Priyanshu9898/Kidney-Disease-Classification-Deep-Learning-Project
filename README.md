## Kidney Disease Classification

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Prriyanshu9898/Kidney-Disease-Classification-Using-Deep-Learning
```
### STEP 01- Create a Python environment after opening the repository

```bash
python -m venv env
```

```bash
env\Scripts\activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```



## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)


MLFLOW_TRACKING_URI=https://dagshub.com/Priyanshu9898/Kidney-Disease-Classification-Deep-Learning-Project.mlflow \
MLFLOW_TRACKING_USERNAME=Priyanshu9898 \
MLFLOW_TRACKING_PASSWORD=1dc505ed931b2af16eacead37f82f256c16d99fe \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Priyanshu9898/Kidney-Disease-Classification-Deep-Learning-Project.mlflow

export MLFLOW_TRACKING_USERNAME=Priyanshu9898 

export MLFLOW_TRACKING_PASSWORD=1dc505ed931b2af16eacead37f82f256c16d99fe

```