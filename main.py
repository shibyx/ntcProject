from flask import Flask
from datetime import datetime
from datetime import date
app = Flask(__name__)

current_date = datetime.now().date()
current_time = datetime.now().time()

@app.route('/')
def index():
    return f"Hello world. Today is {current_date}. Time is {current_time}"
if __name__ == "__main__":
    app.run(debug=True)