from django import template
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_filter(value):
    """Converts markdown to HTML"""
    extras = [
        'fenced-code-blocks',
        'code-friendly',
        'highlightjs',
        'tables',
        'cuddled-lists',
        'strike',
        'smarty-pants',
        'metadata',
        'footnotes',
        'numbering',
    ]
    return markdown.markdown(value, extras=extras)