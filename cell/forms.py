from django import forms
from .models import Cell

class CellForm(forms.ModelForm):
    class Meta:
        model = Cell
        fields = ('title', 'content', 'image',)

#
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)
#
