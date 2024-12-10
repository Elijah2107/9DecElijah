# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def come():
    agent.teleport_to_player()
player.on_chat("tp", come)

def turn_left():
    agent.turn(LEFT)

def turn_right():
    agent.turn(RIGHT)

def move_forward(steps):
    agent.move(FORWARD, steps)

def move_up(steps):
    agent.move(UP, steps)

def move_down(steps):
    agent.move(DOWN, steps)

def move_back(steps):
    agent.move(DOWN, steps)

player.on_chat("tl", turn_left)
player.on_chat("tr", turn_right)
player.on_chat("fw", move_forward)
player.on_chat("up", move_up)
player.on_chat("dn",move_down)

def choptree(tall):
    for count in range(tall):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, tall)    
    agent.collect_all()
        
player.on_chat("chop", choptree)

def dig():
    for count in range(24):
        for inside in range(26):
            agent.destroy(FORWARD)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.destroy(DOWN)
            agent.collect_all()
            agent.move(FORWARD, 1)
        agent.move(BACK, 26)
        agent.move(DOWN, 1)

player.on_chat("mine", dig)