# ninja-bear-distributor-fs
This [ninja-bear](https://pypi.org/project/ninja-bear) plugin provides the possibility to distribute generated files to other locations on the file system.

```yaml
distributors:  # Specifies which distributor plugins to load.
  # -------------------------------------------------------------------------
  # Property description for ninja-bear-distributor-fs.
  #
  # distributor    (required): ninja-bear-distributor-fs
  # as             (required): Specifies how the distributor will be referenced
  #                            at the language level (in this case fs).
  # paths          (required): Path or list of paths (relative or absolute) to
  #                            copy the configs to.
  # create_parents (optional): If true, parent directories will be created if
  #                            they don't exist.
  # ignore         (optional): If true, the section gets ignored.
  # -------------------------------------------------------------------------
  - distributor: ninja-bear-distributor-fs
    as: fs
    paths:
      - ../configs/configs-1
      - ../configs/configs-2
    create_parents: true

languages:
  - language: ninja-bear-language-examplescript
    distributors:  # Specifies which distributor plugins to use for the language.
      - fs

properties:
  - type: bool
    name: myBoolean
    value: true

  - type: int
    name: myInteger
    value: 142

  - type: float
    name: myFloat
    value: 322f  # Float with float specifier. However, an additional specifier (f) is not required and will be trimmed.

  - type: float
    name: myCombinedFloat
    value: ${myInteger} * ${myFloat}  # Number and boolean combinations get evaluated during the dump process.

  - type: double
    name: myDouble
    value: 233.9

  - type: string
    name: myString
    value: Hello World
    hidden: true  # If a property should act as a helper but should not be written to the generated file, it must be marked as 'hidden'.

  - type: regex
    name: myRegex
    value: Test Reg(E|e)x
    comment: Just another RegEx.  # Variables can be described using the comment property.

  - type: string
    name: mySubstitutedString
    value: Sometimes I just want to scream ${myString}!  # To use the value of another property, simply use its name with ${}. E.g., ${myString}.
```
