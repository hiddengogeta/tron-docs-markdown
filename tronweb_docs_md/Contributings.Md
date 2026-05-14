

* Contributings
Version: 6.3.0

On this page

# Contributings

TronWeb is open to the community, which has allowed it to grow significantly. Contributions of all kinds—such as pull requests and issue reports—are always welcome. To contribute, simply follow these rules:

* Security is the top priority of this repository. Please keep it in mind when submitting issues or pull requests.
* Be cautious when submitting changes that break backward compatibility — in most cases, such changes will not be accepted.
* We aim to keep this repository lightweight and accessible, so that new users can get started easily without facing unnecessary complexity.

Finally, we truly appreciate it when you submit an issue before starting a pull request, so we can discuss and determine the best way to solve the problem.

## Code Style[​](#code-style "Direct link to Code Style")

* TronWeb uses `ESLint` to enforce coding standards, extending the `eslint:recommended`, `plugin:@typescript-eslint/recommended` and `prettier` rule sets.
* Use `npm run lint` to lint the code and `npm run lint:fix` to fix the lint errors

## Process[​](#process "Direct link to Process")

* Fork this repo and clone it locally.
* Install the dependencies — `npm i`.
* Do your changes to the code.
* Build the TronWeb dist files — `npm run build:all`.
* Run a local private network using Tron [TRE](/docu/docs/Build local node).
* Run the tests — `npm run test`.
* Push your changes and open a pull request.

Contact the team [here](https://cn.developers.tron.network/docs/online-technical-support).