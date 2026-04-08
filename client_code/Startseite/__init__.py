from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("data_grid_Kurs", "show")
  def data_grid_Kurs_show(self, **event_args):
    """This method is called when the data grid is shown on the screen"""
    return_value = anvil.server.call('get_Kurs')
    self.repeating_panel_Kurs.items = return_value

