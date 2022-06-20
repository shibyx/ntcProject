import os
from flask import Flask
from datetime import datetime
from datetime import date
app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))


@app.route('/')
def index():
    current_date = datetime.now().date()
    current_time = datetime.now().time()
    return f"Hello world. Today is {current_date}. Time is {current_time}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
