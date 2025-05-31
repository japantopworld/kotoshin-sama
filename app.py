# 🎯 賭神様 - AI予想アプリ ホーム画面

import streamlit as st
from datetime import datetime, timedelta

# ページ設定
st.set_page_config(page_title="賭神様｜AI予想アプリ", layout="centered")

st.title("🎯 賭神様 - AI予想アプリ")
now = datetime.utcnow() + timedelta(hours=9)
st.markdown(f"🕒 現在の時刻：**{now.strftime('%Y年%m月%d日 %H:%M:%S')}**（日本時間）")

# 注意事項
st.markdown("### 📌 注意事項")
st.info("""
- 本アプリはあくまで参考予想です。的中や損益を保証するものではありません。
- 20歳未満の方は公営ギャンブルに参加できません。
- 予想結果の利用は自己責任でお願いします。
""")

# 同意チェック
agree = st.checkbox("上記の注意事項に同意します")
if agree:
    st.success("✅ 同意が確認されました。以下から予想を開始してください。")

    st.markdown("### 🚀 予想したい競技を選んでください")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🛥 競艇"):
            st.switch_page("pages/kyotei.py")
        if st.button("🏍 オートレース"):
            st.switch_page("pages/auto.py")

    with col2:
        if st.button("🏇 競馬"):
            st.switch_page("pages/keiba.py")
        if st.button("🚲 競輪"):
            st.switch_page("pages/keirin.py")

    with col3:
        if st.button("⚡ ピストシックス"):
            st.switch_page("pages/pist6.py")
else:
    st.warning("⚠️ 利用には注意事項への同意が必要です。")

# フッター
st.markdown("---")
st.caption("制作：日本トップワールド 小島崇彦｜Powered by Streamlit")
