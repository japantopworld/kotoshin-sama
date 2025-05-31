import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import random

# ページ設定（ダークテーマ対応）
st.set_page_config(page_title="賭神様｜AI予想", layout="centered")

# タイトルと時刻
st.markdown("<h1 style='text-align:center;'>賭神様｜AI予想</h1>", unsafe_allow_html=True)
japan_time = datetime.utcnow() + timedelta(hours=9)
st.markdown(f"<p style='text-align:center;'>現在の日本時刻：{japan_time.strftime('%Y-%m-%d %H:%M:%S')}</p>", unsafe_allow_html=True)

# 日付選択
today = japan_time.date()
tomorrow = today + timedelta(days=1)
selected_date = st.selectbox("日付を選択", [today, tomorrow])

# 競艇場一覧（拡充）
boat_race_courses = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川",
    "浜名湖", "蒲郡", "常滑", "津", "三国",
    "びわこ", "住之江", "尼崎", "鳴門", "丸亀",
    "児島", "宮島", "徳山", "下関", "若松",
    "芦屋", "福岡", "唐津", "大村"
]

# UI選択
mode = st.radio("モード選択", ["競艇（AI）", "競艇（出走表取得）"])

race_course = st.selectbox("レース場を選択", boat_race_courses)
race_number = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

# 出走表取得関数（簡易・BOAT RACEオフィシャルHTML取得）
def fetch_race_table(place, date, race_no):
    place_ids = {
        "桐生": 1, "戸田": 2, "江戸川": 3, "平和島": 4, "多摩川": 5,
        "浜名湖": 6, "蒲郡": 7, "常滑": 8, "津": 9, "三国": 10,
        "びわこ": 11, "住之江": 12, "尼崎": 13, "鳴門": 14, "丸亀": 15,
        "児島": 16, "宮島": 17, "徳山": 18, "下関": 19, "若松": 20,
        "芦屋": 21, "福岡": 22, "唐津": 23, "大村": 24
    }
    target_id = place_ids.get(place)
    ymd = date.strftime("%Y%m%d")
    url = f"https://www.boatrace.jp/owpc/pc/race/racelist?rno={race_no[:-1]}&jcd={str(target_id).zfill(2)}&hd={ymd}"
    res = requests.get(url)
    if res.status_code != 200:
        return "出走表を取得できませんでした。"
    soup = BeautifulSoup(res.text, "html.parser")
    rows = soup.select("table.is-w495 tbody tr")
    data = []
    for row in rows:
        cols = [col.text.strip() for col in row.find_all("td")]
        if len(cols) >= 5:
            data.append(cols[:5])
    df = pd.DataFrame(data, columns=["枠", "選手名", "登録番号", "級別", "支部"])
    return df if not df.empty else "出走表データがありません。"

# AI予想ロジック（簡易・ルールベース）
def ai_prediction():
    return f"{race_course} {race_number} 本命：1-2-3（的中率優先）"

# 表示切り替え
if st.button("予想／出走表を表示"):
    if mode == "競艇（AI）":
        st.success(ai_prediction())
    else:
        result = fetch_race_table(race_course, selected_date, race_number)
        if isinstance(result, str):
            st.error(result)
        else:
            st.dataframe(result)

# フッター
st.markdown("---")
st.markdown("<p style='text-align:center;'>制作：日本トップワールド　小島崇彦</p>", unsafe_allow_html=True)
