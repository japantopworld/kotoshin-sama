import streamlit as st

st.title("賭神様｜競艇AI予想")
st.write("本日の競艇AI予想")

predictions = [
    "桐生 12R：1-2-3 本命 ◎",
    "住之江 10R：3-1-6 穴狙い △",
    "浜名湖 9R：2-4-1 安定狙い ○"
]

import random
pred = random.choice(predictions)

st.markdown(f"### 今日の予想: {pred}")
