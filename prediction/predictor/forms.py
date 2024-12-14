from django import forms

class PredictionForm(forms.Form):
    user_reputation = forms.FloatField(label='User Reputation')
    taker_mpxr_delta = forms.FloatField(label='Taker MPXR Delta')
