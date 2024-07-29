# forms.py
from django import forms
from .models import User, Discussion, Comment, Hashtag

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email', 'mobile_no']

class DiscussionForm(forms.ModelForm):
    hashtags = forms.ModelMultipleChoiceField(
        queryset=Hashtag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Discussion
        fields = ['text_field', 'image', 'hashtags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['tag']
