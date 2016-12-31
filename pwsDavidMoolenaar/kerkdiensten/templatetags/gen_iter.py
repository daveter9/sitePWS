from django import template

register = template.Library()

@register.filter(name='dj_iter')
def dj_iter(gen):
    try:
       return next(gen)
    except StopIteration:
       return 'Completed Iteration'