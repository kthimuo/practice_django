import django
django.setup()

from stock_manager.models import Maker
name = 'Samusung'
maker = Maker(name=name)
maker.save()
print(name + 'is registered')
