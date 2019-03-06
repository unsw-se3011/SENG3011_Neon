from django.contrib import admin

# Register your models here.
from .models import Report, Article, Disease, Syndrome, ReportEvent

admin.site.register(Report)
