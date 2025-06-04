import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import random

# ======= 設定エリア =======
GMAIL_USER = "japantopworld@gmail.com"
APP_PASSWORD = "agrq jmit jxvz nrdt"  # ←Gmailアプリパスワード（半角スペースOK）
TO_EMAIL = "taka9121@icloud.com"
# ===========================

# 仮AI予想（競艇・競馬ランダム予想）
def make_predictions(label, race_list):
    result = f"📊 {label} AI予想 上位5件：\n"
    for i, race in enumerate(race_list[:5]):
        players = race["選手"]
        shuffled = players.copy()
        random.shuffle(shuffled)
        result += f"\n第{i+1}R：{shuffled[0]} → {shuffled[1]} → {shuffled[2]}"
    return result

# 仮レースデータ（競艇6レース・競馬5レース）
boat_races = [
    {"選手": ["今垣光太郎", "白井英治", "峰竜太", "毒島誠", "瓜生正義", "平本真之"]},
    {"選手": ["桐生順平", "赤岩善生", "松井繁", "石野貴之", "岡崎恭裕", "井口佳典"]},
    {"選手": ["寺田祥", "濱野谷憲吾", "西山貴浩", "篠崎元志", "前本泰和", "茅原悠紀"]},
    {"選手": ["馬場貴也", "石渡鉄兵", "山口剛", "田村隆信", "菊地孝平", "山田康二"]},
    {"選手": ["岡崎恭裕", "白井英治", "平高奈菜", "大山千広", "遠藤エミ", "守屋美穂"]},
    {"選手": ["井口佳典", "毒島誠", "峰竜太", "桐生順平", "石野貴之", "松井繁"]}
]

horse_races = [
    {"選手": ["イクイノックス", "ドウデュース", "ジャスティンパレス", "スターズオンアース", "タイトルホルダー", "ソールオリエンス"]},
    {"選手": ["リバティアイランド", "ソングライン", "ナミュール", "サウンズオブアース", "シャフリヤール", "ダノンベルーガ"]},
    {"選手": ["パンサラッサ", "ジオグリフ", "ヴェラアズール", "キタサンブラック", "シンボリクリスエス", "エフフォーリア"]},
    {"選手": ["グランアレグリア", "アーモンドアイ", "クロノジェネシス", "ラッキーライラック", "サートゥルナーリア", "フィエールマン"]},
    {"選手": ["ドゥラメンテ", "コントレイル", "アスクビクターモア", "シンハライト", "リアアメリア", "マカヒキ"]}
]

# 日付と本文生成
jst_now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
today_str = jst_now.strftime("%Y-%m-%d")

boat_predictions = make_predictions("🚤 競艇", boat_races)
horse_predictions = make_predictions("🐎 競馬", horse_races)

body = f"""📅 {today_str} のAI予想結果

{boat_predictions}

-------------------------------

{horse_predictions}

📩 Powered by 賭神様AI（仮）
"""

# メール送信処理
msg = MIMEMultipart()
msg["Subject"] = f"{today_str}：競艇・競馬AI予想（上位5）"
msg["From"] = GMAIL_USER
msg["To"] = TO_EMAIL
msg.attach(MIMEText(body, "plain"))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, APP_PASSWORD)
        server.send_message(msg)
    print("✅ メール送信完了！")
except Exception as e:
    print("❌ メール送信に失敗しました:", e)
