
def user():
    print('hi i am a user module ')
def fact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return(res)
# fact(1)
print(__name__)