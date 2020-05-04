si = input ("inserisci un numero: " )
i = float(si)

if i < 0 :
    print("numero inferiore a zero") 
elif i == 0:
    print("inseiro uguale a zero")
else:
    print("numero maggiore di zero")


si = eval(input ("inserisci un numero: " )) # The expression argument 
                                            # is parsed and evaluated as a 
                                            # Python expression (technically 
                                            # speaking, a condition list) 
                                            # using the globals and locals 
                                            # dictionaries as global and local 
                                            # namespace. 

if si < 0 :
    print("numero inferiore a zero") 
elif si == 0:
    print("inseiro uguale a zero")
else:
    print("numero maggiore di zero")


