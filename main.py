from fastapi import FastAPI, Request
import requests
import uvicorn

app = FastAPI()

# Buraya Alpaca'dan aldığınız anahtarları yazın
ALPACA_KEY = "PKD4VGJJ36TKA6P76LOR2YHGNF"
ALPACA_SECRET = "AAXCDTv2Q5DLgrxRxFy2v9tiiPS9CrGuZnfuGFcWn59u"
BASE_URL = "https://paper-api.alpaca.markets"

@app.post("/webhook")
async def sinyal_yakala(request: Request):
    veri = await request.json()
    
    # Güvenlik Kontrolü [2]
    if veri.get("secret")!= "Mevlut123":
        return {"hata": "Yetkisiz sinyal!"}
    
    # Alpaca'ya Emir Gönder 
    endpoint = f"{BASE_URL}/v2/orders"
    payload = {
        "symbol": veri["ticker"],
        "qty": 1, # 1 adet al/sat. Gelişmiş sistemde bu hesaplanır.
        "side": veri["action"],
        "type": "market",
        "time_in_force": "gtc"
    }
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET
    }
    
    cevap = requests.post(endpoint, json=payload, headers=headers)
    return cevap.json()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
