from .models import ODApproval
from django import forms

class ODApprovalForm(forms.ModelForm):
    class Meta:
        model = ODApproval
        fields = ['student_name', 'student_id', 'department', 'od_date', 'reason']
