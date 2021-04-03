class TaskManager:
    def __init__(self):
        self.tasks = []

    def parse_add(self, command, numero, statut):
        return Action_add("add", command[2:], "1", "a faire") 

    def parse_del(self, command, numero, statut):
        return Action_del("del", command[2:], 1, "a faire")

    def parse_statut_x(self,command, numero, statut):
        return Action_add("del", command[2:], 1, "a faire")

    def parse_statut_o(self,command, numero, statut):
        return Action_add("del", command[2:], 1, "fait")

class Action_add:
    def __init__(self, name, description, numero, statut):
        self.name = name
        self.description = description
        self.numero = numero
        self.statut = statut

    def __del__(self):
        del self   

class Action_del:
    def __init__(self, name, description, numero, statut):
        self.name = name
        self.description = description
        self.numero = numero
        self.statut = statut
        del self
        