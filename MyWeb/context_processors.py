from .models import category ,type ,language

def menu_links(request):
    links= category.objects.all()
    link2 = type.objects.all()
    user_id = request.user.id
    if user_id is None:
        return dict(links=links,links2=link2)
    else:
        link3 = language.objects.all().filter(user = user_id)
        return dict(links=links,links2=link2,link3=link3 )



