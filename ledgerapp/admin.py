from django.contrib import admin
from .models import BookModel, PreviousMonthData
# Register your models here.
admin.site.register(BookModel)
admin.site.register(PreviousMonthData)