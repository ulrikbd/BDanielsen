from django.db import models

class Vinmonopolet(models.Model):

    CHOICES = [
        ('Rødvin', 'Rødvin'),
        ('Hvitvin', 'Hvitvin'),
        ('Rosévin', 'Rosévin'),
        ('Musserende vin', 'Musserende vin'),
        ('Portvin', 'Portvin'),
        ('Champagne, brut', 'Champagne, brut'),
        ('Champagne, extra brut', 'Champagne, extra brut'),
        ('Champagne, rosé', 'Champagne, rosé'),
        ('Vodka', 'Vodka'),
        ('Gin', 'Gin'),
        ('Akevitt', 'Akevitt'),
        ('Rom', 'Rom'),
        ('Whisky', 'Whisky'),
        ('Brennevin, annet', 'Brennevin, annet'),
        ('Likør', 'Likør'),
        ('Vermut', 'Vermut')
    ]

    alcohol_type = models.CharField('Type of alcohol',max_length=30, choices=CHOICES, default='Rødvin'
                                 )
    number = models.IntegerField('How many results?', default=10)

    def get_alcohol_type(self):
        return self.alcohol_type

    def get_number(self):
        return self.number
