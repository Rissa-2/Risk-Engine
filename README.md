# Uncertainty-Aware Probabilistic Risk Scoring Engine
## Description 
This project is a probabilistic risk scoring engine for cybersecurity. The system will act as a decision-support tool: every score/percentage is accompanied by how much to trust it, and the system actively tells its human operators when it's out of its depth, rather than confidently guessing. 

## Folder Structure

``` text
probabilistic-risk-engine/
│
├─— README.md
├── .gitignore
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   ├── NSL-KDD_Datasets/
│   │   │   ├── index.html
│   │   │   ├── KDDTest-21.arff
│   │   │   ├── KDDTest-21.txt
│   │   │   ├── KDDTest+.arff
│   │   │   ├── KDDTest+.txt
│   │   │   ├── KDDTest1.jpg
│   │   │   ├── KDDTrain+_20Percent.arff
│   │   │   ├── KDDTrain+_20Percent.txt
│   │   │   ├── KDDTrain+.arff
│   │   │   ├── KDDTrain+.txt
│   │   │   ├── KDDTrain1.jpg
│   │   │   └── README.md
│   │   
│   └── processed/
│   
│
├── src/
│   ├── data/
│   │   ├── load_data.py
│   │   └── preprocess.py
│   │
│   ├── models/
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   │
│   ├── uncertainty/
│   │   └── intervals.py
│   │
│   ├── calibration/
│   │   └── calibrate.py
│   │
│   └── drift/
│       └── drift_detection.py
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── notes
│       ├── routes/
│       └── services/
│
├── models/
│   └── notes/
│
├── tests/
│   └── notes
│
├── docs/
│   ├── First steps suggestions
│   └── Attributes
```

## Enviornment Set Up Instructions
### Do this in your terminal
Create the environment:
    python -m venv .venv
Activate it:
    .venv\Scripts\Activate.ps1
(.venv) should be at the start of all your prompts in the terminal now
Install the needed packages:
    pip install -r requirements.txt
Everything should be set up, HOWEVER i believe that the XGBoost package still needs to be installed
*Side note*: If powershell is blocking/disabling the virtual environment from being activated, run this line and then try the steps again:
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

