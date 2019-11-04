from django.db import models

# Create your models here.
class Roles(models.Model):
    role = models.fields.CharField(max_length=255)

    class Meta:
        verbose_name_plural='roles'

    def __str__(self):
        return self.role

    def __repr__(self):
        return self.role

class Goals(models.Model):
    goal = models.fields.CharField(max_length=255)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='goals'

    def __str__(self):
        return self.goal

    def __repr__(self):
        return self.goal