import pyomo.environ as pyo
import numpy as np
from rulewrapper import wrap

m = pyo.ConcreteModel()
m.i = pyo.RangeSet(1, 5)

n = [1, 2, 3, 4, 5]
lb = [0.1, 0.2, 0.3, 0.4, 0.5]
ub = np.array([10, 20, 30, 40, 50])

m.param1 = pyo.Param(m.i, initialize=wrap(n, offset=1))
m.var1 = pyo.Var(m.i, bounds=wrap(lb, ub, offset=1))

m.pprint()
