import csv
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.database import SessionLocal, engine, Base
from app.models.olympic import OlympicEvent

def seed():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    path = os.path.join(os.path.dirname(__file__), "..", "data", "athlete_events.csv")

    with open(path, newline="", encoding="utf-8") as f: 
        reader = csv.DictReader(f)
        for row in reader:
            event = OlympicEvent(
                athlete_id=int(row["ID"]) if row["ID"] else None,
                name=row["Name"],
                sex=row["Sex"],
                age=int(row["Age"]) if row["Age"].isdigit() else None,
                height=int(row["Height"]) if row["Height"].isdigit() else None,
                weight=int(float(row["Weight"])) if row["Weight"].replace(".", "").isdigit() else None,
                team=row["Team"],
                noc=row["NOC"],
                year=int(row["Year"]),
                season=row["Season"],
                city=row["City"],
                sport=row["Sport"],
                event=row["Event"],
                medal=row["Medal"] if row["Medal"] != "NA" else None,
            )
            db.add(event)
    db.commit()
    db.close()
    print("Done seeding!")
if __name__ == "__main__":
    seed()
