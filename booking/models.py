from django.db import models

TIME_SLOT_CHOICES = (
    ("9:00", "9:00"),
    ("9:15", "9:15"),
    ("9:30", "9:30")
)

# 1) The user selects a date and time
# 2) That data gets queried back to the DB and checks if someone already has the same date
# 3) If they do, check what time they took.
# 4)


class Date(models.Model):
    date_field = models.DateField()


class Time(models.Model):
    time = models.CharField(max_length=100)
    date = models.ForeignKey(Date, related_name="date_model",
                             on_delete=models.CASCADE)
