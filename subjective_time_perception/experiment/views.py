import csv
import json
import logging
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic import TemplateView
from subjective_time_perception.experiment.models import Experiment
from subjective_time_perception.experiment.models import Trial

log = logging.getLogger('subjective_time_perception')


class ExperimentCreateView(View):
    http_method_names = ['post', 'get']

    def clean_data(self, data):
        return json.loads(data.replace('\n', ''))

    def get(self, *args, **kwargs):



        return HttpResponse()

    def post(self, request, *args, **kwargs):
        for record in self.clean_data(request.body.decode('utf-8')):
            Experiment.add(**record)
        response = JsonResponse({'status': 'ok', 'code': 200})
        response['Access-Control-Allow-Origin'] = '*'
        return response


class ExperimentResultCsvView(TemplateView):
    template_name = 'experiment/results.csv'

    def get_output_data(self, experiment):
        log.warning('Calculating results for: {}'.format(experiment))
        """
        - ID użytkownika
        - name
        - start_date
        - polarization

        - C1 - Ilość kliknięć wszystkich - podejście 1
        - CW1 - Ilość kliknięć białych - podejście 1
        - CR1 - Ilość kliknięć czerwonych - podejście 1
        - CB1 - Ilość kliknięć niebieskich - podejście 1

        - PC1 - Współczynnik procentowy wszystkich - podejście 1
        - PC2 - Współczynnik procentowy wszystkich - podejście 2
        - PCW1 - Współczynnik procentowy białego - podejście 1
        - PCW2 - Współczynnik procentowy białego - podejście 2
        - PCR1 - Współczynnik procentowy czerwonego - podejście 1
        - PCR2 - Współczynnik procentowy czerwonego - podejście 2
        - PCB1 - Współczynnik procentowy niebieskiego - podejście 1
        - PCB2 - Współczynnik procentowy niebieskiego - podejście 2

        - TCSD1 - Współczynnik czasowy wszystkich - podejście 1 (odchylenie standardowe 60 środkowych interwałów czasowych wszystkich)
        - TCSD2 - Współczynnik czasowy wszystkich - podejście 2 (odchylenie standardowe 60 środkowych interwałów czasowych wszystkich)
        - TCSDW1 - Współczynnik czasowy białego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych białego)
        - TCSDW2 - Współczynnik czasowy białego - podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych białego)
        - TCSDR1 - Współczynnik czasowy czerwonego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych czerwonego)
        - TCSDR2 - Współczynnik czasowy czerwonego- podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych czerwonego)
        - TCSDB1 - Współczynnik czasowy niebieskiego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych niebieskiego)
        - TCSDB2 - Współczynnik czasowy niebieskiego - podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych niebieskiego)

        - TCM1 - Średnia 60 środkowych interwałów czasowych wszystkich - podejście 1
        - TCMW1 - Średnia 60 środkowych interwałów czasowych białych - podejście 1
        - TCMR1 - Średnia 60 środkowych interwałów czasowych czerwonych - podejście 1
        - TCMB1 - Średnia 60 środkowych interwałów czasowych niebieskich - podejście 1
        """

        return {
            'ID': experiment.id,
            'name': '{last_name} {first_name}'.format(**experiment.__dict__),
            'polarization': experiment.polarization,
            'start_date': experiment.experiment_start,

            'C1': experiment.count_clicks()['all'],
            'CW1': experiment.count_clicks()['white'],
            'CR1': experiment.count_clicks()['red'],
            'CB1': experiment.count_clicks()['blue'],

            'PC1': experiment.regularity_coefficient_percent()['all'],
            'PCW1': experiment.regularity_coefficient_percent()['white'],
            'PCR1': experiment.regularity_coefficient_percent()['red'],
            'PCB1': experiment.regularity_coefficient_percent()['blue'],

            'TCSD1': experiment.stdev()['all'],
            'TCSDW1': experiment.stdev()['white'],
            'TCSDR1': experiment.stdev()['red'],
            'TCSDB1': experiment.stdev()['blue'],

            'TCM1': experiment.mean()['all'],
            'TCMW1': experiment.mean()['white'],
            'TCMR1': experiment.mean()['red'],
            'TCMB1': experiment.mean()['blue'],
        }

    def get_context_data(self, *args, **kwargs):
        return {'results': [self.get_output_data(e) for e in Experiment.get()]}


class ExperimentResultHtmlView(TemplateView):
    template_name = 'experiment/results.html'
