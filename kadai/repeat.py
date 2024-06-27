def repeat(xs,n):
    if n<0:
        raise ValueError("n must be non-negative")
    result=[]
    for x in xs:
        result.append(x*n)
    return result