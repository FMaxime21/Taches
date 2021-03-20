class TaskManager:
    def __init__(self):
        self.tasks = []

    def parse_add(self, command, numero):
        return Action_add("add", command[2:], 1) 

    def parse_del(self, command, numero):
        return Action_del("del", command[2:], 1)

class Action_add:
    def __init__(self, name, description, numero):
        self.name = name
        self.description = description
        self.numero = numero

    def __del__(self):
        del self   

class Action_del:
    def __init__(self, name, description, numero):
        self.name = name
        self.description = description
        self.numero = numero
        del self            
        