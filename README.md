# Symbio Reference Application

[![Build Status](https://jenkins.hq.symbiorobotics.com/buildStatus/icon?job=Reference+App%2Fmaster)](https://jenkins.hq.symbiorobotics.com/job/Reference%20App/job/master/)

The _Symbio Reference Application_ implements the minimal requirements for
integrating with our automation framework.

## Contents

- **`activate`** is a symbolic link to a shared script that provides convenience
  functions for common tasks.
- **`app/`** contains the Python application code.
- **`bootstrap`** is a front-end for managing development environments.
- **`app/configuration/`** contains files used to control runtime behavior such as
  the workcell definition and logging.
- **`infrastructure/`** is a submodule that provides automation support.
- **`Jenkinsfile`** is a declarative pipeline that provides continuous
  integration and release automation.
- **`ui/`** contains the JavaScript code if the application has a user
  interface.

## Application Setup

This section describes the process for creating new applications. Upon
success, your will be able to:

1. Create development environments using a downloaded or local version of SDCS.
2. Verify changes with a pull request builder.
3. Build, test, and publish development images.
4. Build, test, and publish release candidates.
5. Build, test, and publish releases.

### Create the New Repository

To get started, message a member of the [DevOps team][dev-ops-team] to perform
the following steps:

1. Click the button labeled _Use this template_. This will create a new
   repository with the same directory structure. Unlike creating a fork,
   the new repo will not retain the commit history.

2. Name the repository `CUSTOMER_CODENAME-APP_NAME` as in `gemini-seating`,
   `mercury-wax`, or `symbio-bolt_picking`. Exclusively use `-` to separate
   `CUSTOMER_CODENAME` from `APP_NAME`. Use `_` for multi-word names.
   This convention will sort repositories by owner and simplify programmatic
   parsing. Ensure that the new repository is `Private` (radial button is

3. Go to the _Settings_ tab of the new repository. Configure the
   sections _Options_, _Manage Access_, and _Branches_ to match
   [this repository][reference-settings] with the following exception.

   - Do not check 'Template repository' in the new repo.

### Create the Elastic Container Registry (ECR) image repository
To add a repository in ECR for the new application, refer to the [_Usage_](SymbioRobotics/symbio-cloud-infrastructure/artifact-storage/docker-image-repositories#usage) section of in [_Docker Image Repositories_](SymbioRobotics/symbio-cloud-infrastructure/artifact-storage/docker-image-repositories).

### Create the Jenkins Multibranch Pipeline

Once the repository has been created. Configure a multibranch pipeline to
build `master`, release branches, and pull requests.

1. Click the tab that displays all jobs for the customer. If this is a new
   customer, click the `+` to create a new tab; enter the customer code name in the _View name_ input box; select `MultiJob View` from the list and press _OK_.
2. Click _New Item_ on the lefthand side of the page.
3. Check the box labeled _Add to current view_ (next to the _OK_ button).
4. Set the name to the user friendly application name as in _Gemini Seating_,
   _Mercury Wax_, or _Symbio Bolt Picking_.
5. At the bottom of the list, type `Reference App` in the box labeled _Copy from_.

### Configure the New Repository

1. Create a branch.
2. The `symbio-build-tools` submodule in `infrastructure` should already be set up in the repository. If it isn't, it can be setup by running:\
   `git submodule add ../../SymbioRobotics/symbio-build-tools.git infrastructure`
3. Remove this content from `README.md` and set the user friendly application
   name.
4. Rename the directory `app/symbio_reference` to
   `app/CUSTOMER_CODENAME_APP_NAME` as in `gemini_seating`, `mercury_wax`, or
   `symbio_bolt_picking`.
5. Find and replace references to `symbio_reference` with your project's root
   package name.
6. Create a pull request.
7. Create and configure a ZenHub workspace with the user friendly application
   name.

## Tool Configuration

### Linting

* `.flake8` specifies the rules and exclusions for linting Python code. The
  initial ruleset matches the rules for SDCS.
* The target-specific variable `SBT_FLAKE8_ARGS` in `app/Makefile` specifies
  which directories and files must conform to the rules specified in `.flake8`.
* `.mypy.ini` specifies the rules and exclusions for type annotations.
* The target-specific variable `SBT_MYPY_ARGS` in `app/Makefile` specifies
  which packages and modules must conform to the rules specified in
  `.mypy.ini`. Note that `mypy` relies on Python imports while `flake8` uses
  the filesystem. Specify `export SBT_MYPY_ARGS=` to disable `mypy`.

### Automated Testing

* *Unit*, *integration*, and *functional* tests all use Pytest.
* `app/tests` contains a subdirectory for each one with its own `pytest.ini`
  for customizations.
* `app/Makefile` contains a target for each one. You can disable a test suite
  by removing the appropriately-named target. While it may be sensible to
  disable integration or functional tests in some circumstances, please strive
  to run and maintain unit tests.

### Continuous Integration

* `Jenkinsfile` is a declarative pipeline that bootstraps, lints, and runs
  all automated test suites. Following the application setup directions will
  result in a single job that runs for all pull requests and merges to `master`.
* Refer to the [SDCS repo][sdcs-repo] and the corresponding Jenkins jobs for
  an example of how to selectively run test suites via more elaborate triggers.

## Contributing

This project tests our automation and build systems, not SDCS or its
APIs. For example, its unit tests merely verify that imports work and `pytest`
runs with all of the bells and whistles. Revisions should primarily be motivated
by changes to [Symbio Build Tools][build-tools-repo].

[dev-ops-team]: https://github.com/orgs/SymbioRobotics/teams/symbio-dev-ops
[build-tools-repo]: https://github.com/SymbioRobotics/symbio-build-tools
[sdcs-repo]: https://github.com/SymbioRobotics/symbio-dcs
[reference-settings]: https://github.com/SymbioRobotics/symbio-reference/settings
