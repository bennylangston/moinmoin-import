# Contributing to moinmoin-import

## Workflow

To contribute, fork the project on [GitHub](https://github.com/greenbone/moinmoin-import), clone your fork locally, use a new branch for every change, push that branch to GitHub and create a pull request there!

A pull request will be reviewed by one of the maintainers.

## Release management

We follow the [Semantic Versioning Specification](https://semver.org/). Tag releases with git!

"Release early, release often!"

## Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

Add your changes to the **Unreleased** section in your pull request!

Template:

```
### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security
```

## Commit messages

Follow the seven rules of a great git commit message!

- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line
- Wrap the body at 72 characters
- Use the body to explain what and why vs. how

Source and explanation: https://chris.beams.io/posts/git-commit/

## Code Style

We use [Black](https://black.readthedocs.io/en/stable/) to format the code automatically, so developers can focus on more important matters.

Just run it once before you commit:

    black gvm_performance_tests/

Also use [Pylint](https://www.pylint.org/) to check the code for common problems:

    pylint gvm_performance_tests/
