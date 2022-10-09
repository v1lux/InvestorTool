from flask import Flask, render_template, request, redirect, url_for
from module import get_company_details, get_10k_url_by_ticker, get_risk_section, get_tickers

app = Flask('Investor Tool')


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


# @app.route('/temp/', methods=['GET', 'POST'])
# def temp():
#     if request.method == 'POST':
#         search_ticker = request.form['get_ticker']
#         return render_template('temp.html', title='Investor tool',
#                                search_hits=get_tickers(search_ticker))


@app.route('/search/', methods=['POST'])
def search():
    if request.method == 'POST':
        ticker = request.form['ticker']
        return render_template('search.html', title='Investor tool',
                               detailed_information=get_company_details(ticker),
                               risk=get_risk_section(ticker),
                               annual_report_URL=get_10k_url_by_ticker(ticker))


@app.route('/watchlist/')
def watchlist():
    return render_template('watchlist.html')


if __name__ == '__main__':
    app.run(debug=True)
