from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Application(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        APPLIED = "APPLIED", "Applied"
        SCREENING = "SCREENING", "Screening"
        TECH = "TECH", "Tech"
        ONSITE = "ONSITE", "Onsite"
        OFFER = "OFFER", "Offer"
        REJECTED = "REJECTED", "Rejected"
        WITHDRAWN = "WITHDRAWN", "Withdrawn"

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="applications")

    role_title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    source = models.CharField(max_length=100, blank=True, null=True)          # LinkedIn/Seek/Referral
    job_url = models.URLField(blank=True, null=True)
    applied_date = models.DateTimeField(blank=True, null=True)
    notes_brief = models.TextField(blank=True, null=True)

    # JD fields
    jd_url = models.URLField(blank=True, null=True)
    jd_text = models.TextField(blank=True, null=True)
    jd_updated_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
