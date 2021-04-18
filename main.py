from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    price_in_hours = None
    price_in_minutes = None
    if request.method == 'POST':
        yearly_income = 1000. * float(request.form['yearly-k'])
        price = float(request.form['price'])
        # 262 working days, 8 hours a day
        hourly_income = yearly_income / (262 * 8)
        price_in_hours = price / hourly_income
        price_in_minutes = price_in_hours * 60.
    has_price_in_hours = price_in_hours is not None
    return render_template(
        'index.html',
        has_price_in_hours=has_price_in_hours,
        price_in_hours=f'{price_in_hours:.2f}' if price_in_hours is not None else None,
        price_in_minutes=f'{price_in_minutes:.0f}' if price_in_minutes is not None else None,
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
