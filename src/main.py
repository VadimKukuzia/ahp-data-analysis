import os
import yaml
import logging
import numpy as np
from data_loader import load_dataset
from ahp_analysis import run_ahp_analysis

logging.basicConfig(level=logging.INFO)

# Загрузка конфигурации
with open("src/config.yaml", "r") as file:
    config = yaml.safe_load(file)

DATASET_PATH = config["data"]["datasets_path"]
RESULTS_PATH = config["data"]["results_path"]
DEFAULT_N = config["ahp"]["default_N"]
ENV_N = config["ahp"]["environmental_N"]

def process_datasets(category: str):
    """Process datasets for a given category (economic, social, environmental)."""
    dataset_path = os.path.join(DATASET_PATH, category)
    result_path = os.path.join(RESULTS_PATH, category)
    
    for dataset_file in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, dataset_file)
        
        factor_label = {"economic": "E", "social": "S", "environmental": "Env"}.get(category, "error")
        N = ENV_N if factor_label == "Env" else DEFAULT_N
       
        df = load_dataset(file_path)
        rankings = np.array(df.values[:, 1:N])  # Извлекаем нужные столбцы

        dataset_result_path = os.path.join(result_path, dataset_file[:-4])
        run_ahp_analysis(rankings, factor_label, N, dataset_result_path)

if __name__ == "__main__":
    logging.info("Starting AHP Analysis...")
    
    for category in ["economic", "social", "environmental"]:
        process_datasets(category)
    
    logging.info("AHP Analysis Completed!")
