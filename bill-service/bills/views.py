from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Bill
from .serializers import BillSerializer


@api_view(["GET"])
def health_check(request):
    return Response({
        "service": "bill-service",
        "status": "healthy"
    })


@api_view(["GET", "POST"])
def bill_list(request):

    if request.method == "GET":
        bills = Bill.objects.all().order_by("-created_at")
        serializer = BillSerializer(bills, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        serializer = BillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def bill_detail(request, pk):

    try:
        bill = Bill.objects.get(pk=pk)
    except Bill.DoesNotExist:
        return Response(
            {"error": "Bill not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = BillSerializer(bill)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BillSerializer(
            bill,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == "DELETE":
        bill.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )