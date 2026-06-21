#Test 
#20.4.2026
#Test program - citacia Einsteina + jednoducha uprava textu
quote = ' "a person who never made a mistake never tried anything new." '
name = " albert "
surname = " einstein "
full_name = f"{name.strip()}{surname.rstrip()}"
message = f"\t{full_name.title()} once said, \n\t{quote.upper().rstrip()}"
print(message)