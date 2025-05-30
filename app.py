import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import requests
from io import BytesIO
import time

# ロゴ画像の読み込み
logo_url = "https://raw.githubusercontent.com/japantopworld/kotoshin-sama/main/%E9%A6%AC%E3%81%A8%E6%B3%A2%E3%81%AE%E7%A5%9E%E7%B4%8B.png"
response = requests.get(logo_url)
logo_image = Image.open(BytesIO(response.content))

# ロゴ表示
st.image(logo_image, use_column_width=True)
st.title("賭神様｜AI予想")

# 🔁 現在時刻（日本時間）をリアルタイムで表示
with st.empty():
    while True:
        now = datetime.utcnow() + timedelta(hours=9)
        st.markdown(f"### 現在の日本時刻：{now.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(1)
        break  # ←1回表示したら止める（無限ループ防止）

# 予想データ
boat_predictions = [
    "桐生 12R：1-2-3 本命 ◎",
    "住之江 10R：3-1-6 穴狙い △",
    "浜名湖 9R：2-4-1 安定狙い ○"
]

horse_predictions = [
    "東京 5R：2-4-5 本命 ◎",
    "中山 7R：1-3-6 穴狙い △",
    "阪神 9R：4-5-1 安定狙い ○"
]

# 切り替えボタン
mode = st.radio("予想を選んでください", ("競艇", "競馬"))

if st.button("予想を表示"):
    if mode == "競艇":
        for p in boat_predictions:
            st.write(p)
    else:
        for p in horse_predictions:
            st.write(p)

# クレジット
st.markdown("---")
st.markdown("制作：日本トップワールド　小島崇彦")
