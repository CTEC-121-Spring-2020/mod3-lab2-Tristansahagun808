"""
CTEC 121
<Tristan Sahagun>
<Module 3 Lab 2>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nDivision by zero is impossible, Exiting\n")
        exit
    except TypeError:
        print("Type Error")
        exit
    except:
        print("Unknown Error")
        exit

main()    