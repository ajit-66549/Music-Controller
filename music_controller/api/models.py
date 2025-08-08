from django.db import models
import string
import random

def unique_code_generator():
    length = 6
    
    while True:
        Code = "".join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=Code).count() == 0:
            break
        return Code

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=80, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)