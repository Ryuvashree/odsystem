from django.contrib import admin

# Register your models here.
from .models import ODApproval

class ODApprovalAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'od_date', 'HOD_approval')  # Use correct fields from the model
    list_filter = ('HOD_approval', 'od_date')  # Use correct fields from the model

admin.site.register(ODApproval, ODApprovalAdmin)