import panel as pn

from panel.interact import interact, interactive, fixed, interact_manual
from panel import widgets

pn.extension()

def f(x):
    return x

interact(f, x=10)
interact(f, x=True)
interact(f, x='Hello there!')

@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)
g

layout = interact(f, x=10)

pn.Column('**A custom interact layout**', pn.Row(layout[0], layout[1]))

def h(p, q):
    return (p, q)

interact(h, p=5, q=fixed(20))

interact(f, x=widgets.IntSlider(start=-10,end=30,step=1,value=10))






