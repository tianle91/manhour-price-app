from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    price_in_hours = None
    if request.method == 'POST':
        yearly_income = 1000. * float(request.form['yearly-income-in-thousands'])
        price = float(request.form['price'].strip().lower())
        # 262 working days, 8 hours a day
        hourly_income = yearly_income / (262 * 8)
        price_in_hours = price / hourly_income
    return render_template('index.html', price_in_hours=price_in_hours)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
