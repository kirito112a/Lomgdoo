from .models import category ,type

def menu_links(request):
    links= category.objects.all()
    link2 = type.objects.all()
    
    return dict(links=links,links2=link2 )



