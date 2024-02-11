from django import template

register = template.Library()

cnz_list = [
    'редиска',
    'редисок',
    "редиски",
    "редиской",
    "редисками",
    'сволочь',
    "сволочи",
    "сволочей",
    "сволочью",
    "сволочами"
]

@register.filter()
def cenz(some_string):
    lst = some_string.split(' ')
    for i in range(len(lst)):
        lstr = lst[i].lower()
        for j in cnz_list:
            if lstr == j:
                lst[i] = lst[i][0] + '*'*(len(lst[i])-1)
    return ' '.join(lst)
