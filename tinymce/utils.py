""" http://djangosnippets.org/snippets/1804/ """

from django.contrib.admin.util import unquote
from django.utils.functional import update_wrapper


class ExtendibleModelAdminMixin(object):
    def _getobj(self, request, object_id):
            opts = self.model._meta
            app_label = opts.app_label

            try:
                obj = self.queryset(request).get(pk=unquote(object_id))
            except self.model.DoesNotExist:
                # Don't raise Http404 just yet, because we haven't checked
                # permissions yet. We don't want an unauthenticated user to be able
                # to determine whether a given object exists.
                obj = None

            if obj is None:
                raise Http404(_('%(name)s object with primary key %(key)r does not exist.') % {'name': force_unicode(opts.verbose_name), 'key': escape(object_id)})

            return obj

    def _wrap(self, view):
        def wrapper(*args, **kwargs):
            return self.admin_site.admin_view(view)(*args, **kwargs)
        return update_wrapper(wrapper, view)

    def _view_name(self, name):
        info = self.model._meta.app_label, self.model._meta.module_name, name

        return '%s_%s_%s' % info
