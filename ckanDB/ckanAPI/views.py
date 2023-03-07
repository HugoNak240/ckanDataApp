from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import StS2020toCurrent


class IndexView(generic.ListView):
    model = StS2020toCurrent
    template_name = 'ckanAPI/index.html'
    context_object_name = 'avg_ecoli'

    def average_results_per_analyte(self):
        analyte_choice = str(input("Choose analyte"))
        all_results_set = StS2020toCurrent.objects.filter(
            analyte=analyte_choice)
        all_results = all_results_set
        total_samples = len(all_results)
        for r in range(0, total_samples, 1):
            if all_results[r]['result'] is not None:
                sum_results += all_results[r]['result']
        avg_result_analyte = sum_results/total_samples
        return avg_result_analyte


""" There is a list of key:value dictionaries, how do i get just the value?
    loop throught list 
    for r in all_results:
        values = all_results.values('result')[r]['result']

"""

class 
