

# Create a project [​](#create-a-project)

Most of the TronBox commands are run under the directories of TronBox projects. So the first step is to create a TronBox project. You can create a bare project, but for those getting started, you can use `TronBox Boxes`, which offers example applications and project templates. We'll use the `MetaCoin box`, which creates a token that can be transferred between accounts.

1. Create a directory for MetaCoin:

Terminal

shell

```
mkdir MetaCoin
cd MetaCoin
```

2. Download ("unbox") the MetaCoin project:

Terminal

shell

```
tronbox unbox metacoin
```

TIP

*NOTE: You can create a bare project without smart contracts using `tronbox init`.*

Once this operation is completed, you will have a project directory structure with the following items:

* `contracts/`: Directory for [Solidity contracts](/docs/guides/interact-with-contracts)
* `migrations/`: Directory for [scriptable deployment files](/docs/guides/deploy-contracts)
* `test/`: Directory for [test contracts](/docs/guides/test-contracts)
* `tronbox.js`: TronBox [configuration file](/docs/reference/configuration)