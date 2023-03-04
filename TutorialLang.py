
def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

fl = input("Enter name of Camus File to run: ")
with open(fl, "r") as f:  # Open file for reading
    file_contents = f.read()  # Read file contents
    splittin = file_contents.splitlines()

def anal():
    try:
        if "output our string" in line:
            print(eval(find_between(line, "output our string ", ".")))
        if "output our number" in line:
            print(eval(find_between(line, "output our number ", ".")))
        if "output our variable" in line:
            print(eval(find_between(line, "output our variable ", ".")))
        if "allocate" and "into the variable" in line:
            vardata = (eval(find_between(line, "allocate ", " into the variable ")))
            varname = ((find_between(line, " into the variable ", ".")))
            globals()[varname] = (vardata)
        
        if "change our variable" and "to a string." in line:
            varname = ((find_between(line, "change our variable ", " to a string.")))
            globals()[varname] = str(eval(varname))
        if "change our variable" and "to an integer." in line:
            varname = ((find_between(line, "change our variable ", " to an integer.")))
            globals()[varname] = int(eval(varname))
        if "change our variable" and "to a float." in line:
            varname = ((find_between(line, "change our variable ", " to a float.")))
            globals()[varname] = float(eval(varname))
        if "change our variable" and "to a bool." in line:
            varname = ((find_between(line, "change our variable ", " to a bool.")))
            globals()[varname] = bool(eval(varname))
        if "output the type of" in line:
            varname = ((find_between(line, "output the type of ", ".")))
            print(type(globals()[varname]))
    
        
        else:
            pass
        
    except SyntaxError as e:
        print("\033[1;31mCaught Syntax Error\033[0m")
        print("")
        print("\033[1;31mFile: "+fl+"\033[0m")
        print("\033[1;31m     "+"^"*len(fl)+"\033[0m")
        print("\033[1;31m"+e.msg+"\033[0m")
        print("\033[1;31mLN:"+str(e.lineno)+"\nCOL:"+str(e.offset)+"\033[0m")
        print("\033[1;35;3mHelp, Your code has a "+e.msg+"\nYour code that is causing this issue is '"+str(e.args[1])+"'\033[0m")
        print("\033[1;35;3m                                          "+"^"*len(str(e.args[1]))+"\033[0m")
for i, line in enumerate(splittin):
    anal()