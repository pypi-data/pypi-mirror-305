import pytest

from .tool.transformer import ExampleTransformer
from . import available
from .types import value_from_dict_for_app


def test_available():
    assert len(available) > 0


@pytest.mark.parametrize("title, input_data", available.items())
def test_entries(title, input_data):
    assert len(input_data.examples) > 0


@pytest.mark.parametrize("title, input_data", available.items())
async def test_entries_support_result(title, input_data):
    example_transformer = ExampleTransformer()
    if input_data.support_table:
        func = value_from_dict_for_app(input_data.support_result, "activity")

        for ex in input_data.examples:
            activity = await example_transformer.create_activity(ex)

            result = func(activity)

            assert isinstance(result, str)


@pytest.mark.parametrize("title, input_data", available.items())
async def test_entries_support_result_on_None(title, input_data):
    if input_data.support_table:
        func = value_from_dict_for_app(input_data.support_result, "mastodon")

        for ex in input_data.examples:
            result = func(None)

            assert result == "❌"


@pytest.mark.parametrize("title, input_data", available.items())
async def test_entries_detail_extractor(title, input_data):
    example_transformer = ExampleTransformer()
    if input_data.detail_table:
        func = value_from_dict_for_app(input_data.detail_extractor, "activity")

        for ex in input_data.examples:
            activity = await example_transformer.create_activity(ex)

            result = func(activity)

            assert isinstance(result, list)


@pytest.mark.parametrize("title, input_data", available.items())
async def test_entries_detail_on_none_and_empty_dict(title, input_data):
    if input_data.detail_table:
        for app in input_data.detail_extractor.keys():
            func = value_from_dict_for_app(input_data.detail_extractor, app)

            func(None)
            func({})
