#
from django import template

register = template.Library()
@register.filter(name='filsym')
def filsym(value):
    R = value.split(" ")
    R2 = []
    for k in R:
        if "\n" in k:
            k1 = k.split("\n")
            for p in k1:
                R2.append(p)
        else:
            R2.append(k)
    sy = 0
    for l in R2:
        l1 = l.replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('+', '')
        try:
            sy += int(l1)
        except:
            pass
    return sy
#