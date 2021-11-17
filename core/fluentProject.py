from fluent.runtime import FluentLocalization, FluentResource

class DemoLocalization(FluentLocalization):
  def __init__(self, fluent_content, locale='en', functions=None):
    # Call super() with one locale, no resources nor loader
    super(DemoLocalization, self).__init__([locale], [], None, functions=functions)
    self.resource = FluentResource(fluent_content)
    

  def _bundles(self):
    bundle = self._create_bundle(self.locales)
    bundle.add_resource(self.resource)
    yield bundle


  
