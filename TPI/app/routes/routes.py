from app.helpers import helper
from app.controller import companies_controller
from flask import Blueprint, render_template, Response, request, g
from app.models.models import Company

global_scope = Blueprint("views", __name__)


# @global_scope.before_request
# def before_request():
#     g.company = request.args.get("ticker")


@global_scope.route("/", methods=["GET"])
def home():
    """Landing page route."""

    return render_template("home.html")


@global_scope.route("/company", methods=["GET"])
def companyData():

    ticker = request.args.get("ticker")
    helper.validate_ticker(ticker)
    company = companies_controller.getCompanyData(Company(ticker=ticker))

    company_data = {
        "name": company.name,
        "contry": company.country,
        "city": company.city,
        "industry": company.industry,
        "employees": company.employees,
        "business": company.business,
    }

    # Timeline plots
    timeline = companies_controller.getTimelinePlot(ticker)

    # Dividends plot
    dividends = companies_controller.getDividendsPlot(ticker)

    # Comparation plot
    comparation = companies_controller.getComparationPlot(ticker)

    return render_template(
        "companyData.html",
        **company_data,
        timeline=timeline,
        dividends=dividends,
        comparation=comparation
    )
