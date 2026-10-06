# Uncertainty-Aware Probabilistic Risk Scoring Engine
## Description 
This project is a probabilistic risk scoring engine for cybersecurity. The system will act as a decision-support tool: every score/percentage is accompanied by how much to trust it, and the system actively tells its human operators when it's out of its depth, rather than confidently guessing. 

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
│   └── notees