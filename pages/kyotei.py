import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pytz
import random

# 日本時間取得
jst = pytz.timezone("Asia/Tokyo")
now = datetime.now(jst)
today_str = now.strftime("%Y%m%d")
now_str = now.strftime("%Y-%m-%d %H:%M:%S")

# ページ設定
st.set_page_config(page_title="競艇AI予想", layout="wide")
st.title("🚤 競艇AI予想 - 出走表＋予想結果")
st.markdown(f"📅 本日：{today_str}")
st.markdown(f"🕒 現在時刻：{now_str}")

# レースURL（とりあえず桐生競艇場）
BASE_URL = "https://www.boatrace.jp/owpc/pc/race/racelist"
params = {"rno": 1, "jcd": "01", "hd": today_str}

def get_race_data():
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        # レース名
        race_title = soup.select_one(".heading span").text.strip()

        # 選手名抽出（仮に6名）
        names = soup.select(".table1 tbody tr td.is-name span")
        players = [n.text.strip() for n in names if n.text.strip()][:6]

        if not players:
            return {"エラー": "出走表が取得できませんでした（選手データなし）"}

        return {"レース名": race_title, "選手": players}

    except Exception as e:
        return {"エラー": str(e)}

# 仮AI予想ロジック
def predict(players):
    order = players.copy()
    random.shuffle(order)
    return f"🎯 仮AI予想：{order[0]} → {order[1]} → {order[2]}"

# 表示処理
race = get_race_data()

if "エラー" in race:
    st.error(f"⚠️ 出走表データを取得できませんでした。\n{race['エラー']}")
else:
    st.subheader(race["レース名"])
    st.write("### 🚩 出走表")
    for i, name in enumerate(race["選手"], 1):
        st.write(f"{i}号艇：{name}")

    st.write("### 🤖 AI予想")
    st.success(predict(race["選手"]))

    st.caption("※ 現在は仮AIです。今後、本物のAI学習モデル（LightGBMなど）に進化予定。")
