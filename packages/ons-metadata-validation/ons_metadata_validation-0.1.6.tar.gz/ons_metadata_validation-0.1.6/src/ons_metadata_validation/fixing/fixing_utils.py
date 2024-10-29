import logging
from datetime import datetime

import pandas as pd
from openpyxl import Workbook

import ons_metadata_validation.fixing.string_fixes as sf
from ons_metadata_validation.utils.logger import (
    compress_logging_value,
)

logger = logging.getLogger()


FIX_FUNCTIONS = {
    "must_not_start_with_whitespace": sf.remove_whitespace,
    "must_not_end_with_whitespace": sf.remove_whitespace,
    "must_end_with_a_full_stop_or_question_mark": sf.add_full_stop,
    "must_not_contain_double_spaces": sf.remove_multiple_spaces,
    "must_be_alphanumeric_only": sf.replace_non_breaking_space,
    "must_be_alphanumeric_with_spaces": sf.replace_non_breaking_space,
    "must_be_alphanumeric_with_underscores": sf.replace_non_breaking_space,
    "must_be_alphanumeric_with_spaces_or_underscores": sf.replace_non_breaking_space,
    "must_be_alphanumeric_with_dashes": sf.replace_non_breaking_space,
}


def fix_main(wb: Workbook, fail_df: pd.DataFrame, filename: str):
    """main function for fixing metadata issues

    Args:
        wb (Workbook): the workbook to be modified (passed by reference)
        fails_dict (Dict[str, pd.DataFrame]): hard and soft fail dfs in a dict
        filename (str): the original filename of the metadata
    """
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    fails = fail_df.to_dict("records")
    if not all(map(lambda fail: fix_fail(wb, fail), fails)):
        msg = "not all correction functions successful"
        logger.error(msg)
        print(msg)

    validation_datetime = datetime.now().strftime("%Y%m%d_%H%M")
    wb.save(filename.replace(".xlsx", f"_FIXED_{validation_datetime}.xlsx"))


def fix_fail(wb: Workbook, fail: dict) -> bool:
    """fixes a single fail, modifies workbook in place

    Args:
        wb (Workbook): the workbook to be modified (passed by reference)
        fail (dict): a dict with fail

    Returns:
        bool: True if all refs are corrected for listed reasons
    """

    if fail["reason"] not in FIX_FUNCTIONS or fail["cell_ref"] == "":
        return True
    try:
        wb[fail["tab"]][fail["cell_ref"]].value = FIX_FUNCTIONS[
            fail["reason"]
        ](fail["value"])
        return True
    except Exception as e:
        logger.error(e)
        return False
