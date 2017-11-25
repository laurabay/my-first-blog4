from django import forms
from .models import Post

class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            fields = ('titulo','fecha_publicacion','autor','editorial','genero','imagen','sinopsis',)
