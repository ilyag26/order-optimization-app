import xlsxwriter
from scipy.optimize import minimize

def delta(z):
    a = 2 #коефіцієнти, які визначають вплив обсягу замовлення на вартість
    b = 3
    return a*z+b

def calculate_expression(variables):

    C = lambda z, y: z * y
    T = int(variables[0])
    K = int(variables[1])
    h = int(variables[3])
    I = int(variables[4])
    z = int(variables[5])  
    y = int(variables[6])

    return sum(K * delta(z) + C(z, y) + h * I for _ in range(1, T + 1))

def count(entry_z,entry_t,entry_kt,entry_ctz,entry_ht,entry_it,entry_zt,entry_xt,entry_yt):

    data = {
        "z":int(entry_z),
        "t":int(entry_t),
        "kt":int(entry_kt),
        "ctz":int(entry_ctz),
        "ht":int(entry_ht),
        "it":int(entry_it),
        "zt":int(entry_zt),
        "xt":int(entry_xt),
        "yt":int(entry_yt),
    }
    
    initial_guess = [float(data["t"]), float(data["kt"]),float(data["ctz"]),float(data["ht"]),float(data["it"]),float(data["zt"]),float(data["yt"])]
    result2 = minimize(calculate_expression, initial_guess, method='BFGS')

    optimal_value = result2.fun

    print("Оптимальне значення функції:", optimal_value)
    
    workbook = xlsxwriter.Workbook('logical.xlsx')
    
    cell_format = workbook.add_format()
    cell_format.set_bold()
    cell_format.set_font_color('black')
    cell_format.set_bg_color("#9bbb59")

    worksheet = workbook.add_worksheet()

    worksheet.write('B2:C2', "Вхідні дані:")

    i = 3
    for x in data:
        worksheet.write('B'+str(i), x)
        worksheet.write('C'+str(i), data[x])
        i += 1

    worksheet.write('B13', "Оптимальне значення функції:",cell_format)
    worksheet.write('C13', optimal_value,cell_format)
    workbook.close()