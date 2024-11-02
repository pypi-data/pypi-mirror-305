---
gitea: none
include_toc: true
---
# dictionaries/rougail/00-base.yml

```yaml
---
version: '1.1'
general:  # a family
  int:
    description: a first number
    type: number
    validators:
      - type: jinja
        jinja: |
          {% if _.int == int2 %}
          int and int2 must be different
          {% endif %}
        params:
          int2:
            type: variable
            variable: _.int2
            optional: true
        description: int and int2 must be different
      - type: jinja
        jinja: |
          {% if _.int == int3 %}
          int and int3 must be different
          {% endif %}
        params:
          int3:
            type: variable
            variable: _.int3
            optional: true
        description: int and int3 must be different
  int2: 1  # a second number
```
# Variables for "rougail"

## a family

`basic`

| Variable&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **rougail.general.int**<br/>[`number`](https://rougail.readthedocs.io/en/latest/variable.html#variables-types) `basic` `mandatory`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | A first number.<br/>**Validators**:<br/>- int and int2 must be different.<br/>- int and int3 must be different.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **rougail.general.int2**<br/>[`number`](https://rougail.readthedocs.io/en/latest/variable.html#variables-types) `standard` `mandatory`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | A second number.<br/>**Default**: 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |


# Example with mandatory variables not filled in

```yaml
---
rougail:
  general:
    int: 42
```
# Example with all variables modifiable

```yaml
---
rougail:
  general:
    int: 42
    int2: 1
```
