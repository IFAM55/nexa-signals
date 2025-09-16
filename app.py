from flask import Flask, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

openai.api_key = 'YOUR_OPENAI_KEY'

@app.route("/get_signals")
def get_signals():
    prompt = """
    Generate 3 crypto trading signals (BTC, ETH, ADA) with format:
    Time: Morning/Afternoon/Night
    Coin: BTC/ETH/ADA
    Type: Buy/Sell
    Price: ...
    Target: ...
    Stop-loss: ...
    Return as JSON array
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=250
    )

    raw_text = response.choices[0].text.strip()
    
    # Convert OpenAI output to JSON
    import json
    try:
        signals = json.loads(raw_text)
    except:
        signals = [
            {"time": "Morning", "coin": "BTC", "type": "Buy", "price": "29500", "target": "30200", "stoploss": "29000"},
            {"time": "Afternoon", "coin": "ETH", "type": "Sell", "price": "1850", "target": "1800", "stoploss": "1880"},
            {"time": "Night", "coin": "ADA", "type": "Buy", "price": "0.35", "target": "0.38", "stoploss": "0.34"}
        ]
    return jsonify(signals)

if __name__ == "__main__":
    app.run(port=5000)
