from django import template
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_filter(value):
    """Converts markdown to HTML"""
    extensions = ['extra', 'codehilite', 'fenced_code']
    return markdown.markdown(value, extensions=extensions)