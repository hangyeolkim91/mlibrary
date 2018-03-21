from django import forms
import datetime

class BookcaseForm(forms.Form):
    bookcase_name = forms.CharField(label='bookcase name', max_length=500)

class NovelForm(forms.Form):
    title = forms.CharField(max_length=500)
    author = forms.CharField(max_length=200)
    published_date = forms.DateField(
            widget=forms.SelectDateWidget(
                empty_label=("Choose Year", "Choose Month", "Choose Day"),
                years=range(1985, datetime.date.today().year+10)
                ),
            )
    file = forms.FileField()
