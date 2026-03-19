import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import platform

# 시각화 환경 설정
def get_font():
    os_name = platform.system()
    if os_name == "Windows":
        return "Malgun Gothic"
    elif os_name == "Darwin":
        return "AppleGothic"
    else:
        return "NanumGothic"

def initialize_environment(font="Malgun Gothic"):
    # 1. 시각화 스타일
    sns.set(style="whitegrid")

    # 2. 폰트 설정
    plt.rcParams['font.family'] = font

    # 3. 마이너스 깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False

# 데이터 적재
def load_penguins():
    df = sns.load_dataset("penguins")
    return df

# 공통 초기화 함
def setup_all(font="Malgun Gothic"):
    initialize_environment(font)
    df = load_penguins()
    return df