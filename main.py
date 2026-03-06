from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

# Alpaca Bilgileri (Burası borsaya bağlanmamızı sağlar)
ALPACA_KEY = "BURAYA_KEY_ID_YAZ"
ALPACA_SECRET = "BURAYA_SECRET_KEY_YAZ"
URL = "https://paper-api.alpaca.markets/v2/orders"

@app.post("/webhook")
async def sinyal_al(request: Request):
    veri = await request.json()
    
    # Güvenlik: Şifreniz doğru mu?
    if veri.get("password")!= "Mevlut123":
        return {"hata": "Yanlış şifre!"}

    # Alpaca'ya emir paketi hazırla
    emir = {
        "symbol": veri["ticker"],
        "qty": 1, 
        "side": veri["action"],
        "type": "market",
        "time_in_force": "gtc"
    }
    
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET
    }

    # Emri gönder
    cevap = requests.post(URL, json=emir, headers=headers)
    return cevap.json()
