from django.db import models


class Pizza(models.Model):
    weight = models.DecimalField('Weight in grams', max_digits=10, decimal_places=2, default=250,
                                  help_text='250 g gives a normal pizza, 300 g gives a large pizza',
                                 )
    water_percentage = models.DecimalField(max_digits=10, decimal_places=2, default=65,
                                           help_text='57%-70%'
                                           )
    number = models.DecimalField('Number of pizzas', max_digits=10, decimal_places=2, default=3)

    def get_weight(self):
        return self.weight

    def get_percentage(self):
        return self.water_percentage

    def get_number(self):
        return self.number
