from flask import Flask, render_template, request
from calculator import get_income_in_minutes

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    price_in_minutes = None
    if request.method == 'POST':
        monthly_income = float(request.form['monthly-income'])
        monthly_hours = float(request.form['monthly-hours'])
        price = float(request.form['price'])
        income_in_minutes = get_income_in_minutes(
            monthly_income=monthly_income, monthly_hours=monthly_hours)
        price_in_minutes = price / income_in_minutes
    has_price_in_minutes = price_in_minutes is not None
    return render_template(
        'index.html',
        has_price_in_minutes=has_price_in_minutes,
        price_in_hours=f'{price_in_minutes/60:.2f}' if has_price_in_minutes else None,
        price_in_minutes=f'{price_in_minutes:.2f}' if has_price_in_minutes else None,
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
