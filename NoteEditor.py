import datetime


class NoteEditor:
    @staticmethod
    def add_note(notes):
        """
        Функция для добавления новой заметки
        :param notes: все заметки
        :return: создание заметки
        """
        if notes:
            last_id = notes[-1]['id']
        else:
            last_id = 0

        title = input("Введите заголовок заметки: ")
        body = input("Введите заметку: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note = {
            'ID': last_id + 1,
            'Заголовок': title,
            'Заметка': body,
            'Дата и время': timestamp
        }
        notes.append(note)
        print("Заметка успешно сохранена.")

    @staticmethod
    def delete_note(notes):
        """
        Функция для удаления заметки
        :param notes: все заметки
        :return: удаление заметки
        """
        note_id = int(input("Введите ID заметки для удаления: "))
        for note in notes:
            if note['ID'] == note_id:
                notes.remove(note)
                print("Заметка успешно удалена.")
                return
        print("Заметка с указанным ID не найдена.")

    @staticmethod
    def edit_note(notes):
        """
        Функция для редактирования заметки
        :param notes: все заметки
        :return: изменённая заметка
        """
        note_id = int(input("Введите ID заметки для редактирования: "))
        for note in notes:
            if note['id'] == note_id:
                title = input("Введите новый заголовок заметки: ")
                body = input("Введите новое тело заметки: ")
                note['Заголовок'] = title
                note['Заметка'] = body
                note['Дата и время'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Заметка успешно отредактирована.")
                return
        print("Заметка с указанным ID не найдена.")
