from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Row, Column, Fieldset
from crispy_forms.bootstrap import StrictButton


class AboutForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label="Do you like this website?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial='1',
        required=True,
    )
    like_pizza = forms.CharField(
        label='Do you like the pizza calculator?'
    )
    favourite_food = forms.CharField(
        label="What is your favourite food?",
        max_length=80,
        required=True,
    )

    CHOICES = [
        ('Rødvin', 'Rødvin'),
        ('Hvitvin', 'Hvitvin')
        ]

    options = forms.ChoiceField(
        choices=CHOICES)


    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-aboutForm'
        self.helper.form_method = 'post'
        self.helper.form_class = 'bootstrap4'

        self.helper.layout = Layout(
            Row(
                Column('like_pizza', css_class='form-group col-md-6 mb-0'),
                Column('favourite_food', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('like_website', css_class='form-group col-md-6 mb-0'),
                Column('options', css_class='form-group col-md-6 mb-0')
            ),
            ButtonHolder(
                StrictButton('Submit', type='submit', css_class='btn btn-outline-info')
            )
        )
