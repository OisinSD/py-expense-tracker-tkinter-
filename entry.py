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

    def add(self, title: str, date: date, entry_type: str, description: str, amount: int) -> Entry:
        new_id = 1
        if self.entries:
            new_id = int(self.entries[-1].id) + 1

        new_entry = Entry(new_id, title, date, entry_type, description, amount)
        self.entries.append(new_entry)
        return new_entry
    
    def delete(self, entry_id: int) -> Entry | None:
        for entry in self.entries:
            if entry.id == entry_id:
                self.entries.remove(entry)
                return entry
        return None
    
    def edit():
        pass

    def save():
        pass

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


