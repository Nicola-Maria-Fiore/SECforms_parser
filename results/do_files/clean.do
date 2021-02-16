*replace "nan" with "."
ds, has(type string)
foreach v in `r(varlist)' {
	replace `v' ="." if `v'=="nan"
	}

*missings dropvars, force

*destring all vars
destring, replace
