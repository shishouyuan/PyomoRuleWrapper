# Pyomo Construction Rule Wrapper
**A function helps create Pyomo construction rules for the given data in a very simple way.**

+ Shouyuan Shi @ South China University of Technology    
+ Created in 2021/05/28
## Parameters
+ `*data`: One or more list or dict used for the data source.
+ `offset`: The first index value that Pyomo is going to pass in. Set to None if it is key rather than numerical index.



## Example
### Code
``` python
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
```
### Result
```
1 RangeSet Declarations
    i : Dimen=1, Size=5, Bounds=(1, 5)
        Key  : Finite : Members
        None :   True :   [1:5]

1 Param Declarations
    param1 : Size=5, Index=i, Domain=Any, Default=None, Mutable=False
        Key : Value
          1 :     1
          2 :     2
          3 :     3
          4 :     4
          5 :     5

1 Var Declarations
    var1 : Size=5, Index=i
        Key : Lower : Value : Upper : Fixed : Stale : Domain
          1 :   0.1 :  None :    10 : False :  True :  Reals
          2 :   0.2 :  None :    20 : False :  True :  Reals
          3 :   0.3 :  None :    30 : False :  True :  Reals
          4 :   0.4 :  None :    40 : False :  True :  Reals
          5 :   0.5 :  None :    50 : False :  True :  Reals

3 Declarations: i param1 var1
```