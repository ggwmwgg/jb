import csv
from sqlalchemy import create_engine, MetaData, Table, Column, Float, String, case, func
from sqlalchemy.orm import sessionmaker, mapper, column_property
from sqlalchemy.sql.expression import desc


engine = create_engine('sqlite:///investor.db?check_same_thread=False')
metadata = MetaData()

companies_t = Table('companies', metadata,
                    Column('ticker', String, primary_key=True),
                    Column('name', String),
                    Column('sector', String))

financial_t = Table('financial', metadata,
                    Column('ticker', String, primary_key=True),
                    Column('ebitda', Float, nullable=True),
                    Column('sales', Float, nullable=True),
                    Column('net_profit', Float, nullable=True),
                    Column('market_price', Float, nullable=True),
                    Column('net_debt', Float, nullable=True),
                    Column('assets', Float, nullable=True),
                    Column('equity', Float, nullable=True),
                    Column('cash_equivalents', Float, nullable=True),
                    Column('liabilities', Float, nullable=True))


class Companies(object):
    def __init__(self, ticker, name, sector):
        self.ticker = ticker
        self.name = name
        self.sector = sector


class Financial(object):
    def __init__(self, ticker, ebitda, sales, net_profit, market_price, net_debt,
                 assets, equity, cash_equivalents, liabilities):
        self.ticker = ticker
        self.ebitda = ebitda
        self.sales = sales
        self.net_profit = net_profit
        self.market_price = market_price
        self.net_debt = net_debt
        self.assets = assets
        self.equity = equity
        self.cash_equivalents = cash_equivalents
        self.liabilities = liabilities



mapper(Companies, companies_t)
mapper(Financial, financial_t)

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

query_com = session.query(Companies)
query_fin = session.query(Financial)

# try:
#     with open('companies.csv') as companies:
#         file_reader = csv.DictReader(companies, delimiter=",")
#         for line in file_reader:
#             session.add(Companies(ticker=line['ticker'], name=line['name'], sector=line['sector']))
#         session.commit()
#
#     with open('financial.csv') as financial:
#         file_reader = csv.DictReader(financial, delimiter=",")
#         for line in file_reader:
#             for value in line:
#                 if line[value] == '':
#                     line[value] = None
#                 if value != 'ticker':
#                     try:
#                         line[value] = float(line[value])
#                     except TypeError:
#                         continue
#             session.add(Financial(ticker=line['ticker'], ebitda=line['ebitda'], sales=line['sales'],
#                                   net_profit=line['net_profit'], market_price=line['market_price'],
#                                   net_debt=line['net_debt'], assets=line['assets'], equity=line['equity'],
#                                   cash_equivalents=line['cash_equivalents'], liabilities=line['liabilities']))
#         session.commit()
# except Exception:
#     pass


#print('Database created successfully!')


def main_menu():
    option = 0
    options = ['Exit', 'CRUD operations',
               'Show top ten companies by criteria']
    while True:
        print('MAIN MENU')
        for opt, i in zip(options, range(3)):
            print(f'{i} {opt}')
        try:
            option = int(input('Enter an option:\n'))
        except ValueError:
            print('Invalid option!')
            continue
        if option == 0:
            print('Have a nice day!')
            session.close()
            exit()

        elif option == 1:
            crud_menu()
            continue
        elif option == 2:
            top_ten_menu()
            continue
        else:
            print('Invalid option!')
            continue

def crud_menu():
    options = ['Back', 'Create a company', 'Read a company',
               'Update a company', 'Delete a company',
               'List all companies']
    while True:
        print('CRUD MENU')
        for opt, i in zip(options, range(6)):
            print(f'{i} {opt}')
        try:
            option = int(input('Enter an option:\n'))
        except ValueError:
            print('Invalid option!')
            continue
        if option == 0:
            print('Have a nice day!')
            break
        elif option == 1:
            create_company()

            break
        elif option == 2:
            read_company()
            break
        elif option == 3:
            update_company()
            break
        elif option == 4:
            delete_company()
            break
        elif option == 5:
            list_all_companies()
            break
        else:
            print('Invalid option!')
            continue

def create_company():
    ticker = str(input("Enter ticker (in the format 'MOON'):\n"))
    company = input("Enter company (in the format 'Moon Corp'):\n")
    industry = input("Enter industries (in the format 'Technology'):\n")
    ebitda = int(input("Enter ebitda (in the format '987654321'):\n"))
    sales = int(input("Enter sales (in the format '987654321'):\n"))
    net_profit = int(input("Enter net profit (in the format '987654321'):\n"))
    market_price = int(input("Enter market price (in the format '987654321'):\n"))
    net_debt = int(input("Enter net debt (in the format '987654321'):\n"))
    assets = int(input("Enter assets (in the format '987654321'):\n"))
    equity = int(input("Enter equity (in the format '987654321'):\n"))
    cash_equivalents = int(input("Enter cash equivalents (in the format '987654321'):\n"))
    liabilities = int(input("Enter liabilities (in the format '987654321'):\n"))
    session.add(Companies(ticker=ticker, name=company, sector=industry))
    session.add(Financial(ticker=ticker, ebitda=ebitda, sales=sales, net_profit=net_profit,
                            market_price=market_price, net_debt=net_debt, assets=assets,
                            equity=equity, cash_equivalents=cash_equivalents, liabilities=liabilities))
    session.commit()
    print('Company created successfully!')
    main_menu()

def read_company():
    name = input("Enter company name:\n")
    company = session.query(Companies).filter(Companies.name.contains(name)).all()
    if company is None:
        print('Company not found!')
        main_menu()
    elif len(company) == 0:
        print('Company not found!')
        main_menu()
    else: # list the matching companies with indexes
        for i, comp in zip(range(len(company)), company):
            print(f'{i} {comp.name}')

        try:

            option = int(input('Enter company number:\n'))
            financial_c = session.query(Financial).filter(Financial.ticker == company[option].ticker).first()
            print(f"{company[option].ticker} {company[option].name}")
            print(f"P/E = {(financial_c.market_price / financial_c.net_profit):.2f}")
            print(f"P/S = {(financial_c.market_price / financial_c.sales):.2f}")
            print(f"P/B = {(financial_c.market_price / financial_c.assets):.2f}")
            nd = None
            try:
                nd = financial_c.net_debt / financial_c.ebitda
            except TypeError:
                pass
            print(f"ND/EBITDA = {nd}")
            print(f"ROE = {(financial_c.net_profit / financial_c.equity):.2f}")
            print(f"ROA = {(financial_c.net_profit / financial_c.assets):.2f}")
            print(f"L/A = {(financial_c.liabilities / financial_c.assets):.2f}")
        except ValueError:
            print('Invalid option!')

        # calculate the financial indicators with the given formula
        '''
        P/E = Market price / Net profit
        P/S = Market price / Sales
        P/B = Market price / Assets
        ND/EBITDA = Net debt / EBITDA
        ROE = Net profit / Equity
        ROA = Net profit / Assets
        L/A = Liabilities / Assets
        '''
        main_menu()

def update_company():
    name = input("Enter company name:\n")
    company = session.query(Companies).filter(Companies.name.contains(name)).all()
    if company is None:
        print('Company not found!')
        main_menu()
    elif len(company) == 0:
        print('Company not found!')
        main_menu()
    else:  # list the matching companies with indexes
        for i, comp in zip(range(len(company)), company):
            print(f'{i} {comp.name}')

        try:
            option = int(input('Enter company number:\n'))
            financial_c = session.query(Financial).filter(Financial.ticker == company[option].ticker).first()
            ebitda = input("Enter ebitda (in the format '987654321'):\n")
            sales = input("Enter sales (in the format '987654321'):\n")
            net_profit = input("Enter net profit (in the format '987654321'):\n")
            market_price = input("Enter market price (in the format '987654321'):\n")
            net_debt = input("Enter net debt (in the format '987654321'):\n")
            assets = input("Enter assets (in the format '987654321'):\n")
            equity = input("Enter equity (in the format '987654321'):\n")
            cash_equivalents = input("Enter cash equivalents (in the format '987654321'):\n")
            liabilities = input("Enter liabilities (in the format '987654321'):\n")
            financial_c.ebitda = ebitda
            financial_c.sales = sales
            financial_c.net_profit = net_profit
            financial_c.market_price = market_price
            financial_c.net_debt = net_debt
            financial_c.assets = assets
            financial_c.equity = equity
            financial_c.cash_equivalents = cash_equivalents
            financial_c.liabilities = liabilities
            session.commit()
            print("Company updated successfully!")

        except ValueError:
            print('Invalid option!')

        main_menu()

def delete_company():
    name = input("Enter company name:\n")
    company = session.query(Companies).filter(Companies.name.contains(name)).all()
    if company is None:
        print('Company not found!')
        main_menu()
    elif len(company) == 0:
        print('Company not found!')
        main_menu()
    else:  # list the matching companies with indexes
        for i, comp in zip(range(len(company)), company):
            print(f'{i} {comp.name}')

        try:
            option = int(input('Enter company number:\n'))
            financial_c = session.query(Financial).filter(Financial.ticker == company[0].ticker).first()
            # delete the company
            session.delete(company[option])
            session.delete(financial_c)
            session.commit()
            print("Company deleted successfully!")
            main_menu()

        except ValueError:
            print('Invalid option!')

def list_all_companies():
    print("COMPANY LIST\n")
    # print the ticker, name and industry ordered by ticker from the companies table
    companies = session.query(Companies).order_by(Companies.ticker).all()
    for company in companies:
        print(f"{company.ticker} {company.name} {company.sector}")
    main_menu()

def top_ten_menu():
    options = ['Back', 'List by ND/EBITDA', 'List by ROE',
               'List by ROA']
    while True:
        print('TOP TEN MENU')
        for opt, i in zip(options, range(4)):
            print(f'{i} {opt}')
        try:
            option = int(input('Enter an option:'))
        except ValueError:
            print('Invalid option!')
            continue
        if option == 0:
            print('Have a nice day!')
            break
        elif option == 1:
            list_top_10_nd_ebitda()
            break
        elif option == 2:
            list_top_10_roe()
            break
        elif option == 3:
            list_top_10_roa()
            break
        else:
            print('Invalid option!')
            main_menu()

def list_top_10_nd_ebitda():
    # return the top 10 financial with the highest ND/EBITDA using func.round from sqlalchemy
    # and order by the result
    print("TICKER ND/EBITDA")
    top_10 = session.query(Financial).order_by(func.round(Financial.net_debt / Financial.ebitda, 2).desc()).limit(10).all()
    for company in top_10:
        print(f"{company.ticker} {round(company.net_debt / company.ebitda, 2)}")
    main_menu()
    pass


def list_top_10_roe():
    # return the top 10 companies with the highest ROE
    # and order by the result
    print("TICKER ROE")
    top_10 = session.query(Financial).order_by(func.round(Financial.net_profit / Financial.equity, 2).desc()).limit(
        10).all()
    for company in top_10:
        print(f"{company.ticker} {round(company.net_profit / company.equity, 2)}")
    main_menu()
    pass

def list_top_10_roa():
    # return the top 10 companies with the highest ROA
    # and order by the result
    print("TICKER ROA")
    top_10 = session.query(Financial).order_by(func.round(Financial.net_profit / Financial.assets, 2).desc()).limit(
        10).all()
    for company in top_10:
        print(f"{company.ticker} {round(company.net_profit / company.assets, 2)}")
    main_menu()
    pass


print('Welcome to the Investor Program!')
main_menu()