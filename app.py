from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def main_page():
        return render_template("main_page/index.html")

if __name__ == "__main__":
        app.run(debug=False)