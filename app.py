from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route("/get_stream", methods=["GET"])
def get_stream():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing URL"}), 400

    try:
        with YoutubeDL({'quiet': True, 'format': 'best[ext=mp4]/best'}) as ydl:
            info = ydl.extract_info(url, download=False)
            stream_url = info["url"]
            return jsonify({"stream_url": stream_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
