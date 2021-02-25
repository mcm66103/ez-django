from django.core.exceptions import ObjectDoesNotExist

from call_to_actions.models import BlogEmbeddedCTA, HeaderCTA

def call_to_actions_context(request):

    try:
        header_cta = HeaderCTA.objects.get(status='P')
    except ObjectDoesNotExist:
        header_cta = False

    try:
        blog_embedded_cta = BlogEmbeddedCTA.objects.get(status='P')
    except ObjectDoesNotExist:
        blog_embedded_cta = False

    context = {}

    if header_cta:
        context["HEADER_CTA"] = header_cta.cta
        context['HEADER_CTA_MESSAGE'] = header_cta.message
        context['HEADER_CTA_LINK']= header_cta.cta_link

    if blog_embedded_cta:
        context['BLOG_CTA'] = blog_embedded_cta.cta
        context['BLOG_CTA_MESSAGE'] = blog_embedded_cta.message
        context['BLOG_CTA_LINK']= blog_embedded_cta.cta_link

    return context