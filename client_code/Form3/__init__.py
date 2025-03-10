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

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.unit_test_link.role = 'selected'

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('start_tests')
