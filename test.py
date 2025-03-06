from pathlib import Path
path = Path('artifacts/model_evaluation/metrics.json')

with open(path,'r') as f:
    file = f.read()