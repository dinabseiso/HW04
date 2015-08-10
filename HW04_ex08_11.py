#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
        This will execute the function only for the first letter
        of the string. RETURN will cause it to exit the loop and stop
        checking.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
        The IF check here will not even regard the string. It will constantly
        check whether the letter in quotations, c, is in lowercase. Which, it 
        always is, as it is hardcoded that way. 
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
        Variable flag is being rewritten as c transverses s. So, it will retain
        the value of the last check in string s. If the last letter is 
        lowercase, then the flag will return True, irregardless of any other
        lowercase letters preceding it.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
        This should work. So long at any point, there is one lowercase letter
        to make the comparison True, then the flag will be True. 
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
        As soon as a character is uppercase, the return value is stuck as false
        and will not make it outside of the loop. In fact, the for loop will
        be broken out of once the if condition is met (meaning, it finds 
            an uppercase value).        
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    any_lowercase1("Soliterallyeveryotherletterofthisstringislowercase")
    any_lowercase2("SHOUTSHOUTLETITALLOUT")
    any_lowercase3("uuuuuuuuuuuuuuuuuUUUUUHHHHHMMMMMMMMMM")
    any_lowercase5("dunananananananaBATMAN")
    

if __name__ == '__main__':
    main()