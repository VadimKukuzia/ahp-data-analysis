import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

def calculate_mean_ranking(rankings: np.ndarray) -> list:
    """Calculate mean ranking from expert assessments."""
    return [round(np.mean(rankings[:, i]), 2) for i in range(len(rankings[0]))]

def build_ahp_matrix(rankings: list, N: int) -> np.ndarray:
    """Build an AHP pairwise comparison matrix based on rankings."""
    matrix = np.zeros((N, N))
    
    for i in range(N):
        for j in range(N):
            if rankings[i] == rankings[j]:
                matrix[i][j] = 1.0
            elif rankings[i] > rankings[j]:
                matrix[i][j] = round(float(rankings[i] - rankings[j] + 1), 2)
                matrix[j][i] = round(1 / (rankings[i] - rankings[j] + 1), 2)

    return matrix
