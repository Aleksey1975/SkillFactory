from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CURRENCIES_SYMBOLS[code]

   return f'{value} {postfix}'

#
# Декоратор register.filter() указывает Django, что нужно запомнить про существование нового фильтра.
# Название фильтра по умолчанию берется равным названию функции, то есть в шаблонах мы можем писать
# {{ price|currency }}. Однако Django дает нам возможность самим указать название фильтра. Например,
# если бы мы указали register.filter(name=’currency_rub’), а название функции не меняли, тогда в шаблонах
# мы вызывали фильтр следующим образом {{ price|currency_rub }}.