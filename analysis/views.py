from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.decorators import api_view, permission_classes
# Create your views here.


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def months_wise_analysis(request):
    data = [
        {
            "Months": "JAN",
            "left_in_cart": "100",
            "total_sold": "200"
        },
        {
            "Months": "FEB",
            "left_in_cart": "50",
            "total_sold": "100"
        },
        {
            "Months": "MAR",
            "left_in_cart": "25",
            "total_sold": "50"
        },
        {
            "Months": "APRL",
            "left_in_cart": "25",
            "total_sold": "50"
        },
        {
            "Months": "MAY",
            "left_in_cart": "75",
            "total_sold": "200"
        },
        {
            "Months": "JUN",
            "left_in_cart": "50",
            "total_sold": "300"
        },
        {
            "Months": "JUL",
            "left_in_cart": "100",
            "total_sold": "1000"
        },
        {
            "Months": "AUG",
            "left_in_cart": "500",
            "total_sold": "2000"
        },
        {
            "Months": "SEP",
            "left_in_cart": "100",
            "total_sold": "200"
        },
        {
            "Months": "OCT",
            "left_in_cart": "500",
            "total_sold": "1000"
        },
        {
            "Months": "NOV",
            "left_in_cart": "1000",
            "total_sold": "10000"
        },
        {
            "Months": "DEC",
            "left_in_cart": "500",
            "total_sold": "20000"
        }
    ]
    return Response(data, status=status.HTTP_200_OK)
