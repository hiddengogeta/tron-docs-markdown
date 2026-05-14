

# Command line options [​](#command-line-options)

This section will describe every command available in the TronBox application.

## Usage [​](#usage)

All commands are in the following form:

Terminal

shell

```
tronbox <command> [options]
```

Passing no arguments is equivalent to `tronbox help`, which will display all commands and then exit.

## Commands [​](#commands)

### compile [​](#compile)

Compile source files of smart contracts.

Terminal

shell

```
tronbox compile [--all] [--quiet] [--evm]
```

Only contracts that have changed since the last compilation will be compiled if there is no –all. Options:

* `--all`: Compile all contracts instead of only the contracts that have changed since the last compilation.
* `--quiet`: Suppress all compilation output.
* `--evm`: Use EVM related configuration (Requires TronBox v4.0.0 or later).

### console [​](#console)

Run a console with contract abstractions and commands available.

Terminal

shell

```
tronbox console [--network <name>] [--evm]
```

An interface that interacts with contracts via the command line. In addition, many TronBox commands can be used in the console (without the `tronbox` prefix). Option:

* `--network <name>`: Specify the network to use. The network name must exist in the configuration.
* `--evm`: Use EVM related configuration (Requires TronBox v4.0.0 or later).

### deploy [​](#deploy)

An alias for `migrate`. Please see [Deploy contracts](/docs/guides/deploy-contracts).

### flatten [​](#flatten)

The built-in flatten task lets you combine the source code of multiple Solidity files.

Terminal

shell

```
tronbox flatten <file_path>
```

Options:

* `<file_path>`: The path to the file that needs flatten (must be required)

TIP

*NOTE: This feature requires TronBox v3.3.0 or later.*

### help [​](#help)

Display a list of all commands.

Terminal

shell

```
tronbox help
```

### init [​](#init)

Initialize a new (empty) TronBox project.

Terminal

shell

```
tronbox init
```

Create a new, empty TronBox project in the current working directory.

### migrate [​](#migrate)

Run migration files to deploy contracts.

Terminal

shell

```
tronbox migrate [--reset] [--f <number>] [--to <number>] [--network <name>] [--compile-all] [--evm]
```

This will run from the last completed migration unless otherwise specified. For more information, please see [Deploy contracts](/docs/guides/deploy-contracts).

Options:

* `--reset`: Run all migrations from the beginning, instead of running from the last completed migration.
* `--f <number>`: Run contracts from a specific migration. The number refers to the prefix of the migration file.
* `--to <number>`: Run contracts to a specific migration. The number refers to the prefix of the migration file.
* `--network <name>`: Specify the network to use. The network name must exist in the configuration.
* `--compile-all`: Compile all contracts, instead of intelligently choosing the contracts that need to be compiled.
* `--evm`: Use EVM related configuration (Requires TronBox v4.0.0 or later).

### test [​](#test)

Run JavaScript tests.

Terminal

shell

```
tronbox test [<test_file>] [--network <name>] [--evm]
```

Run all or some test files in the `test/` directory as specified. For more information, please see [Test contracts](/docs/guides/test-contracts) . Options:

* `<test_file>`: The name of the test file to be run. Include the path information if the file does not exist in the current directory.
* `--network <name>`: Specify the network to use. The network name must exist in the configuration.
* `--evm`: Use EVM related configuration (Requires TronBox v4.0.0 or later).

### unbox [​](#unbox)

Download a [TronBox Box](https://github.com/tronsuper), which is a pre-built TronBox project.

Terminal

shell

```
tronbox unbox <box_name>
```

Download a TronBox Box to the current working directory. Option:

* `<box_name>`: The name of the TronBox Box (required).

### version [​](#version)

Display the version number and then exit.

Terminal

shell

```
tronbox version
```