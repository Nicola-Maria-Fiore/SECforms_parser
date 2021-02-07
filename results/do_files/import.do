
import delimited "main.csv", varnames(1) stringcols(_all) 
 save "main.dta" 
 clear all
import delimited "issuerList.csv", varnames(1) stringcols(_all) 
 save "issuerList.dta" 
 clear all
import delimited "relatedPersonsList.csv", varnames(1) stringcols(_all) 
 save "relatedPersonsList.dta" 
 clear all
import delimited "salesCompensationList.csv", varnames(1) stringcols(_all) 
 save "salesCompensationList.dta" 
 clear all