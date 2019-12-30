import math

def vector_from_points(p1, p2):
    '''
    (List[int],List[int]) -> List[int]
    Creates vector of n components from 2 points in the nth dimension
    Returns empty list if n is 0
    >>>vector_from_points([0, 0], [1, 2])   
    [1, 2] 
    >>>vector_from_points([3, -1, 0], [10, 0, 1]) 
    [7, 1, 1] 
    '''
    vctr = []
    n = len(p1)
    for i in range(0, n, 1):
       vctr.append(p2[i] - p1[i])
    return vctr
        
        

def vector_length(v):
    '''
    (List[int]) -> float
    Given a vector as input, returns the magnitude of the vector as a float
    If input is empty list, then it returns -1
    >>>vector_length([2, 1])  
    2.23606797749979 
    >>>vector_length([])  
    -1
    '''
    n = len(v)
    length = 0
    if n == 0:
        return -1
    else:
        for i in range(0, n, 1):
            length = length + (v[i])*v[i]
    return math.sqrt(length)

     
    
def angle_between(v, w):
    '''
    (List[num],List[num]) -> float
    Returns angle between two vectors
    >>>angle_between([-1], [2])   
    180.0 
    >>>angle_between([0, 1, 0, 1], [1, 3, 4, 5]) 
    37.61611202673532 
    '''
    dp = dot_product(v,w)

    cos = dp / (vector_length(v)*vector_length(w))

    theta = math.acos(cos)

    return theta*180/math.pi
    

def dot_product(v,w):
    '''
    If input list solely has integers in it, type contract is:
    (List[int]) -> int
    if input list has floats in it, type contract is:
    (List[float]) -> float
    Returns the dot product of two vectors
    >>>dot_product( [-1], [2])    
    -2 
    >>>dot_product( [0, 1, 0, 1], [1, 3, 4, 5])     
    8 
    >>>dot_product([0, 0], [0, 0])     
    0 
    '''
    dp = 0
    n = len(v)
    
    for i in range(0, n, 1):
       dp = dp + v[i]*w[i]
    return dp

def unit_vector(v):
    '''
    (List[num]) -> List[float]
    Returns a unit vector with the same direction vector as input and magnitude of one
    If input vector has 0 components, returns empty list
    >>>unit_vector([2, 1]) 
    [0.8944271909999159, 0.4472135954999579] 
    >>>unit_vector([]) 
    []
    '''
    length = vector_length(v)

    new_vector = []

    n = len(v)
    
    for i in range(0, n, 1):
        new_vector.append(v[i] / length)
    return new_vector
    

    
def cross_product(v,w):
    '''
    (List[num],List[num]) -> List[num]
    Returns cross product v x w.
    If either input has >3 components, then empty list is returned
    >>>cross_product([], [2])  
    [0, 0, 0] 
    >>>cross_product([2, 8], [1, 4, 3])   
    [24, -6, 0] 
    >>>cross_product([1, 1, 1], [5.5, 5.5, 5.5])  
    [0.0, -0.0, 0.0] 
    >>>cross_product( [1, 1, 1, 0], [1, 5.5])  
    []
    '''
    n = len(v)
    m = len(w)
    if(n > 3 or m > 3):
       return[]
    else:
        for i in range(0, 3-n, 1):
            v.append(0)
        for q in range(0, 3-m, 1):
            w.append(0)
        cross =[v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0]]
        return cross 
        
    

def scalar_projection(v,w):
    '''
    (list,list) -> float
    Returns scalar projection of w onto v
    >>> scalar_projection([-2], [1.5]) 
    -1.5 
    >>> scalar_projection([0, 3], [1.5, 2])     
    2.0 
    '''
    a = angle_between(w,v)
    dp = dot_product(v,w)
    cos = dp / (vector_length(v)*vector_length(w))
    theta = math.acos(cos)
    proj = vector_length(w)* math.cos(theta)
    return proj

def vector_projection(v,w):
    '''
    (list, list) -> list
    Returns vector projection of w onto v
    >>> vector_projection([-2], [1.5]) 
    [1.5] 
    >>> vector_projection([0, 3], [1.5, 2])     
    [0.0, 2.0]
    '''
    
    proj = dot_product(w,v)/(vector_length(v))
    uv = unit_vector(v) 
    n = len(uv)
    vp = []
    for i in range(0, n, 1):
            vp.append(uv[i]* proj)
    return vp
if __name__ == "__main__":
    # test your vector operations here
    print("Testing Functions.....")
