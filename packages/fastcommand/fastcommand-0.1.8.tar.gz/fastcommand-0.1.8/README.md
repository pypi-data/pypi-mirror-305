# fastcommand

[![build](https://github.com/jbmorley/fastcommand/actions/workflows/build.yaml/badge.svg)](https://github.com/jbmorley/fastcommand/actions/workflows/build.yaml)

Python module for defining multi-command cli programs

## Description

The `fastcommand` module is a lightweight wrapper over `argparse` which aims to make it easier to write multi-command cli programs and utilities. It does so by providing convenience decorators that allow for quickly defining sub-commands.

## Usage

```python
import fastcommand


@fastcommand.command("hello", help="say hello")
def command_hello(options):
    print("Hello, World!")


@fastcommand.command("goodbye", help="say goodbye", arguments=[
    fastcommand.Argument("name"),
    fastcommand.Argument("--wave", "-w", action="store_true", default=False)
])
def command_goodbye(options):
    print(f"Goodbye, {options.name}!")
    if options.wave:
        print("👋")


def main():
    cli = fastcommand.CommandParser(description="Simple fastcommand example.")
    cli.use_logging(format="[%(levelname)s] %(message)s")
    cli.run()


if __name__ == "__main__":
    main()
```
