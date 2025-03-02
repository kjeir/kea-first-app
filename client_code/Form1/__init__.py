from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Display a popup that says 'You clicked the button'
    #alert("You clicked the button")
    #name = self.repo_path_box.text
    anvil.server.call('start_jobs')
    # Show a popup
    #Notification("Job(ss) started !").show()
    #self.clear_inputs()

  def clear_inputs(self):
    # Clear our three text boxes
    #self.name_box.text = ""
    #self.email_box.text = ""
    #self.feedback_box.text = ""
    pass

  def unit_test_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form3')

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    #self.reset_links()
    self.build_link.role = 'selected'
    pass

def reset_links(self, **event_args):
  self.build_link.role = ''
  self.unit_test_link.role = ''