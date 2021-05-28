def wrap(*data: list, offset: int = 0):
    '''
    Create a Pyomo construction rule for the given data.

    `*data`: One or more list or dict used for the data source.
    `offset`: The first index value that Pyomo is going to pass in. Set to None if it is key rather than numerical index.

    Shouyuan Shi @ South China University of Technology    
    Created in 2021/05/28
    '''

    if len(data) > 1:
        def rule(m, key): return tuple(data[d][key] for d in range(len(data)))
    else:
        def rule(m, key): return data[0][key]
    if offset == None:
        return rule
    else:
        return lambda m, i: rule(m, i-offset)
