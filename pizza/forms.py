from django import forms
from .models import Pizza
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Column, Row, Fieldset, HTML
from crispy_forms.bootstrap import StrictButton


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['weight', 'water_percentage', 'number']

    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-pizzaForm'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Fieldset(
                'Pizzadough Calculator',
                HTML('''<p>This calculator uses the official measurements given by the Associazone Verace Pizza Napoletana!</p>'''),
                'weight',
                Row(
                    Column('water_percentage', css_class='form-group col-md-6 mb-0'),
                    Column('number', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                ButtonHolder(StrictButton('Calculate!', type='submit', css_class='btn btn-outline-info'))
            ))
