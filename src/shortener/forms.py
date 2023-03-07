from django import forms

from .validators import validate_dot_com, validate_url


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit Url', validators=[
            validate_url,
            validate_dot_com,
            ])
