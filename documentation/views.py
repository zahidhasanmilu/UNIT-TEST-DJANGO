from django.shortcuts import render
from documentation.models import Documentation


def documentation_list(request):
    documentation = Documentation.objects.all()

    context = {
        'documentation': documentation
    }

    return render(request, 'documentation/documentation_list.html', context)

def documentation_detail(request, pk):
    documentation = Documentation.objects.select_related(
        'language'
    ).prefetch_related('framwork', 'tags').get(pk=pk)

    all_documentations = Documentation.objects.all()

    return render(request, 'documentation/documentation.html', {
        'documentation': documentation,
        'all_documentations': all_documentations,
        'selected_id': documentation.id,
    })
