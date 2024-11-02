---
gitea: none
include_toc: true
---
# dictionaries/rougail/00-base.yml

```yaml
---
version: '1.1'
my_family:
  _type: family
  _description: This is a great family
  _help: This is a great family
  _mode: basic
  _hidden: true
  _disabled: true
  type:
    description: a type family
    type: family
    my_variable:
  description:
    description: This is a other great family
    my_variable:
  help:
    description: a help family
    help: This is a other great family
    my_variable:
  mode:
    description: a mode family
    mode: advanced
    my_variable:
      mandatory: false
  hidden:
    description: an hidden family
    hidden: true
    my_variable:
  disabled:
    description: an disabled family
    disabled: true
    my_variable:
```
