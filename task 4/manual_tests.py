from task4 import *

manager = TaskManager()
task = manager.create_task('Cleaning', 'Clean your room')
complex_task = manager.create_complex_task('Exams preparation', 'Finish all assignments before exams start')
subtask_1 = manager.create_subtask('Python', 'Prepare your git and send it to the teacher', complex_task)
subtask_2 = manager.create_subtask('Statistics', 'Solve HW-8', complex_task)
subtask_3 = manager.create_subtask('Algorithms', 'Solve theoretical HW-9 and contest', complex_task)
manager.get_tasks()
manager.get_complex_tasks()
manager.get_complex_tasks_by_id(complex_task.id)
manager.update_status(subtask_1, 'finished')
manager.get_complex_tasks()
manager.update_status(subtask_2, 'finished')
manager.get_complex_tasks()
manager.update_status(complex_task, 'finished')
manager.get_subtasks()
manager.update_status(task, 'finished')
manager.get_tasks()
