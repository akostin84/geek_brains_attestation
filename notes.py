from datetime import datetime, date, time
import uuid


PATH = "my_notes.txt"
SEPARATOR = "|"


def main():
    print("Проект 'Заметки'")
    n = Notes(PATH)
    n.show()
    a = Note()
    a.id = "d3413dee-b227-4a73-ae30-64de38f31e10"
    a.created = "03.24.2023, 22:29:09"
    print("new note")
    a.text = "new note 3"
    n.add(a)
    print("notes with new one")
    n.show()
    n.write(PATH)
  

class Notes:
    # конструктор списка заметок
    def __init__(self, path):
        n = []
        with open(path, 'r') as fp:
            for line in fp:
                n.append(Note.str2Note(line))
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

 
class Note:
    # конструктор заметки
    def __init__(self):
        self._id = 0
        self._created = 0
        self._text = ""

    @property
    def id(self):
        return self._id 

    @id.setter    
    def id(self, stringID):
        self._id = uuid.UUID(stringID)
    
    @property    
    def created(self):
        return self._created.strftime("%m.%d.%Y, %H:%M:%S")

    @created.setter 
    def created(self, stringDate):
        self._created = datetime.strptime(stringDate, "%m.%d.%Y, %H:%M:%S")

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def __str__(self):
        # для вывода на экран
        return self.toString()
    
    def toString(self):
        return '{}: {}'.format(self.created, self.text)
    
    def toLine(self):
        # для вывода в файл
        return "{}{}{}{}{}\n".format(self.id, SEPARATOR, self.created, SEPARATOR, self.text)
    
    def str2Note(sNote):
        splitted = sNote.split(SEPARATOR)
        new_note = Note()
        new_note.id = splitted[0]
        new_note.created = splitted[1]
        new_note.text = splitted[2].rstrip()
        return new_note


if __name__ == '__main__':
    main()