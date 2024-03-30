import datetime
import json
import os.path
from operator import itemgetter

fn = "note.json"
notes = {}
id = 1
def write(data, faleName):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(faleName, 'w', encoding='utf-8')as file:
        json.dump(data, file, indent=4)

def read (fileName):
    with open(fileName,'r',encoding='utf-8') as file:
        return json.load(file)

def enterNote(id):
    titleNote = input("Введите заголовок заметки: ")
    bodyNote = input("Введите тело заметки: ")
    dataNote = datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')
    note = {"id": id, "date": dataNote, "title": titleNote, "body": bodyNote}
    return note
def add (id):
    notes.append(enterNote(id))
    write(notes, fn)
    print("Заметка успешно сохранена")


def selectDate():
    try:
        notesDate = []
        date = input("Введите дату для поиска заметки: ")
        dateObj = datetime.datetime.strptime(date,'%d.%m.%Y')
        for note in notes:
            if dateObj.date() == datetime.datetime.strptime(note['date'],'%y/%m/%d %H:%M:%S').date():
                notesDate.append(note)
        printNote(notesDate)
    except ValueError:
        print("Введен неверный формат")

def selectEntry():
    notesId = []
    selectId = input("Введите id заметки для поиска: ")
    for note in notes:
        if selectId == str(note['id']):
            notesId.append(note)
    if not notesId:
        print("Заметка с данным id не найдена")
    else:
        printNote(notesId)
def printNote (dict):
    d = sorted(dict,key=itemgetter('date'))
    for elem in d:
        print(elem['id'], ';', elem['title'], ';',elem['body'], elem['date'])

def editNote():
    editId = input("Введите id изменяемой заметки: ")
    flag = True
    for note in notes:
        if editId == str(note['id']):
            noteNew = enterNote(editId)
            note['title'] = noteNew['title']
            note['body'] = noteNew['body']
            note['date'] = datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')
            write(notes,fn)
            flag = False
    if flag:
        print("Заметка с данным id не найдена")

def delete():
    editId = input("Введите id удаляемой заметки: ")
    flag = True
    for note in notes:
        if editId == str(note['id']):
            notes.remove(note)
            write(notes, fn)
            flag = False
    if flag:
        print("Заметка с данным id не найдена")

print("Список команд: \n"
          "add - Добавление заметки\n"
          "date - Поиск по дате\n"
          "id - Поиск по id\n"
          "all - Вывод всех заметок\n"
          "correct - изменение заметки по id\n"
          "del - Удаление заметки по id\n"
          "exit - Выход"
          )
if not os.path.exists(fn):
    notes = []
else:
    notes = read(fn)
    id = len(notes) + 1

while (True):
    command = input("Введите команду: ")
    if command == "add":
        add(id)
    elif command == "date":
        selectDate()
    elif command == "all":
        printNote(notes)
    elif command == "id":
        selectEntry()
    elif command == "correct":
        editNote()
    elif command == "del":
        delete()
    elif command == "exit":
        break
    id = id + 1


