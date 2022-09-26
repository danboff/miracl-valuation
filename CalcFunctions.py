import math
import HelperFunctions as HF
#This file contains all the calculation functions

def calc_env_ben(project_annual_output,project_lifetime,Avoided_fuel_emmiss_intensity,social_cost_of_carbon,avoided_CO,avoided_NO2,avoided_ozone,avoided_SOX,avoided_PX): #Todo: Need explicit inputs rather than single dictionary - have multipoint comment to explain input and units
    #print(inputs["Project annual output"])
    avoid_co2_emiss = (1/907185)*project_annual_output*project_lifetime*Avoided_fuel_emmiss_intensity      #div by 907185 to convert grams into tons
    eco_val_avoid_co2_emiss = avoid_co2_emiss*social_cost_of_carbon
    tot_avoid_emiss = (1/907185)*project_annual_output*project_lifetime*(avoided_CO+avoided_NO2+avoided_ozone+avoided_SOX+avoided_PX)   #div by 907185 to convert grams into tons
    #print(tot_avoid_emiss)
    return round(avoid_co2_emiss,2), round(eco_val_avoid_co2_emiss,2), round(tot_avoid_emiss,2)

def calc_rec(start_year,end_year,project_output,rec_price,discount_rate):
    num_years = end_year - start_year
    pv_rec = []
    for i in range(1,num_years+1):
        pv_rec.append(((1/1000)*project_output*rec_price)/((1 + discount_rate/100)**(i)))	    
    #print(pv_rec)    
    npv_rec = sum(pv_rec)
    return round(npv_rec,2)


def TOU_and_DC_ben(behind_the_meter,on_tou_rate,building_consum_prof,elec_purch_price,building_consum_prof_nowg,on_demand_charge_rate,peak_monthly_demand_wout_sys,peak_monthly_demand_with_sys,demand_charge):
    tot_TOU_savings = 0
    tot_DC_savings = 0
    if behind_the_meter == 'TRUE':
        if on_tou_rate == 'TRUE':
            tot_TOU_savings = (building_consum_prof*elec_purch_price) - (building_consum_prof_nowg*elec_purch_price)
        if on_demand_charge_rate == "TRUE":
            tot_DC_savings = (peak_monthly_demand_wout_sys - peak_monthly_demand_with_sys)*demand_charge
    return 	round(tot_TOU_savings,2),round(tot_DC_savings,2)

def net_energy_benefit(system_ret_date,capture_price,proj_rated_cap,cap_factor,discount_rate):
    num_hours = system_ret_date*8760
    EB = []
    for i in range(1,num_hours+1):
        EB.append((capture_price*proj_rated_cap*cap_factor*math.exp(-1*discount_rate*i)))	    
    #print(EB)    
    NEB = sum(EB)
    return round(NEB,2)

def cal_proj_ann_output(system_profile):
    year_list = HF.unique(system_profile["Year"].values())  #Inferring project lifetime. Number of elements in this list correspond to it
    proj_lifetime = len(year_list)                          #Project lifetime in number of years	
    project_ann_output = dict.fromkeys(year_list)
    
    for k in range(0,len(year_list)):
        res = 0;
        #print(k)
        for i in range(1, len(system_profile["System production (kWh)"].values())+1):
            if system_profile["Year"][i] == year_list[k]:
                res = res + float(system_profile["System production (kWh)"][i])
            project_ann_output[str(year_list[k])] = res
    return project_ann_output, proj_lifetime, year_list

def cal_proj_mon_output(system_profile):
    year_list = HF.unique(system_profile["Year"].values())
    mon_list = HF.unique(system_profile["Month"].values())
    project_mon_output = dict.fromkeys(year_list)
    
    for k in range(0,len(year_list)):
        project_mon_output[str(year_list[k])] = dict.fromkeys(mon_list)
        for j in range(0,len(mon_list)):
            res = 0;
            for i in range(1, len(system_profile["System production (kWh)"].values())+1):
                if system_profile["Year"][i] == year_list[k]:
                    if system_profile["Month"][i] == mon_list[j]:
                        res = res + float(system_profile["System production (kWh)"][i])
                    project_mon_output[str(year_list[k])][str(mon_list[j])] = res
    return project_mon_output

def calc_env_ben_annually(project_annual_output, misc_inputs, annual_inputs):
    avoided_CO2 = dict.fromkeys(list(project_annual_output.keys()))
    avoided_CO2_value = dict.fromkeys(list(project_annual_output.keys()))
    avoided_tot_em = dict.fromkeys(list(project_annual_output.keys()))
    year_ind = 1
    for k in project_annual_output.keys():
        avoided_CO2[k] = round((project_annual_output[k]*float(misc_inputs["Avoided CO2"][1])/1000), 2)
        avoided_tot_em[k] = round((project_annual_output[k]*float(misc_inputs["Avoided CO"][1])/1000 + project_annual_output[k]*float(misc_inputs["Avoided NO"][1])/1000 + project_annual_output[k]*float(misc_inputs["Avoided SO2"][1])/1000 + project_annual_output[k]*float(misc_inputs["Avoided PM2.5"][1])/1000 + project_annual_output[k]*float(misc_inputs["Avoided O3"][1])/1000), 2)
        avoided_CO2_value[k] = round((avoided_CO2[k]*float(annual_inputs["Social cost of carbon"][year_ind])*0.00045359237), 2)
        #print(annual_inputs["Social cost of carbon"][year_ind])
        year_ind = year_ind + 1
        #print(annual_inputs["Social cost of carbon"][year_ind])
    return avoided_CO2, avoided_CO2_value, avoided_tot_em

def cal_rec_mon(system_profile):
    year_list = HF.unique(system_profile["Year"].values())
    mon_list = HF.unique(system_profile["Month"].values())
    mon_rec = dict.fromkeys(year_list)
    
    for k in range(0,len(year_list)):
        mon_rec[str(year_list[k])] = dict.fromkeys(mon_list)
        for j in range(0,len(mon_list)):
            rec = 0;
            for i in range(1, len(system_profile["REC price ($/MWh)"].values())+1):
                if system_profile["Year"][i] == year_list[k]:
                    if system_profile["Month"][i] == mon_list[j]:
                        rec = float(system_profile["REC price ($/MWh)"][i])
                        mon_rec[str(year_list[k])][str(mon_list[j])] = rec
                        break
    return mon_rec

def cal_rec_ben_annually(proj_mon_output, mon_rec):
    year_list = HF.unique(proj_mon_output.keys())
    rec_annual= dict.fromkeys(year_list)
    
    for k in range(0,len(year_list)):
        mon_list = HF.unique(proj_mon_output[str(year_list[k])].keys())
        res = 0
        for j in range(0,len(mon_list)):
            res = res + (proj_mon_output[str(year_list[k])][str(mon_list[j])]*mon_rec[str(year_list[k])][str(mon_list[j])])/1000
        rec_annual[str(year_list[k])] = round(res, 2)
    return rec_annual

def cal_peak_monthly_demand(build_profile, label, util_dc):
    year_list = HF.unique(build_profile["Year"].values())
    mon_list = HF.unique(build_profile["Month"].values())    #This may need a change
    peak_mon_demand= dict.fromkeys(year_list)
    
    if (util_dc == False):
        for k in range(0,len(year_list)):
            peak_mon_demand[str(year_list[k])] = dict.fromkeys(mon_list)
            for j in range(0,len(mon_list)):
                max_demand = 0;
                for i in range(1, len(build_profile[label].values())+1):
                    if build_profile["Year"][i] == year_list[k]:
                        if build_profile["Month"][i] == mon_list[j]:
                            if float(build_profile[label][i]) > max_demand:
                                max_demand = float(build_profile[label][i])
                            peak_mon_demand[str(year_list[k])][str(mon_list[j])] = max_demand
    else:
        for k in range(0,len(year_list)):
            peak_mon_demand[str(year_list[k])] = dict.fromkeys(mon_list)
            for j in range(0,len(mon_list)):
                max_demand = 0;
                for i in range(1, len(build_profile[label].values())+1):
                    if build_profile["Year"][i] == year_list[k]:
                        if build_profile["Month"][i] == mon_list[j]:
                            if (float(build_profile[label][i])*float(build_profile["System peaking charge hour (yes/no)"][i])) > max_demand:
                                max_demand = float(build_profile[label][i])*float(build_profile["System peaking charge hour (yes/no)"][i])
                            peak_mon_demand[str(year_list[k])][str(mon_list[j])] = max_demand
    return peak_mon_demand

def cal_mon_avg_DC(build_profile):
    year_list = HF.unique(build_profile["Year"].values())
    mon_list = HF.unique(build_profile["Month"].values())
    avg_mon_DC = dict.fromkeys(year_list)
    for k in range(0,len(year_list)):
        avg_mon_DC[str(year_list[k])] = dict.fromkeys(mon_list)
        for j in range(0,len(mon_list)):
            sum = 0
            count = 0
            for i in range(1, len(build_profile["Monthly demand charge ($/kW)"].values())+1):
                if build_profile["Year"][i] == year_list[k]:
                    if build_profile["Month"][i] == mon_list[j]:
                        count = count + 1;
                        sum = sum + float(build_profile["Monthly demand charge ($/kW)"][i])
                    if count != 0:
                        avg_mon_DC[str(year_list[k])][str(mon_list[j])] = sum/count
    return avg_mon_DC

def cal_DC_ben_annually(mon_peak, mon_peak_with_sys, mon_DC):
    year_list = HF.unique(mon_peak.keys())
    DC_annual= dict.fromkeys(year_list)
    
    for k in range(0,len(year_list)):
        mon_list = HF.unique(mon_peak[str(year_list[k])].keys())
        res = 0
        for j in range(0,len(mon_list)):
            res = res + (mon_peak[str(year_list[k])][str(mon_list[j])] - mon_peak_with_sys[str(year_list[k])][str(mon_list[j])])*mon_DC[str(year_list[k])][str(mon_list[j])]
        DC_annual[str(year_list[k])] = round(res, 2)
    return DC_annual

def cal_energy_ben_annually(build_prof, sys_prof):
    year_list = HF.unique(build_prof["Year"].values())
    ener_ben= dict.fromkeys(year_list)

    for k in range(0,len(year_list)):
        energy_ben = 0
        cum_energy_ben = 0
        for i in range(1, len(build_prof["Hourly consumption (kWh)"].values())+1):
            if build_prof["Year"][i] == year_list[k]:
                #if (sub_self_consump):
                    #print(energy_ben)
                energy_ben = float(build_prof["Hourly resale price ($/kWh)"][i])*(float(sys_prof["System production (kWh)"][i]) - float(build_prof["Hourly consumption (kWh)"][i])) + float(build_prof["Retail rate, hourly ($/kWh)"][i])*(float(build_prof["Hourly consumption (kWh)"][i]))
                    #print(energy_ben)
                #else:
                #    energy_ben = float(build_prof["Hourly purchase price ($/kWh)"][i])*(float(float(sys_prof["System production (kWh)"][i])))
                cum_energy_ben = cum_energy_ben + abs(energy_ben)        
        ener_ben[str(year_list[k])] = round(cum_energy_ben, 2)
    return ener_ben

def cal_util_DC_ben_annually(build_prof, sys_prof):
    year_list = HF.unique(build_prof["Year"].values())
    util_DC_annual= dict.fromkeys(year_list)
    peak_util_mon_demand = dict.fromkeys(year_list)
    peak_util_demand_charge = dict.fromkeys(year_list)
    peak_sys_output = dict.fromkeys(year_list)
    #print(peak_util_mon_demand)
    
    for k in range(0,len(year_list)):
        mon_list = HF.unique(build_prof["Month"].values())
        peak_util_mon_demand[str(year_list[k])] = dict.fromkeys(mon_list)
        peak_util_demand_charge[str(year_list[k])] = dict.fromkeys(mon_list)
        peak_sys_output[str(year_list[k])] = dict.fromkeys(mon_list)

    for i in range(1, len(build_prof["System peaking charge hour (yes/no)"].values())+1):
        if (build_prof["System peaking charge hour (yes/no)"][i] == "1"):
            peak_util_mon_demand[build_prof["Year"][i]][build_prof["Month"][i]] = float(build_prof["Hourly demand without system (kW)"][i])
            peak_util_demand_charge[build_prof["Year"][i]][build_prof["Month"][i]] = float(build_prof["System peaking charge ($/kW)"][i])
            peak_sys_output[build_prof["Year"][i]][build_prof["Month"][i]] = float(sys_prof["System production (kWh)"][i])
    #return util_DC_annual
    #print(peak_util_mon_demand)
    for k in range(0,len(year_list)):
        mon_list = HF.unique(peak_util_mon_demand[str(year_list[k])].keys())
        res = 0
        for j in range(0,len(mon_list)):
            res = res + abs(((peak_util_mon_demand[str(year_list[k])][str(mon_list[j])])*(peak_util_demand_charge[str(year_list[k])][str(mon_list[j])])) -   ((abs(peak_util_mon_demand[str(year_list[k])][str(mon_list[j])]-peak_sys_output[str(year_list[k])][str(mon_list[j])]))*peak_util_demand_charge[str(year_list[k])][str(mon_list[j])]))
        util_DC_annual[str(year_list[k])] = round(res, 2)
    return util_DC_annual