
import datetime
import functools

logFilePath = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\function_log.txt"


def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        file = open(logFilePath, "a")
        file.write("-" * 20 + "\n")
        file.write("Function '{}' started at {}\n".format(func.__name__, datetime.datetime.now().isoformat()))
        file.write("Following arguments were used:\n")
        file.write(" ".join("{}".format(x) for x in args))
        file.write("\n")
        file.write(" ".join("{}={}".format(k, v) for k, v in kwargs.items()))
        file.write("\n")
        result = func(*args, **kwargs)
        file.write("Function returned {}\n".format(result))
        file.close()
        return result
    return func_with_wrapper


@CreateFunctionWithWrapper
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print("CHANGING SALARY FOR {} TO {} AS BONUS={}".format(emp_name, new_salary, is_bonus))
    return new_salary


print(ChangeSalary("Johnson", 20000, True))
print(ChangeSalary("Johnson", 20000, is_bonus=True))


# II czesc

import datetime
import functools


# logFilePath = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\function_log.txt"


def CreateFunctionWithWrapper_LogToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, "a")
            file.write("-" * 20 + "\n")
            file.write("Function '{}' started at {}\n".format(func.__name__, datetime.datetime.now().isoformat()))
            file.write("Following arguments were used:\n")
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}".format(k, v) for k, v in kwargs.items()))
            file.write("\n")
            result = func(*args, **kwargs)
            print("Function returned {}\n".format(result))
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper


@CreateFunctionWithWrapper_LogToFile(r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\change_salary_log.txt")
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print("CHANGING SALARY FOR {} TO {} AS BONUS={}".format(emp_name, new_salary, is_bonus))
    return new_salary


@CreateFunctionWithWrapper_LogToFile(r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\change_position_log.txt")
def ChangePosition(emp_name, new_position):
    print("CHANGING SALARY FOR {} TO {}".format(emp_name, new_position))
    return new_position


print(ChangeSalary("Johnson", 20000, True))
print(ChangeSalary("Johnson", 20000, is_bonus=True))
print(ChangePosition("Michael", "Salesman"))
print(ChangePosition("Anke", "Manager"))