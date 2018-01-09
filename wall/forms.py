from django import forms

from django.contrib.auth.models import User
from wall.models import Message, Comment


class MessageForm(forms.ModelForm):
    text = forms.CharField()
    user = forms.CharField()
    class Meta:
        model = Message
        fields = ['text', 'user']

    def clean_user(self):
        user = User.objects.get(username=self.cleaned_data.get('user', None))
        return user


class CommentForm(forms.ModelForm):
    text = forms.CharField()
    message = forms.CharField()
    parent = forms.CharField(required=False)
    user = forms.CharField()

    class Meta:
        model = Comment
        fields = ['text', 'message', 'user', 'parent']

    def clean_user(self):
        user = User.objects.get(username=self.cleaned_data.get('user', None))
        return user

    def clean_message(self):
        message = Message.objects.get(id=self.cleaned_data.get('message', None))
        return message

    def clean_parent(self):
        if self.cleaned_data.get('parent', None) == "":
            return None
        else:
            parent = Comment.objects.get(id=self.cleaned_data.get('parent', None))
        return parent




