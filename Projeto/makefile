.PHONY: all
SYS_PYTHON=python3

all: data_gathering data_cleaning data_storage data_analysis

data_gathering:
	@echo "Executing data gathering"
	@$(SYS_PYTHON) scripts/scrapper.py
	@echo "Done with data gathering"

data_cleaning:
	@echo "Executing data cleaning"
	@$(SYS_PYTHON) scripts/clean_data.py
	@echo "Done with data cleaning"							

data_combining:	
	@echo "Executing data combining"
	@$(SYS_PYTHON) scripts/combine_data.py
	@echo "Done with data combining"				

data_analysis:
	@echo "Executing data analysis"
	@Rscript scripts/statistics.R
	@echo "Done with data analysis"
