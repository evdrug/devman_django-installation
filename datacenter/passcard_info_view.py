from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.http import Http404


def passcard_info_view(request, passcode):
  try:
    passcard = Passcard.objects.get(passcode=passcode)
  except Passcard.DoesNotExist:
    raise Http404("Passcard does not exist")

  this_passcard_visits = [
      {
          "entered_at": localtime(card.entered_at),
          "duration": card.format_duration(),
          "is_strange": card.is_visit_long()
      } for card in passcard.visit_set.all()
  ]

  context = {
      "passcard": passcard,
      "this_passcard_visits": this_passcard_visits
  }
  return render(request, 'passcard_info.html', context)
