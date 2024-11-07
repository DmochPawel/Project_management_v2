from datetime import datetime
#deklaracja klasy zadanie w które będziemy przechowywać zadania
class Task:
    task_id = 0

    #deklaracja listy zadań w której będziemy przechowywać zadania
    tasks = []

    #konstruktor klasy Task
    def __init__(self, id, title, description, due_date, status="do zrobienia", priority="średni"):
        self.id = id
        self.title = title
        self.description = description
        try:
            # Konwersja daty na obiekt datetime
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print(f"Błąd formatu daty dla zadania '{title}' – oczekiwany format to 'YYYY-MM-DD'")
            self.due_date = None
        self.status = status
        self.priority = priority
        Task.tasks.append(self)