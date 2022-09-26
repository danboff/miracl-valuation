import csv
import CalcFunctions as CF
import HelperFunctions as HF

misc_inp_csv = "InputFiles/StaticInputs.csv"
sys_prof_csv = "InputFiles/SystemProfile.csv"
build_prof_csv = "InputFiles/BuildingProfile.csv"
annual_costs_csv = "InputFiles/AnnualCosts.csv"

misc_inputs = HF.get_inputs(misc_inp_csv)
sys_prof = HF.get_inputs(sys_prof_csv)
build_prof = HF.get_inputs(build_prof_csv)
annual_inputs = HF.get_inputs(annual_costs_csv)

Environmental = {"Economic Value of Avoided CO2 ($)" : {}}
REC = {"Renewable Energy Credits ($)" : {}}
TOU_DC = {"Demand Charge Savings ($)": {}}
NEB = {"Net Energy Benefit ($)" : {}}
misc_outputs = {"avoid_co2" : {}, "tot_avoid_emiss" : {}}
peak_util_DC = {"System Peaking Charge Savings ($)": {}}

#impl_ind_val_ele_list = ['Economic Value of Avoided CO2 ($)', 'Renewable Energy Credits ($)', 'Demand Charge Savings ($)', 'Net Energy Benefit ($)', 'System Peaking Charge Savings ($)']
impl_ind_val_ele_list = ['Net Energy Benefit ($)', 'Demand Charge Savings ($)', 'System Peaking Charge Savings ($)', 'Renewable Energy Credits ($)' ,'Economic Value of Avoided CO2 ($)']
impl_dep_val_ele_list = []

project_annual_output, proj_lifetime, year_list = CF.cal_proj_ann_output(sys_prof)
project_mon_output = CF.cal_proj_mon_output(sys_prof)
project_mon_rec = CF.cal_rec_mon(sys_prof)

monthly_peak = CF.cal_peak_monthly_demand(build_prof, "Hourly demand without system (kW)", False)
monthly_peak_with_sys = CF.cal_peak_monthly_demand(build_prof, "Hourly demand with system (kW)", False)
monthly_avg_DC = CF.cal_mon_avg_DC(build_prof)

misc_outputs["avoid_co2"], Environmental["Economic Value of Avoided CO2 ($)"], misc_outputs["tot_avoid_emiss"] = CF.calc_env_ben_annually(project_annual_output, misc_inputs, annual_inputs)
REC["Renewable Energy Credits ($)"] = CF.cal_rec_ben_annually(project_mon_output, project_mon_rec)

if ((str(misc_inputs["Meter position"][1]) == 'BTM') and (str(misc_inputs["Demand Charge"][1]) == 'TRUE')):
    TOU_DC["Demand Charge Savings ($)"] = CF.cal_DC_ben_annually(monthly_peak, monthly_peak_with_sys, monthly_avg_DC)
else:
    TOU_DC["Demand Charge Savings ($)"] = 0

peak_util_DC["System Peaking Charge Savings ($)"] = CF.cal_util_DC_ben_annually(build_prof, sys_prof)
NEB["Net Energy Benefit ($)"] = CF.cal_energy_ben_annually(build_prof, sys_prof)

#Environmental["avoid_co2"]['NPV'] = HF.calc_NPV(Environmental['avoid_co2'], year_list, int(misc_inputs['Discount rate'][1]))
Environmental["Economic Value of Avoided CO2 ($)"]['NPV'] = HF.calc_NPV(Environmental['Economic Value of Avoided CO2 ($)'], year_list, int(misc_inputs['Discount rate'][1]))
#Environmental["tot_avoid_emiss"]['NPV'] = HF.calc_NPV(Environmental['tot_avoid_emiss'], year_list, int(misc_inputs['Discount rate'][1]))

REC["Renewable Energy Credits ($)"]['NPV'] = HF.calc_NPV(REC["Renewable Energy Credits ($)"], year_list, int(misc_inputs['Discount rate'][1]))
TOU_DC["Demand Charge Savings ($)"]['NPV'] = HF.calc_NPV(TOU_DC["Demand Charge Savings ($)"], year_list, int(misc_inputs['Discount rate'][1]))
NEB["Net Energy Benefit ($)"]['NPV'] = HF.calc_NPV(NEB["Net Energy Benefit ($)"], year_list, int(misc_inputs['Discount rate'][1]))
peak_util_DC["System Peaking Charge Savings ($)"]['NPV'] = HF.calc_NPV(peak_util_DC["System Peaking Charge Savings ($)"], year_list, int(misc_inputs['Discount rate'][1]))

results = {}
results_all = {}
results.update(Environmental)
results.update(REC)
results.update(TOU_DC)
results.update(NEB)
results.update(peak_util_DC)
results_all.update(results)
results_all.update(misc_outputs)

HF.write_csv_res(results, results_all, year_list, impl_ind_val_ele_list, impl_dep_val_ele_list)   #Todo: place csv write function in HF

import opt
