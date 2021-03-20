from todos import TaskManager, Action_add


def test_can_create_an_action():
    action = Action_add("add", "first task", 1)
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
    task_manager = TaskManager()

    action = task_manager.parse_del(command, numero)

    assert action.numero == 1
    
def test_parse_add():
    command = "+ first task"
    numero = 1
    task_manager = TaskManager()

    action = task_manager.parse_add(command,numero)

    assert action.name == "add"
    assert action.description == "first task"
