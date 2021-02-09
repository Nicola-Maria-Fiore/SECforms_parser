*replace "nan" with "."
ds, has(type string)
foreach v in `r(varlist)' {
	replace `v' ="." if `v'=="nan"
	}


*destring all vars
destring, replace
