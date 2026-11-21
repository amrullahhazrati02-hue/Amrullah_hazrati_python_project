
def is_a_leep_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
input_year = int(input("Enter the year: "))
if is_a_leep_year(input_year):
    print(f"{input_year} is a leep year")
else:
    print(f"{input_year} is not a leep year")