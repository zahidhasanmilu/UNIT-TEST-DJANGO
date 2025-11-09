from django.shortcuts import render
from documentation.models import Documentation

# Cache
from django.views.decorators.cache import cache_page




def documentation_list(request):
    documentation = Documentation.objects.all()

    context = {'documentation': documentation}

    return render(request, 'documentation/documentation_list.html', context)


@cache_page(60 * 2)
def documentation_detail(request, pk):
    documentation = (
        Documentation.objects.select_related('language')
        .prefetch_related('framwork', 'tags')
        .get(pk=pk)
    )

    all_documentations = Documentation.objects.all()

    return render(
        request,
        'documentation/documentation.html',
        {
            'documentation': documentation,
            'all_documentations': all_documentations,
            'selected_id': documentation.id,
        },
    )
