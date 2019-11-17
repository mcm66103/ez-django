from snippets.models import Snippet
from site_info.models import SiteInfo

from ez_django.settings import FB_APP_ID, BASE_URL, MEDIA_URL

def custom_context(request):
    snippets = Snippet.objects.all()
    try:
        site_info = SiteInfo.objects.get(pk=1)
    except:
        site_info = False

    return {
        "boh_snippets": snippets.filter(location='boh'),
        "eoh_snippets": snippets.filter(location='eoh'),
        "bob_snippets": snippets.filter(location='bob'),
        "eob_snippets": snippets.filter(location='bob'),
        "FB_APP_ID": FB_APP_ID,
        "BASE_URL": BASE_URL,
        "SITE_NAME": site_info.name if site_info else "EZ_DJANGO",
        "SITE_LOGO": site_info.logo.url if site_info else "/static/ez_django/images/logo.png",
        "FACEBOOK_URL": site_info.facebook_url if site_info else False,
        "INSTAGRAM_URL": site_info.instagram_url if site_info else False,
        "TWITTER_URL": site_info.twitter_url if site_info else False,
        "LINKEDIN_URL": site_info.linkedin_url if site_info else False,
        "ADDRESS": site_info.address if site_info else False,
        "KEYWORDS": site_info.keywords if site_info else False,
        "FAVICON": site_info.favicon if site_info else "/static/ez_django/images/favicon.png",
        "BLOG_NAME": site_info.blog_name if site_info else "EZ_DJANGO Blog",
        "BLOG_DESCRIPTION": site_info.blog_description if site_info else False,
        "BLOG_IMAGE": site_info.blog_image if site_info else False,
        "MEDIA_URL": MEDIA_URL,
    }