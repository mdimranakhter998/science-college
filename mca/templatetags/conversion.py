from django import template
register = template.Library()
@register.filter
def qualification(value): 
    result=""
    for q in value:
        result=result+str(q)+" "+"," 
    return (result)

@register.filter
def specialization(value):
    sp=[]
    for s in value:
        sp.append(s)
    return(sp)

@register.filter
def experience(value):
    return (str(value)+" "+"years")

@register.filter
def mca_faculty_lenght(value):
    n=len(value)
    return n-1
