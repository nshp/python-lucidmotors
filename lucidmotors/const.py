"""Constants for the Lucid Motors API."""

# Before Lucid was Lucid, it was Atieva. They still use their old domain in
# their mobile apps for now.
MOBILE_API = "mobile.deneb.prod.infotainment.pdx.atieva.com"

# Min/max temperatures for HVAC preconditioning. The API rejects anything
# outside of this range. Values are in Celsius.
# StatusCode.INVALID_ARGUMENT:
# SetCabinTemperature failed
# temperature [15.0 <= x <= 30.0] is required with HVAC_PRECONDITION in SetCabinTemperatureRequest
PRECONDITION_TEMPERATURE_MIN = 15.0
PRECONDITION_TEMPERATURE_MAX = 30.0
