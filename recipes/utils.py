from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError
from fractions import Fraction
import pint 



def validate_ingredient_unit(value):
    ureg = pint.UnitRegistry()
    try:
        validate_unit = ureg(value)
    # except Exception as e:
    #     raise ValidationError(f"{e}")
    except Exception:
        raise ValidationError(f"{value} is not a unit measurement!")
    

def string_to_float(value):
    return value

def number_str_to_float(amount_str:str) -> (any, bool):
    """
    Take in an amount string to return float (if possible).
    
    Valid string returns:
    Float
    Boolean -> True

    Invalid string Returns
    Original String
    Boolean -> False
    
    Examples:
    1 1/2 -> 1.5, True
    32 -> 32.0, True
    Abc -> Abc, False
    """
    success = False
    number_as_float = amount_str
    try:
        number_as_float = float(sum(Fraction(s) for s in f"{amount_str}".split()))
    except:
        pass
    if isinstance(number_as_float, float):
        success = True
    return number_as_float, success