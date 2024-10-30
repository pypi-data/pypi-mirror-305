import numpy as np
from scipy.spatial import distance

# 데이터 구조화 함수
def get_coordinates(df):
    x_coords = np.array(df['X'])
    y_coords = np.array(df['Y'])
    return np.stack([x_coords, y_coords], axis=1)

# 두 지점 집합 간 거리 행렬을 계산함
def operator_distance_matrix(self, pts_matrix_1, pts_matrix_2):
    OD_Dist = distance.cdist(pts_matrix_1, pts_matrix_2)
    return OD_Dist