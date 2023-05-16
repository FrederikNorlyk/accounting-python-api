from django.db import models


class Merchant(models.Model):
    name = models.TextField()
    user = models.ForeignKey("auth.User", related_name="merchants", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
    