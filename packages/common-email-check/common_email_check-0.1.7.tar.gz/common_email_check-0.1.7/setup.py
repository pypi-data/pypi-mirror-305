import sys
from setuptools import setup, find_packages

# Python 버전에 따른 pyo3 버전 설정
pyo3_dependency = []
if sys.version_info < (3, 8):
    pyo3_dependency = ["pyo3>=0.14,<0.15"]   # Python 3.7에 적합
elif (3, 8) <= sys.version_info < (3, 9):
    pyo3_dependency = ["pyo3>=0.15,<0.16"]   # Python 3.8에 적합
else:
    pyo3_dependency = ["pyo3>=0.16"]         # Python 3.9 이상에 적합

setup(
    name="common_email_check",
    version="0.1.7",
    description="A module for email checking",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=[
        *pyo3_dependency,  # Python 버전에 따라 결정된 pyo3 버전 추가
    ],
    python_requires=">=3.7",
)