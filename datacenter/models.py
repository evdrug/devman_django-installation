from django.db import models
from django.utils.timezone import localtime
import datetime

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
        
    def get_duration(self):
      return (localtime(self.leaved_at) -localtime(self.entered_at))
    
    def is_visit_long(self, minutes=60):
      return self.get_duration().total_seconds() > 60 * minutes

    def format_duration(self):
      seconds = int(self.get_duration().total_seconds())
      days = seconds // (60*60*24)
      hours = (seconds - (days * 60*60*24)) // (60*60)
      minutes = (seconds - (hours *60 *60)) // 60 
      return f'{days}д {hours}ч {minutes}м'