from enum import Enum

class Status(Enum):
    assigned = 0
    in_process = 1
    finished = 2


class Task:
    def __init__(self, id, name, description, status = Status.assigned):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class Subtask(Task):
    def __init__(self, id, name, description, parent_id, status = Status.assigned):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id


class ComplexTask(Task):
    def __init__(self, id, name, description, status = Status.assigned):
        super().__init__(id, name, description, status)
        self.subtasks = {}

    #def add_subtask(self, subtask):
     #   self.subtasks.append(subtask.get_id())


class TaskManager:
    id_series = 0

    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}

    def get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1
        return next_id_value

    def create_task(self, name, description):
        current_id = self.get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task

    def create_subtask(self, name, description, complex_task):
        parent_id = complex_task.get_id()
        current_id = self.get_and_increment_id()
        new_subtask = Subtask(current_id, name, description, parent_id)
        self.subtasks[current_id] = new_subtask
        complex_task.subtasks[current_id] = new_subtask
        return new_subtask


    def create_complex_task(self, name, description):
        current_id = self.get_and_increment_id()
        new_complex_task = ComplexTask(current_id, name, description)
        self.complex_tasks[current_id] = new_complex_task
        return new_complex_task


    def get_tasks(self):
        if not self.tasks:
            print("You have no tasks.")
        else:
            print("Your tasks are:")
            print("===============================================")
            for i, task in enumerate(self.tasks.values()):
                print("""{}. Task: {}(id: {}). \n Decription: "{}".\n Current status: {} \n""".format(i+1, task.name, task.id, task.description, task.status.name))
                print("----------------------------------------------")
            print("===============================================")
        return self.tasks


    def get_subtasks(self):
        if not self.subtasks:
            print("No subtasks are found.")
        else:
            print("Your subtasks are:")
            print("===============================================")
            for i, task in enumerate(self.subtasks.values()):
                print("""{}. Subtask "{}" (id: {}) for complex task "{}". \n Decription: "{}".\n Current status: {} """.format(i+1,
                                                                                                                      task.name,
                                                                                                                    task.id,
                                                                                                                self.complex_tasks[task.parent_id].name,
                                                                                                                task.description,
                                                                                                                task.status.name))
                print("------------------------------------------------")
            print("===============================================")
        return self.subtasks



    def get_complex_tasks(self):
        if not self.complex_tasks:
            print("You have no complex tasks.")
        else:
            print("Your complex tasks are:")
            print("===============================================")
            for j, task in enumerate(self.complex_tasks.values()):
                print("""{}. Complex task "{}"(id: {}). \n Decription: "{}".\n Current status: {} \n""".format(j+1,
                                                                                                     task.name,
                                                                                                    task.id,
                                                                                                    task.description,
                                                                                                    task.status.name))

                print("Subtasks of this complex task:")
                for i, subtask in enumerate(task.subtasks.values()):
                    print("""{}. {}(id: {})\n Status: {}.""".format(i+1, subtask.name, subtask.id, subtask.status.name))
                print("----------------------------------------------")
            print("===============================================")
        return self.complex_tasks

    def get_tasks_by_id(self, id):
        task = self.tasks[id]
        print("""Task {}: "{}". \n Decription: "{}". \n Status: {}""".format(id, task.name, task.description, task.status.name))
        return task

    def get_subtasks_by_id(self, id):
        subtask = self.subtasks[id]
        print("""Subtask {} for complex task "{}": "{}". \n Description : "{}".\n Status: {}""".format(id,
                                                                                                       self.complex_tasks[subtask.parent_id].name,
                                                                                                       subtask.name,
                                                                                                       subtask.description,
                                                                                                       subtask.status.name))
        return subtask

    def get_complex_tasks_by_id(self, id):
        complex_task = self.complex_tasks[id]
        print("""Complex task {}: {}. \n Description: {}. \n Status: {}""".format(id,
                                                                                  complex_task.name,
                                                                                  complex_task.description,
                                                                                  complex_task.status.name))
        print("Subtasks of this complex tasks:")
        for i, subtask in enumerate(complex_task.subtasks.values()):
            print("""{}. {}\n Description: {}. \n Status: {}""".format(i+1,
                                                                       subtask.name,
                                                                       subtask.description,
                                                                       subtask.status.name))
        return complex_task

    def remove_tasks(self):
        self.tasks.clear()

    def remove_subtasks(self):
        for complex_task in self.complex_tasks.values():
            complex_task.subtasks = {}
        self.subtasks.clear()


    def remove_complex_tasks(self):
        self.remove_subtasks()
        self.complex_tasks.clear()


    def remove_task_by_id(self, id):
        self.tasks.pop(id)

    def remove_subtask_by_id(self, id):
        self.complex_tasks[self.subtasks[id].parent_id].subtasks.pop(id)
        self.subtasks.pop(id)

    def remove_complex_task_by_id(self, id):
        for key in self.complex_tasks[id].subtasks.keys():
            self.subtasks.pop(key)
        self.complex_tasks.pop(id)

    def update_status(self, task, status):
        name = type(task).__name__
        if status == 'in_process':
            if name == "Task":
                task.status = Status.in_process
            elif name == "Subtask":
                task.status = Status.in_process
                self.complex_tasks[task.parent_id].status = Status.in_process
            else:
                task.status = Status.in_process
        elif status == 'finished':
            if name == 'Task':
                self.remove_task_by_id(task.id)
            elif name == 'Subtask':
                self.remove_subtask_by_id(task.id)
                if not self.complex_tasks[task.parent_id].subtasks:
                    self.remove_complex_task_by_id(task.parent_id)
            else:
                self.remove_complex_task_by_id(task.id)


