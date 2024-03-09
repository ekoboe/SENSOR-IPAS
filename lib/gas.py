import machine
import time

class GasSensor:
    # Load resistance value in ohms
    RL = 20000  # 20 KΩ

    # Calibration values
    calibration_factor_CO2 = 200  # 200 ppm for CO2

    @staticmethod
    def read_CO2_sensor():
        analog_pin = machine.ADC(26)
        sensor_value = analog_pin.read_u16()
        voltage = sensor_value * 3.3 / 65535  # Assuming 3.3V reference voltage

        # Calculate the sensor resistance
        sensor_voltage = 3.3 - voltage
        sensor_resistance = sensor_voltage * GasSensor.RL / voltage

        # Convert to ppm using the calibration factors
        CO2_ppm = sensor_resistance / GasSensor.calibration_factor_CO2

        print("Sensor Value", sensor_value)
        print("CO2 concentration (ppm): ", CO2_ppm)
        return CO2_ppm