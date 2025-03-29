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


task1 = Task("Do the dishes.")
task2 = Task("Do the laundry.")

todo_mgr = TodoManager()

todo_mgr.addTask(task1)
todo_mgr.addTask(task2)

print(todo_mgr.tasks[1].description)