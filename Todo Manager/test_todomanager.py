import unittest

class Test_todomanager(unittest.TestCase):
    def test_addTask(self):
        task1 = Task("Do the dishes.")
        task2 = Task("Do the laundry.")
        
        todo_mgr = Todomanager()
        
        todo_mgr.tasks.append(task1)
        todo_mgr.tasks.append(task2)
        
        self.assertEqual(todo_mgr.tasks.index("1"), 0)
 

if __name__ == '__main__':
    unittest.main()
    