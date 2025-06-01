import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

st.set_page_config(page_title="競艇AI予想", layout="wide")
st.title("🚤 競艇AI予想 - 出走表＋予想結果")

# --- 日付設定（今日） ---
from datetime import datetime
today = datetime.now().strftime("%Y%m%d")
TODAY_URL = f"https://www.boatrace.jp/owpc/pc/race/raceindex?hd={today}"

# --- 出走表スクレイピング（1場1Rのみ例） ---
def get_real_race_table():
    try:
        response = requests.get(TODAY_URL)
        soup = BeautifulSoup(response.content, "html.parser")

        # 最初のリンクを取得（例：蒲郡1R）
        race_link = soup.select_one("div.race_index_table a")
        if race_link is None:
            return {"エラー": "レース情報が見つかりません"}
        
        href = race_link.get("href")
        race_url = f"https://www.boatrace.jp{href}"

        # レースページへ移動
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

# --- AI予想ロジック（仮） ---
def predict_ai(players):
    if len(players) < 3:
        return "選手が足りません"
    shuffled = players.copy()
    random.shuffle(shuffled)
    return f"🎯 予想：{shuffled[0]} → {shuffled[1]} → {shuffled[2]}"

# --- 表示 ---
data = get_real_race_table()

if "エラー" in data:
    st.error(f"出走表の取得に失敗しました：{data['エラー']}")
else:
    st.subheader(data["レース名"])
    st.write("### 🚩 出走表")
    for i, player in enumerate(data["選手"], start=1):
        st.write(f"{i}号艇：{player}")

    st.write("### 🤖 AI予想")
    prediction = predict_ai(data["選手"])
    st.success(prediction)

    st.caption("※仮のAIロジックです。今後本物の学習モデルに進化予定。")
