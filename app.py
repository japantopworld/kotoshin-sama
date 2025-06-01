import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="賭神様｜予想AIスタート", layout="centered")
st.title("🎌 賭神様 - スタートメニュー")

# 現在時刻の表示（日本時間）
now = datetime.utcnow()
jst = now.hour + 9
jst_day = now.strftime('%Y-%m-%d')
st.write(f"🕒 現在時刻（日本時間）: {jst_day} {jst%24:02d}:{now.minute:02d}")

# 説明・注意事項
with st.expander("📜 はじめにお読みください"):
    st.markdown("""
    - このアプリは **競艇・競馬・オート・競輪・ピスト6** のAI予想を目指して開発中です。
    - 公式情報を元にした分析予想です。
    - 将来的には高的中率AI・自動更新・カスタマイズ機能も搭載予定です。
    """)

    agree = st.checkbox("✅ 同意して使う")
    if not agree:
        st.stop()

# ボタンでページを選択
st.subheader("🎮 予想カテゴリを選んでください")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎯 競艇"):
        st.switch_page("pages/kyotei.py")
with col2:
    if st.button("🏇 競馬"):
        st.switch_page("pages/keiba.py")
with col3:
    if st.button("🏍️ オートレース"):
        st.switch_page("pages/auto.py")

col4, col5, _ = st.columns(3)
with col4:
    if st.button("🚴 競輪"):
        st.switch_page("pages/keirin.py")
with col5:
    if st.button("🎽 PIST6"):
        st.switch_page("pages/pist6.py")

st.markdown("---")
st.caption("制作：日本トップワールド 小島崇彦")
