from django import forms

class AddBookForm(forms.Form):
    name = forms.CharField()
    author = forms.CharField()
    translator = forms.CharField()
    year = forms.IntegerField()
    genre = forms.CharField()
    summary = forms.CharField(widget=forms.Textarea)
    cover = forms.ImageField()

class AddCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    user_name = forms.CharField()
    user_email = forms.EmailField()
    