from django.shortcuts import render
from django.db.models import Q
from projects.models import Project

# Create your views here.


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query) | Q(idea__icontains=query)

            results= Project.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search_.html', context)

        else:
            return render(request, 'search_.html')

    else:
        return render(request, 'search_.html')




