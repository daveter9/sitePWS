from django import template

register = template.Library()

@register.filter(name='dj_iter')
def dj_iter(gen):
    try:
       return next(gen)
    except StopIteration:
       return 'Completed Iteration'

@register.filter(name='dictkey')
def keyvalue(dict, key):
    return dict[key]

@register.filter(name='listindex')
def listindex(list, key):
    return list[key]

@register.filter(name='attribute')
def getattribute(object, attributeToGet):
    try:
        return getattr(object, attributeToGet)
    except:
        return None

@register.filter(name='typecheck')
def checktype(var, iType):
    return type(var).__name__ == str(iType)