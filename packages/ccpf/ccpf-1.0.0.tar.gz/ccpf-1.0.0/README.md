## ccpf

A CPF (brazilian register numbers for persons) library that can:
* Validate CPFs
* Generate random CPFs
* Apply and remove masks from CPFs
* Check if CPFs are masked

### Install

Just do `pip3 install ccpf` and you are good to go.

### How to use

After `import`ing `ccpf` you can:

* `generate()` - Generate a random valid unmasked CPF.

```
import ccpf
cpf = ccpf.generate()
assert ccpf.validate(cpf)
```

* `validate(cpf)` - Validate if a string is a valid CPF. Works for masked and unmasked CPFs.

```
import ccpf
cpf = ccpf.generate()
assert ccpf.validate(cpf)
```

* `has_mask(cpf)` - Return wheter or not the given CPF is masked. If CPF format is invalid, it will raise a `CPFInvalidFormat` exception.

```
import ccpf
cpf = ccpf.generate()
assert not ccpf.has_mask(cpf)
```

* `mask(cpf)` - Return the masked version of the given CPF. If the CPF is already masked, just return it. If CPF format is invalid, it will raise a `CPFInvalidFormat` exception.

```
import ccpf
cpf = ccpf.generate()
assert not ccpf.has_mask(cpf)
masked = ccpf.mask(cpf)
assert ccpf.has_mask(masked)
masked2 = ccpf.mask(masked)
assert ccpf.has_mask(masked2)
```

* `unmask(cpf)` - Return unmasked version of the given CPF. If the CPF is already unmasked, just return it. If CPF format is invalid, it will raise a `CPFInvalidFormat` exception.

```
import ccpf
cpf = ccpf.generate()
assert not ccpf.has_mask(cpf)
unmasked = ccpf.unmask(cpf)
assert not ccpf.has_mask(unmasked)
masked = ccpf.mask(unmasked)
assert ccpf.has_mask(masked)
unmasked2 = ccpf.unmask(masked)
assert not ccpf.has_mask(unmasked2)
```

#### `CPFInvalidFormat`

A CPF may have a valid _format_, but be invalid:

* without mask but invalid: 
```
invalid_cpf_with_right_format = '12345678901'
assert not ccpf.validate(invalid_cpf_with_right_format)
error = False
try:
    ccpf.unmask(invalid_cpf_with_right_format)
except ccpf.CPFInvalidFormat:
    error = True
finally:
    assert not error
```
* with mask but invalid.
```
invalid_cpf_with_right_format = '123.456.789-01'
assert not ccpf.validate(invalid_cpf_with_right_format)
error = False
try:
    ccpf.unmask(invalid_cpf_with_right_format)
except ccpf.CPFInvalidFormat:
    error = True
finally:
    assert not error
```

* `CPFInvalidFormat` will be raised when the format is invalid. It does not say whether the CPF itself is invalid or not.

```
cpf_with_wrong_format = 'thisisclearlynotinthecpfformat'
assert not ccpf.validate(cpf_with_wrong_format)
error = False
try:
    ccpf.unmask(cpf_with_wrong_format)
except ccpf.CPFInvalidFormat:
    error = True
finally:
    assert error
```

### Run tests

Just execute `tox` by calling it: 

```
tox
```
