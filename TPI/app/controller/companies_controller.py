from ..database import company_db
from ..models.models import Company
#from ..helpers import helper
import yfinance as yf
import datetime
from matplotlib.figure import Figure
import pandas as pd

def getCompanyData(ticker: str) -> Company:

    tk = yf.Ticker(ticker)
    stockinfo = tk.info
    company = Company(name = stockinfo['longName'], 
        country = stockinfo.get('country', 'Sin Datos'),
        city = stockinfo.get('city', 'Sin Datos'),
        industry = stockinfo.get('industry', 'Sin Datos'),
        employees = stockinfo.get('fullTimeEmployees', 'Sin Datos'),
        business =stockinfo.get('longBusinessSummary', 'Sin Datos')
        )

    return company

def getTimelineFigure(ticker: str) -> Figure:

    tk = yf.Ticker(ticker)

    # Fechas
    today = datetime.datetime.today() # Fecha de hoy
    start = datetime.date(today.year-12,1,1) # Fecha - 12 años

    stockinfo = tk.info
    grafico = tk.history(start=start, end=today)

    fig = Figure()
    ax = fig.subplots()
    ax.plot(grafico['Close'])
    #ax.ylabel('Precio $')
    #ax.xlabel('Año')
    #ax.legend(['AP'])
    return fig

def getDividendsFigure(ticker: str) -> Figure:
    
    tk = yf.Ticker(ticker)
    
    dividends = tk.dividends
    div = dividends.resample('Y').sum() # Cantidad acumulada de dividendos en el año
    div = div.reset_index() # Para poder crear nuevas columnas

    div['Year'] = div['Date'].dt.year # Crea una nueva columna


    fig = Figure()
    ax = fig.subplots()
    ax.bar(div['Year'], div['Dividends'])
    #plt.ylabel('Rentabilidad por dividendo ($)')
    #plt.xlabel('Año')
    #plt.show()
    
    return fig

def getComparationFigure(ticker: str) -> Figure:
    
    tk = yf.Ticker(ticker)

    # Fechas
    today = datetime.datetime.today() # Fecha de hoy
    start = datetime.date(today.year-12,1,1) # Fecha - 12 años

    #empresas = ['MSFT', 'GOOGL', 'TSLA', 'KO']
    empresas = ['MSFT']
    empresas.insert(0, tk)

    df = pd.DataFrame()
    
    #for empresa in empresas: 
    #    df[empresa] = yf.Ticker(empresa).history(start=start, end=today).Close # Carga las empresas que esten en la lista
        
    fig = Figure()
    ax = fig.subplots()

    ax.plot(df)
    #plt.ylabel('Precio $')
    #plt.xlabel('Año')
    #plt.legend(empresas)
    #plt.show()

    return fig

## add tk.news