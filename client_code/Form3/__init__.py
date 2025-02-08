from ._anvil_designer import Form3Template
from anvil import *
import anvil.server


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def build_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')
