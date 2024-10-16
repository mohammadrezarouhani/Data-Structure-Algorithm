import traceback

def f():
    name="test"
    g()

def g():
    traceback.print_stack()

f()
