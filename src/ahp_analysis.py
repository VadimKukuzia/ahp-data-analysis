import os
import pickle
import numpy as np
import logging
from prettytable import PrettyTable
from data_processing import calculate_mean_ranking, build_ahp_matrix
from ahp_matrix_processing import get_all_data 

logging.basicConfig(level=logging.INFO)

def run_ahp_analysis(rankings: np.ndarray, factor_label: str, N: int, result_path: str):
    """Perform AHP analysis and save results."""
    avg_ranking = calculate_mean_ranking(rankings)
    N = N - 1
    ahp_matrix = build_ahp_matrix(avg_ranking, N)
    
    sum_rankings = round(sum(avg_ranking), 2)

    # Getting AHP data
    g_means, sum_g_means, priority_vectors, sum_priority_vectors, percent, sum_percent, ranking_ratio, \
        sum_vector_priority_vector, sum_vpv, consistency_index, consistency_ratio = get_all_data(
            ahp_matrix, N, sum_rankings, avg_ranking)

    Fs = [factor_label + str(n + 1) for n in range(N)]

    # Making PrettyTable
    result_table = PrettyTable()
    result_table.field_names = ["", *Fs, "Geo Mean", "Priority Vector", "%", "Rank", "Ranking Ratio"]

    for i in range(N):
        result_table.add_row(
            [Fs[i], *ahp_matrix[i], g_means[i], priority_vectors[i], percent[i], avg_ranking[i], ranking_ratio[i]])

    result_table.add_row(['' for _ in range(N + 6)])
    result_table.add_row(
        ['' for _ in range(N + 1)] + [sum_g_means, sum_priority_vectors, sum_percent, sum_rankings] + [''])
    result_table.add_row(['' for _ in range(N + 6)])
    result_table.add_row(['', *sum_vector_priority_vector, sum_vpv] + ['' for _ in range(4)])
    
    logging.info("\n" + str(result_table))
    logging.info(f"Consistency Index: {consistency_index}")
    logging.info(f"Consistency Ratio: {consistency_ratio}%")

    # Results saving
    os.makedirs(result_path, exist_ok=True)
    with open(os.path.join(result_path, 'results.txt'), 'w', encoding="utf-8") as file:
        file.write(str(result_table))
        file.write(f"\nConsistency Index: {consistency_index}\n")
        file.write(f"Consistency Ratio: {consistency_ratio}%\n")

    with open(os.path.join(result_path, 'variables.pkl'), 'wb') as file:
        pickle.dump((ahp_matrix, g_means, priority_vectors, percent, avg_ranking, ranking_ratio,
                     sum_g_means, sum_priority_vectors, sum_percent, sum_rankings,
                     sum_vector_priority_vector, sum_vpv,
                     consistency_index, consistency_ratio), file)
