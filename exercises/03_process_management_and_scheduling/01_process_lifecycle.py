class Process:
    def __init__(self, id):
        self.id = id
        self.state = "new"

    def ready(self):
        # Transition to ready state
        self.state = "ready"
        print(f"Process {self.id} is now in the ready state.")

    def running(self):
        # Transition to running state
        if self.state == "ready":
            self.state = "running"
            print(f"Process {self.id} is now in the running state.")
    
    def waiting(self):
        # Transition to waiting state
        if self.state == "running":
            self.state = "waiting"
            print(f"Process {self.id} is now in the waiting state.")

    def terminated(self):
        # Transition to terminated state
        if self.state == "waiting":
            self.state = "terminated"
            print(f"Process {self.id} is now in the terminated state.")


# Example usage
p1 = Process(1)
p1.ready()
p1.running()
p1.waiting()
# p1.terminated()

p2 = Process(2)
p2.ready()
p2.running()
p2.waiting()
# p2.terminated()
