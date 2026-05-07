memory_value = 0

def memory_store(value):
    global memory_value
    memory_value = value

def memory_recall():
    return memory_value

def memory_add(value):
    global memory_value
    memory_value += value
    return memory_value

def memory_clear():
    global memory_value
    memory_value = 0
