import logging
from flask import Flask, render_template, request, redirect, url_for, jsonify
from utils.yandex_api import get_file_list, get_user_info, get_download_url

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        public_key = request.form['public_key']  # OAuth token from the form

        # Validate the public_key by making a request to Yandex API
        user_info = get_user_info(public_key)
        
        if user_info:
            return redirect(url_for('main', public_key=public_key))
        else:
            return render_template('error.html', message="Invalid public_key or API request failed")

    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    public_key = request.args.get('public_key')

    if public_key:
        # Fetch the file list and user information using Yandex API
        files = get_file_list(public_key)
        user_info = get_user_info(public_key)

        if files and user_info:
            total_space_gb = round(user_info['total_space'] / (1024 ** 3), 2)  # Convert to GB
            used_space_gb = round(user_info['used_space'] / (1024 ** 3), 2)    # Convert to GB
            available_space_gb = round((user_info['total_space'] - user_info['used_space']) / (1024 ** 3), 2)

            return render_template('main.html', files=files, total_space_gb=total_space_gb, 
                                   used_space_gb=used_space_gb, available_space_gb=available_space_gb, user=user_info['user'])
        else:
            return render_template('error.html', message="Failed to fetch data from Yandex Disk")
    return redirect(url_for('index'))


@app.route('/download', methods=['GET'])
def download():
    public_key = request.args.get('public_key')  # OAuth token
    file_path = request.args.get('path')  # Path of the file to download

    if public_key and file_path:
        # Fetch the download URL using Yandex API
        download_info = get_download_url(public_key, file_path)

        if download_info:
            return jsonify(download_info)
        else:
            return jsonify({'error': 'Failed to get download URL'}), 400

    return jsonify({'error': 'Invalid request parameters'}), 400


@app.route('/error')
def error():
    return render_template('error.html', message="Something went wrong")


if __name__ == '__main__':
    app.run(port=3000, debug=True)
