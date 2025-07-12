from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.utils.translation import gettext_lazy as _

user = settings.AUTH_USER_MODEL

class BaseModel(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name=_("User"))
    amount = models.FloatField(_("Amount"), validators=[MinValueValidator(0.0)])
    source = models.CharField(_("Source"), max_length=255, blank=True, null=True)
    date = models.DateTimeField(verbose_name=_("Date"))
    created_at = models.DateTimeField(_("Created_at"), auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.user.username} = {self.amount}'


class Income(BaseModel):
    class Meta:
        verbose_name = _("Income")
        verbose_name_plural = _("Incomes")

class Expense(BaseModel):
    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")