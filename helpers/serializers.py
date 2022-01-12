from rest_framework import serializers


class TimestampSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(source="created_at", read_only=True)
    updated = serializers.DateTimeField(source="updated_at", read_only=True)
