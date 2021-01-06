# This file contains all configuration variables for the sensor daemon.

# Glider plane details
BATTERY_CAPACITY_MAX = 12.65  # 12.65 is the standard for full lead batteries
BATTERY_CAPACITY_MIN = 11.90  # 11.90 is the standard for empty lead batteries

SEA_LEVEL_PRESSURE = 1013.25  # hPa. Reference for the barometric measures.


# Measurement settings
MEASUREMENT_SYSTEM = "METRIC"  # Alternative: IMPERIAL. Without function yet. TODO: Add imperial measures.
# Please indicate the number of samples to draw per second. Keep in mind that a higher sampling rate also increases
# resource utilization and battery drain. A good indication is to have between 5 and 10 samples per second.
SENSOR_SAMPLING_RATE_PER_SECOND = 5  # Samples per second.

# System Configuration
XCSOAR_PORT = 4353  # Default OpenVario Port for XCSoar