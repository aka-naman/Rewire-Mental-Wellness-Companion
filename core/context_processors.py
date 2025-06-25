def debug(request):
    """
    Return context variables for the debug template context processor.
    This adds the DEBUG setting to the template context.
    """
    from django.conf import settings
    return {'DEBUG': settings.DEBUG}

def media(request):
    """
    Return context variables for the media template context processor.
    This adds the MEDIA_URL setting to the template context.
    """
    from django.conf import settings
    return {'MEDIA_URL': settings.MEDIA_URL}