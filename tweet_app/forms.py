from django import forms

class AddTweetForms(forms.Form):
    nickname_input = forms.CharField(label="Nickname", max_length=5)
    message_input = forms.CharField(label="Message", max_length=10)