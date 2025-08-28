from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.static_folder, "uploads")

@app.route("/")
def main_page():
    videos = [f for f in os.listdir(UPLOAD_FOLDER) if f.lower().endswith(('.mp4', '.webm', '.ogg'))]
    video_paths = [url_for('static', filename=f"uploads/{v}") for v in videos]
    return render_template("main_page/index.html", video_paths=video_paths)

@app.route("/video_player")
def video_player():
    video_file = request.args.get('file')
    if not video_file:
        return "No video specified", 400
    video_url = url_for('static', filename=f"uploads/{video_file}")
    return render_template("video_player/index.html", video=video_url, name=video_file)

if __name__ == "__main__":
    app.run(debug=True)
