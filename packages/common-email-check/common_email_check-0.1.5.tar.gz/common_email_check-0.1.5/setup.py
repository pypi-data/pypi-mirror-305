from setuptools import setup, find_packages

setup(
    name="common_email_check",       # 패키지 이름
    version="0.1.5",                 # 버전
    description="A module for email checking",  # 설명
    author="Your Name",              # 작성자 이름
    author_email="your_email@example.com",  # 작성자 이메일
    packages=find_packages(),        # 패키지 목록 자동 탐색
    install_requires=[
        "pyo3>=0.15"  # pyo3 최신 버전 (필요 시 버전을 지정)
    ],
    python_requires=">=3.7",  # Python 버전 권장
)