from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def subtract(context, obj):
    difference = obj.needed_upvotes - obj.upvotes
    return difference

