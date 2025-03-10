from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html

admin.site.site_header = "Case Admin Portal"
admin.site.site_title = "Case Admin"
admin.site.index_title = "Case Root"

admin.site.register(LogEntry)


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return "-"
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f"admin:{app_label}_{model_name}_change"
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html(
            '<a target="_blank" style="color:#ff7000;" href="{}">{}</a>',
            link_url,
            linked_obj,
        )

    _linkify.short_description = field_name  # Sets column name
    return _linkify
