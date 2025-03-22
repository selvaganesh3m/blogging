from django import template
import markdown2

register = template.Library()

@register.filter(name='markdown')
def markdown_filter(value):
    """Converts markdown to HTML"""
    extensions = ['fenced-code-blocks', 'code-friendly', 'highlightjs']
    return markdown2.markdown(value, extras=extensions)