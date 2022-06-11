
arr='ABCDEFGH'
def line_intersection(start,end):
    s = [int(arr.index(start[0]))+1,int(start[1])] # list of the start postiion with the format [a,b] where a and b are int
    e = [int(arr.index(end[0]))+1,int(end[1])]   # .............. end .......
    
    sol1 ,sol2 ='','' # two possible solutions max

    # making two lines and finding the intersection between them (positive first)
    solpx = (-s[1]+s[0]+e[1]+e[0])/2
    solpy = solpx+s[1]-s[0]

    if not solpx.is_integer():
        return ['no solution']

    # check if they are on the board
    if solpx>0 and solpx<9 and solpy>0 and solpy<9:
        sol1= arr[int(solpx)-1]+f'{int(solpy)}'
    

    solnx = (-e[1]+e[0]+s[1]+s[0])/2
    solny = -solnx+s[1]+s[0]

    if solnx>0 and solnx<9 and solny>0 and solny<9:
        sol2= arr[int(solnx)-1]+f'{int(solny)}'

    
    if sol1 ==start or sol1 ==end:
        return [start, end]
    if sol1:
        return [start, sol1, end]
    else:
        return [start, sol2, end]


a = 'A1'
b  = 'A1'
print(line_intersection(a,b))
