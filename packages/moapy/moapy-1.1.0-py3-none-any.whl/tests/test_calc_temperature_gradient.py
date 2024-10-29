from moapy.plugins.temperature_gradient.calc_nonlinear_temperature_effect import (
    calc_nonlinear_temperature_effect,
)
import json
from moapy.plugins.temperature_gradient.section.data_input import (
    NonlinearTemperatureInput,
)
from moapy.plugins.temperature_gradient.section.data_post import (
    ResultNonlinearTemperatureEffect,
)
from moapy.plugins.temperature_gradient.section.data_pre import (
    CompositeBoxGirderSection,
    CompositeIGirderSection,
    CompositeTubSection,
    PSC1CellSection,
    PSC2CellSection,
    PSC_ISection,
    PSC_TSection,
    SteelBoxGirderSection,
    SteelIGirderSection,
)


BASE_SECTION_RESULT_DIR = "./tests/calc_temperature_gradient/data/"


def get_json_data(file_path):
    # if file_path is relative path, convert to absolute path
    if not file_path.startswith("/"):
        file_path = BASE_SECTION_RESULT_DIR + file_path

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_result(file_path):
    # if file_path is relative path, convert to absolute path
    if not file_path.startswith("/"):
        file_path = BASE_SECTION_RESULT_DIR + file_path

    with open(file_path, "r") as f:
        model = ResultNonlinearTemperatureEffect.model_validate_json(f.read())
        return model


def test_calc_temperature_gradient_SteelBoxGirderSection():
    input_data = get_json_data("./input/steel_box_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(
        nonlinear_temperature_input.section_input.section, SteelBoxGirderSection
    )

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("steel_box_example.json")
    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer


def test_calc_temperature_gradient_SteelIGirderSection():
    input_data = get_json_data("./input/steel_I_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(
        nonlinear_temperature_input.section_input.section, SteelIGirderSection
    )

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("steel_I_example.json")

    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer


def test_calc_temperature_gradient_CompositeSteelBoxSection():
    input_data = get_json_data("./input/composite_steel_box_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(
        nonlinear_temperature_input.section_input.section, CompositeBoxGirderSection
    )

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("composite_steel_box_example.json")

    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer


def test_calc_temperature_gradient_CompositeIGirderSection():
    input_data = get_json_data("./input/composite_steel_I_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(
        nonlinear_temperature_input.section_input.section, CompositeIGirderSection
    )

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("composite_steel_I_example.json")

    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer


def test_calc_temperature_gradient_CompositeTubGirderSection():
    input_data = get_json_data("./input/composite_steel_tub_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(
        nonlinear_temperature_input.section_input.section, CompositeTubSection
    )

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("composite_steel_tub_example.json")

    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer


def test_calc_temperature_gradient_PSC1CellSection():
    input_data = get_json_data("./input/psc_1_cell_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(
        nonlinear_temperature_input.section_input.section, PSC1CellSection
    )

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("psc_1_cell_example.json")

    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer


def test_calc_temperature_gradient_PSC2CellSection():
    input_data = get_json_data("./input/psc_2_cell_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(
        nonlinear_temperature_input.section_input.section, PSC2CellSection
    )

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("psc_2_cell_example.json")

    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer


def test_calc_temperature_gradient_PSC_ISection():
    input_data = get_json_data("./input/psc_I_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(nonlinear_temperature_input.section_input.section, PSC_ISection)

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("psc_I_example.json")

    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer


def test_calc_temperature_gradient_PSC_TSection():
    input_data = get_json_data("./input/psc_T_input.json")
    nonlinear_temperature_input = NonlinearTemperatureInput.model_validate(
        input_data["nonlinear_temperature_input"]
    )
    assert isinstance(nonlinear_temperature_input.section_input.section, PSC_TSection)

    res = calc_nonlinear_temperature_effect(nonlinear_temperature_input)
    expected = get_result("psc_T_example.json")

    assert res.heating == expected.heating
    assert res.temp_heating == expected.temp_heating
    assert res.cooling == expected.cooling
    assert res.temp_cooling == expected.temp_cooling
    assert res.inner == expected.inner
    assert res.outer == expected.outer
