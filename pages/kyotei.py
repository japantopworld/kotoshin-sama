import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime

# --- ページ設定 ---
st.set_page_config(page_title="競艇AI予想", layout="wide")
st.title("🚤 競艇AI予想 - 出走表＋予想結果")

# --- 日付を選択してURLを作成 ---
today = datetime.today().strftime("%Y%m%d")
selected_date = st.sidebar.date_input("予想する日付を選んでください", datetime.today())
date_str = selected_date.strftime("%Y%m%d")
TODAY_URL = f"https://www.boatrace.jp/owpc/pc/race/raceindex?hd={date_str}"

# --- ダミー選手（仮） ---
dummy_players = ["今垣光太郎", "白井英治", "峰竜太", "毒島誠", "瓜生正義", "平本真之"]

# --- 出走表取得（仮：スクレイピング未実装） ---
def get_race_table():
    try:
        response = requests.get(TODAY_URL)
        if response.status_code != 200:
            raise Exception("Webサイトにアクセスできませんでした")
        soup = BeautifulSoup(response.content, "html.parser")

        # ここに本物のスクレイピング処理を入れる予定
        race_data = {
            "レース名": "第1R 予選",
            "選手": dummy_players
        }
        return race_data
    except Exception as e:
        return {"エラー": str(e)}

# --- AI予想（仮のランダム） ---
def predict_ai(players):
    shuffled = players.copy()
    random.shuffle(shuffled)
    return f"🎯 予想：{shuffled[0]} → {shuffled[1]} → {shuffled[2]}"

# --- メイン処理 ---
data = get_race_table()

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

    st.caption("※予想は仮ロジックです。後日AIモデルを強化します。")
