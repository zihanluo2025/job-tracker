from rest_framework import serializers
from .models import Company, Application


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "website"]


class ApplicationSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True,
        source="company",
    )

    class Meta:
        model = Application
        fields = [
            "id",
            "company",
            "company_id",
            "role_title",
            "status",
            "source",
            "job_url",
            "applied_date",
            "notes_brief",
            "jd_url",
            "jd_text",
            "jd_updated_at",
            "created_at",
            "updated_at",
        ]
