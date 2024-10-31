from setuptools import setup, find_packages
setup(
name='lsymm', # pip가 참조하는 이 패키지 이름
version='0.0.1', # 버전
packages=find_packages(), # 패키지 자동 탐색
install_requires=[], # dependencies를 위해 사전 설치 필요한 패키지들
python_requires='>=3.6', # 최소 파이썬 설치 버전을 지정
keywords= ['python package', 'pypi', 'school'], # 패키지 키워드
description='for student', # 설명
author='seongkai', # 작성자 이름
author_email='lsy45508297lee@gmail.com', # 작성자 이메일
url='https://github.com/seongkai102', # 패키지의 URL
classifiers=[ # PYPI에 등록될 메타 데이터 설정. 예) 파이썬 버전 정보 등
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',]
)