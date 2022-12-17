import unittest

from task4 import *

class TestManager(unittest.TestCase):

    def test_delete_subtasks(self):
        manager = TaskManager()
        complex_task = manager.create_complex_task('Exam Preparation', 'Prepare for the exam')
        subtask_1 = manager.create_subtask('Lectures', 'Revise lecture material', complex_task)
        subtask_2 = manager.create_subtask('Practice', 'Revise practice tasks', complex_task)
        subtask_3 = manager.create_subtask('Consultation', 'Ask questions in the before-exam consultation', complex_task)
        manager.update_status(subtask_1, 'finished')
        manager.update_status(subtask_2, 'finished')
        manager.update_status(subtask_3, 'finished')
        with self.assertRaises(KeyError):
            manager.get_complex_tasks_by_id(complex_task.id)

    def test_delete_complex_tasks(self):
        manager = TaskManager()
        complex_task = manager.create_complex_task('Exam Preparation', 'Prepare for the exam')
        subtask_1 = manager.create_subtask('Lectures', 'Revise lecture material', complex_task)
        manager.update_status(complex_task, 'finished')
        with self.assertRaises(KeyError):
            manager.get_subtasks_by_id(subtask_1.id)

    def test_update_subtask_status(self):
        manager = TaskManager()
        complex_task = manager.create_complex_task('Exam Preparation', 'Prepare for the exam')
        subtask_1 = manager.create_subtask('Lectures', 'Revise lecture material', complex_task)
        manager.update_status(subtask_1, 'in_process')
        self.assertEqual(complex_task.status.name, 'in_process')

    def test_remove_complex_tasks(self):
        manager = TaskManager()
        complex_task = manager.create_complex_task('Exam Preparation', 'Prepare for the exam')
        subtask_1 = manager.create_subtask('Lectures', 'Revise lecture material', complex_task)
        manager.remove_complex_tasks()
        with self.assertRaises(KeyError):
            manager.get_subtasks_by_id(subtask_1.id)






if __name__ == '__main__':
    unittest.main()

