# scraper_kyotei.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_kyotei_data(race_url: str) -> pd.DataFrame:
    res = requests.get(race_url)
    soup = BeautifulSoup(res.content, "html.parser")

    data = []
    rows = soup.select("table.is-w495 tbody tr")

    for row in rows:
        tds = row.find_all("td")
        if len(tds) < 8:
            continue
        data.append({
            "艇番": int(tds[0].text.strip()),
            "選手名": tds[1].text.strip(),
            "体重": float(tds[2].text.strip()),
            "調整": tds[3].text.strip(),
            "チルト": float(tds[4].text.strip()),
            "展示": float(tds[5].text.strip()),
            "進入": int(tds[6].text.strip()),
            "ST": float(tds[7].text.strip())
        })

    return pd.DataFrame(data)
