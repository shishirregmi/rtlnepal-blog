from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','image','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control','size':'1.5'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent', 'id':'summernote'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')
        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control'})
        }

