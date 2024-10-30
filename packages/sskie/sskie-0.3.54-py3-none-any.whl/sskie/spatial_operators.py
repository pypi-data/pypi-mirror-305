import numpy as np
from scipy.spatial import distance


# 두 지점 집합 간 거리 행렬을 계산함
def operator_distance_matrix(pts_matrix_1, pts_matrix_2):
    OD_Dist = distance.cdist(pts_matrix_1, pts_matrix_2)
    return OD_Dist