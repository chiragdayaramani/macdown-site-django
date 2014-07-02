from django.core.urlresolvers import Http404
from django.views.generic import RedirectView
from sparkle.models import Version
from base.models import get_macdown


class VersionView(RedirectView):

    permanent = False

    def get_version(self, version_string=None):
        try:
            return get_macdown().active_versions().get(
                short_version=version_string,
            )
        except Version.DoesNotExist:
            raise Http404

    def get_redirect_url(self, *args, **kwargs):
        version_string = kwargs.get('version')
        return self.get_version(version_string).update_url


class LatestVersionView(VersionView):
    def get_version(self, version_string=None):
        return get_macdown().active_versions().latest()


version = VersionView.as_view()
latest = LatestVersionView.as_view()