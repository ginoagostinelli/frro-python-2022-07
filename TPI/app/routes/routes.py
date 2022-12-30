from app.models.models import Company, User
from app.controller import companies_controller
from flask import Blueprint, render_template, Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

global_scope = Blueprint("views", __name__)

nav = [
    {"name": "Listar Todos", "url": "/api/users"},
    {"name": "Contacto ID 1", "url": "/api/users/1"},
]

nav2 = [
    {"name": "Listar Todos", "url": "/company"}
]

@global_scope.route("/", methods=['GET'])
def home():
    """Landing page route."""

    parameters = {"title": "Flask and Jinja Practical work",
                  "description": "This is a simple page made for implement the basics concepts of Flask and Jinja2"
                  }

    return render_template("home.html", nav=nav, **parameters)

@global_scope.route("/company", methods=['GET'])
def companyData():

    company = companies_controller.getCompanyData("GOOGL")

    parameters = {
        "name": company.name,
        "contry": company.country,
        "city": company.city,
        "industry": company.industry,
        "employees": company.employees,
        "business": company.business,
    }

    return render_template("companyData.html", **parameters)


@global_scope.route('/timeline.png')
def plot_timeline():
    fig = companies_controller.getTimelineFigure("AAPL")
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@global_scope.route('/dividends.png')
def plot_dividends():
    fig = companies_controller.getDividendsFigure("AAPL")
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@global_scope.route('/comparation.png')
def plot_comparation():
    fig = companies_controller.getComparationFigure("AAPL")
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')