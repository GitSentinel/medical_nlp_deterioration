import os

# Seed for Reproducibility
RANDOM_STATE = 42

# Raw Data
DATA_ROOT = os.path.join('data', 'raw', 'mimic-iv-clinical-database-demo-2.2')
HOSP_DIR  = os.path.join(DATA_ROOT, 'hosp')
ICU_DIR   = os.path.join(DATA_ROOT, 'icu')

# Processed Data
PROCESSED_DIR         = os.path.join('data', 'processed')

# Results
PLOTS_DIR             = os.path.join('results', 'plots')
METRICS_DIR           = os.path.join('results', 'metrics')

# Label definitions
READMISSION_WINDOW_DAYS = 30   
NUM_LABELS              = 2    

# Data Split for Model Training/ Validation
TEST_SIZE = 0.20    
VAL_SIZE  = 0.50    

# Output Directories
_dirs = [PROCESSED_DIR, PLOTS_DIR, METRICS_DIR]
for _d in _dirs:
    os.makedirs(_d, exist_ok=True)