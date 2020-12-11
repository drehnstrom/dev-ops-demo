from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def main():
    model = {"title": "Hello World!"}
    return render_template('index.html', model=model)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
