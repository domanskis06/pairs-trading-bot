"""Central place for strategy parameters — no magic numbers inline elsewhere."""

# data
DATA_CACHE_DIR = "data_cache"

# pair selection
COINTEGRATION_PVALUE_THRESHOLD = 0.05

# signal generation
LOOKBACK_WINDOW = 60  # trading days for rolling spread mean/std
ZSCORE_ENTRY = 2.0
ZSCORE_EXIT = 0.0

# risk
STOP_LOSS_ZSCORE = 4.0
