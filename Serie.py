
#serie 4,3,2,1,4,3,2....
# c = controlador
# w = interruptor

n = int(input("ingrese un número: "))
c = 0
w = 4

while c < n:
    print(w)
    if w > 1:
        w = w -1
    else:
        w = 4
    c = c+1