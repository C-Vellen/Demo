from django import forms


class PromptForm(forms.Form):
    prompt = forms.CharField(
        label="",
        max_length=1000,
        widget=forms.Textarea(attrs={"class": "prompt"}),
    )

    class Meta:
        widgets = {}
