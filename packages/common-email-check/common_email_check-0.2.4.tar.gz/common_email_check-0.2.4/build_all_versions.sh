#!/bin/bash

# pyenv 초기화 설정 추가
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# 사용할 Python 버전 리스트
PYTHON_VERSIONS=("3.7.12" "3.8.12" "3.9.12" "3.10.4" "3.11.0" "3.12.7")

# 각 Python 버전에 대해 빌드 진행
for PYTHON_VERSION in "${PYTHON_VERSIONS[@]}"
do
    # pyenv로 해당 버전의 Python 설정
    pyenv shell "$PYTHON_VERSION" || continue  # 설정 실패 시 다음 버전으로 넘어감

    # 가상 환경 생성
    python -m venv "venv_$PYTHON_VERSION"
    source "venv_$PYTHON_VERSION/bin/activate" || { echo "Failed to activate venv for $PYTHON_VERSION"; continue; }

    # maturin 설치
    pip install --upgrade pip
    pip install maturin

    # 빌드 실행
    maturin build

    # 가상 환경 비활성화
    deactivate

    echo "Finished building for Python $PYTHON_VERSION"
done

# pyenv 기본 설정으로 복귀
pyenv shell system

