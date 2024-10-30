import numpy as np
from scipy.spatial import distance


# 두 지점 집합 간 거리 행렬을 계산함
def operator_distance_matrix(pts_matrix_1, pts_matrix_2):
    OD_Dist = distance.cdist(pts_matrix_1, pts_matrix_2)
    return OD_Dist

def create_buffer(gdf, distance):
    """지정한 거리만큼의 버퍼를 생성하여 반환합니다."""
    gdf['buffer'] = gdf.buffer(distance)
    gdf['geometry'] = gdf['buffer']
    return gdf

def sjoin_within_radius(gdf_1, gdf_2):
    gdf_sjoin = gpd.sjoin(gdf_1, gdf_2, predicate='intersects', how='left')
    return gdf_sjoin[~gdf_sjoin['index_right'].isnull()]