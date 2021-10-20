def show_menu():
    print("1. Citre lista .")
    print("2. Afisare lista numere intregi.")
    print("3. Să se afișeze toate numerele care aparțin unui interval deschis citit de la tastatură.")
    print("4. Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare")
    print("4. Optiune.")
    print("4. Optiune.")

def read_list() :
    '''
    Citirea listei de numere float
    :return: Lista de float-uri
    '''
    lst=[]
    lst_str=input("Dati numere separate prin spatiu: ")
    lst_str_split=lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(float(num_str))
    return lst

def list_of_int(lst):
    '''
    Afișarea părții întregi a tuturor numerelor din listă
    :param lst: Lista de float-uri
    :return: Partile intregi a fiecarui numar din lista initiala
    '''
    lst_int=[]
    for i in lst:
        lst_int.append(int(i))
    return lst_int

def get_interval(lst):
    '''
    Citeste numerele care descriu intervalul si returneaza lista cu elemente din lista care apartin acelui interval
    :param lst: Lista de foat-uri
    :return: Lista caare apartine intervalului
    '''
    lst_interval=[]
    prim=float(input("Primul numar al intervalului este: "))
    secund=float(input("Al doilea numar al intervalului este: "))
    if prim>secund:
        aux=prim
        prim=secund
        secund=aux
    for i in lst:
        if i>=prim and i<=secund:
            lst_interval.append(i)
    return lst_interval

def parte_frac(n):
    if n<0: m=n*(-1)
    else: m=n
    b=str(m)[::-1]
    b=int(float(b))
    b=int(float(str(b)[::-1]))
    a=int(m)
    if b==0: return False
    if b%a==0: return True
def get_div(lst):
    lst_div=[]
    for i in lst:
        if parte_frac(i)==True:
            lst_div.append(i)
    return lst_div


def nume(i):
    a=1
    lst_name=[]
    if i<0:
        lst_name.append("minus")
        a=i*(-1)
    else: a=i
    if i==0:return "zero"
    while a!=0:
        aux=a%1
        if aux=='1':lst_name.append("unu")
        elif aux=='2':lst_name.append("doi")
        elif aux=='3':lst_name.append("trei")
        elif aux=='4':lst_name.append("patru")
        elif aux=='5':lst_name.append("cinci")
        elif aux=='6':lst_name.append("sase")
        elif aux=='7':lst_name.append("sapte")
        elif aux=='8':lst_name.append("opt")
        elif aux=='9':lst_name.append("noua")
        elif aux=='0':lst_name.append("zero")
        elif aux==' ':lst_name.append(" ")
        else: lst_name.append("virgula")
    return lst_name
def get_name(lst):
    lst_name=[]
    for j in lst:
        lst_name.append(nume(j))
    return lst_name
def main():
    while True:
        show_menu()
        opt = input("Optiunea dorita este: ")
        if opt == '1':
            lst = read_list()
        elif opt == '2':
            print(list_of_int(lst))
        elif opt == '3':
            print(get_interval(lst))
        elif opt == '4':
                print(get_div(lst))
        elif opt == '5':
            print(get_name(lst))
        elif opt == 'x':
            break
        else:
            print("Optiune invalida.")


if __name__ == '__main__':
    main()
