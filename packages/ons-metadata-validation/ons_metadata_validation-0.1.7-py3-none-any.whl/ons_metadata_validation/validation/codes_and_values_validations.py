from typing import Sequence, Tuple

from ons_metadata_validation.validation._validation_utils import (
    validate_field,
)
from ons_metadata_validation.validation.dataset_file_validations import (
    validate_DatasetFile_notes,
)
from ons_metadata_validation.validation.dataset_series_validations import (
    validate_DatasetSeries_google_cloud_platform_bigquery_table_name,
)
from ons_metadata_validation.validation.variables_validations import (
    validate_Variables_variable_name,
)


def validate_CodesandValues_google_cloud_platform_bigquery_table_name(
    values: Sequence,
) -> Tuple:
    return validate_DatasetSeries_google_cloud_platform_bigquery_table_name(
        values
    )


def validate_CodesandValues_variable_name(values: Sequence) -> Tuple:
    return validate_Variables_variable_name(values)


# no checks
def validate_CodesandValues_key(values: Sequence) -> Tuple:
    return validate_field(values)


# no checks
def validate_CodesandValues_value(values: Sequence) -> Tuple:
    return validate_field(values)


def validate_CodesandValues_notes(values: Sequence) -> Tuple:
    return validate_DatasetFile_notes(values)
