from typing import Any
from fastapi import APIRouter, Body

from valid_password.schemas.rule import RuleRequest
from valid_password.core.rules import is_valid_rule


router = APIRouter()


@router.post(
    "/verify",
    status_code=200,
)
def checker(check: RuleRequest = Body(..., description="")) -> Any:
    """
    Given a password and a pre-defined set of rules, check whether or not the password follows the given set of rules.
    """
    request_rules = check.dict()
    secret = request_rules["password"]
    no_match = []
    verify = True

    for rule in request_rules["rules"]:
        ans = is_valid_rule(secret, rule["value"], rule["rule"])
        if not ans:
            no_match.append(rule["rule"])
            verify = False

    return {"verify": verify, "noMatch": no_match}
