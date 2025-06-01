import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random

st.set_page_config(page_title="競艇AI予想", layout="centered")
st.title("🚤 競艇AI予想 - 出走表＋AI予想")

# 📅 カレンダー（ユーザーが日付選択）
selected_date = st.date_input("📅 レース日を選択", datetime.today())
date_str = selected_date.strftime("%Y%m%d")
TODAY_URL = f"https://www.boatrace.jp/owpc/pc/race/raceindex?hd={date_str}"

# 🧠 AI予想ロジック（仮）
def predict_ai(players):
    if len(players) < 3:
        return "選手が足りません"
    shuffled = players.copy()
    random.shuffle(shuffled)
    return f"{shuffled[0]} → {shuffled[1]} → {shuffled[2]}"

# 📥 出走表を取得（スクレイピング）
def get_race_data():
    try:
        response = requests.get(TODAY_URL)
        soup = BeautifulSoup(response.content, "html.parser")
        race_link = soup.select_one("div.race_index_table a")
        if not race_link:
            return {"エラー": "レースリンクが見つかりません"}
        race_url = "https://www.boatrace.jp" + race_link["href"]

        race_page = requests.get(race_url)
        race_soup = BeautifulSoup(race_page.content, "html.parser")
        race_name = race_soup.select_one("div.race_title").text.strip()
        names = race_soup.select("div.race_card_name span.name")
        players = [n.text.strip() for n in names if n.text.strip()]
        return {
            "レース名": race_name,
            "選手": players
        }
    except Exception as e:
        return {"エラー": str(e)}

# 🔄 表示
data = get_race_data()

if "エラー" in data:
    st.error(f"❌ 出走表の取得に失敗しました：{data['エラー']}")
else:
    st.subheader(f"📄 {data['レース名']}")
    
    st.write("### 🚩 出走表（選手一覧）")
    st.table({f"{i+1}号艇": [name] for i, name in enumerate(data["選手"])})

    st.write("### 🤖 AI予想")
    st.success(f"🎯 本日の予想：{predict_ai(data['選手'])}")

    st.caption("※予想は仮ロジックです。後日AI学習モデルに進化予定です。")
