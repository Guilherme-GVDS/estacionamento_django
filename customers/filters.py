from dj_rql.filter_cls import AutoRQLFilterClass

from customers.models import Customer


class CustomerFilter(AutoRQLFilterClass):
    MODEL = Customer
