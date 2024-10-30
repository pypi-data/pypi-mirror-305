from typing import Sequence, Tuple

import ons_metadata_validation.validation._validation_checks as vc
from ons_metadata_validation.validation._validation_constants import (
    STRING_HYGIENE_CHECKS,
)
from ons_metadata_validation.validation._validation_utils import (
    validate_field,
)
from ons_metadata_validation.validation.dataset_series_validations import (
    validate_DatasetSeries_google_cloud_platform_bigquery_table_name,
    validate_DatasetSeries_reference_period,
)


def validate_DatasetFile_google_cloud_platform_bigquery_table_name(
    values: Sequence,
) -> Tuple:
    return validate_DatasetSeries_google_cloud_platform_bigquery_table_name(
        values
    )


def validate_DatasetFile_file_path_and_name(values: Sequence) -> Tuple:
    hard_checks = [vc.must_not_include_backslashes, *STRING_HYGIENE_CHECKS]
    soft_checks = [
        vc.must_have_timestamp_in_filename,
        vc.must_have_plausible_filepath,  # 20240808 - E: moving this to soft checks until its less strict
    ]
    return validate_field(values, hard_checks, soft_checks)


# mandatory, enum, no other checks
def validate_DatasetFile_file_format(values: Sequence) -> Tuple:
    return validate_field(values)


# mandatory, enum, no other checks
def validate_DatasetFile_column_seperator(values: Sequence) -> Tuple:
    return validate_field(values)


# not sure if there's a reasonable list of possible valid string identifiers?
def validate_DatasetFile_string_identifier(values: Sequence) -> Tuple:
    soft_checks = [*STRING_HYGIENE_CHECKS]
    return validate_field(values, soft_checks=soft_checks)


def validate_DatasetFile_file_description(values: Sequence) -> Tuple:
    soft_checks = [*STRING_HYGIENE_CHECKS]
    return validate_field(values, soft_checks=soft_checks)


def validate_DatasetFile_reference_period(values: Sequence) -> Tuple:
    return validate_DatasetSeries_reference_period(values)


# don't think there's anything we can usefully check, since the plausible range
# depends on the unit - FG
def validate_DatasetFile_file_size(values: Sequence) -> Tuple:
    return validate_field(values)


# no enumeration / set list of options yet, so this is all we can do
def validate_DatasetFile_file_size_unit(values: Sequence) -> Tuple:
    hard_checks = [
        vc.must_have_intelligible_file_size_unit,
        *STRING_HYGIENE_CHECKS,
    ]
    return validate_field(values, hard_checks)


# mandatory, enum, no other checks
def validate_DatasetFile_is_code_list(values: Sequence) -> Tuple:
    return validate_field(values)


def validate_DatasetFile_number_of_records(values: Sequence) -> Tuple:
    hard_checks = [vc.must_be_0_or_greater]
    return validate_field(values, hard_checks)


# mandatory, enum, no other checks
def validate_DatasetFile_is_this_file_one_of_a_sequence_to_be_appended_back_together(
    values: Sequence,
) -> Tuple:
    return validate_field(values)


def validate_DatasetFile_number_of_header_rows(values: Sequence) -> Tuple:
    hard_checks = [vc.must_be_0_or_greater]
    return validate_field(values, hard_checks)


def validate_DatasetFile_number_of_footer_rows(values: Sequence) -> Tuple:
    hard_checks = [vc.must_be_0_or_greater]
    return validate_field(values, hard_checks)


def validate_DatasetFile_character_encoding(values: Sequence) -> Tuple:
    hard_checks = [vc.must_be_valid_encoding, *STRING_HYGIENE_CHECKS]
    return validate_field(values, hard_checks)


def validate_DatasetFile_hash_value_for_checksum(values: Sequence) -> Tuple:
    hard_checks = [
        vc.must_be_alphanumeric_only,
        vc.must_be_exactly_32_chars,
        *STRING_HYGIENE_CHECKS,
    ]
    return validate_field(values, hard_checks)


# TODO: could enforce starting with a capital and ending with a full stop,
# So, cross reference with what TISS are doing
def validate_DatasetFile_notes(values: Sequence) -> Tuple:

    soft_checks = [*STRING_HYGIENE_CHECKS, vc.must_be_within_length_1800]
    return validate_field(values, soft_checks=soft_checks)
