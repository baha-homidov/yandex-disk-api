# Yandex Disk API Flask App

This project is a Flask-based web application that interacts with the Yandex Disk API. It allows users to enter their Yandex Disk OAuth token, view their disk information (such as total and used space), see a list of files, and download files from Yandex Disk.

## Requirements

- Python 3.x
- Yandex Disk OAuth token (used to authenticate requests to Yandex Disk API)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yandex-disk-flask-app.git
   cd yandex-disk-flask-app
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate  # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Start the app

```bash
    python app.py
```

Open your web browser and navigate to http://localhost:3000.
