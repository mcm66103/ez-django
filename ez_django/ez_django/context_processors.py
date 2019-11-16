from snippets.models import Snippet

def custom_context(request):
    snippets = Snippet.objects.all()
    return {
        "boh_snippets": snippets.filter(location='boh'),
        "eoh_snippets": snippets.filter(location='eoh'),
        "bob_snippets": snippets.filter(location='bob'),
        "eob_snippets": snippets.filter(location='bob'),
    }
