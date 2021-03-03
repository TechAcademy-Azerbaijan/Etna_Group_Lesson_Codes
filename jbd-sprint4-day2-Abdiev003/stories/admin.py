from django.contrib import admin
from stories.models import (
    Recipe,
    Contact,
)


admin.site.register([Recipe, Contact])
