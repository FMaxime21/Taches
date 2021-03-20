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
    statut = "à faire"
    task_manager = TaskManager()

    action = task_manager.parse_del(command, numero, statut)

    assert action.numero == 1

def test_parse_add():
    command = "+ first task"
    numero = 1
    statut = "à faire"
    task_manager = TaskManager()

    action = task_manager.parse_add(command,numero, statut)

    assert action.name == "add"
    assert action.description == "first task"
    assert action.statut == "à faire"

def test_parse_statut_x():
    command = "x numero"
    numero = 1
    statut = "à faire"
    task_manager = TaskManager()

    action = task_manager.parse_statut_x(command, numero, statut)

    assert action.numero == 1
    assert action.statut == "à faire"

def test_parse_statut_o():
    command = "x numero"
    numero = 1
    statut = "fait"
    task_manager = TaskManager()

    action = task_manager.parse_statut_o(command, numero, statut)

    assert action.numero == 1
    assert action.statut == "fait"
