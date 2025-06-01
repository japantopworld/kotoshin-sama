import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

st.set_page_config(page_title="競艇AI予想", layout="wide")
st.title("🚤 今日の競艇AI予想 - 出走表＋予想")

# --- 設定 ---
BASE_URL = "https://www.boatrace.jp/owpc/pc/race/raceindex?hd=20250601"
RACE_URL_TEMPLATE = "https://www.boatrace.jp/owpc/pc/race/racelist?rno={rno}&jcd={jcd}&hd={date}"

dummy_players = ["今垣光太郎", "白井英治", "峰竜太", "毒島誠", "瓜生正義", "平本真之"]

# --- 会場一覧を取得 ---
def get_venues(date_str):
    try:
        res = requests.get(BASE_URL)
        soup = BeautifulSoup(res.content, "html.parser")
        venue_tags = soup.select(".contentsFrameInner .racePlace")
        venue_codes = [tag['href'].split("jcd=")[1].split("&")[0] for tag in venue_tags]
        venue_names = [tag.text.strip() for tag in venue_tags]
        return list(zip(venue_codes, venue_names))
    except:
        return []

# --- 出走表を取得（仮：ランダム6人） ---
def get_race_players(jcd, rno, date_str):
    # 本物の取得は後日
    players = random.sample(dummy_players, 6)
    return players

# --- AI予想（仮ロジック） ---
def predict_ai(players):
    shuffled = players.copy()
    random.shuffle(shuffled)
    return f"{shuffled[0]} → {shuffled[1]} → {shuffled[2]}"

# --- 表示処理 ---
date_str = "20250601"
venues = get_venues(date_str)

if not venues:
    st.error("⚠️ 出走表データを取得できませんでした。")
else:
    for jcd, name in venues:
        st.subheader(f"🏁 {name}（コード: {jcd}）")
        for rno in range(1, 13):
            st.write(f"### {rno}R 出走表")
            players = get_race_players(jcd, rno, date_str)
            for i, p in enumerate(players):
                st.write(f"{i+1}号艇：{p}")
            st.success(f"🎯 AI予想：{predict_ai(players)}")
        st.markdown("---")
