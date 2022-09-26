from __future__ import division
import pyomo.environ as pyo

import pandas as pd
import csv

print("Co-optimizing energy, regulation up, regulation down, spinning reserve, and non-spinning reserve value streams...")
model = pyo.AbstractModel()

model.T = pyo.Param(initialize=96360, within=pyo.NonNegativeIntegers)

model.t = pyo.RangeSet(1, model.T)

#Declaring coefficients 
model.price_energy = pyo.Param(model.t)
model.price_RU = pyo.Param(model.t)
model.price_RD = pyo.Param(model.t)
model.price_RMU = pyo.Param(model.t)
model.price_RMD = pyo.Param(model.t)
model.price_SR = pyo.Param(model.t)
model.price_NR = pyo.Param(model.t)

model.beta_RMU = pyo.Param(model.t)
model.beta_RMD = pyo.Param(model.t)

model.M_RMU = pyo.Param(model.t)
model.M_RMD = pyo.Param(model.t)

model.pay_RMU = pyo.Param()
model.pay_RMD = pyo.Param()

model.total_gen = pyo.Param(model.t)

#Declaring decision variables
model.e_E = pyo.Var(model.t, domain=pyo.NonNegativeReals)
model.p_RU = pyo.Var(model.t, domain=pyo.NonNegativeReals)
model.p_RD = pyo.Var(model.t, domain=pyo.NonNegativeReals)
model.p_SR = pyo.Var(model.t, domain=pyo.NonNegativeReals)
model.p_NR = pyo.Var(model.t, domain=pyo.NonNegativeReals)

#Declaring objective function
def energy_cost(m):
    return -1*(pyo.summation(m.price_energy, m.e_E))

def reserve_cost(m):
    return -1*(pyo.summation(m.price_SR, m.p_SR) + pyo.summation(m.price_NR, m.p_NR))

def regulation_cost(m):
    return -1*(pyo.summation(m.price_RU, m.p_RU) + pyo.summation(m.price_RD, m.p_RD))

def obj_func(m):
    return (energy_cost(m) + reserve_cost(m) + regulation_cost(m))

model.OBJ = pyo.Objective(rule=obj_func)

#Defining constraints
def constraint_power_bal(m, i):
    return m.e_E[i] + m.p_RU[i] + m.p_RD[i] + m.p_SR[i] + m.p_NR[i] == m.total_gen[i]


model.AxbConstraint = pyo.Constraint(model.t, rule=constraint_power_bal)


#Initializing data
data = pyo.DataPortal()


data.load(filename='InputFiles/Prices.csv', param=(model.price_RU, model.price_RD, model.price_SR, model.price_NR, model.price_RMU, model.price_RMD, model.price_energy, model.total_gen))
instance = model.create_instance(data)


opt = pyo.SolverFactory('Ipopt')
results = opt.solve(instance)
#instance.display()
print(results) 


list_of_vars =[v[1].value for v in instance.component_objects(ctype=pyo.Var, active=True, descend_into=True)]

var_names =[v.name for v in instance.component_objects(ctype=pyo.Var, active=True, descend_into=True)]

#print(list_of_vars)
#print(var_names)


#result_series = pd.Series(list_of_vars,index=var_names)
#result_series.to_csv('my_results.csv')


# opening the csv file in 'w+' mode
file = open('OutputFiles/my_results_mod.csv', 'w', newline ='')

with file:
    header = var_names
    writer = csv.writer(file)
	
    writer.writerow(header)
    writer.writerow(list_of_vars)
	
    for x in range(2,96361):
        writer.writerow([v[x].value for v in instance.component_objects(ctype=pyo.Var, active=True, descend_into=True)])


df_res = pd.read_csv ('OutputFiles/my_results_mod.csv')
#print(df_res)

df_inp = pd.read_csv ('InputFiles/Prices.csv')
#print(df_inp)

df_val = pd.DataFrame()

df_val['val_E'] = df_inp['LMP_mod ($/kW)']*df_res['e_E']
df_val['val_RU'] = df_inp['Regulation up ($/kW)']*df_res['p_RU']
df_val['val_RD'] = df_inp['Regulation down ($/kW)']*df_res['p_RD']
df_val['val_SR'] = df_inp['Spinning reserve ($/kW)']*df_res['p_SR']
df_val['val_NR'] = df_inp['Non-spinning reserve ($/kW)']*df_res['p_NR']

#print(df_val)

df_1 = df_val.iloc[0:8760,:]
df_2 = df_val.iloc[8760:17520,:]
df_3 = df_val.iloc[17520:26280,:]
df_4 = df_val.iloc[26280:35040,:]
df_5 = df_val.iloc[35040:43800,:]
df_6 = df_val.iloc[43800:52560,:]
df_7 = df_val.iloc[52560:61320,:]
df_8 = df_val.iloc[61320:70080,:]
df_9 = df_val.iloc[70080:78840,:]
df_10 = df_val.iloc[78840:87600,:]
df_11 = df_val.iloc[87600:96360,:]

frames = [(df_1.cumsum()).iloc[-1:], (df_2.cumsum()).iloc[-1:]*1.02, (df_3.cumsum()).iloc[-1:]*1.04, (df_4.cumsum()).iloc[-1:]*1.06, (df_5.cumsum()).iloc[-1:]*1.08, (df_6.cumsum()).iloc[-1:]*1.1, (df_7.cumsum()).iloc[-1:]*1.12, (df_8.cumsum()).iloc[-1:]*1.14, (df_9.cumsum()).iloc[-1:]*1.16, (df_10.cumsum()).iloc[-1:]*1.18, (df_11.cumsum()).iloc[-1:]*1.20]
  
result = pd.concat(frames)
#print(result)

#result_transposed = result.T
#result_transposed_new = result_transposed.rename(index={0: 2021}, columns={'value of Energy': 'val_E'})

result_copy = result.copy()
result_copy.rename(columns={'val_E': 'Energy value ($)', 'val_RU':'Regulation up value ($)','val_RD':'Regulation down value ($)','val_SR':'Spinning reserve value ($)','val_NR':'Non-spinning reserve value ($)'}, index={8759: 2020, 17519:2021, 26279:2022, 35039:2023, 43799:2024, 52559:2025, 61319:2026, 70079:2027, 78839:2028, 87599:2029, 96359:2030}, inplace=True)

result_copy_t = result_copy.T

result_copy_t.to_csv("OutputFiles/val_co_opt.csv")

print("Optimization done")

print("Results written to val_co_opt.csv file")
