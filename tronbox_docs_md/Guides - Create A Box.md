

# Create a Box [​](#create-a-box)

To create a TronBox Box, you need:

* A GitHub repository
* A configuration file

The configuration file belongs in the top-level directory of your repo. With this file in place, and your repo on GitHub, the unbox command will be: `tronbox unbox {USER_NAME || ORG_NAME}/{REPO_NAME}`

## Configuration file [​](#configuration-file)

Every TronBox Box includes a `tronbox.json` configuration file with the following attributes: `ignore`, `commands`, and `hooks`.

### `ignore` (array) [​](#ignore-array)

An array of files or relative paths that TronBox ignores when unboxing, usually including `readme.md` or `.gitignore`. These files will not be copied from the Box's repository when you unbox.

JSON

json

```
{
  "ignore": ["README.md", ".gitignore"]
}
```

### `commands` (object) [​](#commands-object)

An object whose key-value pairs are a descriptor and console command respectively. Once your Box is successfully unboxed, the key-value pairs will be shown to users and can be seen as quick instructions.

The following example provides commands not only to compile, migrate, and test smart contracts but also for frontend development.

JSON

json

```
{
  "commands": {
    "Compile": "tronbox compile",
    "Migrate": "tronbox migrate",
    "Test contracts": "tronbox test",
    "Test dapp": "npm test",
    "Run dev server": "npm run start",
    "Build for production": "npm run build"
  }
}
```

### `hooks` (object) [​](#hooks-object)

An object that contains console commands to be executed after unboxing. The command is usually `npm install` as we are using Node.js.

JSON

json

```
{
  "hooks": {
    "post-unpack": "npm install"
  }
}
```