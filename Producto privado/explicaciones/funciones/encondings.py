def default():
    return "Opción no válida"

def encondings(numero,a,b,n,beta,alpha):
    switch_dict = {
        1: encoding_1,
        2: encoding_2,
        3: encoding_3,
        4: encoding_4,
    }

    # Obtén la función del diccionario, y llama a la función predeterminada si no existe
    case_func = switch_dict.get(numero, default)
    return case_func(a, b, n, beta, alpha)


def encoding_1(a,b,n,beta,alpha):
    #n = 2**n
    Xa_A = alpha ** n * a   #alpha^n*a
    Xb_B = 0 
    Zb_B = alpha ** (-n) * b
    if(a == 0):
        Za_A = beta
    else: 
        Za_A = 0

    operators = [Xa_A, Xb_B, Za_A, Zb_B]
    return operators

def encoding_2(a,b,n,beta,alpha):
    #n = 2**n
    Za_A = alpha ** n * a   #alpha^n*a
    Xb_B = alpha ** (-n) * b
    Zb_B = 0
    if(a == 0):
        Xa_A = beta
    else: 
        Xa_A = 0

    operators = [Xa_A, Xb_B, Za_A, Zb_B]
    return operators

def encoding_3(a,b,n,beta,alpha):
    #n = 2**n
    Xa_A = alpha ** n * a   #alpha^n*a
    Zb_B = alpha ** (-n) * b
    Za_A = 0
    if(a == 0):
        Xb_B = -beta
    else: 
        Xb_B = 0

    operators = [Xa_A, Xb_B, Za_A, Zb_B]
    return operators

def encoding_4(a,b,n,beta,alpha):  
    #n = 2**n 
    Za_A = alpha ** n * a   #alpha^n*a
    Xb_B = alpha ** (-n) * b
    Xa_A = 0
    if(a == 0):
        Zb_B = -beta
    else: 
        Zb_B = 0

    operators = [Xa_A, Xb_B, Za_A, Zb_B]
    return operators