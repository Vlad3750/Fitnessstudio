from ._anvil_designer import AnmeldungenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Anmeldungen(AnmeldungenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # table = anvil.server.call('app_tables_holen')
    # angemeldet = {i['mitglied'] for i in table.search(Kurs=Kurs)}
  
    # Any code you write here will run before the form opens.

  @handle("data_grid_anmelden", "show")
  def data_grid_anmelden_show(self, **event_args):
    """This method is called when the data grid is shown on the screen"""
    return_value = anvil.server.call('get_Mitglied')
    self.repeating_panel_anmelden.items = return_value
