from setuptools import setup, find_packages

setup(
    name="common_email_check",       # 패키지 이름
    version="0.1.6",                 # 버전
    description="A module for email checking",  # 설명
    author="Your Name",              # 작성자 이름
    author_email="your_email@example.com",  # 작성자 이메일
    packages=find_packages(),        # 패키지 목록 자동 탐색
    extras_require={
        'pyo3:python_version<"3.8"': ["pyo3>=0.14,<0.15"],   # Python 3.7에 적합한 pyo3
        'pyo3:python_version>="3.8" and python_version<"3.9"': ["pyo3>=0.15,<0.16"],  # Python 3.8에 적합한 pyo3
        'pyo3:python_version>="3.9"': ["pyo3>=0.16"],         # Python 3.9 이상에 적합한 pyo3
    },
    python_requires=">=3.7",  # Python 버전 권장
)