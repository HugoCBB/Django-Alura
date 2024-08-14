from django.forms import ModelForm
from . models import Fotografia

class FotografiaForm(ModelForm):
    class Meta:
        model = Fotografia
        fields = ['nome','descricao','foto','categoria','publicada']