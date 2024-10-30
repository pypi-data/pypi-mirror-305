import numpy as np
from scipy.spatial import distance
import geopandas as gpd

# 두 지점 집합 간 거리 행렬을 계산함
def operator_distance_matrix(pts_matrix_1, pts_matrix_2):
    OD_Dist = distance.cdist(pts_matrix_1, pts_matrix_2)
    return OD_Dist

def create_buffer(gdf, distance):
    """지정한 거리만큼의 버퍼를 생성하여 반환합니다."""
    gdf['buffer'] = gdf.buffer(distance)
    gdf['geometry'] = gdf['buffer']
    return gdf

def sjoin_within_gdf2(gdf1, gdf2):
    gdf_sjoin = gpd.sjoin(gdf1, gdf2, predicate='intersects', how='left')
    return gdf_sjoin[~gdf_sjoin['index_right'].isnull()]

# 재화의 도달거리 계산
def calculate_reach_distance(area, facility_count):
    tsw = area * 1000000
    d_ij = np.sqrt(tsw / facility_count)
    return d_ij

# 거리 계산
def calculate_distance(df1, df2):
    df1['distance_to_df2'] = df1.distance(df2.geometry)
    return df1