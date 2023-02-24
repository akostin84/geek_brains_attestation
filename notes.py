from datetime import datetime, date, time
import uuid

def main():
    print("Проект 'Заметки'")
    a = Note(uuid.uuid4(), datetime.now(), "bb")
    b = Note(uuid.uuid4(), datetime.now(), "aa")
    print(a)
    print(b)
    b.text ="gg"
    print(b)
    print(a.toLine())


class Note:
    # конструктор заметки
    def __init__(self, id, created, text):
        self._id = id
        self._created = created
        self._text = text

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
        return '({}: {})'.format(self.created, self.text)

    def toLine(self):
        # для вывода в файл
        return "{}|{}|{}".format(self.id, self.created, self.text)


if __name__ == '__main__':
    main()