from todoData import getTodoData, setTodoData

def completeTask(id):
    if "-" not in id and "." not in id and id.isdigit():
        id = int(id)
    else:
        print("Invalid id.")
        return

    todoData = getTodoData()
    
    for i, o in enumerate(todoData.tasks):
        if o.id == id:
            todoData.tasks[i].done = True
            todoData.completed.append(todoData.tasks[i])
            del todoData.tasks[i]
            break

    setTodoData(todoData)