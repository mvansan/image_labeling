from django import forms

class CaptionForm(forms.Form):
    caption = forms.CharField(
        max_length=500,  
        min_length=20,   
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter a caption', 
            'class': 'caption-input'  
        }),
        error_messages={
            'required': 'Caption không được để trống.',
            'max_length': 'Caption không được dài hơn 500 ký tự.',
            'min_length': 'Caption phải dài ít nhất 20 ký tự.'
        }
    )
