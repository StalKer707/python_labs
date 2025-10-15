roan = ("адольф гитлер верховный","ABB-07", 3.999)
def fio(roan):
    if len (roan[0])> 0 :
        fio = roan[0].split()
        iniliats = ''.join(i [0]for i in fio).upper()
        if len (iniliats) == 3 :
            return fio[0][0].upper() + fio [0][1:] + " " + iniliats [1]  +  " " + iniliats[2] + " "
        elif len (iniliats) == 2:
            return fio[0][0].upper() + fio [0][1:] + " " + iniliats [1]  +  " "
        else:
             return fio[0][0].upper() + fio [0][1:]
    else:
        raise ValueError
def gpa(roan):
    if len(str(roan[2])) > 0 :
        return round (roan[2], 2)
    else:
        raise ValueError

def format_record(roan):
    if tuple(roan) == roan:
        if len (str(roan[1]))> 0:
            res = fio(roan) + "," + " " + " mr" + roan [1] + "," + " " + "NBA" + " " + str(gpa(roan))
            print(roan) 
            print(res)   
        else:
            raise ValueError
format_record(roan)
