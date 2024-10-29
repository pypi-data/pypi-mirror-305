from typing import Sequence, Tuple

import ons_metadata_validation.validation._validation_checks as vc
from ons_metadata_validation.validation._validation_constants import (
    STRING_HYGIENE_CHECKS,
)
from ons_metadata_validation.validation._validation_utils import (
    validate_field,
)

######################
"""Dataset Series"""
######################


def validate_DatasetSeries_dataset_series_name(values: Sequence) -> Tuple:
    hard_checks = [
        vc.must_be_alphanumeric_with_spaces,
        vc.must_not_start_with_digit,
        vc.must_be_within_length_1024,
        *STRING_HYGIENE_CHECKS,
    ]
    return validate_field(values, hard_checks)


def validate_DatasetSeries_google_cloud_platform_bigquery_table_name(
    values: Sequence,
) -> Tuple:
    hard_checks = [
        vc.must_be_alphanumeric_with_underscores,
        vc.must_be_all_lower_case,
        vc.must_not_start_with_digit,
        vc.must_be_within_length_30,
        *STRING_HYGIENE_CHECKS,
    ]
    return validate_field(values, hard_checks)


def validate_DatasetSeries_description(values: Sequence) -> Tuple:
    hard_checks = [vc.must_be_within_length_1800, *STRING_HYGIENE_CHECKS]
    soft_checks = [
        vc.must_end_with_a_full_stop_or_question_mark,
        vc.must_have_no_obvious_acronyms,
    ]  # explicit req on back office, implicit here and dataset file?
    return validate_field(values, hard_checks, soft_checks)


def validate_DatasetSeries_reference_period(values: Sequence) -> Tuple:
    hard_checks = [
        vc.must_be_in_long_date_format,
        vc.must_have_no_leading_apostrophe,
        *STRING_HYGIENE_CHECKS,
    ]
    soft_checks = [vc.must_have_long_date_in_plausible_range]
    return validate_field(values, hard_checks, soft_checks)


# mandatory, enum, no other checks
# TODO geographic_coverage = named locations
def validate_DatasetSeries_geographic_coverage(values: Sequence) -> Tuple:
    soft_checks = [*STRING_HYGIENE_CHECKS]
    return validate_field(values, soft_checks=soft_checks)


# mandatory, enum, no other checks
def validate_DatasetSeries_frequency(values: Sequence) -> Tuple:
    return validate_field(values)


# mandatory, enum, no other checks
def validate_DatasetSeries_supply_type(values: Sequence) -> Tuple:
    return validate_field(values)


# no checks
def validate_DatasetSeries_wave_numbertime_period_covered_survey_only(
    values: Sequence,
) -> Tuple:
    soft_checks = [*STRING_HYGIENE_CHECKS]
    return validate_field(values, soft_checks=soft_checks)


def validate_DatasetSeries_links_to_online_documentation_and_other_useful_materials(
    values: Sequence,
) -> Tuple:
    hard_checks = [*STRING_HYGIENE_CHECKS]
    soft_checks = [vc.must_be_valid_url]
    return validate_field(values, hard_checks, soft_checks)
