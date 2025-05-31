# このコードは Streamlit が動作する環境専用です。ローカルや Streamlit Cloud 上でご利用ください。

try:
    import streamlit as st
    from datetime import datetime, timedelta
    import random

    # ページ設定とタイトル
    st.set_page_config(page_title="賭神様｜AI予想", layout="centered")
    st.title("賭神様｜AI予想")

    # 現在の日本時刻を表示
    now = datetime.utcnow() + timedelta(hours=9)
    st.markdown(f"### 現在の日本時刻：{now.strftime('%Y-%m-%d %H:%M:%S')}")

    # 日付選択（本日と翌日の選択）
    today = datetime.utcnow() + timedelta(hours=9)
    tomorrow = today + timedelta(days=1)
    date_option = st.selectbox("日付を選択", [
        today.strftime("%Y-%m-%d"),
        tomorrow.strftime("%Y-%m-%d")
    ])

    # レース場リスト
    boat_race_courses = ["桐生", "住之江", "浜名湖"]
    horse_race_courses = ["東京", "中山", "阪神"]

    # モード選択
    mode = st.radio("予想を選んでください", ("競艇", "競馬"))

    # レース場とレース番号選択
    if mode == "競艇":
        race_course = st.selectbox("競艇レース場を選択", boat_race_courses)
        race_nums = [f"{i}R" for i in range(1, 13)]
    else:
        race_course = st.selectbox("競馬場を選択", horse_race_courses)
        race_nums = [f"{i}R" for i in range(1, 13)]

    race_number = st.selectbox("レース番号を選択", race_nums)

    # AI予想ボタン
    if st.button("AI予想を表示"):
        if mode == "競艇":
            numbers = random.sample(range(1, 7), 3)
        else:
            numbers = random.sample(range(1, 18), 3)
        marks = ["◎", "○", "▲", "△"]
        mark = random.choice(marks)
        prediction = f"{race_course} {race_number}：{numbers[0]}-{numbers[1]}-{numbers[2]} 本命 {mark}"
        st.success(prediction)

    # クレジット
    st.markdown("---")
    st.markdown("制作：日本トップワールド　小島崇彦")

except ModuleNotFoundError as e:
    import sys
    sys.stderr.write("\nこのコードを実行するには Streamlit ライブラリが必要です。'pip install streamlit' を使ってインストールしてください。\n")
    sys.stderr.write(f"エラー詳細: {e}\n")
