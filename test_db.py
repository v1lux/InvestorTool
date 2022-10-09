from postgres_conn import pg_conn


db = pg_conn()

with db:
    crs = db.cursor()
    query = """INSERT INTO "public"."InvestorTool" (company_name,ticker,exchange,industry,company_location,file_url) 
    VALUES (%s, %s, %s, %s, %s, %s)"""
    crs.execute(query, ('Apple Inc.', 'AAPL', 'NYSE', 'Software', 'Cupertino; U.S.A.', 'AAPL_risk.html'))
    crs.execute(query, ('Apple Inc.', 'AAPL', 'NYSE', 'Software', 'Cupertino; U.S.A.', 'AAPL_risk.html'))
    # res = crs.fetchall()
    # print(res)

# querry = """INSERT INTO "public"."InvestorTool" (company_name, ticker, exchange, industry,company_location,file_url) VALUES
# 	 ('UIPATH INC','PATH', 'NYSE', 'Software', 'New York; U.S.A.', 'PATH_risk.html')"""

# query = """INSERT INTO "public"."InvestorTool" (company_name, ticker, exchange, industry, company_location,file_url)
# VALUES ('%s','%s', '%s', '%s', '%s', '%s')"""


