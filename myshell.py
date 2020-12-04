import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings") ## (always same, name of project (not app))

import django
django.setup()

from pizza_app.models import Pizza, Topping

topping = Topping.objects.all()
pizza = Pizza.objects.all()

for t in topping:
    print("Topping ID", t.id, "Topping:", t)
for p in pizza:
    print("Pizza ID", p.id, "Pizza:", p)