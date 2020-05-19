"""keypress - Detecting OS of user based on a single key entry"""

# run from command line
if __name__ == '__main__':
    
    print("For program to detect your OS, please press any letter key")
    
    # Exception block for Windows input
    try:
        import msvcrt
        
        def getkey():
            """ Wait for a keypress and return a single character string """
            return msvcrt.getch()

        # invoke getkey and store input as str
        user_input:str = getkey().decode()
        print(f"You are using Windows!\nYour input: {user_input}")
        
    except ImportError:
        
        print("Hmm.. You are definitely not using a Windows machine.\nLet's try again. Please press any letter key once again.")
        
        # import stuff required for Unix based input
        import sys
        import tty
        import termios
        
        def getkey():
            """ Wait for a keypress and return a single character string """
            fd = sys.stdin.fileno()
            original_attributes = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            except ImportError:
                print("Damn! Unix OS based input also failed :(")
            finally:
                termios.tcsetatter(fd, termios.TCSADRIAN, original_attributes)
                print(f"You are using Unix based system!\nYour input: {ch}")
            return ch
        
        # invoke getkey for Unix based OS
        getkey()
        
        # If either of the Unix-specific tty or termios are not found,
        # we allow the ImportError to propagate from here