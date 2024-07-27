import xlsxwriter
import pulp

# Calculating the total cost of the function C
def func_C(d_t, h_t, Z_t, I_t,s_t):
    s = s_t/100
    return h_t*(I_t+(Z_t+Z_t*s_t)-d_t)


def count(K,c,h,d,s):
    k_value = K.split(',')
    c_value = c.split(',')
    h_value = h.split(',')
    d_value = d.split(',')
    s_value = s.split(',')

    T = 4
    data = {
        "K": [float(k_value[0]),float(k_value[1]),float(k_value[2]),float(k_value[3])], # fixed order costs for each period
        "c": [float(c_value[0]),float(c_value[1]),float(c_value[2]),float(c_value[3])], # variable product costs for each period
        "h": [float(h_value[0]),float(h_value[1]),float(h_value[2]),float(h_value[3])], # storage costs for each period
        "d": [float(d_value[0]),float(d_value[1]),float(d_value[2]),float(d_value[3])], # demand for each period
        "s": [float(s_value[0]),float(s_value[1]),float(s_value[2]),float(s_value[3])]  # % lack of goods
    }
    
    # Creating a minimization problem
    prob = pulp.LpProblem("Inventory_Management", pulp.LpMinimize)
    
    # Variables
    I = [pulp.LpVariable(f'I_{t}', lowBound=0, cat='Continuous') for t in range(T)]  # Inventories at the end of each period
    z = [pulp.LpVariable(f'z_{t}', lowBound=0, cat='Continuous') for t in range(T)]  # order volume in each period
    y = [pulp.LpVariable(f'y_{t}', cat='Binary') for t in range(T)]  # the fact of the order (0 or 1) in each period
    
    #The cost function
    prob += pulp.lpSum([data["K"][t] * y[t] + func_C(data["d"][t], data["h"][t], z[t], I[t-1], data["s"][t]) + data["h"][t] * I[t] for t in range(T)])

    # Inventory balance
    for t in range(T):
        if t == 0:
            prob += I[t] == z[t] - data["d"][t]  # Inventory balance for the first period
        else:
            prob += I[t] == I[t-1] + z[t] - data["d"][t]  # Inventory balance for the following periods
    
    # Fixed costs per order (y_t must be 1 if z_t > 0)
    M = 1000000  # a large number for approximation
    for t in range(T):
        prob += z[t] <= M * y[t]  # Limitations on the inclusion of fixed costs
    
    # Solution to the problem
    prob.solve()
    
    # Getting results
    I_opt = [pulp.value(I[t]) for t in range(T)]
    z_opt = [pulp.value(z[t]) for t in range(T)]
    y_opt = [pulp.value(y[t]) for t in range(T)]
    
    print("Optimal inventory:", I_opt)
    print("Optimal order volumes:", z_opt)
    print("The fact of the order (0 or 1):", y_opt)
    print("Minimal costs:", pulp.value(prob.objective))
    
    workbook = xlsxwriter.Workbook('logical.xlsx')

    cell_format1 = workbook.add_format({'border':1})
    cell_format1.set_bold()
    cell_format1.set_font_color('black')

    cell_format2 = workbook.add_format({'border':1})
    cell_format2.set_font_color('black')

    cell_format3 = workbook.add_format({'border':1})
    cell_format3.set_bold()

    cell_format4 = workbook.add_format({'border':1})

    worksheet = workbook.add_worksheet()

    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 1, 46)

    merge_format_top = workbook.add_format(
        {
            "bold": 1,
            "border": 1,
            "align": "center",
            "fg_color": "#9bbb59",
        }
    )

    merge_format = workbook.add_format(
        {
            "border": 1,
            "align": "center",
        }
    )

    worksheet.merge_range("B2:F2", "Input data:",merge_format_top)

    i = 3
    print(data)
    for x in data:
        worksheet.write('B'+str(i), 
        'fixed order costs for each period' if x == 'K' 
        else 'variable product costs for each period' if x == 'c' 
        else 'storage costs for each period' if x == 'h' 
        else 'demand for each period' if x == 'd' 
        else 'shortage of goods' if x == 's' 
        else x,cell_format4)
        worksheet.write('C'+str(i), data[x][0],cell_format4)
        worksheet.write('D'+str(i), data[x][1],cell_format4)
        worksheet.write('E'+str(i), data[x][2],cell_format4)
        worksheet.write('F'+str(i), data[x][3],cell_format4)
        i += 1
    
    worksheet.merge_range("B9:F9", "Results of the calculation",merge_format_top)
    worksheet.write('B10', "Optimal inventory",cell_format2)
    worksheet.write('C10', I_opt[0],cell_format2)
    worksheet.write('D10', I_opt[1],cell_format2)
    worksheet.write('E10', I_opt[2],cell_format2)
    worksheet.write('F10', I_opt[3],cell_format2)
    worksheet.write('B11', "Optimal order volumes",cell_format2)
    worksheet.write('C11', z_opt[0],cell_format2)
    worksheet.write('D11', z_opt[1],cell_format2)
    worksheet.write('E11', z_opt[2],cell_format2)
    worksheet.write('F11', z_opt[3],cell_format2)
    worksheet.write('B12', "The fact of the order (0 or 1)",cell_format2)
    worksheet.write('C12', y_opt[0],cell_format2)
    worksheet.write('D12', y_opt[1],cell_format2)
    worksheet.write('E12', y_opt[2],cell_format2)
    worksheet.write('F12', y_opt[3],cell_format2)
    worksheet.write('B13', "Minimum costs per 1 box",cell_format2)
    worksheet.merge_range("C13:F13", pulp.value(prob.objective),merge_format)

    chart = workbook.add_chart({'type': 'line'})
    chart.add_series({
            'values': '=Sheet1!$C$10:$F$10',
            'trendline': {
            'type': 'polynomial',
            'name': 'Тренд',
            'order': 2,
            'forward': 0.5,
            'backward': 0.5,
            'display_equation': True,
            'line': {
                'color': 'red',
                'width': 1,
                'dash_type': 'long_dash',
            },
        },
    })
    worksheet.insert_chart('H2', chart)
    workbook.close()