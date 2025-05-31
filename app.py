# このコードは Streamlit Cloud またはローカルで実行可能です。

try:
    import streamlit as st
    from datetime import datetime, timedelta
    import random

    # ページ設定
    st.set_page_config(page_title="賭神様｜AI予想", layout="centered")
    st.title("賭神様｜AI予想")

    # 日本時刻表示
    now = datetime.utcnow() + timedelta(hours=9)
    st.markdown(f"#### 現在の日本時刻：{now.strftime('%Y-%m-%d %H:%M:%S')}")

    # 日付選択（本日 or 翌日）
    today = now.date()
    tomorrow = today + timedelta(days=1)
    date_option = st.selectbox("日付を選択", [today.strftime("%Y-%m-%d"), tomorrow.strftime("%Y-%m-%d")])

    # モード選択：競艇 or 競馬
    mode = st.radio("モードを選択", ("競艇", "競馬"))

    # レース場とレース番号
    boat_courses = ["桐生", "住之江", "浜名湖"]
    horse_courses = ["東京", "中山", "阪神"]

    if mode == "競艇":
        course = st.selectbox("競艇場を選択", boat_courses)
        max_horses = 6
    else:
        course = st.selectbox("競馬場を選択", horse_courses)
        max_horses = 18

    race_nums = [f"{i}R" for i in range(1, 13)]
    race_number = st.selectbox("レース番号を選択", race_nums)

    # 出走表（簡易サンプル）
    def get_dummy_entries(n):
        return [f"{i}号艇（選手{i}）" for i in range(1, n+1)]

    st.markdown("##### 出走表（仮データ）")
    st.write(get_dummy_entries(max_horses))

    # AI予想（単レース）
    if st.button("このレースをAI予想"):
        prediction = random.sample(range(1, max_horses+1), 3)
        marks = ["◎", "○", "▲", "△"]
        mark = random.choice(marks)
        st.success(f"{course} {race_number}：{prediction[0]} - {prediction[1]} - {prediction[2]}　本命 {mark}")

    # 一括AI予想（1〜12R）
    if st.button("全12R分を一括AI予想"):
        for r in range(1, 13):
            prediction = random.sample(range(1, max_horses+1), 3)
            mark = random.choice(["◎", "○", "▲", "△"])
            st.info(f"{course} {r}R：{prediction[0]} - {prediction[1]} - {prediction[2]}　本命 {mark}")

    # クレジット
    st.markdown("---")
    st.markdown("制作：日本トップワールド　小島崇彦")

except ModuleNotFoundError as e:
    import sys
    sys.stderr.write("⚠️ Streamlit がインストールされていません。\n")
    sys.stderr.write("➡️ pip install streamlit を実行してください。\n")
    sys.stderr.write(f"詳細エラー: {e}\n")
