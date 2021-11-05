print ("Hallo, welkom bij Kugapalan's café")

name= input ("Wat is uw naam? \n" )

print ("\nHallo "+ name +", Dankuwel voor het binnenkomen bij ons café.\n" )

menu= "Koffie,Thee,Expresso,Chocolademelk,Cola en Bubble tea\n"

print (name + " wat wilt u van ons menu?\nDit is wat wij serveren.\n" +menu )

order= input ()

if order == "Koffie" or order == "Thee" or order == "Expresso" or order == "Chocolademelk" or order == "Cola" or order == "Bubble tea" :
  print ("\nDat klinkt goed. "+ name +", We hebben dat genoteerd." +"\nHet is zo klaar.\n")
  print ("Dankuwel voor het wachten hier is uw " + order)

elif order != menu: 
     print ("Het spijt ons maar " +order+"\nserveren wij helaas niet")

print ("Fijne dag nog verder")

#elif order != menu:
# print ("Het spijt ons maar "+ order +"serveren wij helaas niet")
