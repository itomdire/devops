from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = [
            "id",
            "customer_name",
            "amount",
            "description",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]