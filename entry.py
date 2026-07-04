import json
from pathlib import Path
from datetime import date


class Entry:
    """ Each Entry has ... """
    def __init__(self, id, title, date, type, description, amount):
        self.id = id
        self.title = title
        self.date = date 
        self.type = type
        self.description = description
        self.amount = amount 

    

class EntryLogic:
    """ Each Entry has CRUD functionality which is defined in this class """
    def __init__(self, entries: list[Entry]):
        self.entries = entries


    def validate_entry(): 
        pass

    def add(self, title: str, date: date, entry_type: str, description: str, amount: int, entry_id: int | None = None) -> Entry:
        if entry_id is None:
            new_id = 1
            if self.entries:
                new_id = int(self.entries[-1].id) + 1
        else:
            new_id = entry_id

        new_entry = Entry(new_id, title, date, entry_type, description, amount)
        self.entries.append(new_entry)
        return new_entry
    
    def delete(self, entry_id: int) -> Entry | None:
        for entry in self.entries:
            if entry.id == entry_id:
                self.entries.remove(entry)
                return entry
        return None
    
    def update(self, entry_id: int, title: str, date: date, entry_type: str, description: str, amount: int) -> Entry | None:
        for entry in self.entries:
            if entry.id == entry_id:
                entry.title = title
                entry.date = date
                entry.type = entry_type
                entry.description = description
                entry.amount = amount
                return entry
        return None

    def edit(self, entry_id: int, title: str, date: date, entry_type: str, description: str, amount: int) -> Entry | None:
        return self.update(entry_id, title, date, entry_type, description, amount)
        

    def save_to_file(self, file_path: str | Path) -> None:
        data = []
        for entry in self.entries:
            data.append(
                {
                    "id": entry.id,
                    "title": entry.title,
                    "date": entry.date,
                    "type": entry.type,
                    "description": entry.description,
                    "amount": entry.amount,
                }
            )

        path = Path(file_path)
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def from_file(cls, file_path: str | Path) -> "EntryLogic":
        path = Path(file_path)
        if not path.exists():
            return cls([])

        raw_text = path.read_text(encoding="utf-8").strip()
        if not raw_text:
            return cls([])

        payload = json.loads(raw_text)
        entries = []
        for item in payload:
            entries.append(
                Entry(
                    item["id"],
                    item["title"],
                    item["date"],
                    item["type"],
                    item["description"],
                    item["amount"],
                )
            )
        return cls(entries)

    def get_income(self) -> float:
        income = 0
        for entry in self.entries:
            if entry.type.lower() == "income":
                income += entry.amount
        return income

    def get_expenses(self) -> float:
        expense = 0
        for entry in self.entries:
            if entry.type.lower() == "expense":
                expense += entry.amount
        return expense

    def get_net_income(self) -> float:
        return self.get_income() - self.get_expenses() 


