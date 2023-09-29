sitea = True
doors = True
spawn = True
passcode = 1275
slider = [30, 50, 100]

def set_sitea():
    global sitea
    sitea = not sitea

def get_sitea():
    return sitea

def set_doors():
    global doors
    doors = not doors

def get_doors():
    return doors

def set_spawn():
    global spawn
    spawn = not spawn

def get_spawn():
    return spawn
