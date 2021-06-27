#from django.db import models

# Create your models here.





VARIETIES = {
    'amnesia-haze' : {'name' : "Amnesia Haze"},
    'critical-2.0': {'name' : "Critical 2.0" },
    'lemon-haze' : {'name' : "Lemon Haze" },
}

PRICES = [
    {'price' : '10', 'varieties' : [VARIETIES['amnesia-haze']]},
    {'price' : '15', 'varieties' : [VARIETIES['critical-2.0']]},
    {'price' : '8', 'varieties' : [VARIETIES['lemon-haze']]},
]