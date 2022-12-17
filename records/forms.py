from django.forms import ModelForm
from records.models import Log


class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = [
            "date", "time", "description", "category"
        ]
