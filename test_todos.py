import sqlite3
from todos import TaskManager, Action_add


def test_can_create_an_action():
    action = Action_add("add", "first task", 1, "à faire")
    assert action.name == "add"
    assert action.description == "first task"
    assert action.numero == 1


def test_can_create_a_task_manager():
    task_manager = TaskManager()


def test_task_manager_starts_with_no_tasks():
    task_manager = TaskManager()

    assert task_manager.tasks == []

def test_parse_del():
    command = "- numero"
    numero = 1
    statut = "a faire"
    task_manager = TaskManager()

    action = task_manager.parse_del(command, numero, statut)

    assert action.numero == 1

def test_parse_add():
    command = "+ first task"
    numero = 1
    statut = "a faire"
    task_manager = TaskManager()

    action = task_manager.parse_add(command,numero, statut)

    assert action.name == "add"
    assert action.description == "first task"
    assert action.statut == "a faire"

def test_parse_statut_x():
    command = "x numero"
    numero = 1
    statut = "a faire"
    task_manager = TaskManager()

    action = task_manager.parse_statut_x(command, numero, statut)

    assert action.numero == 1
    assert action.statut == "a faire"

def test_parse_statut_o():
    command = "x numero"
    numero = 1
    statut = "fait"
    task_manager = TaskManager()

    action = task_manager.parse_statut_o(command, numero, statut)

    assert action.numero == 1
    assert action.statut == "fait"

def test_repository():
    task_manager = TaskManager()
    tache1 = task_manager.parse_add("tache1", "1", "A faire")
    tasks = [tache1]

    assert task_manager.tasks == []

def test_read_file():
    fichier = open("liste_taches.txt", "r")
    Read = fichier.read()
    print(Read)
    fichier.close()

def test_write_file_tasks():
    fichier = open("liste_taches.txt", "w")
    task_manager = TaskManager()
    tache1 = task_manager.parse_add("", "", "")
    fichier.write(tache1.name)
    fichier.write(" ")
    fichier.write(tache1.numero)
    fichier.write(" ")
    fichier.write(tache1.statut)
    fichier.write(" ")
    fichier.close()