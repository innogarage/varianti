
from django.conf import settings
from django.forms.models import modelform_factory
from django.forms import ValidationError

from tema.links.models import Link


BaseLinkForm = modelform_factory(Link, fields=["title"])


class LinkForm(BaseLinkForm):
    pass

    # def clean(self):
    #     link = self.cleaned_data.get("link", None)
    #     description = self.cleaned_data.get("description", None)
    #     if not link and not description:
    #         raise ValidationError("Either a link or description is required")
    #     return self.cleaned_data
