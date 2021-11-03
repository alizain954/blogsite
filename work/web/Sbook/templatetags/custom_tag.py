from django import template

register = template.Library()
@register.simple_tag
def get_half_content( discription):
    return  discription[:int(len( discription)/2)]