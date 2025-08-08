

from django import template
import re

register = template.Library()

@register.filter(name='linkify')
def linkify(text):
    if not text:
        return ''
    url_pattern = re.compile(r'(https?://[^\s]+)')
    return url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', text)