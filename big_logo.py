
# This function allows you to print a beautiul logo on top of your programm.

def genlogo(logo_text="Dante"):
    try:
        import os
        from pyfiglet import Figlet
    except:
        print("Libary not found!")

    c_text = Figlet(font="slant")
    easy_output = c_text.renderText(logo_text)

    os.system("cls")
    os.system("mode con: cols=75 lines=30")
    print(easy_output)






genlogo("Hello World")    # Just call the Function with a string as parameter.
