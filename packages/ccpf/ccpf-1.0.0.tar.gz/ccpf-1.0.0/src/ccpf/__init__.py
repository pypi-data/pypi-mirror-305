import native as _native


class CPFInvalidFormat(Exception):
    """
    Raised when CPF is not in a valid format.
    The CPF itself may still be invalid if this is not raised.
    """
    def __init__(self, cpf):
        super(Exception, self).__init__(cpf)


def validate(cpf: str) -> bool:
    """
    Validate if a string is a valid CPF.
    Works for masked and unmasked CPFs.
    """
    return _native.validate(cpf)


def generate() -> str:
    """
    Generate a random valid unmasked CPF.
    """
    return _native.generate()


def has_mask(cpf: str) -> bool:
    """
    Return wheter or not the given CPF is masked.
    If CPF format is invalid, it will raise a `CPFInvalidFormat` exception.
    """
    try:
        return _native.has_mask(cpf)
    except _native.CPFInvalidFormat:
        raise CPFInvalidFormat(cpf)


def mask(cpf: str) -> str:
    """
    Return the masked version of the given CPF.
    If the CPF is already masked, just return it.
    If CPF format is invalid, it will raise a `CPFInvalidFormat` exception.
    """
    try:
        return _native.mask(cpf)
    except _native.CPFInvalidFormat:
        raise CPFInvalidFormat(cpf)


def unmask(cpf: str) -> str:
    """
    Return unmasked version of the given CPF.
    If the CPF is already unmasked, just return it.
    If CPF format is invalid, it will raise a `CPFInvalidFormat` exception.
    """
    try:
        return _native.unmask(cpf)
    except _native.CPFInvalidFormat:
        raise CPFInvalidFormat(cpf)
