from typing import Literal, Optional

from pydantic import Field

from datagarden_models.models.base import DataGardenModel, DataGardenModelLegends

TEMP_SCALES: Literal["CELSIUS", "FAHRENHEID"]


class WeatherV1Keys:
	MIN_TEMP = "min_temp"
	MAX_TEMP = "max_temp"
	MEAN_TEMP = "mean_temp"
	RAIN_FALL_MM = "rain_fall_mm"
	SEA_LEVEL_PRESSURE_HPA = "sea_level_pressure_hpa"
	CLOUD_COVER_OKTA = "cloud_cover_okta"
	TEMP_SCALE = "temp_scale"
	WIND_DIRECTION = "wind_direction"
	WIND_SPEED_M_S = "wind_speed_m_s"
	MAX_WIND_GUST_M_S = "max_wind_gust_m_s"
	SUN_HOURS = "sun_hours"
	SNOW_DEPTH_CM = "snow_depth_cm"
	RADIATION_PER_SQUARE_M = "radiation_per_square_m"
	HUMIDITY = "humidity"
	DATAGARDEN_MODEL_NAME = "WeatherData"


class WeatherV1Legends(DataGardenModelLegends):
	MIN_TEMP = "minimum temperature"
	MAX_TEMP = "maximum temperature"
	MEAN_TEMP = "mean temperature"
	TEMP_SCALE = "unit of temperature(Celsius or Fahrenheit)"
	RAIN_FALL_MM = "rainfall in mm"
	SEA_LEVEL_PRESSURE_HPA = "sea level pressure in hPa"
	CLOUD_COVER_OKTA = "cloud cover in oktas"
	WIND_DIRECTION = "wind direction in degrees"
	WIND_SPEED_M_S = "wind speed in m/s"
	MAX_WIND_GUST_M_S = "max wind gust in m/s"
	SUN_HOURS = "sun hours"
	SNOW_DEPTH_CM = "snow depth in cm"
	RADIATION_PER_SQUARE_M = "radiation per square meter in W/m²"
	HUMIDITY = "humidity in %"


L = WeatherV1Legends


class WeatherObservationV1(DataGardenModel):
	datagarden_model_version: str = Field(
		"v1.0", frozen=True, description=L.DATAGARDEN_MODEL_VERSION
	)
	min_temp: Optional[float] = Field(None, ge=-70, le=70)
	max_temp: Optional[float] = Field(None, ge=-70, le=70)
	mean_temp: Optional[float] = Field(None, ge=-70, le=70)
	rain_fall_mm: Optional[float] = Field(None, ge=0)
	sea_level_pressure_hpa: Optional[float] = Field(None, ge=850, le=1100)
	cloud_cover_okta: Optional[int] = Field(None, ge=0, le=8)
	temp_scale: Literal["CELSIUS", "FAHRENHEID"] = "CELSIUS"
	wind_direction: Optional[int] = Field(None, ge=0, le=359)
	wind_speed_m_s: Optional[float] = Field(None, ge=0, le=110)
	max_wind_gust_m_s: Optional[float] = Field(None, ge=0, le=110)
	sun_hours: Optional[float] = Field(None, ge=0, le=24)
	snow_depth_cm: Optional[float] = Field(None, ge=0, le=10000)
	radiation_per_square_m: Optional[float] = Field(None, ge=-100, le=2000)
	humidity: Optional[float] = Field(None, ge=0, le=100)

	@property
	def is_empty(self) -> bool:
		return all(
			getattr(self, field) is None
			for field in self.model_fields
			if field not in ["temp_scale", "datagarden_model_version"]
		)

	def __bool__(self) -> bool:
		return not self.is_empty
