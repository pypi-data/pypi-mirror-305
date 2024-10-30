from imputegap.recovery.optimization import Optimization
from imputegap.recovery.imputation import Imputation
from imputegap.recovery.manager import TimeSeries
from imputegap.tools import utils

# 1. initiate the TimeSeries() object that will stay with you throughout the analysis
ts_1 = TimeSeries()

# 2. load the timeseries from file or from the code
ts_1.load_timeseries(utils.search_path("eeg"), header=True)
ts_1.normalize()

# 3. infected_data of the data
infected_data = ts_1.Contaminate.mcar(ts=ts_1.data, series_impacted=0.05, missing_rate=0.05, use_seed=True, seed=42)

# 4. imputation of the contaminated data
# imputation with AutoML which will discover the optimal hyperparameters for your dataset and your algorithm
cdrec = Imputation.MatrixCompletion.CDRec(infected_data).impute(user_defined=False, params={"ground_truth": ts_1.data, "optimizer": "bayesian", "options": {"n_calls": 15}})

# 5. score the imputation with the raw_data
cdrec.score(ts_1.data, cdrec.imputed_matrix)

# 6. display the results
ts_1.print_results(cdrec.metrics)

ts_1.plot(raw_data=ts_1.data, infected_data=infected_data, imputed_data=cdrec.imputed_matrix, title="imputation", max_series=1, save_path="./assets", display=True)

# 7. save hyperparameters
utils.save_optimization(optimal_params=cdrec.parameters, algorithm="cdrec", dataset="eeg", optimizer="t")
