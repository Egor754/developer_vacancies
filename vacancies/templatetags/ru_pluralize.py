from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def ru_pluralize(value, arg="вакансия,вакансии,вакансий"):
    args = arg.split(",")
    number = abs(int(value))
    arg1 = number % 10
    arg2 = number % 100

    if (arg1 == 1) and (arg2 != 11):
        return args[0]
    elif (arg1 >= 2) and (arg1 <= 4) and ((arg2 < 10) or (arg2 >= 20)):
        return args[1]
    else:
        return args[2]


@register.filter
@stringfilter
def f_replace(stroka, arg1=' • '):
    result = stroka.replace(',', arg1)
    return result
