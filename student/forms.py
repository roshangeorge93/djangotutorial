from django import forms

# creating a form 
class StudentForm(forms.Form):
    usn = forms.CharField(max_length = 20,required=True)
    sem = forms.IntegerField(min_value=1,max_value=8,required=True)
	
