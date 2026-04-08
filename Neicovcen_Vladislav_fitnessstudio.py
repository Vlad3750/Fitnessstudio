import sqlite3

conn = sqlite3.connect("Neicovcen_Vladislav_fitnessstudio.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Trainer (
        TrainerID     INTEGER PRIMARY KEY AUTOINCREMENT,
        Vorname       TEXT NOT NULL,
        Nachname      TEXT NOT NULL,
        Spezialgebiet TEXT
    );

    CREATE TABLE IF NOT EXISTS Kurs (
        KursID         INTEGER PRIMARY KEY AUTOINCREMENT,
        Bezeichnung    TEXT NOT NULL,
        Wochentag      TEXT NOT NULL,
        Uhrzeit        TEXT NOT NULL,
        Max_Teilnehmer INTEGER NOT NULL,
        TrainerID      INTEGER NOT NULL,
        FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID)
    );

    CREATE TABLE IF NOT EXISTS Mitglied (
        MitgliedsID    INTEGER PRIMARY KEY AUTOINCREMENT,
        Vorname        TEXT NOT NULL,
        Nachname       TEXT NOT NULL,
        E_Mail         TEXT NOT NULL UNIQUE,
        Beitrittsdatum DATETIME NOT NULL
    );

    CREATE TABLE IF NOT EXISTS anmelden (
        AnmeldungsID INTEGER PRIMARY KEY AUTOINCREMENT,
        MitgliedsID  INTEGER NOT NULL,
        KursID       INTEGER NOT NULL,
        Anmeldung    DATETIME NOT NULL,
        FOREIGN KEY (MitgliedsID) REFERENCES Mitglied(MitgliedsID),
        FOREIGN KEY (KursID)      REFERENCES Kurs(KursID)
    );
""")

cursor.executemany(
    "INSERT INTO Trainer (Vorname, Nachname, Spezialgebiet) VALUES (?, ?, ?)",
    [
        ("Anna",   "Müller",  "Yoga & Meditation"),
        ("Bernd",  "Schmid",  "Krafttraining & Bodybuilding"),
        ("Lisa",   "Weber",   "Cardio & Ausdauer"),
        ("Markus", "Huber",   "Kampfsport & Selbstverteidigung"),
    ]
)

cursor.executemany(
    "INSERT INTO Kurs (Bezeichnung, Wochentag, Uhrzeit, Max_Teilnehmer, TrainerID) VALUES (?, ?, ?, ?, ?)",
    [
        ("Yoga Grundkurs",     "Montag",     "09:00", 12, 1),
        ("Yoga Fortgeschritt", "Donnerstag", "10:00",  8, 1),
        ("Pump & Burn",        "Dienstag",   "17:30", 15, 2),
        ("Rückenfit",          "Mittwoch",   "18:00", 20, 2),
        ("Cardio Blast",       "Freitag",    "07:00", 25, 3),
        ("Lauftreff",          "Samstag",    "08:30", 30, 3),
        ("Kickboxen Basis",    "Montag",     "19:00", 10, 4),
    ]
)

cursor.executemany(
    "INSERT INTO Mitglied (Vorname, Nachname, E_Mail, Beitrittsdatum) VALUES (?, ?, ?, ?)",
    [
        ("Klaus",   "Huber",   "k.huber@mail.at",   "2023-03-10 09:00:00"),
        ("Sandra",  "Bauer",   "s.bauer@mail.at",   "2023-07-22 14:00:00"),
        ("Tobias",  "Fischer", "t.fischer@mail.at", "2024-01-05 11:00:00"),
        ("Maria",   "Hofer",   "m.hofer@mail.at",   "2024-04-18 10:30:00"),
        ("Felix",   "Wagner",  "f.wagner@mail.at",  "2024-06-30 08:00:00"),
        ("Julia",   "Berger",  "j.berger@mail.at",  "2024-09-01 15:00:00"),
        ("Stefan",  "Mayer",   "s.mayer@mail.at",   "2025-01-12 13:00:00"),
    ]
)

cursor.executemany(
    "INSERT INTO anmelden (MitgliedsID, KursID, Anmeldung) VALUES (?, ?, ?)",
    [
        (1, 1, "2025-01-05 09:00:00"),  # Klaus   → Yoga Grundkurs
        (1, 5, "2025-01-05 09:10:00"),  # Klaus   → Cardio Blast
        (2, 1, "2025-01-06 10:00:00"),  # Sandra  → Yoga Grundkurs
        (2, 2, "2025-01-06 10:05:00"),  # Sandra  → Yoga Fortgeschritt
        (3, 3, "2025-01-07 14:00:00"),  # Tobias  → Pump & Burn
        (4, 4, "2025-01-08 11:00:00"),  # Maria   → Rückenfit
        (4, 6, "2025-01-08 11:10:00"),  # Maria   → Lauftreff
        (5, 7, "2025-02-01 08:00:00"),  # Felix   → Kickboxen Basis
        (6, 5, "2025-02-03 16:00:00"),  # Julia   → Cardio Blast
        (6, 3, "2025-02-03 16:05:00"),  # Julia   → Pump & Burn
        (7, 4, "2025-03-10 12:00:00"),  # Stefan  → Rückenfit
        (7, 7, "2025-03-10 12:10:00"),  # Stefan  → Kickboxen Basis
    ]
)

conn.commit()
conn.close()

print("Datenbank 'fitnessstudio.db' erfolgreich erstellt.")