import psycopg2
from flask import Flask, render_template, request, redirect, url_for
from module import get_company_details, get_10k_url_by_ticker, get_risk_section, get_tickers, insert_to_db, del_from_db
from postgres_conn import pg_conn


app = Flask('Investor Tool')
db = pg_conn()

# ticker = 'IBM'
# https://www.sec.gov/files/company_tickers.json

@app.route('/')
@app.route('/home/', methods=['POST'])
def home():
    if request.method == 'POST':
        search_ticker = request.form['get_ticker']
        return render_template('home.html', title='Investor tool',
                               search_hits=get_tickers(search_ticker))
    return render_template('home.html', title='Investor tool')


@app.route('/search/', methods=['POST'])
def search():
    if request.method == 'POST':
        ticker = request.form['ticker']

        return render_template('search.html', title='Investor tool',
                               detailed_information=get_company_details(ticker),
                               risk=get_risk_section(ticker),
                               annual_report_URL=get_10k_url_by_ticker(ticker))


@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        srch = request.form
    else:
        srch = request.args

    added = srch.get('insert_sql')
    insert_to_db(added)
    msg = f"Company {added} was added!"
    return render_template('add.html', title='DB insert',
                           company=added,
                           m=msg)


@app.route('/del/', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        srch = request.form
    else:
        srch = request.args

    deleted = srch.get('del_sql')
    del_from_db(deleted)
    msg = f"Company {deleted} was deleted from watchlist!"
    return render_template('del.html', title='DB delete',
                           company=deleted,
                           m=msg)


@app.route('/watchlist/<ticker_url>/')
def show(ticker_url):
    # ticker = 'IBM'
    # url = f'{ticker}.html'
    ticker = ticker_url.split('.')[0]
    file_path = f"watchlist/{ticker_url}"
    with open(file_path, 'r') as f:
        my_file = f.read()

    return render_template('company.html', title='ticker', c=ticker, file=my_file)


@app.route('/watchlist/')
def watchlist():
    with db:
        query = """select * from "public"."InvestorTool" as IT """
        crs = db.cursor()
        crs.execute(query)
        info = crs.fetchall()
    return render_template('watchlist.html', data=info, title="Watchlist")


if __name__ == '__main__':
    app.run(debug=True)
