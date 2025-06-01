import streamlit as st
from datetime import datetime
import pytz

# 日本時間を取得（JST）
jst = pytz.timezone("Asia/Tokyo")
now = datetime.now(jst)
now_str = now.strftime("%Y/%m/%d %H:%M:%S")

st.set_page_config(page_title="賭神様 - スタートメニュー", layout="wide")
st.title("🎌 賭神様 - スタートメニュー")
st.markdown(f"🕒 現在時刻（日本時間）: {now_str}")

st.markdown("---")
st.markdown("👈 左のメニューから「競艇AI予想」を選んでください")
