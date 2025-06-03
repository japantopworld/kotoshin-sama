# kyotei_ai_predictor.py
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_and_predict(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    X = df.drop(['race_id', 'result'], axis=1)
    y = df['result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = lgb.LGBMClassifier()
    model.fit(X_train, y_train)

    df['ai_prediction'] = model.predict(X)
    df['correct'] = (df['ai_prediction'] == df['result'])

    accuracy = accuracy_score(y, df['ai_prediction'])
    print(f"AI予想の精度: {accuracy:.2%}")

    return df[['race_id', 'result', 'ai_prediction', 'correct']]
