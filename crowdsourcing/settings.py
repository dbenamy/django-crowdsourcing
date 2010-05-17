import re

from django.conf import settings as _gs


MODERATE_SUBMISSIONS = getattr(_gs,
                               'CROWDSOURCING_MODERATE_SUBMISSIONS',
                               False)


IMAGE_UPLOAD_PATTERN = getattr(_gs,
                               'CROWDSOURCING_IMAGE_UPLOAD_PATTERN',
                               'crowdsourcing/images/%Y/%m/%d')


FLICKR_API_KEY = getattr(_gs, 'CROWDSOURCING_FLICKR_API_KEY', '')


FLICKR_API_SECRET = getattr(_gs, 'CROWDSOURCING_FLICKR_API_SECRET', '')

"""

Here is how I got the token and frob using the django shell.

import flickrapi
from django.conf import settings
_flickr = flickrapi.FlickrAPI(settings.CROWDSOURCING_FLICKR_API_KEY,
    settings.CROWDSOURCING_FLICKR_API_SECRET)
_flickr.web_login_url("write")
# go there. e.g.
"http://api.flickr.com/services/auth/?perms=write&api_sig=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&api_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# That sends you back to the callback url you set by "editing the
# authentication workflow" or something like that.
# this link will contain a frob in the form
"xxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx-xxxxxxxx"
_flickr.get_token("xxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx-xxxxxxxx")
# that returns the token. put it, along with the frob, in your settings.
# Then test with

import flickrapi
from django.conf import settings
_flickr = flickrapi.FlickrAPI(settings.CROWDSOURCING_FLICKR_API_KEY,
    settings.CROWDSOURCING_FLICKR_API_SECRET,
    token=settings.CROWDSOURCING_FLICKR_TOKEN)
_flickr.groups_pools_getGroups()
"""

FLICKR_TOKEN = getattr(_gs, 'CROWDSOURCING_FLICKR_TOKEN', '')


FLICKR_FROB = getattr(_gs, 'CROWDSOURCING_FLICKR_FROB', '')


FLICKR_LIVE = getattr(_gs, 'CROWDSOURCING_FLICKR_LIVE', False)


FLICKR_TOKENCACHE_PATH = getattr(_gs,
                                 'CROWDSOURCING_FLICKR_TOKENCACHE_PATH',
                                 '/tmp/flickr_tokencache')


# You can set a function that does additional processing on the submission
# list before rendering. For example, if your user interface has sorting
# based on votes, you could set this value. Use a python path to a function
# that takes a submission list and a request object.
PRE_REPORT = getattr(_gs, 'CROWDSOURCING_PRE_REPORT', '')


# If a survey is set to e-mail someone every time someone enters the survey,
# this will be the return address.
SURVEY_EMAIL_FROM = getattr(_gs,
                            'CROWDSOURCING_SURVEY_EMAIL_FROM',
                            'donotreply@donotreply.com')


SURVEY_ADMIN_SITE = getattr(_gs, 'CROWDSOURCING_SURVEY_ADMIN_SITE', '')


# You can set a custom def oembed_expand(url, **opts) which takes the url to
# a video and returns html embed code.
OEMBED_EXPAND = getattr(_gs, 'CROWDSOURCING_OEMBED_EXPAND', '')


# What URL should we redirect users to if they try to enter a survey that
# requires a login?
LOGIN_VIEW = getattr(_gs, 'CROWDSOURCING_LOGIN_VIEW', '')


# youtube has a lot of characters in their ids now so use [^&]
# youtube also likes to add additional query arguments, so no trailing $
# If you have oembed installed, we use the oembed configuration and ignore
# this.
VIDEO_URL_PATTERNS = getattr(
    _gs,
    'CROWDSOURCING_VIDEO_URL_PATTERNS',
    (r'^http://www\.youtube\.com/watch\?v=[^&]+',))
