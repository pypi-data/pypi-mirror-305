from setuptools import setup, find_packages

setup(
    name="common_email_check",
    version="0.2.5",
    description="A module for email checking",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "pandas",  # pandas를 설치 요구사항으로 추가
    ],
)