a =[ input () for _ in [ 0 ]* 3 ]
d = dict ( zip ( 'rsp' , 'spr' ))
r = 'FMS'

for i in range ( 3 ):
    if sum ( x [ 0 ]== d [ a [ i ][ 0 ]] for x in a )== 2 :
        print ( r [ i ])
        exit ()
        print ( '?' )