# 🔮 完全版：競艇AI予想（出走表＋全レース表示＋現在時刻＋開催地）

import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime

st.set_page_config(page_title="競艇AI予想", layout="wide")

# --- 設定 ---
TODAY = datetime.now().strftime("%Y%m%d")
BASE_URL = f"https://www.boatrace.jp/owpc/pc/race/raceindex?hd={TODAY}"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# --- ヘッダー ---
st.title("🚤 競艇AI予想 - 出走表＋予想")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.write(f"🕐 現在時刻：{now}")

# --- 開催地名を取得 ---
def get_place_name():
    try:
        res = requests.get(BASE_URL, headers=HEADERS)
        soup = BeautifulSoup(res.content, "html.parser")
        title = soup.select_one("h2.heading02")
        return title.text.strip() if title else "開催地不明"
    except:
        return "取得失敗"

# --- レースリンクを取得（全R）---
def get_race_links():
    try:
        res = requests.get(BASE_URL, headers=HEADERS)
        soup = BeautifulSoup(res.content, "html.parser")
        links = soup.select("ul.race_num li a")
        race_urls = ["https://www.boatrace.jp" + link["href"] for link in links]
        return race_urls
    except:
        return []

# --- 出走表取得 ---
def get_race_info(url):
    try:
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.content, "html.parser")

        race_name = soup.select_one("div.race_title h3")
        race_title = race_name.text.strip() if race_name else "レース名不明"

        rows = soup.select("table.boatRaceMembersTable tbody tr")
        players = [td.text.strip() for row in rows for td in row.select("td.is-name")]
        return race_title, players
    except:
        return "取得エラー", []

# --- 仮AI予想（ランダム3連単） ---
def predict(players):
    if len(players) < 3:
        return "予想不可"
    pick = players.copy()
    random.shuffle(pick)
    return f"🎯 予想：{pick[0]} → {pick[1]} → {pick[2]}"

# --- メイン表示 ---
st.header(f"📍 開催地：{get_place_name()}")

race_urls = get_race_links()

if not race_urls:
    st.error("⚠️ 出走表データを取得できませんでした。")
else:
    for url in race_urls:
        race_title, players = get_race_info(url)
        st.subheader(f"📝 {race_title}")
        if players:
            for i, p in enumerate(players, 1):
                st.write(f"{i}号艇：{p}")
            st.success(predict(players))
        else:
            st.warning("選手情報を取得できませんでした。")
        st.markdown("---")
