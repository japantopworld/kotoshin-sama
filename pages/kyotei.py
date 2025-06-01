import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime

# --- ページ設定 ---
st.set_page_config(page_title="競艇AI予想", layout="wide")
st.title("🚤 競艇AI予想 - 出走表＋予想結果")

# --- 本日の日付を取得（例: 20250601）---
today = datetime.now().strftime("%Y%m%d")
st.caption(f"📅 本日：{today}")

# --- URL構成（BOATRACEの出走表トップページ）---
BASE_URL = f"https://www.boatrace.jp/owpc/pc/race/raceindex?hd={today}"

# --- レース会場一覧を取得（10会場前後）---
def get_race_sites():
    try:
        res = requests.get(BASE_URL)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")
        site_tags = soup.select(".contentsFrameInner .race_place")  # 会場名
        href_tags = soup.select(".contentsFrameInner .race_place a")  # リンク
        sites = []
        for name_tag, href_tag in zip(site_tags, href_tags):
            name = name_tag.text.strip()
            href = href_tag.get("href")
            if href:
                full_url = f"https://www.boatrace.jp{href}"
                sites.append((name, full_url))
        return sites
    except Exception as e:
        st.error(f"会場の取得に失敗しました：{e}")
        return []

# --- 特定会場の第1R出走表を取得 ---
def get_race_table(site_url):
    try:
        race_url = site_url.replace("index", "beforeinfo") + "&rno=1"  # 第1レース用
        res = requests.get(race_url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")
        rows = soup.select("table.is-w495 tbody tr")

        players = []
        for row in rows:
            cols = row.select("td")
            if len(cols) >= 2:
                player_name = cols[1].text.strip()
                if player_name:
                    players.append(player_name)

        race_title_tag = soup.select_one(".headingBlock h2")
        race_title = race_title_tag.text.strip() if race_title_tag else "レース名不明"

        return {"レース名": race_title, "選手": players}
    except Exception as e:
        return {"エラー": str(e)}

# --- 仮AI予想（ランダム3連単） ---
def predict_ai(players):
    shuffled = players.copy()
    random.shuffle(shuffled)
    return f"🎯 予想：{shuffled[0]} → {shuffled[1]} → {shuffled[2]}"

# --- メイン処理 ---
sites = get_race_sites()

if not sites:
    st.warning("⚠️ 出走表データを取得できませんでした。")
else:
    for name, url in sites:
        st.divider()
        st.subheader(f"📍 開催地：{name}")
        data = get_race_table(url)

        if "エラー" in data:
            st.error(f"❌ 出走表取得エラー：{data['エラー']}")
            continue

        st.write(f"### 🚩 {data['レース名']}")
        for i, p in enumerate(data["選手"], start=1):
            st.write(f"{i}号艇：{p}")

        st.write("### 🤖 仮AI予想")
        prediction = predict_ai(data["選手"])
        st.success(prediction)

st.caption("※ 現在は仮AIです。今後、本物のAI学習モデル（LightGBMなど）に進化予定。")

