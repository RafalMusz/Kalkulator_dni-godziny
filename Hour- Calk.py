import time

#variables
calculation_to_units = 24
name_of_units = "godzin"
user_input = ""

# Calculations
def days_to_unit(num_of_days):
  if num_of_days > 0:
    return f"{num_of_days} dni to {num_of_days * calculation_to_units} {name_of_units}/n"
    time.sleep(2)
    if num_of_days == 0:
      return " zero równa się ZERO"
  else:
    return "wpisałeś wartość ujemną, wpisz prosze warotść dodatnią"

#checks
def sprawdzanie():
  if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_value = days_to_unit(user_input_number)
    print(calculated_value)
  else:
    print("Wpisz prosze poprawną wartość")

#Loop
while user_input != "exit" :
  user_input = input("Hej wpisz   ilść dni to kalkulacji\n")
  user_input_number =         int(user_input)
  sprawdzanie()


#calculated_value = days_to_unit(user_input_number)
#print(calculated_value)
