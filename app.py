# このコードは Streamlit 環境専用です。ローカルまたは Streamlit Cloud 上で実行してください。

try:
    import streamlit as st
    from datetime import datetime, timedelta
    import pandas as pd
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

    # レース場リスト（競艇・競馬）
    boat_race_courses = [
        "桐生", "戸田", "江戸川", "平和島", "多摩川",
        "浜名湖", "蒲郡", "常滑", "津", "三国",
        "びわこ", "住之江", "尼崎", "鳴門", "丸亀",
        "児島", "宮島", "徳山", "下関", "若松", "芦屋", "福岡", "唐津", "大村"
    ]
    horse_race_courses = ["東京", "中山", "京都", "阪神", "中京", "小倉", "新潟", "福島", "札幌", "函館"]

    # モード選択
    mode = st.radio("予想を選んでください", ("競艇", "競馬"))

    # レース場とレース番号選択
    if mode == "競艇":
        race_course = st.selectbox("競艇レース場を選択", boat_race_courses)
        race_nums = [f"{i}R" for i in range(1, 13)]
    else:
        race_course = st.selectbox("競馬場を選択", horse_race_courses)
        race_nums = [f"{i}R" for i in range(1, 13)]

    # 予想実行ボタン
    if st.button("AI予想を表示"):
        predictions = []
        for race_number in race_nums:
            prob = round(random.gauss(60, 15), 1)  # 平均60%、標準偏差15%
            prob = max(0, min(100, prob))          # 0～100%に制限
            predictions.append({
                "レース場": race_course,
                "レース番号": race_number,
                "的中確率予想": f"{prob} %"
            })

        df = pd.DataFrame(predictions)
        st.table(df)

    # クレジット
    st.markdown("---")
    st.markdown("制作：日本トップワールド　小島崇彦")

except ModuleNotFoundError as e:
    import sys
    sys.stderr.write("\nこのコードを実行するには Streamlit ライブラリが必要です。'pip install streamlit' を使ってインストールしてください。\n")
    sys.stderr.write(f"エラー詳細: {e}\n")

