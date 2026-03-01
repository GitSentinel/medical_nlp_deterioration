import os
from pathlib import Path

# Project root 
BASE_DIR = Path(__file__).resolve().parent

# Seed for Reproducibility
RANDOM_STATE = 42

# Raw Data
DATA_ROOT = BASE_DIR / "data" / "raw" / "mimic-iv-3.1"
HOSP_DIR = DATA_ROOT / "hosp"
ICU_DIR = DATA_ROOT / "icu"

# Processed Data
PROCESSED_DIR = BASE_DIR / "data" / "processed"
LABELLED_DATASET = os.path.join(PROCESSED_DIR, 'labelled_dataset.csv')

# Results
PLOTS_DIR = BASE_DIR / "results" / "plots"
METRICS_DIR = BASE_DIR / "results" / "metrics"

# Label definitions
READMISSION_WINDOW_DAYS = 30
NUM_LABELS = 2  

# Data Split for Model Training/ Validation
TEST_SIZE = 0.20
VAL_SIZE = 0.50 

# Output Directories
for d in [PROCESSED_DIR, PLOTS_DIR, METRICS_DIR]:
    d.mkdir(parents=True, exist_ok=True)