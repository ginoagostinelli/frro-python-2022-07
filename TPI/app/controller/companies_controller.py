from ..database import company_db
from ..models.models import Company

# from ..helpers import helper
import yfinance as yf
import datetime
from matplotlib.figure import Figure
import pandas as pd
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io


def get_company_data(company: Company) -> Company:

    tk = yf.Ticker("AAPL")
    stockinfo = tk.info

    # companyWithData = Company(
    #     name=stockinfo.get("longName", "Sin Datos"),
    #     # ticker=company.ticker,
    #     country=stockinfo.get("country", "Sin Datos"),
    #     city=stockinfo.get("city", "Sin Datos"),
    #     industry=stockinfo.get("industry", "Sin Datos"),
    #     employees=stockinfo.get("fullTimeEmployees", "Sin Datos"),
    #     business=stockinfo.get("longBusinessSummary", "Sin Datos"),
    # )
    companyWithData = Company(
        name=stockinfo["longName"],
        country=stockinfo.get("country", "Sin Datos"),
        city=stockinfo.get("city", "Sin Datos"),
        industry=stockinfo.get("industry", "Sin Datos"),
        employees=stockinfo.get("fullTimeEmployees", "Sin Datos"),
        business=stockinfo.get("longBusinessSummary", "Sin Datos"),
    )

    return companyWithData


def get_timeline_plot(ticker: str) -> Figure:

    tk = yf.Ticker(ticker)

    # Fechas
    today = datetime.datetime.today()  # Fecha de hoy
    start = datetime.date(today.year - 12, 1, 1)  # Fecha - 12 años

    # stockinfo = tk.info
    grafico = tk.history(start=start, end=today)

    fig = Figure()
    ax = fig.subplots()
    ax.plot(grafico["Close"])
    # ax.ylabel('Precio $')
    # ax.xlabel('Año')
    # ax.legend(['AP'])

    # Building the base64 images

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    fig.savefig(output, format="png")

    output.seek(0)
    timeline_base64 = base64.b64encode(output.getvalue()).decode("utf-8")

    return timeline_base64


def get_dividends_plot(ticker: str) -> Figure:
    tk = yf.Ticker(ticker)

    dividends = tk.dividends
    div = dividends.resample("Y").sum()  # Cantidad acumulada de dividendos en el año
    div = div.reset_index()  # Para poder crear nuevas columnas

    div["Year"] = div["Date"].dt.year  # Crea una nueva columna

    fig = Figure()
    ax = fig.subplots()
    ax.bar(div["Year"], div["Dividends"])
    # plt.ylabel('Rentabilidad por dividendo ($)')
    # plt.xlabel('Año')
    # plt.show()

    # Building the base64 images
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    fig.savefig(output, format="png")

    output.seek(0)
    png_base64 = base64.b64encode(output.getvalue()).decode("utf-8")
    dividends_base64 = png_base64

    return dividends_base64


def get_comparation_plot(ticker: str) -> Figure:
    tk = yf.Ticker(ticker)

    # Fechas
    today = datetime.datetime.today()  # Fecha de hoy
    start = datetime.date(today.year - 12, 1, 1)  # Fecha - 12 años

    # empresas = ['MSFT', 'GOOGL', 'TSLA', 'KO']
    empresas = ["MSFT"]
    empresas.insert(0, tk)

    df = pd.DataFrame()

    # for empresa in empresas:
    #    df[empresa] = yf.Ticker(empresa).history(start=start, end=today).Close # Carga las empresas que esten en la lista

    fig = Figure()
    ax = fig.subplots()

    ax.plot(df)
    # plt.ylabel('Precio $')
    # plt.xlabel('Año')
    # plt.legend(empresas)
    # plt.show()

    # Building the base64 images
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    fig.savefig(output, format="png")

    output.seek(0)
    png_base64 = base64.b64encode(output.getvalue()).decode("utf-8")
    comparation_base64 = png_base64

    return comparation_base64


def get_news(company: Company) -> None:
    pass
