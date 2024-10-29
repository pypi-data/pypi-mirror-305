import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple

# short, permissive url regex courtesy of gskinner at https://regexr.com/3e6m0
# Update 20/9/24: Sharepoint URLs can contain parentheses after the domain
URL_PATTERN = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/=\(\)]*)"


def _regex_search(pattern: str, item: str) -> bool:
    if not isinstance(item, str):
        raise TypeError(
            f"_regex_search() expected type str but got {type(item)}"
        )
    return bool(re.search(pattern, item))


def _regex_match(pattern: str, item: str) -> bool:
    if not isinstance(item, str):
        raise TypeError(
            f"_regex_match() expected type str but got {type(item)}"
        )
    return bool(re.match(pattern, item))


def validate_field(
    values: Sequence,
    hard_checks: Optional[list] = None,
    soft_checks: Optional[list] = None,
) -> Tuple[Dict[str, str], Dict[str, str]]:
    hard_checks = hard_checks or []
    soft_checks = soft_checks or []
    return check_fails(values, hard_checks), check_fails(values, soft_checks)


def check_fails(values: Sequence, checks: List[Callable]) -> Dict[str, str]:
    check_failures = {}

    # we now convert to set earlier so can just iterate over
    # values here
    for val in values:
        fails = [
            f"{check_pass.__name__}. "
            for check_pass in checks
            if not check_pass(val)
        ]
        if fails:
            if val not in check_failures:
                check_failures[val] = fails
            else:
                check_failures[val].append(fails)
    return check_failures
