# -*- coding: utf-8 -*-
{
    'name': 'Service Team Import',
    'version': '16.0.1',
    'author': 'EisaA',
    'category': 'Services',
    'summary': 'Field Service',
    'description': """
        This module holds all the base import data for service team. 
 """,
    'website': 'https://www.fiverr.com/eisaahmed63',
    'depends': ['service_team'],
    'data': [
        'static/csv/product.template.csv',
        'static/csv/client.obligation.csv',
        'static/csv/contract.obligation.csv',
        'static/csv/covered.pest.csv',
        'static/csv/job.area.csv',
        'static/csv/job.type.csv',
        'static/csv/service.callback.csv',
        'static/csv/service.frequency.csv',
        'static/csv/service.payment.term.csv',
        'static/csv/service.scope.work.csv',
        'static/csv/service.validity.csv',
        'static/csv/area.area.csv',
        'static/csv/premise.type.csv',
    ],
    'installable': True,
    'auto_install': False,
}
