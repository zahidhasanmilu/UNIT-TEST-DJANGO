from documentation.models import Documentation


def all_documentations(request):
    all_documentations = (
        Documentation.objects.select_related('language')
        .prefetch_related('framwork', 'tags')
        .all()
    )
    context = {'all_documentations': all_documentations}
    return context
