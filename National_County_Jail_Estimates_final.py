#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:41:54 2020

@author: tobijegede
"""


#Cleaner Version of National County Jail Estimates Data 

#----------- DATA SOURCES ------------------ #
# CENSUS DATA  = https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html
# COUNTY JAIL DATA (SPEFICICALLY, 2013 CENSUS OF JAILS = https://www.bjs.gov/index.cfm?ty=dcdetail&iid=254 


# ----- IMPORTING THE DATA ------------ # 
#def main():
    #importing Census Data for Pennslyvania
import pandas as pd
gen_pa_census = pd.read_csv('/Users/tobijegede/Documents/PghD4BL/cc-est2019-alldata-42.csv')


#Subsetting the data to just include desired columns (SELECT)
sub_gen_pa = gen_pa_census[["COUNTY", "STNAME" ,"CTYNAME", "YEAR", "AGEGRP", "TOT_POP","WA_MALE", "WA_FEMALE", "BA_MALE", "BA_FEMALE"]]


# ------ GETTING THE POPULATION COUNTS IN ALLEGHENY COUNTY FOR 2017, 2018, & 2019 ------- #
#def popCountByYear():


#General Allegheny County subset of Data
alleg_count = sub_gen_pa[sub_gen_pa['COUNTY'] == 3]

#Question -- What was the population of Allegheny County in
# 2017, 2018, and 2019?

#Total Population in 2017 (of Allegheny County)
alleg_count_17 = alleg_count[alleg_count['YEAR'] == 10]

#total population in allegheny county as a single value 
alleg_count_17_totpop = alleg_count_17[alleg_count_17['AGEGRP'] == 0]
ac_totpop_2017 = int(alleg_count_17_totpop['TOT_POP'])


#Total Population in 2018 (of Allegheny County)
alleg_count_18 = alleg_count[alleg_count['YEAR'] == 11]
alleg_count_18_totpop = alleg_count_18['TOT_POP']

#Total population in 2018 in Allegheny County as a single value
alleg_count_18_totpop = alleg_count_18[alleg_count_18['AGEGRP'] == 0]
ac_totpop_2018 = int(alleg_count_18_totpop['TOT_POP'])


#Total Popualtion in 2019 (of Allegheny County)
alleg_count_19 = alleg_count[alleg_count['YEAR'] == 12]
alleg_count_19_totpop = alleg_count_19['TOT_POP']

alleg_count_19_totpop = alleg_count_19[alleg_count_19['AGEGRP'] == 0]
ac_totpop_2019 = int(alleg_count_19_totpop['TOT_POP'])

#Total Population in 2013
alleg_count_13 = alleg_count[alleg_count['YEAR'] == 6]
alleg_count_13_totpop = alleg_count_13[alleg_count_13['AGEGRP'] == 0]
ac_totpop_2013 = int(alleg_count_13_totpop['TOT_POP'])


#Find the racial breakdown for pittsburgh based on 2019 data
#print(alleg_count_19_totpop)

ac_white_19 = int(alleg_count_19_totpop['WA_MALE'])
#print(ac_white_17)
ac_percent_white_19 = round((ac_white_19/ac_totpop_2019) * 100, 2)
#print(ac_percent_white_17) 

ac_black_19 = int(alleg_count_19_totpop['BA_MALE'])
#print(ac_black_19)
ac_percent_black_19 = round((ac_black_19/ac_totpop_2019) * 100, 2)
#print(ac_percent_black_19)
#Counts of the 2017, 2018, and 2019 populations in Allegheny County
#2017
#print(ac_totpop_2017)
#2018
#print(ac_totpop_2018)
#2019
#print(ac_totpop_2019)

# -------------------------------- COMPARING COUNTIES ------------------------------ #

#Look at Original PA data and Just Subset for all of the total population Data
total_pop_by_county_pa_19 = sub_gen_pa[(sub_gen_pa['AGEGRP'] == 0) & (sub_gen_pa['YEAR'] == 12)]
#print(total_pop_by_county_pa_17)

#SIMILAR -- defined as populations within 200,000 above or below that year's population for Allegheny County
#Allegheny County Population = aprox. 1.2 million
pop_min_19 = ac_totpop_2019 - 200000
pop_max_19 = ac_totpop_2019 + 200000

#Adding demographic restrictions for the comparison (+/- 5%)
white_min_19 = ac_percent_white_19 - 5.0
white_max_19 = ac_percent_white_19 + 5.0

black_min_19 = ac_percent_black_19 - 5.0
black_max_19 = ac_percent_black_19 + 5.0


#----------- ALL UNITED STATES DATA ---------------------------#


#Change to this instruction when sharing the data with other people
#filename1 = str(input("Please provide the full path for where you have the Census Data for All United States County Populations stored on your device. If this dataset is not already downloaded, please go to the Census webstie and download the cc-est2019-alldata.csv file. ex: '/Users/tobijegede/Documents/PghD4BL/cc-est2019-alldata.csv: "))



gen_usa_census = pd.read_csv('cc-est2019-alldata.csv', encoding = 'ISO-8859-1')


#Subsetting the general USA data
sub_gen_usa = gen_usa_census[["COUNTY", "STNAME" ,"CTYNAME", "YEAR", "AGEGRP", "TOT_POP", "WA_MALE", "WA_FEMALE", "BA_MALE", "BA_FEMALE"]]



#Creating a list of total population by county in 2019
total_pop_by_county_usa_19 = sub_gen_usa[(sub_gen_usa['AGEGRP'] == 0) & (sub_gen_usa['YEAR'] == 12)]


simi_size_count_usa_19 = total_pop_by_county_usa_19[(total_pop_by_county_usa_19['TOT_POP'] >= pop_min_19) & 
                                                   (total_pop_by_county_usa_19['TOT_POP'] <= pop_max_19)]

simi_size_count_usa_19['PERCENT_WHITE'] = round(simi_size_count_usa_19['WA_MALE']/simi_size_count_usa_19['TOT_POP'] * 100, 2)
simi_size_count_usa_19['PERCENT_BLACK'] = round(simi_size_count_usa_19['BA_MALE']/simi_size_count_usa_19['TOT_POP'] * 100, 2)



simi_size_count_usa_19 = simi_size_count_usa_19[(simi_size_count_usa_19['PERCENT_WHITE'] >= white_min_19) & (simi_size_count_usa_19['PERCENT_WHITE'] <= white_max_19)]
simi_size_count_usa_19 = simi_size_count_usa_19[(simi_size_count_usa_19['PERCENT_BLACK'] >= black_min_19) & (simi_size_count_usa_19['PERCENT_BLACK'] <= black_max_19)]



print(simi_size_count_usa_19)


#all of the counties in the USA in 2017 with a similar size as Allegheny County in 2017
#print(simi_size_count_usa_17)

#create a csv file with this information
    #1. Remove Allegheny County from this dataset
#simi_size_count_usa_19 = simi_size_count_usa_19.drop(512069)

simi_size_count_usa_19.to_csv('similar_countiesbypop_Allegheny_2019.csv')

#print(simi_size_count_usa_19) #simi_size_count_usa_19.shape[0])


#------- COMPARABLE COUNTES in 2013 ------------- # (In order to do the BJS 2013 comparison)

'''
#Creating a list of total population by county in 2013
total_pop_by_county_usa_13 = sub_gen_usa[(sub_gen_usa['AGEGRP'] == 0) & (sub_gen_usa['YEAR'] == 6)]


#New Comparison for 2013
pop_min_13 = ac_totpop_2013 - 200000
pop_max_13 = ac_totpop_2013 + 200000

simi_size_count_usa_13 = total_pop_by_county_usa_13[(total_pop_by_county_usa_13['TOT_POP'] >= pop_min_13) & 
                                                   (total_pop_by_county_usa_13['TOT_POP'] <= pop_max_13)]


#Additional Subsetting of hte Data according to the demographic information 

#all of the counties in the USA in 2017 with a similar size as Allegheny County in 2017
#print(simi_size_count_usa_13)

#create a csv file with this information
    #1. Remove Allegheny County from this dataset
#simi_size_count_usa_13 = simi_size_count_usa_19.drop(512069)

#simi_size_count_usa_13.to_csv('similar_countiesbypop_Allegheny_2013.csv')

#print(simi_size_count_usa_13)# simi_size_count_usa_19.shape[0], simi_size_count_usa_13.shape[0])  '''



#------- LOADING IN COUNTY JAIL DATA --------------- # 

nat_county_jail = pd.read_csv('CountyJail_Info_2013.tsv', sep = '\t')


sub_nat_county_jail = nat_county_jail[["NAME", "TOTPOP", "BLACK", "WHITE"]] #"HISP", "AIAN", "ASIAN"]]

#Creating Black Population Percentage
sub_nat_county_jail = sub_nat_county_jail.assign(PERCENT_BLACK=sub_nat_county_jail['BLACK'] / sub_nat_county_jail['TOTPOP'] * 100)

#Creating White Population Percentage
sub_nat_county_jail  = sub_nat_county_jail.assign(PERCENT_WHITE=sub_nat_county_jail['WHITE'] / sub_nat_county_jail['TOTPOP'] * 100)



#OMITTED CATGORIES: "JURISID", "JURISSIZE" "ADULTF","TOTPOP_FLAG", "ADULTM"

#print(sub_nat_county_jail)

# Jail Population at the Similar Sized Counties as Allegheny County


#isolate just the county names 
county_names = simi_size_count_usa_19['CTYNAME'].tolist()

#Removing the "County" at the end of the list of counties 

new_county_names = []

for i in range(len(county_names)):
    new_name = county_names[i][:-7]
    new_county_names.append(new_name) 
    
#print(new_county_names)


#Getting Rid of Franklin & Orange Counties that are not in Ohio and Florida (respectively)
#c
#new_county_names.remove('Orange')
#new_county_names.append('Franklin County Correctional Center')
#new_county_names.append('Orange County Corrections Department')
#print(new_county_names)
#new_county_names_edit = new_county_names_edit.remove('Orange')


pattern = '|'.join(new_county_names)

#ISOLATE THE ROWS IN THE NATIONAL COUNTY JAIL DATABASE THAT ARE FOR COUNTIES OF A COMPARABLE SIZE TO ALLEGHENY COUNTY
jail_pop_similar_counties = sub_nat_county_jail[sub_nat_county_jail['NAME'].str.contains(pattern, case = False)]

#removing Collins matches that aren't appropriate
jail_pop_similar_counties = jail_pop_similar_counties[jail_pop_similar_counties['NAME'] != "Collingsworth Co. Jail"]
jail_pop_similar_counties = jail_pop_similar_counties[jail_pop_similar_counties['NAME'] != "Collins City Jail"]
jail_pop_similar_counties = jail_pop_similar_counties[jail_pop_similar_counties['NAME'] != "Collinsville City Jail"]

print(jail_pop_similar_counties)


#TOTAL POP (of all jails) IN COUNTIES WITH A SIMILAR POPULATION TO ALLEGHENY COUNTY
count = 0 
jail_totpop_count = []
jail_county_name = []
for i in range(len(new_county_names)):
    if jail_pop_similar_counties['NAME'].str.contains(new_county_names[i]).any():
        jail_pop_onecounty =  jail_pop_similar_counties[jail_pop_similar_counties['NAME'].str.contains(new_county_names[i])]
        jail_pop_onecounty = jail_pop_onecounty['TOTPOP'].tolist()
        for k in range(len(jail_pop_onecounty)):
            count += jail_pop_onecounty[k]
        county_name = str(new_county_names[i]) 
        jail_totpop_count.append(count)
        jail_county_name.append(county_name)
    count = 0 
print(jail_totpop_count)
print(jail_county_name) 


#Create a dictionary of the total jail population with associated county names
jailtotpop_bycounty = dict(zip(jail_county_name, jail_totpop_count))

#Converting the dictionary back to a DataFrame
jailtotpop_bycounty = pd.DataFrame.from_dict(jailtotpop_bycounty, orient = 'index', columns = ['Aggregate Population Across All Jails in County'])
print(jailtotpop_bycounty)
        
jail_pop_similar_counties.to_csv('jailpopulations_similarcounties_2013.csv')

jailtotpop_bycounty.to_csv('Aggregate Jail Population By County_2013.csv')


#if __name__ == '__main__':
 #   main()









