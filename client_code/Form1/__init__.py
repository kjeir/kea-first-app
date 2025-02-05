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
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    anvil.server.call('send_feedback', name, email, feedback)
    # Show a popup that says 'Feedback submitted!'
    Notification("Feedback submitted!").show()
    self.clear_inputs()
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""
