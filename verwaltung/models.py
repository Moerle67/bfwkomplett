from django.db import models
from django.urls import reverse

# Create your models here.

class Grp_status(models.Model):
    status = models.CharField(("Status"), max_length=10)
    description = models.TextField(("Beschreibung"), blank=True, null=True)

    class Meta:
        verbose_name = ("Gruppen Status")
        verbose_name_plural = ("Gruppen Status")

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse("grp_status_detail", kwargs={"pk": self.pk})

class Group(models.Model):
    group_name = models.CharField(("Gruppenname"), max_length=50)
    short_name = models.CharField(("Kürzel"), max_length=10)
    status = models.ForeignKey(Grp_status, verbose_name=("Status"), on_delete=models.RESTRICT)
    description = models.TextField(("Beschreibung"), blank=True, null=True)
    color = models.CharField(("Farbe"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ("Gruppe")
        verbose_name_plural = ("Gruppen")

    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return reverse("group_detail", kwargs={"pk": self.pk})
