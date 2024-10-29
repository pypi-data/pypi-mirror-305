from typing import Sequence, Tuple

import ons_metadata_validation.validation._validation_checks as vc
from ons_metadata_validation.validation._validation_constants import (
    STRING_HYGIENE_CHECKS,
)
from ons_metadata_validation.validation._validation_utils import (
    validate_field,
)

######################
"""Dataset Resource"""
######################


def validate_DatasetResource_dataset_resource_name(values: Sequence) -> Tuple:
    hard_checks = [
        vc.must_be_alphanumeric_with_spaces,
        *STRING_HYGIENE_CHECKS,
    ]

    soft_checks = [
        vc.must_have_no_obvious_acronyms,
        vc.must_be_within_length_80,
    ]
    return validate_field(values, hard_checks, soft_checks)


def validate_DatasetResource_acronym(values: Sequence) -> Tuple:
    hard_checks = [*STRING_HYGIENE_CHECKS]
    soft_checks = [
        vc.must_have_no_full_stops_in_acronym,
        vc.must_not_include_spaces,
    ]  # we want one acronym only
    return validate_field(values, hard_checks, soft_checks)


# no checks
def validate_DatasetResource_significant_changes(values: Sequence) -> Tuple:
    soft_checks = [*STRING_HYGIENE_CHECKS]
    return validate_field(values, soft_checks=soft_checks)


def validate_DatasetResource_data_creator(values: Sequence) -> Tuple:
    hard_checks = [
        vc.must_not_include_apostrophes,  # issue ticket #8. Causes ingest fails.
        *STRING_HYGIENE_CHECKS,
    ]
    soft_checks = [
        vc.must_have_no_obvious_acronyms,
        vc.must_not_say_ONS,
        vc.must_not_say_office_of_national_statistics,
        vc.must_not_have_capitalised_for,
    ]
    return validate_field(values, hard_checks, soft_checks)


def validate_DatasetResource_data_contributors(values: Sequence) -> Tuple:
    return validate_DatasetResource_data_creator(values)


# no specific checks
def validate_DatasetResource_purpose_of_this_dataset_resource(
    values: Sequence,
) -> Tuple:
    soft_checks = [*STRING_HYGIENE_CHECKS]
    return validate_field(values, soft_checks=soft_checks)


def validate_DatasetResource_search_keywords(values: Sequence) -> Tuple:
    hard_checks = [*STRING_HYGIENE_CHECKS]
    soft_checks = [
        vc.must_not_include_pipes,
        vc.must_start_with_capital,
        vc.must_have_no_more_than_five_list_items,
        vc.must_have_caps_after_commas,
    ]
    return validate_field(values, hard_checks, soft_checks)


# enum only
def validate_DatasetResource_dataset_theme(values: Sequence) -> Tuple:
    return validate_field(values)


# TODO geographic_level = geographic category - e.g. LSOA (NOT AS AN ACRONYM THOUGH)
def validate_DatasetResource_geographic_level(values: Sequence) -> Tuple:
    soft_checks = [*STRING_HYGIENE_CHECKS]
    return validate_field(values, soft_checks=soft_checks)


def validate_DatasetResource_provenance(values: Sequence) -> Tuple:
    hard_checks = [*STRING_HYGIENE_CHECKS]
    soft_checks = [vc.must_not_be_option_from_dataset_resource_type]
    return validate_field(values, hard_checks, soft_checks)


# + contingent check for later: must match number of rows on corresponding sheet
def validate_DatasetResource_number_of_dataset_series(
    values: Sequence,
) -> Tuple:
    hard_checks = [vc.must_be_1_or_greater]
    return validate_field(values, hard_checks)


def validate_DatasetResource_number_of_structural_data_files(
    values: Sequence,
) -> Tuple:
    hard_checks = [vc.must_be_1_or_greater]
    return validate_field(values, hard_checks)


def validate_DatasetResource_date_of_completion(values: Sequence) -> Tuple:
    hard_checks = [
        vc.must_be_in_short_date_format,
        # vc.must_have_no_leading_apostrophe, # 20240808 - E: commenting out due to the leading apostrophe being necessary
        vc.must_have_leading_apostrophe,  # 20240909 - E+F: added
        *STRING_HYGIENE_CHECKS,
    ]
    soft_checks = [vc.must_have_short_date_in_plausible_range]
    return validate_field(values, hard_checks, soft_checks)


def validate_DatasetResource_name_and_email_of_individual_completing_this_template(
    values: Sequence,
) -> Tuple:
    hard_checks = [
        vc.must_contain_an_email_address,  # not pipeline breaking but we need the contact details of who filled in the template
        vc.must_have_comma_and_space,
        *STRING_HYGIENE_CHECKS,
    ]
    soft_checks = []
    return validate_field(values, hard_checks, soft_checks)


# enum only
def validate_DatasetResource_security_classification(
    values: Sequence,
) -> Tuple:
    return validate_field(values)


# enum only
def validate_DatasetResource_dataset_resource_type(values: Sequence) -> Tuple:
    return validate_field(values)


def validate_DatasetResource_number_of_non_structural_reference_files(
    values: Sequence,
) -> Tuple:
    hard_checks = [vc.must_be_0_or_greater]
    soft_checks = []
    return validate_field(values, hard_checks, soft_checks)


def validate_DatasetResource_number_of_code_list_files(
    values: Sequence,
) -> Tuple:
    hard_checks = [vc.must_be_0_or_greater]
    soft_checks = []
    return validate_field(values, hard_checks, soft_checks)
