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
            if j in lstr:
                sh = ''
                l = len(lstr)-1
                ind = lstr.index(j)
                for k in range(l):
                    sh += '*'
                lst[i] = lstr[ind]+sh
    return ' '.join(lst)
