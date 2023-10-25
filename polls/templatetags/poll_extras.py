from django import template

register = template.Library()


@register.filter(name='there_digits_number')
def there_digits_number(value: int):
    return ' {:,} تومان'.format(value)
