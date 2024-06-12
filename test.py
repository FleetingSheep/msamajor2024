#write a program to convert pounds to kilograms
pounds_to_kg = 2.205
#grab pounds from user, check if valid number, then convert to kg
def convert():
  pounds = input("How many pounds?\n")
  try: #try to run, goto except if an error is thrown
    pounds = float(pounds)
    if pounds >= 0:
      print(f"{pounds} pounds are equal to around {(pounds / pounds_to_kg):.2f} kilograms")
    else:
      print("Please enter a positive number.")
      convert()
  except: #if an error is thrown upon conversion
    print("Please exclude all letters and special characters and try again.")
    convert()
convert()