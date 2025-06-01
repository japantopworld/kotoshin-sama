import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="賭神様 - スタートメニュー", layout="centered")

st.title("🎌 賭神様 - スタートメニュー")

# --- 現在時刻を定期的に更新 ---
placeholder = st.empty()

for _ in range(1000):  # ループ回数（多めでOK）
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    placeholder.markdown(f"🕒 **現在時刻（日本時間）:** {now}")
    time.sleep(1)
