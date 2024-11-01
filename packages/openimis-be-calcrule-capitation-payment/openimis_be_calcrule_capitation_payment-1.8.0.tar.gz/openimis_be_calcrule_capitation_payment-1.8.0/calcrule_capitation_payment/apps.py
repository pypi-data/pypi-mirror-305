import importlib
import inspect
from django.apps import AppConfig
from calculation.apps import CALCULATION_RULES

from core.abs_calculation_rule import AbsStrategy


MODULE_NAME = "calcrule_capitation_payment"
DEFAULT_CFG = {}


def read_all_calculation_rules():
    """function to read all calculation rules from that module"""
    for name, cls in inspect.getmembers(importlib.import_module("calcrule_capitation_payment.calculation_rule"), inspect.isclass):
        if cls.__module__.split('.')[1] == 'calculation_rule':
            CALCULATION_RULES.append(cls)
            cls.ready()


class CalcruleCapitationPaymentConfig(AppConfig):
    name = MODULE_NAME

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(MODULE_NAME, DEFAULT_CFG)
        read_all_calculation_rules()
