import os
from pathlib import Path

# Project root 
BASE_DIR = Path(__file__).resolve().parent

# Seed for Reproducibility
RANDOM_STATE = 42

# Data Subset Configuration
SUBSET_PATIENTS = 10000

# Raw Data
DATA_ROOT = BASE_DIR / "data" / "raw" / "mimic-iv-3.1"
HOSP_DIR = DATA_ROOT / "hosp"
ICU_DIR = DATA_ROOT / "icu"

# Processed Data
PROCESSED_DIR = BASE_DIR / "data" / "processed"
LABELLED_DATASET = os.path.join(PROCESSED_DIR, 'labelled_dataset.csv')
BEST_BASELINE_PKL = os.path.join(PROCESSED_DIR, 'best_baseline.pkl')
DISTILBERT_PREDS_PKL = os.path.join(PROCESSED_DIR, 'preds_distilbert.pkl')
PUBMEDBERT_PREDS_PKL = os.path.join(PROCESSED_DIR, 'preds_pubmedbert.pkl')
BIOBERT_PREDS_PKL = os.path.join(PROCESSED_DIR, 'preds_biobert.pkl')

# Results
PLOTS_DIR = BASE_DIR / "results" / "plots"
METRICS_DIR = BASE_DIR / "results" / "metrics"
BASELINE_RESULTS_CSV = os.path.join(METRICS_DIR, 'baseline_results.csv')
DISTILBERT_RESULTS_CSV = os.path.join(METRICS_DIR, 'distilbert_results.csv')
PUBMEDBERT_RESULTS_CSV = os.path.join(METRICS_DIR, 'pubmedbert_results.csv')
BIOBERT_RESULTS_CSV = os.path.join(METRICS_DIR, 'biobert_results.csv')

# Label definitions
READMISSION_WINDOW_DAYS = 30
NUM_LABELS = 2  

# Data Split for Model Training/ Validation
TEST_SIZE = 0.20
VAL_SIZE = 0.50 

# Transformer hyperparameters 
MAX_LENGTH = 256
NUM_EPOCHS = 8
BATCH_SIZE = 32
LEARNING_RATE = 3e-5
WEIGHT_DECAY = 0.01
WARMUP_STEPS = 200
EARLY_STOPPING_PATIENCE = 3

# Model paths
MODELS_DIR = BASE_DIR / 'models'
DISTILBERT_DIR = str(BASE_DIR / 'models' / 'distilbert')
PUBMEDBERT_DIR = str(BASE_DIR / 'models' / 'pubmedbert')
BIOBERT_DIR = str(BASE_DIR / 'models' / 'biobert')

# HuggingFace model IDs (used in tokeniser comparison)
DISTILBERT_MODEL_ID = 'distilbert-base-uncased'
PUBMEDBERT_MODEL_ID = 'microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext'
BIOBERT_MODEL_ID = 'dmis-lab/biobert-base-cased-v1.2'

# Output Directories
for d in [PROCESSED_DIR, PLOTS_DIR, METRICS_DIR]:
    d.mkdir(parents=True, exist_ok=True)