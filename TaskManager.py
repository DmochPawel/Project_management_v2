from Task import *
from colorama import Fore, Style, init
import csv
from datetime import datetime

# Inicjalizacja colorama (wymagana na Windowsie)
init(autoreset=True)

class TaskManager:

    #konstruktor klasy TaskManager
    def __init__():
       pass

    def add_task():

        title = input("Podaj tytuł zadania: ")
        description = input("Podaj opis zadania: ")
        due_date = input("Podaj termin wykonania (YYYY-MM-DD): ")
        status = input("Podaj status zadania (np. 'do zrobienia', 'w toku', 'zakończone'): ")
        priority = input("Priorytet (np. 'niski', 'średni', 'wysoki'): ")
        Task.task_id += 1
        id = Task.task_id
        task = Task(id, title, description, due_date, status, priority)
        print(Fore.GREEN +"Zadanie dodane!\n")

    def __repr__(self):
         return f"{self.id}"

    #funkcja wyświetlająca listę zadań
    def view_tasks(list):
        for task in list:
            print(Fore.YELLOW +"""ID: {}
                  Title: {}
                  Description: {}
                  Due date: {}
                  Status: {}
                  Priority: {}
                  """.format(task.id, task.title, task.description, task.due_date, task.status, task.priority )) 

    # #funkcja wyświetlająca konkretne zadanie z listy zadań
    # def view_task():
    #     id = input("Podaj ID zadania: ")
    #     for task in Task.tasks:
    #             if task.id == int(id):
    #                 print(Fore.YELLOW +"""ID: {}
    #               Title: {}
    #               Description: {}
    #               Due date: {}
    #               Status: {}
    #               Priority: {}
    #               """.format(task.id, task.title, task.description, task.due_date, task.status, task.priority )) 
    #                 return
    #     print(Fore.RED +"Brak zadania o tym ID")
        

    #funkcja usuwająca konkretne zadanie z listy zadań
    def remove_task():  
        id = input("Podaj ID zadania: ")      
        for task in Task.tasks:   
            if task.id == int(id):
                Task.tasks.remove(task)
                print(Fore.GREEN +"Usunieto zadanie ID: {}".format(task.id))
                return
        print(Fore.RED +"Brak zadania o tym ID\n")

    #funkcja usuwająca konkretne zadanie z listy zadań
    def filter_tasks_by_date():
        date_input = input("Podaj poszukiwaną datę (YYYY-MM-DD): ")
        
        try:
            # Konwersja wprowadzonej daty na obiekt datetime
            search_date = datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print(Fore.RED + "Nieprawidłowy format daty. Wprowadź datę w formacie YYYY-MM-DD.\n")
            return
        
    # Filtrowanie zadań po dacie
        temp_list = [task for task in Task.tasks if datetime.date(task.due_date) == datetime.date(search_date)]
    
        if not temp_list:
            print(Fore.RED + "Brak zadania z tą datą\n")
        else:
            TaskManager.view_tasks(temp_list)
        
    #funkcja edytująca konkretne zadanie z listy zadań
    def edit_task():
        while True:
            id = input("Podaj ID zadania: ") 
            print("\nWybór parametru")
            print("1. Tytuł")
            print("2. Opis")
            print("3. Data wykonania")
            print("4. Status")
            print("5. Priorytet")
            print("6. Przerwij")

            choice = input("wybierz opcję 1-6: ")

            if choice == '1':
                arg = "title"
            elif choice == '2':
                arg = "description"
            elif choice == '3':
                arg = "due_date"
            elif choice == '4':
                arg = "status"
            elif choice == '5':
                arg = "priority"
            elif choice == '6':
                break
            else:
                print(Fore.RED +"Wybrałeś wartość spoza zakresu!")
            
            new_value = input("Podaj nową wartość: ")
        
            for task in Task.tasks: 
                if task.id == int(id):
                    setattr(task, arg, new_value)
                    print("Zmieniono wartość {} zadania {} na {}".format(arg, task.id, new_value))
                    return
            
            print(Fore.RED +"Brak zadania o tym ID\n")

    def load_tasks_from_csv(filename):
        with open(filename, mode = 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Task.task_id += 1
                try:
                    task = Task(
                        id = Task.task_id,
                        title=row['title'],
                        description=row['description'],
                        due_date=row['due_date'],
                        status=row['status'],
                        priority=row['priority']
                    )
                except KeyError as e:
                    print(Fore.RED +f"Błąd: brakujący klucz {e} w wierszu {row}")
        return

    def main_menu():
        while True:
            print("\n===System zarządzania zadaniami===")
            print("1. Dodaj zadanie")
            print("2. Edytuj zadanie")
            print("3. Usuń zadanie")
            print("4. Wyświetl wszystkie zadania")
            print("5. Filtruj po dacie")
            print("6. Wyjdź")
            choice = input("wybierz opcję 1-6: ")

            if choice == '1':
                TaskManager.add_task()
            elif choice == '2':
                TaskManager.edit_task()
            elif choice == '3':
                TaskManager.remove_task()
            elif choice == '4':
                TaskManager.view_tasks(Task.tasks)
            elif choice == '5':
                TaskManager.filter_tasks_by_date()       
            elif choice == '6':
                print(Fore.BLUE +"Do widzenia!")
                break
            else:
                print(Fore.RED +"Wybrałeś wartość spoza zakresu!")
                        