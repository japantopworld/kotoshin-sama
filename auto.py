# auto.py
import pandas as pd
from scraper_kyotei import get_kyotei_data
from kyotei_ai_predictor import train_and_predict

# 👇テスト用：実際の出走表URLを指定（例：ボートレース公式サイトのレース情報ページ）
race_url = "https://www.boatrace.jp/owpc/pc/race/racelist?rno=1&jcd=09&hd=20250603"

# 📥 出走表を取得
print("📦 出走表取得中...")
df = get_kyotei_data(race_url)
print(df.head())

# 仮にresult列をランダムで追加（本番は過去レースの学習に使用）
import numpy as np
df["race_id"] = "20250603_1"
df["result"] = np.random.randint(1, 7, size=len(df))

# 🤖 AI学習＆予測
print("🤖 AI予想中...")
result_df = train_and_predict(df)

# ✅ 予想結果を表示
print("✅ 予想結果：")
print(result_df)

