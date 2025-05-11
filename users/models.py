from django.db import models
from django.contrib.auth.models import User

#Product Model
class Users(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'delete'))
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.IntegerField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
