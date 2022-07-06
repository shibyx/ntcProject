import os
from flask import Flask
from datetime import datetime
from datetime import date
import pytz

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def index():
    mskTz = pytz.timezone("Europe/Moscow")
    timeInMSK = datetime.now(mskTz)
    current_date = datetime.now().date()
    current_time = timeInMSK.strftime("%H:%M:%S")
    return f"Hello world. Today is {current_date}. Time is {current_time} 123 test update"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
