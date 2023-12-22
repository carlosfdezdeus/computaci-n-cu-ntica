def default():
    return "Opción no válida"

def encondings(numero,a,b,alpha,beta,n,p):
    switch_dict = {
        1: encoding_1,
        2: encoding_2,
        3: encoding_3,
        4: encoding_4,
    }

    # Obtén la función del diccionario, y llama a la función predeterminada si no existe
    case_func = switch_dict.get(numero, default)
    return case_func(a,b,alpha,beta,n,p)


def encoding_1(a,b,alpha,beta,n,p): #Ejemplo paper
    Xa_A = alpha ** n * a   #alpha^n*a
    Zb_B = alpha ** (-n) * b
    Xb_B = 0 
    if(a == 0):
        Za_A = beta
    else: 
        Za_A = 0

    Xa_A, Zb_B = calculos_mod_p(Xa_A, Zb_B, p)

    operators = [Xa_A, Xb_B, Za_A, Zb_B]
    return operators

def encoding_2(a,b,alpha,beta,n,p):
    Za_A = alpha ** n * a   #alpha^n*a
    Xb_B = alpha ** (-n) * b
    Zb_B = 0
    if(a == 0):
        Xa_A = beta
    else: 
        Xa_A = 0

    Za_A, Xb_B = calculos_mod_p(Za_A, Xb_B, p)

    operators = [Xa_A, Xb_B, Za_A, Zb_B]
    return operators

def encoding_3(a,b,alpha,beta,n,p):
    Xa_A = alpha ** n * a   #alpha^n*a
    Zb_B = alpha ** (-n) * b
    Za_A = 0
    if(a == 0):
        Xb_B = -beta
    else: 
        Xb_B = 0

    Xa_A, Zb_B = calculos_mod_p(Xa_A, Zb_B, p)

    operators = [Xa_A, Xb_B, Za_A, Zb_B]
    return operators

def encoding_4(a,b,alpha,beta,n,p):  
    Za_A = alpha ** n * a   #alpha^n*a
    Xb_B = alpha ** (-n) * b
    Xa_A = 0
    if(a == 0):
        Zb_B = -beta
    else: 
        Zb_B = 0

    Za_A, Xb_B = calculos_mod_p(Za_A, Xb_B, p)

    operators = [Xa_A, Xb_B, Za_A, Zb_B]
    return operators


def calculos_mod_p(operador1, operador2, p):
    # Los calculos están hecho para una matriz con p=5 (primo)
    # Esto se debe a los inversos (1/2=3,...)
    # La operación: "operador mod p" es correcta para todo p primo (Fp).
    if (operador1 == 1/2):
        operador1 = 3
        operador2 = operador2 % p

    elif (operador2 == 1/2):
        operador2 = 3
        operador1 = operador1 % p

    elif (operador1 == 1/3):
        operador1 = 2
        operador2 = operador2 % p

    elif (operador2 == 1/3):
        operador2 = 2
        operador1 = operador1 % p

    elif (operador1 == 1/4):
        operador1 = 4
        operador2 = operador2 % p

    elif (operador2 == 1/4):
        operador2 = 4
        operador1 = operador1 % p
    
    operadores = [operador1, operador2]
    return operadores