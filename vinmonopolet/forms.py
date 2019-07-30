from django import forms
from .models import Vinmonopolet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Column, Row, Fieldset, HTML
from crispy_forms.bootstrap import StrictButton


class VinmonopoletForm(forms.ModelForm):
    class Meta:
        model = Vinmonopolet
        fields = ['alcohol_type', 'number']

    def __init__(self, *args, **kwargs):
        super(VinmonopoletForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-vinmonopoletForm'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Fieldset(
                'Vinmonopolet Calculator',
                HTML('''<p>This calculator uses information from Vinmonopolet.no</p>'''),
                Row(
                    Column('alcohol_type', css_class='form-group col-md-6 mb-0'),
                    Column('number', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                ButtonHolder(StrictButton('Calculate!', type='submit', css_class='btn btn-outline-info'))
            ))
