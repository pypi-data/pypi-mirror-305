import re

def clean_car_plateno(regnum,carno):

    if carno is None:
        carno = None
    
    if regnum is None or regnum == "nan" or regnum =="" or regnum.strip() == "":
        return False,f"Invalid no data"
    regnum = str(regnum)
    regex = r"(^[0-9]{2}-[0-9]{4}$)"
    regexkaba = r"(^[0-9][ก-ฮ]{2}[1-9][0-9]{3})"
    regnum2 = regnum
    findno = re.search('([0-9]{2}--[0-9]{4}|[0-9]{2}-[0-9]{4}|[0-9]{6})',regnum)
    findkaba = re.search('((^|)[0-9]{2}[- ]?[ก-ฮ]{2}[- ]?[1-9][0-9]{3}|(^|)[0-9]{2}[- ]?[ก-ฮ]{2}[- ]?[1-9][0-9]{2}|(^|)[0-9]{2}[- ]?[ก-ฮ]{2}[- ]?[1-9][0-9]{1}|(^|)[0-9]{2}[- ]?[ก-ฮ]{2}[- ]?[1-9]|(^|)[0-9][- ]?[ก-ฮ]{2}[- ]?[1-9][0-9]{3}|(^|)[0-9][- ]?[ก-ฮ]{2}[- ]?[1-9][0-9]{2}|(^|)[0-9][- ]?[ก-ฮ]{2}[- ]?[1-9][0-9]{1}|(^|)[0-9][- ]?[ก-ฮ]{2}[- ]?[1-9]|(^|)[0-9][- ]?[ก-ฮ][- ]?[1-9][0-9]{3}|(^|)[0-9][- ]?[ก-ฮ][- ]?[1-9][0-9]{2}|(^|)[0-9][- ]?[ก-ฮ][- ]?[1-9][0-9]{1}|(^|)[0-9][- ]?[ก-ฮ][- ]?[1-9])|^[ก-ฮ]{2}[- ]?[1-9][0-9]{3}|^[ก-ฮ]{2}[- ]?[1-9][0-9]{2}',regnum)
    z = None
    
    if findkaba != None:
        regnum2 = regnum[findkaba.start():findkaba.end()]
        regnum2 = re.sub('[ -]','',regnum2)
    if findno != None:
        regnum2 = regnum[findno.start():findno.end()]
        x,y,z = re.split('([0-9]{2}--[0-9]{4}|[0-9]{2}-[0-9]{4}|[0-9]{6})', regnum)
        z = z.strip()
        check = re.search("[0-9]", z)
        if z == '':
            z = None
        if check is None:
            z = None

    if re.match('[0-9]{6}', regnum2):
        regnum2 = f"{regnum[0:2]}-{regnum[2:]}"

    if re.match('[0-9]{2}--[0-9]{4}', regnum2):
        regnum2 = f"{regnum[0:2]}-{regnum[4:]}"

    if regnum2[0:2] == '00':
        return False,f"Invalid format"
    elif regnum2 == '00-0000':
        return False,f"Invalid format"
    elif re.match(regex, regnum2):
        con = f"{regnum2}"
        if carno == z :
                return True,f"Valid"
        else:
            if carno is None :
                return True,f"Valid"
            elif z is None :
                return True,f"Valid"
            else:
                return True,f"Valid"
            

    elif findkaba != None:
        con = f"{regnum2}"
        return True,f"Valid"
    else:
        return False,f"Invalid format"
    
