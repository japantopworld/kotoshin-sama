# 🚀 BOATRACE 出走表 自動取得＆一覧表示（Streamlit版）

import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# ページ設定
st.set_page_config(page_title="BOATRACE 出走表", layout="wide")
st.title("🛥 BOATRACE｜本日の全出走表（公式自動取得）")

# 日付選択（本日・翌日）
today = datetime.utcnow() + timedelta(hours=9)
tomorrow = today + timedelta(days=1)
date_option = st.selectbox("📅 日付を選んでください", [
    today.strftime("%Y-%m-%d"),
    tomorrow.strftime("%Y-%m-%d")
])

# 会場一覧（拡充済み）
courses = {
    "桐生": "01", "戸田": "02", "江戸川": "03", "平和島": "04", "多摩川": "05",
    "浜名湖": "06", "蒲郡": "07", "常滑": "08", "津": "09", "三国": "10",
    "びわこ": "11", "住之江": "12", "尼崎": "13", "鳴門": "14", "丸亀": "15",
    "児島": "16", "宮島": "17", "徳山": "18", "下関": "19", "若松": "20",
    "芦屋": "21", "福岡": "22", "唐津": "23", "大村": "24",
    "桜本": "25", "洞海": "26", "小戸": "27", "徳重": "28", "谷山": "29",
    "新門司": "30", "柳川": "31", "熊本": "32", "荒尾": "33", "宮崎": "34"
}

# 出走表取得関数
def get_race_data(yyyyMMdd, course_id, course_name):
    dfs = []
    for race_no in range(1, 13):
        url = f"https://www.boatrace.jp/owpc/pc/race/racelist?rno={race_no}&jcd={course_id}&hd={yyyyMMdd}"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")

        table = soup.find("table", class_="is-w495")
        if not table:
            continue

        rows = table.find_all("tr")
        race_data = []
        for row in rows[1:]:
            cols = [col.text.strip() for col in row.find_all("td")]
            if cols:
                race_data.append(cols)

        if race_data:
            df = pd.DataFrame(race_data, columns=["枠番", "選手名", "年齢", "体重", "支部", "勝率", "展示", "進入", "ST"], dtype=str)
            df.insert(0, "レース", f"{course_name} {race_no}R")
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True) if dfs else None

# 全会場ループして出走表を表示
yyyyMMdd = date_option.replace("-", "")
for name, cid in courses.items():
    with st.expander(f"📍 {name} の出走表を表示"):
        df = get_race_data(yyyyMMdd, cid, name)
        if df is not None:
            st.dataframe(
                df.style.set_table_styles([
                    {'selector': 'th', 'props': [('text-align', 'center')]},
                    {'selector': 'td', 'props': [('text-align', 'center'), ('font-family', 'monospace')]}
                ]),
                use_container_width=True
            )
        else:
            st.warning(f"{name} の出走表がまだ公開されていないか、取得できませんでした。")

st.markdown("---")
st.caption("制作：日本トップワールド 小島崇彦｜データ提供：BOATRACE公式")
