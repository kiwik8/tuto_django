#from django.db import models

# Create your models here.


PRICES = {
    'amnesia-haze' : {'price' : "10"},
    'critical-2.0': {'price' : "15" },
    'lemon-haze' : {'price' : "8" },
}

VARIETIES = [
    {'name' : 'Amnesia Haze', 'prices' : [PRICES['amnesia-haze']]},
    {'name' : 'Critical 2.0 + ', 'prices' : [PRICES['critical-2.0']]},
    {'name' : 'Lemon Haze', 'prices' : [PRICES['lemon-haze']]},
]