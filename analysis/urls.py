
from django.urls.conf import path

from analysis.views import months_wise_analysis

urlpatterns = [
    path("forecast", months_wise_analysis),
]
