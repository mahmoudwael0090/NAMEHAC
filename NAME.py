import pyfiglet

x =str(input('<+> Enter Your Name >> ')) 
 print(' '*60)
 z =pyfiglet.figlet_format('NAME HAC')
 print(z)
 
 print(' '*70)
 v =pyfiglet.figlet_format(x)
 
print('''
 < 1 > YELLOW
 
 < 2 > GREEN
 
 < 3 > BLACK
 
 < 4 > RED
 
 < 5 > WHITE
''')
 
print(' '*50)
 
c =input('<+> choose the Colour >> ')
 
if c == '1':
    print('\033[;33;m')
    print(v)
if c == '2':
    print('\033[;32;m')
    print(v)

if c == '4':
    print('\033[;31;m')
    print(v)
  
  
