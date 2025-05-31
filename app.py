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
st.image(logo_image, use_container_width=True)

# タイトルと現在時刻
st.title("賭神様｜AI予想")
now = datetime.utcnow() + timedelta(hours=9)
st.markdown(f"### 現在の日本時刻：{now.strftime('%Y-%m-%d %H:%M:%S')}")

# 日付選択（本日と翌日の選択）
today = datetime.utcnow() + timedelta(hours=9)
tomorrow = today + timedelta(days=1)
date_option = st.selectbox("日付を選択", [
    today.strftime("%Y-%m-%d"),
    tomorrow.strftime("%Y-%m-%d")
])

# レース場選択（例）
boat_race_courses = ["桐生", "住之江", "浜名湖"]
horse_race_courses = ["東京", "中山", "阪神"]

# 競艇 or 競馬
mode = st.radio("予想を選んでください", ("競艇", "競馬"))

if mode == "競艇":
    race_course = st.selectbox("競艇レース場を選択", boat_race_courses)
    race_nums = [f"{i}R" for i in range(1, 13)]
else:
    race_course = st.selectbox("競馬場を選択", horse_race_courses)
    race_nums = [f"{i}R" for i in range(1, 13)]

race_number = st.selectbox("レース番号を選択", race_nums)

# 予想表示ボタン
if st.button("AI予想を表示"):
    # ランダムな予想（簡易AI）
    if mode == "競艇":
        numbers = random.sample(range(1, 7), 3)
    else:
        numbers = random.sample(range(1, 18), 3)
    marks = ["◎", "○", "▲", "△"]
    mark = random.choice(marks)
    prediction = f"{race_course} {race_number}：{numbers[0]}-{numbers[1]}-{numbers[2]} 本命 {mark}"
    st.success(prediction)

# クレジット表示
st.markdown("---")
st.markdown("制作：日本トップワールド　小島崇彦")
