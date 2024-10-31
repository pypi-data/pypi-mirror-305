from moapy.data_pre import Length, Point, Stress, Temperature
from moapy.enum_pre import enUnitLength, enUnitStress, enUnitTemperature
from moapy.plugins.temperature_gradient.eqv_stress import self_equilibrating_stress
from moapy.plugins.temperature_gradient.eurocode.nonlinear_eurocode import (
    interpolate_temperature,
)
from moapy.plugins.temperature_gradient.eurocode.data_post import (
    ResultNonlinearTemperatureEffect,
    ResultThermal,
)
from moapy.plugins.temperature_gradient.eurocode.data_input import (
    NonlinearTemperatureInput,
    SurfaceType,
)
from moapy.plugins.temperature_gradient.eurocode.data_pre import (
    CompositeSection,
)
from moapy.plugins.temperature_gradient.section_properties import section_calculator, section_dimension


def calc_section_temperature_gradient(
    outer, inner, slab, g_thermal, s_thermal, g_elastic, s_elastic, group, surf_thick
):
    # Calculate the section properties
    sec_prop = section_calculator(outer, inner, slab, g_elastic, s_elastic)
    sec_dim = section_dimension(outer, inner, slab)

    slab_depth = sec_dim["slab_thick"]
    sect_height = sec_dim["height"]

    # print section calculation results
    # preprocess_result_print(outer, inner, slab, sec_prop, sec_dim)

    # Calculate the temperature distribution
    inf_point, inf_temp_h, inf_temp_c, point_h, temp_h, point_c, temp_c = (
        interpolate_temperature(group, sect_height, surf_thick, slab_depth)
    )

    # print temperature distribution results
    # plot_graphs("Steel Box", outer, inner, slab, point_h, temp_h, point_c, temp_c)

    # Calculate the self equilibrating stress
    self_eq_stress = self_equilibrating_stress(
        outer,
        inner,
        slab,
        g_thermal,
        s_thermal,
        g_elastic,
        s_elastic,
        sec_prop,
        sec_dim,
        inf_point,
        inf_temp_h,
        inf_temp_c,
    )
    out_points = [
        Point(
            x=Length(value=xv, unit=enUnitLength.MM),
            y=Length(value=yv, unit=enUnitLength.MM),
        )
        for xv, yv in zip(outer[0], outer[1])
    ]
    inner_points = [
        [
            Point(
                x=Length(value=xv, unit=enUnitLength.MM),
                y=Length(value=yv, unit=enUnitLength.MM),
            )
            for xv, yv in zip(inner[0], inner[1])
        ]
    ]
    heating = ResultThermal(
        y=list(
            Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[0][0]["y"]
        ),
        z=list(
            Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[0][0]["z"]
        ),
        temp=list(
            Temperature(value=xv, unit=enUnitTemperature.Celsius)
            for xv in self_eq_stress[0][0]["t"]
        ),
        stress=list(
            Stress(value=xv, unit=enUnitStress.MPa) for xv in self_eq_stress[0][0]["s"]
        ),
    )
    cooling = ResultThermal(
        y=list(
            Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[1][0]["y"]
        ),
        z=list(
            Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[1][0]["z"]
        ),
        temp=list(
            Temperature(value=xv, unit=enUnitTemperature.Celsius)
            for xv in self_eq_stress[1][0]["t"]
        ),
        stress=list(
            Stress(value=xv, unit=enUnitStress.MPa) for xv in self_eq_stress[1][0]["s"]
        ),
    )
    return ResultNonlinearTemperatureEffect(
        height=Length(value=sect_height, unit=enUnitLength.MM),
        outer=out_points,
        inner=inner_points,
        heating=heating,
        cooling=cooling,
        temperature_heating=[
            Point(
                x=Length(value=xv, unit=enUnitLength.MM),
                y=Length(value=yv, unit=enUnitLength.MM),
            )
            for xv, yv in zip(temp_h, point_h)
        ],
        temperature_cooling=[
            Point(
                x=Length(value=xv, unit=enUnitLength.MM),
                y=Length(value=yv, unit=enUnitLength.MM),
            )
            for xv, yv in zip(temp_c, point_c)
        ],
    )


def calc_nonlinear_temperature_effect(
    nonlinear_temperature_input: NonlinearTemperatureInput,
) -> ResultNonlinearTemperatureEffect:
    section = nonlinear_temperature_input.section_input.section
    surface = nonlinear_temperature_input.surfacing_input

    geometry = section.calc_section_coordinate()
    section_group = section.get_group()

    if isinstance(section, CompositeSection):
        girder_material = section.girder_section.material
        slab_material = section.slab_section.material
    else:
        girder_material = section.material
        slab_material = section.material

    match surface.surfacing_type:
        case SurfaceType.UNSURFACED | SurfaceType.WATERPROOFED:
            surface_thickness = surface.surfacing_type
        case SurfaceType.THICKNESS:
            surface_thickness = surface.surfacing_thickness.value
        case _:
            raise ValueError(f"Invalid surfacing_type: {surface.surfacing_type}")

    return calc_section_temperature_gradient(
        outer=geometry.outer,
        inner=geometry.inner,
        slab=geometry.comp,
        g_thermal=girder_material.thermal_expansion.value,
        s_thermal=slab_material.thermal_expansion.value,
        g_elastic=girder_material.elastic_modulus.value,
        s_elastic=slab_material.elastic_modulus.value,
        group=section_group,
        surf_thick=surface_thickness,
    )
