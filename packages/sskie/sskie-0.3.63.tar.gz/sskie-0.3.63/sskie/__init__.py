from .spatial_analysis import SpatialAnalysis

__version__ = '0.3.63'

# 아래 할때는 build, dist, egg 지워야됨 + __version__ 수정
# python setup.py sdist bdist_wheel

# python -m twine upload dist/*

# pypi-AgEIcHlwaS5vcmcCJGMwZTM2YjQxLWE5MzItNDdlMC04OTQwLWUyMGM1ZDFkMTVmMgACDVsxLFsic3NraWUiXV0AAixbMixbImM0YTIyMDQ5LTNlNjgtNDcyZC04MTU4LTI1NjU2ZjIxMDAzZCJdXQAABiD8Ft8yPqIDhBWHSRiP2MxzPWfAsfz0H5iOYIvn05dqhA


# > SSKIE / 경로 폴더(패키지를 담을 폴더)
# 	>build / 패키지 빌드 과정에서 생성된 임시 파일 저장
# 	>dist / 패키지를 배포할 수 있는 최종 결과물이 저장되는 폴더
# 	>sskie.egg-info / 패키지에 대한 메타 데이터를 포함하는 폴더
# 	>sskie / python 패키지 폴더
# 		>__init__.py / 해당 디렉토리를 Python 패키지로 인식하게 함
# 		>spatial_analysis.py / 실제 패키지의 주요 코드가 들어 있는 파일
# 		>spatial_operators.py / rhdrksdustksgkatn
# 	>setup.py / 설정



