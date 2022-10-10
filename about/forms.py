from django import forms
from .models import Movie


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        remarks = {
            "name": "movie title",
            "poster_url": "an URL to the poster",
            "duration": "duration in minutes",
            "release_date": "YYYY-MM-DD",
            "purchase_url": "e.g. link to GV, if not, please set #"
        }
        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "style": "width: 500px"
            })
            if name in remarks:
                field.widget.attrs.update({
                "placeholder": remarks[name]
            })
