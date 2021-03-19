
from django import forms
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from stories.models import Contact, Recipe


from stories.utils.validators import mail_validator


class ContactForm(forms.ModelForm):
    # full_name = forms.CharField(label='Full name', max_length=127, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Your name'
    # }))
    # email = forms.EmailField(label='Email', validators=(mail_validator,),
    #                          widget=forms.EmailInput(attrs={
    #                              'class': 'form-control',
    #                              'placeholder': 'Your email'
    #                          }))

    class Meta:
        model = Contact
        fields = (
            'email',
            'full_name',
            'subject',
            'message'
        )
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'cols': 50,
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('Daxil edilen email yanliz gmail hesabi olmalidir')
        return email

    # full_name = forms.CharField(label='Full name', max_length=127, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Your name'
    # }))
    # email = forms.EmailField(label='Email', max_length=63, widget=forms.EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Your email'
    # }))
    # subject = forms.CharField(label='Subject', max_length=255,  widget=forms.EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Subject'
    # }))
    # message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Message',
    #     'cols': 50,
    # }))


class RecipesForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Recipe
        fields = ('title', 'short_description', 'description', 'image', 'category', 'tags',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Resept Başlığı'),
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Qisa Mezmun'),
            }),
            'description': CKEditorUploadingWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Mezmun',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Category',
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Tags',
            }),
        }
