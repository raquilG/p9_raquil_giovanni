from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.fields.CharField(max_length=128)
    description = models.fields.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.fields.DateTimeField(auto_now_add=True)

    @property
    def has_review(self):
        try:
            Review.objects.get(ticket__pk=self.id)
        except Review.DoesNotExist:
            return False
        return True

    @property
    def type(self):
        return "ticket"


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.fields.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    header = models.fields.CharField(max_length=128)
    body = models.fields.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    @property
    def type(self):
        return "review"

