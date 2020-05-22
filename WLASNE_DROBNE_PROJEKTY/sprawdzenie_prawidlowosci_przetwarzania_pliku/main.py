import os
import datetime

data_input_catalog = r"c:\temp\data_input"
data_output_catalog = r"c:\temp\data_output"
today = datetime.date.today()

today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
print(today_output_catalog)

is_input_catalog_ok = not os.path.exists(data_input_catalog) and not os.path.isdir(data_input_catalog)
print(is_input_catalog_ok)

is_output_catalog_ok = not os.path.exists(data_output_catalog) and not os.path.isdir(data_output_catalog)
print(is_output_catalog_ok)

is_today_output_catalog_ok = not os.path.exists(today_output_catalog) and not os.path.isdir(today_output_catalog)
print(is_today_output_catalog_ok)


if is_input_catalog_ok == True and is_output_catalog_ok == True and is_today_output_catalog_ok == True:
    print("Conditions met! We can continue!")

else:

    if (is_input_catalog_ok == False) and (is_output_catalog_ok == False) and (is_today_output_catalog_ok == False):
        print("Error: input_catalog, output_catalog and today_output_catalog not exists!")
    elif (is_input_catalog_ok == False) and (is_today_output_catalog_ok == False):
        print("Error: input_catalog and today_output_catalog not exists!")
    elif (is_output_catalog_ok == False) and (is_today_output_catalog_ok == False):
        print("Error: output_catalog not exist and today_output_catalog exists!")
    elif (is_input_catalog_ok == False) and (is_output_catalog_ok == False):
        print("Error: input_catalog and output_catalog not exists!")
    elif (is_input_catalog_ok == False):
        print("Error: %s not exist!")
    elif (is_output_catalog_ok == False):
        print("Error: output_catalog not exist!")
    elif (is_today_output_catalog_ok == False):
        print("Error: today_output_catalog")