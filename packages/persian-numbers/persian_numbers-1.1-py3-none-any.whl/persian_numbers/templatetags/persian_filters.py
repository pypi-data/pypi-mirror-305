from django import template

register = template.Library()

@register.filter
def persian_number(value):
    value = str(value)
    number = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹',
    }
    for i, j in number.items():
        value = value.replace(i, j)
    return value
