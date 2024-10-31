from pydantic import Field
from moapy.auto_convert import MBaseModel
from moapy.data_pre import (
    Point,
    Length,
    Stress,
    Temperature,
)


class ResultThermal(MBaseModel):
    """
    Result Thermal
    """

    y: list[Length] = Field(default_factory=list, description="Y")
    z: list[Length] = Field(default_factory=list, description="Z")
    temp: list[Temperature] = Field(
        default_factory=list, description="Temperature"
    )
    stress: list[Stress] = Field(default_factory=list, description="Stress")


class ResultNonlinearTemperatureEffect(MBaseModel):
    """
    Result Nonlinear Temperature Effect
    """
    height: Length = Field(default_factory=Length, description="Height")
    outer: list[Point] = Field(
        default_factory=list[Point], description="Outer polygon"
    )
    inner: list[list[Point]] = Field(
        default_factory=list[Point], description="Inner polygon"
    )
    heating: ResultThermal = Field(
        default_factory=ResultThermal, description="Heating"
    )
    cooling: ResultThermal = Field(
        default_factory=ResultThermal, description="Cooling"
    )
    temperature_heating: list[Point] = Field(
        default_factory=list[Point], description="Temperature Heating"
    )
    temperature_cooling: list[Point] = Field(
        default_factory=list[Point], description="Temperature Cooling"
    )
