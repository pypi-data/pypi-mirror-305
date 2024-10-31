# Django Custom Commands

A Django package which allows specifying custom paths to load managenent commands from. This allows loading management commands which are not in Django apps.

## Installation

```bash
pip install django-custom-commands
```

## Usage

There's two things you need to do to use this package:
1. Import `call_command`, `get_commands` and `execute_from_command_line` from `django_custom_commands.management` instead of `django.core.management`.
2. Define a `CUSTOM_COMMAND_LOCATIONS` setting in your settings.

The `CUSTOM_COMMAND_LOCATIONS` should be a list of strings, where each string points to a module where commands can appear. The string should be a dotted path, similar to how apps are defined. The package will then try to load commands from `.management.commands` in those modules. For example if you have a command in `src.demo.management.commands`, but you can't/don't want to make `src.demo` a Django app, you would configure `CUSTOM_COMMAND_LOCATIONS = ["src.demo"]`.

## Running tests

```bash
poetry run pytest
```
