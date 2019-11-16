from snippets.models import Snippet
from django.conf import FB_APP_ID, BASE_URL

def custom_context(request):
    snippets = Snippet.objects.all()
    return {
        "boh_snippets": snippets.filter(location='boh'),
        "eoh_snippets": snippets.filter(location='eoh'),
        "bob_snippets": snippets.filter(location='bob'),
        "eob_snippets": snippets.filter(location='bob'),
        "FB_APP_ID": FB_APP_ID,
        "BASE_URL": BASE_URL
    }
