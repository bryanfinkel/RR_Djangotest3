from django import forms


class CSVUploadForm(forms.Form):
    file_name = forms.CharField(label="FileName", max_length=100)
    file_content = forms.FileField(label="File")