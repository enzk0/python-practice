class Task:
    def __init__(self, description):
        self.description = description
        self.state = "incomplete"
        
class TodoManager:
    def __init__(self):
        self.tasks = []
        
    def addTask(self, identifier):
        self.tasks.append(identifier)
    
    def removeTask(self, identifier):
        self.tasks.remove(identifier)