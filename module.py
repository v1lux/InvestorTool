import requests
from sec_api import QueryApi, ExtractorApi


# api_key = "1bd1e3119459aa11d5f1d2c9a8cce932c1affe9ad397e9fd4e3bcb79f9e87a12"
api_key = "9e17d9cd2d36e9e441b07ae9798e0307b7932f66c354402068e6a29c3ee02e29"
# api_key = "949b34bed2aa1f1c7b2146ecbc84c78d1411ae9d309c75fa02f27702d861572f"


def get_tickers(company_name: str):
    url = "https://www.sec.gov/files/company_tickers.json"
    response = requests.get(url).json()
    founded_companies = []
    for item in response.items():
        title = item[1]['title']
        ticker = item[1]['ticker']

        if (company_name.lower() in title.lower()) or (company_name.lower() in ticker.lower()):
            founded_companies.append((title, ticker))
    return founded_companies


def get_company_details(tckr: str):
    """ returns a dictionary with company information (name, ticker, exchange, industry, location etc)
    more details on: https://sec-api.io/docs/mapping-api/map-ticker-to-company-details """
    api_endpoint = "https://api.sec-api.io/mapping"
    api_url = api_endpoint + "/ticker/^" + tckr + "$?token=" + api_key
    response = requests.get(api_url)
    dct = response.json()[0]
    # print(dct)
    return dct


def get_10k_url_by_ticker(tckr: str):
    query_api = QueryApi(api_key)
    query = {
      "query": { "query_string": {
          "query": f"ticker:{tckr} AND formType:\"10-K\"" +
                   "AND NOT formType:\"NT 10-K\" " +
                   "AND NOT formType:\"10-K/A\" ",
          "time_zone": "America/New_York"
      } },
      "from": "0",
      "size": "10",
      "sort": [{ "filedAt": { "order": "desc" } }]
    }
    filings = query_api.get_filings(query)
    url = filings['filings'][0]['documentFormatFiles'][0]['documentUrl']
    return url


def get_risk_section(tckr: str):
    """extracts the risk section from the latest Annual Report (10K filling, html version)"""
    extractor_api = ExtractorApi(api_key)
    url = get_10k_url_by_ticker(tckr)
    risk_section = extractor_api.get_section(url, "1A", "html")
    # print(risk_section)
    path = f"risk_reports/{tckr}_risk.html"
    with open(path, 'w') as f:
        f.write(risk_section)
    return risk_section


def add_to_watchlist():
    pass
