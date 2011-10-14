from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.mydemoapp import mydemoappMessageFactory as _


class IMiSaludoView(Interface):
    """
    Mi Saludo view interface
    """

    def test():
        """ test method"""


class MiSaludoView(BrowserView):
    """
    Mi Saludo browser view
    """
    implements(IMiSaludoView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        dummy = _(u'Es es mi saludo al mundo')

        return {'dummy': dummy}
