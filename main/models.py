from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

user = settings.AUTH_USER_MODEL

class BaseModel(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    source = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.user.username} = {self.amount}'


class Income(BaseModel):
    pass

class Expense(BaseModel):
    pass