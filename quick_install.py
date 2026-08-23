import subprocess
import sys

# 必要なライブラリを強制インストール
try:
    import folium
    from streamlit_folium import st_folium
except ModuleNotFoundError:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "folium", "streamlit-folium"]
    )
    import folium
    from streamlit_folium import st_folium

# --- ここから下に元のコードを記述 ---
import io
import pandas as pd
import streamlit as st
