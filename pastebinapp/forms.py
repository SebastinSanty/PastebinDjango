from django import forms
from .models import Pastebin

class PastebinForm(forms.ModelForm):
	class Meta:
		model = Pastebin
		fields = ['name','textpaste']
		readonly_fields = ('pasteurl')