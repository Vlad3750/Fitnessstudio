import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_Kurs():
  with sqlite3.connect(data_files['Neicovcen_Vladislav_fitnessstudio.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
          k.Bezeichnung AS Kurs,
          k.Wochentag,
          k.Uhrzeit,
          t.Nachname || ' ' || t.Vorname AS Trainer,
          COUNT(a.AnmeldungsID) || '/' || k.Max_Teilnehmer AS Teilnehmer
      FROM Kurs k
      JOIN Trainer t ON k.TrainerID = t.TrainerID
      LEFT JOIN anmelden a ON k.KursID = a.KursID
      GROUP BY k.KursID
      ORDER BY k.KursID;
    """).fetchall()
    return [dict(row) for row in result]

@anvil.server.callable
def get_Mitglied():
  with sqlite3.connect(data_files['Neicovcen_Vladislav_fitnessstudio.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
        Nachname || ' ' || Vorname as Name
      FROM Mitglied
    """).fetchall()
    return [dict(row) for row in result]

@anvil.server.callable
def app_tables_holen():
  table = app_tables.anmelden
  return table