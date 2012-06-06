from Products.Five import BrowserView

class HelloWorld(BrowserView):
    """
    Hello word browser view, as simple string
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return "hello word"

