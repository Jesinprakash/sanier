from django.db import models
from sheet1.utils.google_sheet import add_or_update_google_sheet

class Sheet(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save in DB first
        add_or_update_google_sheet(self.id, self.name, self.dob)

    def __str__(self):
        return self.name

