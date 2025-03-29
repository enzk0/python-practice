import unittest
from todomanager import Task
from todomanager import TodoManager

class Test_todomanager(unittest.TestCase):
    def test_addTask(self):
        task1 = Task("Do the dishes.")
        task2 = Task("Do the laundry.")
        
        todo_mgr = TodoManager()
        
        todo_mgr.tasks.append(task1)
        todo_mgr.tasks.append(task2)
               
        self.assertEqual(todo_mgr.tasks[0].description, "Do the dishes.")
        self.assertEqual(todo_mgr.tasks[1].description, "Do the laundry.")
        
    def test_removeTask(self):
        task1 = Task("Do the dishes.")
        task2 = Task("Do the laundry.")
        
        todo_mgr = TodoManager()
        
        todo_mgr.tasks.append(task1)
        todo_mgr.tasks.append(task2)
               
        todo_mgr.tasks.removeTask("Do the dishes.")
        todo_mgr.tasks.removeTask("Do the laundry.")
        
        self.assertNotIn(task1.description, todo_mgr.tasks[0].description, "It is in the list")
 

if __name__ == '__main__':
    unittest.main()
    