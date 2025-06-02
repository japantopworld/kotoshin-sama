import streamlit as st
import random
import datetime

# ---------------------------
# 📅 日付と時刻
# ---------------------------
jst_now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
today_str = jst_now.strftime("%Y%m%d")
time_now = jst_now.strftime("%Y-%m-%d %H:%M:%S")

# ---------------------------
# Streamlit設定
# ---------------------------
st.set_page_config(page_title="競艇AI予想", layout="wide")
st.title("🚤 競艇AI予想 - 出走表＋予想結果")
st.write(f"📅 本日：{today_str}")
st.write(f"🕒 現在時刻（日本時間）：{time_now}")

# ---------------------------
# 仮のレースデータ
# ---------------------------
races = [
    {
        "レース名": "第1R 予選",
        "開催地": "蒲郡",
        "選手": ["今垣光太郎", "白井英治", "峰竜太", "毒島誠", "瓜生正義", "平本真之"]
    },
    {
        "レース名": "第2R 一般",
        "開催地": "丸亀",
        "選手": ["桐生順平", "赤岩善生", "松井繁", "石野貴之", "岡崎恭裕", "井口佳典"]
    },
    {
        "レース名": "第3R 準優勝戦",
        "開催地": "常滑",
        "選手": ["寺田祥", "濱野谷憲吾", "西山貴浩", "篠崎元志", "前本泰和", "茅原悠紀"]
    }
]

# ---------------------------
# 仮AI予想ロジック
# ---------------------------
def predict_ai(players):
    shuffled = players.copy()
    random.shuffle(shuffled)
    return f"🎯 予想：{shuffled[0]} → {shuffled[1]} → {shuffled[2]}"

# ---------------------------
# 表示
# ---------------------------
for race in races:
    st.markdown("---")
    st.subheader(f"🏁 {race['レース名']} @ {race['開催地']}")
    st.write("### 🚩 出走表")
    for i, player in enumerate(race["選手"], start=1):
        st.write(f"{i}号艇：{player}")
    st.write("### 🤖 AI予想")
    prediction = predict_ai(race["選手"])
    st.success(prediction)

st.caption("※ 現在は仮のAIロジックを使用中です。今後、本物のAI学習モデル（LightGBMなど）に進化予定。")
