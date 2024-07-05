from django.db import models

# Create your models here.
class ODApproval(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    od_date = models.DateField()
    reason = models.TextField()
    HOD_approval = models.CharField(max_length=10, choices=[('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='pending')

    def __str__(self):
        return f"{self.student_name} - {self.od_date}"