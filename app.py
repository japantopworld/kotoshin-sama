import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import requests
from io import BytesIO
import random

# ロゴ画像の読み込み
logo_url = "https://raw.githubusercontent.com/japantopworld/kotoshin-sama/main/%E9%A6%AC%E3%81%A8%E6%B3%A2%E3%81%AE%E7%A5%9E%E7%B4%8B.png"
response = requests.get(logo_url)
logo_image = Image.open(BytesIO(response.content))

# ✅ ロゴを表示
st.image(logo_image, use_container_width=True)

# タイトル
st.markdown("<h1 style='text-align: center; font-size: 36px;'>賭神様｜AI予想</h1>", unsafe_allow_html=True)

# 🔁 現在の日本時刻を表示
now = datetime.utcnow() + timedelta(hours=9)
st.markdown(f"<p style='text-align: right; font-size: 18px;'>現在の日本時刻：{now.strftime('%Y-%m-%d %H:%M:%S')}</p>", unsafe_allow_html=True)

# ===== 出走表データの例（実際にはAPIまたはスクレイピングが必要） =====
boat_races = {
    "桐生": ["12R", "11R", "10R"],
    "住之江": ["12R", "9R"],
    "浜名湖": ["9R", "8R"]
}

horse_races = {
    "東京": ["5R", "6R"],
    "中山": ["7R", "8R"],
    "阪神": ["9R"]
}

# 競艇 or 競馬を選択
mode = st.radio("予想を選んでください", ("競艇", "競馬"))

# レース場選択
venue = st.selectbox("レース場を選んでください", list(boat_races.keys()) if mode == "競艇" else list(horse_races.keys()))

# レース番号選択
race_list = boat_races[venue] if mode == "競艇" else horse_races[venue]
race = st.selectbox("レース番号を選んでください", race_list)

# 📊 簡易AI予想の例（ランダム）
def simple_ai_prediction():
    heads = list(range(1, 7)) if mode == "競艇" else list(range(1, 9))
    choice = random.sample(heads, 3)
    marks = ["◎", "○", "▲", "△"]
    return f"{venue} {race}：{'-'.join(map(str, choice))} 本命 {random.choice(marks)}"

# 表示ボタン
if st.button("予想を表示"):
    st.markdown(f"<div style='font-size: 24px;'>{simple_ai_prediction()}</div>", unsafe_allow_html=True)

# クレジット
st.markdown("---")
st.markdown("<p style='text-align: center;'>制作：日本トップワールド　小島崇彦</p>", unsafe_allow_html=True)
