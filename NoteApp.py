from NoteEditor import NoteEditor
from NotePrinter import NotePrinter
from NoteManager import NoteManager
import re


class NoteApp:
    def __init__(self):
        """
        Создание связей между классами
        """
        self.note_manager = NoteManager()
        self.note_printer = NotePrinter()
        self.note_editor = NoteEditor()

    def run(self):
        """
        Основной цикл программы
        """
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Выборка заметок по дате")
        print("4. Показать определенную заметку по ID")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("0. Выйти")

        choice = input("Введите команду (0-6): ")

        match choice:

            case "1":
                self.note_editor.add_note(self.note_manager.notes)
                self.note_manager.save_notes()
            case '2':
                self.note_printer.display_notes(self.note_manager.notes)
            case "3":
                self.note_printer.filter_notes_by_date(self.note_manager.notes)
            case "4":
                note_id = int(input("Введите ID заметки для отображения: "))
                specific_note = next((note for note in self.note_manager.notes if note['id'] == note_id), None)
                if specific_note:
                    self.note_printer.display_specific_note(specific_note)
                raise Exception('ID не найден')
            case '5':
                self.note_editor.edit_note(self.note_manager.notes)
                self.note_manager.save_notes()
            case '6':
                self.note_editor.delete_note(self.note_manager.notes)
                self.note_manager.save_notes()
            case '0':
                print("До новых встреч!")
        if re.match(r'[7-9]', choice):
            raise Exception("Не корректный выбор")
