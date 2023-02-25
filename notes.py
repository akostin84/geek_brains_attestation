from datetime import datetime, date, time
import uuid
from os.path import exists


PATH = "my_notes.csv"
SEPARATOR = ";"


def main():
    print("Проект 'Заметки'")
    user_choise = -1
    while user_choise != 0:
        n = Notes(PATH)
        user_choise = UI.read_from_console()
        print("you selected:", user_choise)
        if user_choise == 1:
            n.show()
        elif user_choise == 2:
            print("Введите дату в формате ММ.ДД.ГГГГ")
            day = input()
            n.showAtDate(day)
        elif user_choise == 3:
            print("Введите идентификатор заметки")
            id = input()
            UI.delete_note(n, id)
            n.write(PATH)



    # n.show()
    # UI.add_note(n, "first", "beginning")
    # n.show()
    # n.write(PATH)
    # b = n.findID(uuid.UUID("78407295-2341-4a5c-8143-f63ee79d95ea"))
    # print("found", b)
    # print("old text:", b.title)
    # b.title= "new gg"
    # print("new text:", b.title)
    # # print(type(b.created))
    # n.showAtDate("12.24.2023")
    # n.write(PATH)
    # print("edit mode")
    # UI.edit_msg(n,"2113d13a-1a7a-4300-8af6-f9a35748d5fa", "edited")
    # n.write(PATH)
    # print("delete mode")
    # UI.delete_note(n, "713e9664-1f1a-4315-966d-d30c3242d4cf")
    # n.write(PATH)


class UI():  
    def add_note(notes, title, msg):
        new_note = Note()
        new_note.title = title
        new_note.msg = msg
        notes.add(new_note)

    def edit_msg(notes, note_id: str, new_msg: str):
        edited_note = notes.findID(uuid.UUID(note_id))
        edited_note.msg = new_msg

    def edit_title(notes, note_id: str, new_title: str):
        edited_note = notes.findID(uuid.UUID(note_id))
        edited_note.title = new_title

    def delete_note(notes, note_id: str):
        deleted_note = notes.findID(uuid.UUID(note_id))
        if deleted_note in notes.notes:
            notes._notes.remove(deleted_note)
    
    def read_from_console():
        print("Выберите номер действия:")
        print("1. Показать все заметки")
        print("2. Показать заметки за выбранную дату")
        print("3. Удалить заметку")
        print("4. Изменить заголовок заметки")
        print("5. Изменить текст заметки")
        print("6. Добавить заметку")
        print("0. Выйти")
        message = input()
        try:
            selection = int(message)
        except:
            selection = 0
            print("Ошибка ввода. Выход")
        finally:
            if selection not in range(7):
                print("Ошибка ввода. Выход")
                selection = 0
        return selection


class Notes:
    # конструктор списка заметок
    def __init__(self, path):
        n = []
        if exists(path):
            with open(path, 'r') as fp:
                for line in fp:
                    n.append(Note.str2Note(line))
        else:
            open(path, 'a').close()
        self._notes = n
      
    @property
    def notes(self):
        return self._notes

    @notes.setter    
    def notes(self, list_of_notes):
        self._notes = list_of_notes
    
    def show(self):
        # для вывода на экран
        for n in self.notes:
            print(n.toString())
    
    def add(self, n):
        existed = self.notes
        existed.append(n)
        self.notes = existed
    
    def write(self, path):
        f = open(path, "w")
        [f.writelines(i.toLine()) for i in self.notes]
        f.close()
    
    def findID(self, id):
        for n in self.notes:
            if n.id == id:
                return n
    
    def _findDate(self, stringDate):
        notes_at_day = []
        dt = datetime.strptime(stringDate, "%m.%d.%Y")
        for n in self.notes:
            note_day = datetime.strptime(n.created,"%m.%d.%Y, %H:%M:%S").date()
            if dt.date() == note_day:
                notes_at_day.append(n)
        return notes_at_day
    
    def showAtDate(self, stringDate):
        n = self._findDate(stringDate)
        [print(i) for i in n]
    

class Note:
    # конструктор заметки
    def __init__(self):
        self._id = uuid.uuid4()
        self._created = datetime.now().strftime("%m.%d.%Y, %H:%M:%S")
        self._title = ""
        self._msg = ""

    @property
    def id(self):
        return self._id 

    @id.setter    
    def id(self, stringID):
        self._id = uuid.UUID(stringID)
    
    @property    
    def created(self):
        return self._created

    @created.setter 
    def created(self, stringDate):
        self._created = stringDate

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, text):
        self._title = text

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, text):
        self._msg = text

    def __str__(self):
        # для вывода на экран
        return self.toString()
    
    def toString(self):
        return '{} at {}: {}'.format(self.id, self.created, self.title)
    
    def toLine(self):
        # для вывода в файл
        return "{}{}{}{}{}{}{}\n".format(self.id, SEPARATOR, self.created, SEPARATOR, self.title, SEPARATOR, self.msg)
    
    def str2Note(sNote):
        splitted = sNote.split(SEPARATOR)
        new_note = Note()
        new_note.id = splitted[0]
        new_note.created = splitted[1]
        new_note.title = splitted[2]
        new_note.msg = splitted[3].rstrip()
        return new_note


if __name__ == '__main__':
    main()