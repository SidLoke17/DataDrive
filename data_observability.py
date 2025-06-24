import logging

# Configure logging
logging.basicConfig(filename='data_observability.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_event(event_type, message):
    logging.info(f"{event_type} - {message}")

def detect_redundancy(data):
    # Detect duplicates or unused data
    duplicates = data.duplicated()
    if duplicates.any():
        log_event('REDUNDANCY', 'Duplicate data detected')
