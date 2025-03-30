import numpy as np


def get_g_mean(x):
    a = np.log(x)
    return round(np.exp(a.mean()), 3)


def get_all_data(matrix, N, sum_rankings, rankings):
    R = 3
    g_means = [get_g_mean(row) for row in matrix]

    sum_g_means = round(sum(g_means), R)

    priority_vectors = [round(g_mean / sum_g_means, R) for g_mean in g_means]
    sum_priority_vectors = round(sum(priority_vectors))

    percent = [round((pv * 100), R) for pv in priority_vectors]
    sum_percent = round(sum(percent))

    ranking_ratio = [round((ranking / sum_rankings) * 100, R) for ranking in rankings]

    sum_vector_priority_vector = [round((sum(matrix[:, n]) * priority_vectors[n]), R) for n in range(N)]
    sum_vpv = round(sum(sum_vector_priority_vector), R)

    consistency_const = 1.49 if N == 10 else 1.51

    consistency_index = round((sum_vpv - N) / (N - 1), R)
    consistency_ratio = round((consistency_index / consistency_const) * 100, R)

    return g_means, sum_g_means, priority_vectors, sum_priority_vectors, percent, sum_percent, ranking_ratio,\
        sum_vector_priority_vector, sum_vpv, consistency_index, consistency_ratio
