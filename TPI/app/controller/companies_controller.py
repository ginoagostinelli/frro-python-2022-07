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
import plotly.graph_objects as go
import plotly.io as pio


def get_company_data(company: Company) -> Company:

    tk = yf.Ticker(company.ticker)
    stockinfo = tk.info

    companyWithData = Company(
        name=stockinfo.get("longName", "Sin Datos"),
        ticker=company.ticker,
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

    # ***************#
    # Retrieve the stock data using yfinance
    stock = yf.download(ticker, start=start, end=today)

    # Create the figure using Plotly
    fig = go.Figure()

    # Add the closing price trace
    fig.add_trace(
        go.Scatter(
            x=stock.index,
            y=stock["Close"],
            name="Closing Price",
            line=dict(color="royalblue", width=2),
        )
    )

    # Set the layout of the figure
    fig.update_layout(
        title=ticker + " Stock Price",
        xaxis_title="Date",
        yaxis_title="Price",
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
    )

    # Convert the figure to an HTML plot
    plot_html = pio.to_html(fig, full_html=False)

    return plot_html


def get_dividends_plot(ticker: str) -> Figure:

    """
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
    """
    # Define the symbol and time range
    start_date = "2020-01-01"
    end_date = "2023-02-13"

    # Retrieve the stock data using yfinance
    stock = yf.Ticker(ticker)
    dividends = stock.dividends.loc[start_date:end_date]

    # Create the figure using Plotly
    fig = go.Figure()

    # Add the dividends trace
    fig.add_trace(
        go.Scatter(
            x=dividends.index,
            y=dividends,
            name="Dividends",
            line=dict(color="royalblue", width=2),
        )
    )

    # Set the layout of the figure
    fig.update_layout(
        title=ticker + " Dividends",
        xaxis_title="Date",
        yaxis_title="Dividend Amount",
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
    )

    # Convert the figure to an HTML plot
    plot_html = pio.to_html(fig, full_html=False)

    return plot_html


def get_comparation_plot(ticker: str) -> Figure:
    tk = yf.Ticker(ticker)

    # Fechas
    today = datetime.datetime.today()  # Fecha de hoy
    start = datetime.date(today.year - 12, 1, 1)  # Fecha - 12 años

    # Define the symbols and time range
    symbols = ["AAPL", "MSFT", "AMZN"]

    if ticker not in [symbols]:
        symbols.append(ticker)

    # Retrieve the stock data using yfinance
    data = yf.download(symbols, start=start, end=today)["Adj Close"]

    # Create the figure using Plotly
    fig = go.Figure()

    # Add the traces for each stock
    for symbol in symbols:
        fig.add_trace(
            go.Scatter(x=data.index, y=data[symbol], name=symbol, line=dict(width=2))
        )

    # Set the layout of the figure
    fig.update_layout(
        title="Stock Comparison",
        xaxis_title="Date",
        yaxis_title="Adjusted Close Price",
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
    )

    # Convert the figure to an HTML plot
    plot_html = pio.to_html(fig, full_html=False)

    return plot_html


def get_news(ticker: str):
    tk = yf.Ticker(ticker)

    news = {}
    for i in range(3):
        news[f"title_new_{i+1}"] = tk.news[i].get("title", "No disponible")
        news[f"link_new_{i+1}"] = tk.news[i].get("link")
        try:

            news[f"img_new_{i+1}"] = (
                tk.news[i].get("thumbnail").get("resolutions")[0].get("url")
            )
        except:
            print(f"WARNING: No image in news {i+1}")

    return news
