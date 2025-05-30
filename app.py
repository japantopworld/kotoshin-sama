import streamlit as st
from datetime import datetime

# 予想リスト（好きに増やせます）
predictions = [
    "桐生 12R：1-2-3 本命 ◎",
    "住之江 10R：3-1-6 穴狙い △",
    "浜名湖 9R：2-4-1 安定狙い ○",
    "若松 8R：1-3-5 チャンスあり ☆",
    "多摩川 7R：4-2-1 人気集中 ▲",
]

# タイトル表示
st.title("賭神様｜競艇AI予想")

# 今の時刻を取得
now = datetime.now()

# 時刻の「分」を使って表示する予想を切り替える
minute = now.minute
index = minute % len(predictions)
current_prediction = predictions[index]

# 時刻を画面に表示
st.write(f"現在時刻: {now.strftime('%H:%M:%S')}")

# 予想を画面に表示
st.markdown(f"### 今日の予想:\n\n{current_prediction}")

# 10秒ごとにページを自動リロードして予想を更新する
st.markdown(
    """
    <script>
    setTimeout(function(){
        window.location.reload(1);
    }, 10000);
    </script>
    """, unsafe_allow_html=True)
