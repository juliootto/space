from django import forms   
from apps.galeria.models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicado','usuario']
        labels = {
            'nome': 'Nome',
            'legenda': 'Legenda',
            'descricao': 'Descrição',
            'foto': 'Foto',
            'categoria': 'Categoria',
            'publicado': 'Publicado',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário',
        }
        help_texts = {
            'nome': 'Nome da fotografia',
            'legenda': 'Legenda da fotografia',
            'descricao': 'Descrição da fotografia',
            'foto': 'Imagem do Objeto',
            'categoria': 'Categoria da fotografia',
            'publicado': 'Indica se a fotografia está publicada',
            'data_fotografia': 'Data de Reegistro da Fotografia',
            'usuario': 'Usuário que publicou a fotografia',
        }

        widgets = { 
                    'nome': forms.TextInput(attrs={'class': 'form-control'}),
                    'legenda': forms.TextInput(attrs={'class': 'form-control'}),
                    'descricao': forms.Textarea(attrs={'class': 'form-control'}),
                    'foto': forms.FileInput(attrs={'class': 'form-control'}),
                    'categoria': forms.Select(attrs={'class': 'form-control'}),
                    #'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                    'data_fotografia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                    'usuario': forms.Select(attrs={'class': 'form-control'}),
                    }
        #input_formats={'data_fotografia': ['%d/%m/%Y', '%Y-%m-%d']}

