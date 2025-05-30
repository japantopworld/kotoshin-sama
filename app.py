import streamlit as st

# ロゴ画像を表示（GitHubの生画像URLを使用）
st.image("https://raw.githubusercontent.com/japantopworld/kotoshin-sama/main/%E9%A6%AC%E3%81%A8%E6%B3%A2%E3%81%AE%E7%A5%9E%E7%B4%8B.png", width=250)

# タイトルと制作者名
st.title("賭神様｜AI予想")
st.caption("制作：日本トップワールド 小島崇彦")

# 予想リスト（競艇と競馬の例）
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

# 競艇 or 競馬を選択するボタン
mode = st.radio("予想を選んでください", ("競艇", "競馬"))

if st.button("予想を表示"):
    if mode == "競艇":
        for p in boat_predictions:
            st.write(p)
    else:
        for p in horse_predictions:
            st.write(p)

