import ccpf

NUM_TESTS = 100


def test_cpf():
    for i in range(NUM_TESTS):
        try:
            cpf = ccpf.generate()
            assert ccpf.validate(cpf)
            assert not ccpf.has_mask(cpf)
            masked = ccpf.mask(cpf)
            assert ccpf.has_mask(masked)
            assert ccpf.unmask(ccpf.mask(cpf)) == cpf
            cpf = str(int(cpf) + 1)
            assert not ccpf.validate(cpf)
        except ccpf.CPFInvalidFormat:
            assert False


def test_example_generate():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert ccpf.validate(cpf)


def test_example_validate():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert ccpf.validate(cpf)


def test_example_has_mask():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert not ccpf.has_mask(cpf)

    invalid_cpf_with_right_format = '12345678901'
    assert not ccpf.validate(invalid_cpf_with_right_format)
    error = False
    try:
        ccpf.has_mask(invalid_cpf_with_right_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert not error

    invalid_cpf_with_right_format = '123.456.789-01'
    assert not ccpf.validate(invalid_cpf_with_right_format)
    error = False
    try:
        ccpf.has_mask(invalid_cpf_with_right_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert not error

    cpf_with_wrong_format = 'thisisclearlynotinthecpfformat'
    assert not ccpf.validate(cpf_with_wrong_format)
    error = False
    try:
        ccpf.has_mask(cpf_with_wrong_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert error


def test_example_mask():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert not ccpf.has_mask(cpf)
        masked = ccpf.mask(cpf)
        assert ccpf.has_mask(masked)
        masked2 = ccpf.mask(masked)
        assert ccpf.has_mask(masked2)

    invalid_cpf_with_right_format = '12345678901'
    assert not ccpf.validate(invalid_cpf_with_right_format)
    error = False
    try:
        ccpf.mask(invalid_cpf_with_right_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert not error

    invalid_cpf_with_right_format = '123.456.789-01'
    assert not ccpf.validate(invalid_cpf_with_right_format)
    error = False
    try:
        ccpf.mask(invalid_cpf_with_right_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert not error

    cpf_with_wrong_format = 'thisisclearlynotinthecpfformat'
    assert not ccpf.validate(cpf_with_wrong_format)
    error = False
    try:
        ccpf.mask(cpf_with_wrong_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert error


def test_example_unmask():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert not ccpf.has_mask(cpf)
        unmasked = ccpf.unmask(cpf)
        assert not ccpf.has_mask(unmasked)
        masked = ccpf.mask(unmasked)
        assert ccpf.has_mask(masked)
        unmasked2 = ccpf.unmask(masked)
        assert not ccpf.has_mask(unmasked2)

    invalid_cpf_with_right_format = '12345678901'
    assert not ccpf.validate(invalid_cpf_with_right_format)
    error = False
    try:
        ccpf.unmask(invalid_cpf_with_right_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert not error

    invalid_cpf_with_right_format = '123.456.789-01'
    assert not ccpf.validate(invalid_cpf_with_right_format)
    error = False
    try:
        ccpf.unmask(invalid_cpf_with_right_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert not error

    cpf_with_wrong_format = 'thisisclearlynotinthecpfformat'
    assert not ccpf.validate(cpf_with_wrong_format)
    error = False
    try:
        ccpf.unmask(cpf_with_wrong_format)
    except ccpf.CPFInvalidFormat:
        error = True
    finally:
        assert error
