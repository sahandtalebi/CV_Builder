from django.shortcuts import render
from django.views.generic import ListView
from cv_portfolio.models import Portfolio


class PortfolioView(ListView):
    template_name = 'portfolio_page.html'
    model = Portfolio
