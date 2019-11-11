from django.forms import ModelForm
from django import forms
from .models import Notes
class NotesForm(ModelForm):
	class Meta:
		model=Notes
		fields=['title','body','thumb']
		widgets={
			'title':forms.Textarea(
				attrs={'class':'form-control mb-2 mr-sm-2',
				'id':'inlineFormInputName2',
				'placeholder':'title',
				'rows':1,'cols':1}),
			'body':forms.Textarea(
				attrs={'class':'form-control mb-2 mr-sm-2',
				'id':'inlineFormInputName2',
				'placeholder':'Type in your notes here',
				'rows':10,'cols':1}),
			'thumb':forms.FileInput(
				attrs={'style':"border-radius:2px;color:green;margin-bottom:5px;",
				})
		}