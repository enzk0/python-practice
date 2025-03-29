class Task:
    def __init__(self, description):
        self.description = description
        self.state = "incomplete"
        
class TodoManager:
    def __init__(self):
        self.tasks = []
        
    def addTask(self, description):
        self.tasks.append(description)
