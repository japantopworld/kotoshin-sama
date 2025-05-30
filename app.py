import streamlit as st
from PIL import Image

# ロゴ画像の読み込み
logo = Image.open("logo.png")
st.image(logo, use_column_width=True)

# タイトルと制作者名
st.title("賭神様｜AI予想")
st.caption("制作者：日本トップワールド　小島崇彦")

# 予想リスト
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

# モード選択（競艇 or 競馬）
mode = st.radio("予想を選んでください", ("競艇", "競馬"))

# ボタンで表示
if st.button("予想を表示"):
    st.subheader(f"{mode}の予想")
    if mode == "競艇":
        for p in boat_predictions:
            st.write(p)
    else:
        for p in horse_predictions:
            st.write(p)
