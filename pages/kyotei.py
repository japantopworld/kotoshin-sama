import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime

st.set_page_config(page_title="競艇AI予想", layout="wide")
st.title("🚤 競艇AI予想 - 出走表＋予想結果")

# 日付選択
selected_date = st.date_input("表示する日付を選択", datetime.today())
today_str = selected_date.strftime("%Y%m%d")

# URL設定（動的＋ヘッダーつき）
TODAY_URL = f"https://www.boatrace.jp/owpc/pc/race/raceindex?hd={today_str}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# 仮の選手名（データ取得に失敗した場合）
dummy_players = ["今垣光太郎", "白井英治", "峰竜太", "毒島誠", "瓜生正義", "平本真之"]

# 出走表取得
def get_race_table():
    try:
        response = requests.get(TODAY_URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")

        # 仮：選手名のHTML構造が複雑なので、今は仮データ
        race_data = {
            "レース名": "第1R 予選（仮）",
            "選手": dummy_players
        }
        return race_data
    except Exception as e:
        return {"エラー": str(e)}

# AI予想（仮）
def predict_ai(players):
    shuffled = players.copy()
    random.shuffle(shuffled)
    return f"🎯 予想：{shuffled[0]} → {shuffled[1]} → {shuffled[2]}"

# 表示
data = get_race_table()

if "エラー" in data:
    st.error(f"⚠️ 出走表の取得に失敗しました：{data['エラー']}")
    st.caption(f"URL: {TODAY_URL}")
else:
    st.subheader(data["レース名"])
    st.write("### 🚩 出走表")
    for i, player in enumerate(data["選手"], start=1):
        st.write(f"{i}号艇：{player}")

    st.write("### 🤖 AI予想")
    prediction = predict_ai(data["選手"])
    st.success(prediction)

    st.caption("※予想は仮ロジックです。今後AIモデルに進化予定。")
