from flask import Flask, redirect, render_template, url_for, request, flash
import requests

app = Flask(__name__)


YANDEX_API_URL = 'https://cloud-api.yandex.net/v1/disk/'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        public_key = request.form.get('public_key')
        headers = {
            'Authorization': f'OAuth {public_key}'
        }

        # Try to access Yandex API
        response = requests.get(YANDEX_API_URL, headers=headers)

        if response.status_code == 200:
            # Redirect to /main if the request succeeds
            return redirect(url_for('main'))
        else:

            return redirect(url_for('error'))

    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
