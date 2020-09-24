from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def main():
<<<<<<< HEAD
    model = {"title": "Hello 2 Sigma!!!!!!!!!!!!!!"}
=======
    model = {"title": "Hello Broadcom!!"}
>>>>>>> ec017662f56c85a7132f8a4030eb872d27585765
    return render_template('index.html', model=model)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
