""" Script for seeding database; Postrgres, Django """
import logging
import json
import urllib.request
from django.core.management.base import BaseCommand
from ...models import StS2020toCurrent


logging.basicConfig(level=logging.INFO)

""" Clears all and creates data """

MODE_REFRESH = 'refresh'

""" Clear all data do NOT create any object """

MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed databse and for testing and development"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """ Deletes all the table data """
    logger = logging.getLogger(__name__)
    logger.info("Delete Instances")
    # Enter ORM deletion statments here
    StS2020toCurrent.objects.all().delete()


def create_StoSData():
    """ Creates data entries for a select table/model"""
    logger = logging.getLogger(__name__)
    logger.info("Creating SafeToSwim Data")

    """ First, extract data from a source online like an API, parse from a local source, or just make some like the 'Fennestrations' project """
    url = "https://data.ca.gov/datastore/odata3.0/1987c159-ce07-47c6-8d4f-4483db6e6460?$format=json"
    fileobj = urllib.request.urlopen(url)
    response_dict = json.loads(fileobj.read())
    r = response_dict['value']
    # r = query_dict['records']
    # data = r.json()
    # return data

    """ Seed data into respective model """
    for x in r:
        data_entry = StS2020toCurrent(
            analyte=x['Analyte'], lab_agency=x['LabAgency'], lab_batch=x['LabBatch'], lab_sample_id=x['LabSampleID'], matrix_name=x['MatrixName'], method_name=x['MethodName'], program=x['Program'], project=x['Project'], result=x['Result'], reporting_limit=x['RL'])
        data_entry.save()

    logger.info("{}data_entry.".format(data_entry))
    return data_entry


def run_seed(self, mode):
    """ See database based on mode
    :param mode: refresh/clear
    :return :
    """

    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Calls object creater functions
    create_StoSData()
