import numpy as np
from services.data_observability import log_event

def detect_anomalies(data):
    # Detecting fuel anomalies using a rolling mean
    data['rolling_mean'] = data['fuel_consumption'].rolling(window=3).mean()
    anomaly_threshold = 1.5
    anomalies = data['fuel_consumption'] > (data['rolling_mean'] * anomaly_threshold)

    if anomalies.any():
        log_event('ANOMALY', f"Spikes detected at indices: {np.where(anomalies)[0]}")

def periodic_anomaly_check():
    print("Running periodic anomaly check")
    detect_anomalies(data)
