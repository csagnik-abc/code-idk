print("Welcome to Basic CalculatorTM")
e = input("Enter expression or type \"exit\" to exit:\n") # Basic inputs
x = 0
n = []
expr = []
nc = []
exc = []
cn = 0
    

# Keep taking expressions until user exits

while e.lower() != "exit":
    num = 0
    # Construct numbers; we are not discriminating if the user is putting spaces in the expression or not
    for c in e:
        if c.isdigit():
            num = num*10 + int(c)
        else:
            n.append(num) # We make a list of numbers
            nc.append(cn) # We store their index
            if c in ["+", "-", "/", "*", "^", "(", ")"]:
                expr.append(c) # We make a list of operators; note that there should be one operator for every nth and (n+2)th number
                exc.append(cn) # We store their index; this will be useful in case of expressions like 5+4+(((3+3*(((9-3

            # We can solve the multiple bracket problem by thinking them as list within a list
            # Every time we encounter an opening bracket "(", we create a new list. However, we ensure this works only when there's a valid number after the bracket as we cannot write something like 5+(/34 or create a list for consecutive brackets
            if c == "(":
                brac = ""
                iln = []
                ile = []
                exc.append("(") # For us, we only need to consider one opening bracket i.e., 5+((((4-1 to 5+(4-1
                ic = 0 # We keep an index counter for tracking indices within brackets
                for i in e[cn+1:]: # The "cn" variable is also useful here to slice the expression string and parse it
                    if i == "(" or i == ")":
                        if brac != "": # We only parse and append it if brac is non-empty, otherwise we just skip and make another list
                            for a in brac:
                                tnum = 0
                                if a.isdigit():
                                    tnum = tnum*10 + int(a)
                                else:
                                    iln.append(tnum) # We keep list of numbers in one list
                                    if a in ["+", "-", "/", "*", "^"]:
                                        ile.append(a) # We keep list of operators in one list
                        continue
                    brac += i # We make the expression until we encounter another opening bracket, now we need to parse this
                    


    cn += 1 # We keep a track of indices
            
