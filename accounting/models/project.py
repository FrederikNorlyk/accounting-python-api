from django.db import models


class Project(models.Model):
    name = models.TextField()
    user = models.ForeignKey("auth.User", related_name="projects", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        unique_together = ('name', 'user')