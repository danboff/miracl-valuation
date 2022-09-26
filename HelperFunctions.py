import csv
from csv import writer
import numpy as np
#Reads inputs from a .csv file and returns a dictionary
def get_user_inputs(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
    return row


#Reads inputs from a .csv file and returns a 2d dictionary (timeseries)
def get_inputs(filename):
    data = {}
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                for k in list(row.keys()):
                    data[k] = {}
                line_count += 1
            for k in list(row.keys()):
                data[k][line_count] = row[k]	
            line_count += 1
        #print(data)
    return data

# function to get unique values
def unique(inp_list):
    unique_list = []
    # traverse for all elements
    for x in inp_list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def calc_NPV(output, year_list, DR):
    ab = []
    for k in range(0,len(year_list)):
        ab.append((float(output[str(year_list[k])]))/((1 + DR/100)**(k+1)))    
    return round(sum(ab), 2)

def write_csv_res(results, results_all, year_list, impl_ind_val_ele_list, impl_dep_val_ele_list):
    #print(NEB)
    fields = ['',]+year_list+['NPV']
    with open("OutputFiles/Results.csv", "w", newline='') as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        for k in results_all:
            w.writerow({field: results_all[k].get(field) or k for field in fields})

    fields = ['',]+year_list+['NPV']
    with open("OutputFiles/Results_fin.csv", "w", newline='') as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        for k in results:
            w.writerow({field: results[k].get(field) or k for field in fields})
            #print(results[k].get(field).value() for field in fields)

    # print()
    # print("These value streams can be acheived by maximizing output of wind turbine i.e., curtailment is never performed:")
    # sum_ind = 0

    # for k in range(len(impl_ind_val_ele_list)):
        # if (results.get(impl_ind_val_ele_list[k]).get('NPV') != 0):
            # print(impl_ind_val_ele_list[k], end =" ")
            # print("              ", end =" ")
            # print(results.get(impl_ind_val_ele_list[k]).get('NPV'))
            # sum_ind = sum_ind + results.get(impl_ind_val_ele_list[k]).get('NPV')

    # print()
    # print("The following value streams are not maximized by maximizing output of wind turbine:")
    # sum_dep = 0
    # highest_val = 0
    # for k in range(len(impl_dep_val_ele_list)):
        # if (results.get(impl_dep_val_ele_list[k]).get('NPV') != 0):
            # print(impl_dep_val_ele_list[k])
            # sum_dep = sum_dep + results.get(impl_dep_val_ele_list[k]).get('NPV')
            # if (results.get(impl_dep_val_ele_list[k]).get('NPV') > highest_val):
                # highest_val = results.get(impl_dep_val_ele_list[k]).get('NPV')
    
    # if not impl_dep_val_ele_list:
        # print("<none>")
    # print()
    #print("Lower bound on achievable value - Equals highest of either sum of independent value streams or any of the individual dependant value streams:")
    #print(max(sum_ind,highest_val))

    #print("Upper Bound")
    #print(sum_ind + sum_dep)
    #with open("Results_fin.csv", "a", newline='') as f:
    #    writer_object = writer(f)
    #    writer_object.writerow("")
    #    writer_object.writerow(["Lower Bound", "", "",max(sum_ind,highest_val)])
        #writer_object.writerow(["Upper Bound", "", "",sum_ind + sum_dep])
    
    print()
    print("These value streams can be acheived by maximizing output of wind turbine i.e., curtailment is never performed:")
    res_years = year_list+['NPV']
    sum_ind = [0 for k in range(len(res_years))]
    for i in range(len(res_years)):
        for k in range(len(impl_ind_val_ele_list)):
            if ((results.get(impl_ind_val_ele_list[k]).get(res_years[i]) != 0) and (res_years[i] == 'NPV')):
                print('{0: <40}'.format(impl_ind_val_ele_list[k]), end =" ")
                #print("              ", end =" ")
                print(results.get(impl_ind_val_ele_list[k]).get(res_years[i]))
            sum_ind[i] = sum_ind[i] + results.get(impl_ind_val_ele_list[k]).get(res_years[i])
    #print(sum_ind)
    
    print()
    print("The following value streams are not maximized by maximizing output of wind turbine:")
    highest_val_dep = [0 for k in range(len(res_years))]
    for i in range(len(res_years)):
        for k in range(len(impl_dep_val_ele_list)):
            if ((results.get(impl_dep_val_ele_list[k]).get(res_years[i]) != 0) and (res_years[i] == 'NPV')):
                print(impl_dep_val_ele_list[k])
                if (results.get(impl_dep_val_ele_list[k]).get(res_years[i]) > highest_val_dep[i]):
                    highest_val_dep[i] = results.get(impl_dep_val_ele_list[k]).get(res_years[i])
    if not impl_dep_val_ele_list:
        print("<none>")

    print()
    print("Lower bound on achievable value - Equals highest of either sum of independent value streams or any of the individual dependant value streams:")
    print(round(max(sum_ind[-1],highest_val_dep[-1]),2))

    with open("OutputFiles/Results_fin.csv", "a", newline='') as f:
        writer_object = writer(f)
        writer_object.writerow("")
        writer_object.writerow(["Total Value*"] + np.maximum(sum_ind,highest_val_dep).tolist())
        writer_object.writerow(["Values are in nominal USD"])
        writer_object.writerow(["*Values could be higher if co-optimization is utilized"])