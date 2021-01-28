from django.urls import path

from cv_portfolio.views import PortfolioView

urlpatterns = [
    path('portfolio', PortfolioView.as_view(), name='portfolio')
]