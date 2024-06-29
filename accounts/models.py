from django.db import models
from django.contrib.auth.models import User

class Relation(models.Model):
    from_user = models.ForeignKey(User, models.CASCADE, 'followers')
    to_user = models.ForeignKey(User, models.CASCADE, 'following')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'