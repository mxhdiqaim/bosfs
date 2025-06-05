# Simulate handling of multiple hardware interrupts and show how ISR is executed based on interrupt priority.
class Interrupt:
    def __init__(self, irq, priority, handler):
        self.irq = irq
        self.priority = priority
        self.handler = handler

def interrupt_handler_a():
    print(f'Handling Interrupt A')

def interrupt_handler_b():
    print(f'Handling Interrupt B')

# Simulate a list of interrupt with different priority

interrupts = [
    Interrupt(irq=2, priority=1, handler=interrupt_handler_a),
    Interrupt(irq=1, priority=2, handler=interrupt_handler_b),
]

# Sort interrupts by priority
sorted_interrupts = sorted(interrupts, key=lambda intp: intp.priority)

# Execute IRS for the highest priority interrupt
for interrupt in sorted_interrupts:
    interrupt.handler()
    break # Execute only the highest priority

"""
Explanation
This code snippet defines a simple model for handling interrupts, using a class to represent each interrupt with an IRQ and priority

Two interrupt handlers are defined and interrupts are sorted based on priority

The handler of the highest priority interrupt is executed.
"""