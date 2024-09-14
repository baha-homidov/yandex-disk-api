from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


YANDEX_API_URL = 'https://cloud-api.yandex.net/v1/disk/'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        public_key = request.form['public_key']

        # Save public_key in session or pass it around
        response = requests.get(YANDEX_API_URL, headers={
            'Authorization': f'OAuth {public_key}'
        })

        if response.status_code == 200:
            return redirect(url_for('main', public_key=public_key))
        else:
            return render_template('error.html', message="Invalid public_key or API request failed")

    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    public_key = request.args.get('public_key')

    if public_key:
        headers = {
            'Authorization': f'OAuth {public_key}'
        }

        # Fetch file list
        file_response = requests.get(
            YANDEX_API_URL + 'resources/files', headers=headers)

        # Fetch user information
        user_info_response = requests.get(YANDEX_API_URL, headers=headers)

        if file_response.status_code == 200 and user_info_response.status_code == 200:
            files = file_response.json()['items']

            user_info = user_info_response.json()
            total_space_gb = round(
                user_info['total_space'] / (1024 ** 3), 2)  # Convert to GB
            used_space_gb = round(
                user_info['used_space'] / (1024 ** 3), 2)    # Convert to GB
            available_space_gb = round(
                (user_info['total_space'] - user_info['used_space']) / (1024 ** 3), 2)  # Convert to GB

            return render_template('main.html', files=files, total_space_gb=total_space_gb, used_space_gb=used_space_gb, available_space_gb=available_space_gb, user=user_info['user'])
        else:
            return render_template('error.html', message="Failed to fetch data from Yandex Disk")

    return redirect(url_for('index'))


@app.route('/error')
def error():
    return render_template('error.html', message="Something went wrong")


if __name__ == '__main__':
    app.run(port=3000, debug=True)
