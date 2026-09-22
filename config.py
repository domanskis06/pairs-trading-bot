"""Central place for strategy parameters — no magic numbers inline elsewhere."""

# data
DATA_CACHE_DIR = "data_cache"
START_DATE = "2018-01-01"
END_DATE = "2023-12-31"

# first candidate pair: both large-cap non-alcoholic beverage companies,
# same sector/demand drivers -> classic textbook pairs-trading candidate
FIRST_PAIR = ("KO", "PEP")

# pair selection
COINTEGRATION_PVALUE_THRESHOLD = 0.05

# signal generation
LOOKBACK_WINDOW = 60  # trading days for rolling spread mean/std
ZSCORE_ENTRY = 2.0
ZSCORE_EXIT = 0.0

# risk
STOP_LOSS_ZSCORE = 4.0
