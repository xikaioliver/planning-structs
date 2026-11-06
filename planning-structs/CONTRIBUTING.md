# Contributing to planning-structs

Thank you for your interest. Bug reports, questions and pull requests are welcome through
[GitHub issues](https://github.com/xikaioliver/planning-structs/issues).

## Development setup

```bash
git clone https://github.com/xikaioliver/planning-structs.git
cd planning-structs
pip install -e ".[test]"
pytest
```

The test suite runs in a few seconds.

## Branches

- `main` holds the package and always matches the latest release or the work towards the next one.
- Work happens on short-lived branches from `main` (for example `feat/constants`, `fix/pddl-reader`)
  and is merged through a pull request once the tests pass.

## Pull requests

- Keep each pull request to one change, with tests for new behaviour.
- Public functions and classes need docstrings; update `README.md` and
  `CHANGELOG.md` (under "Unreleased") when behaviour changes.
- The package has no dependencies; please discuss adding one in an issue first.

## Versions and releases

Versions follow [Semantic Versioning](https://semver.org/): a patch release fixes bugs, a minor
release adds backward-compatible features, a major release changes the public API. Changes to
learned outputs ship behind an option first.

To release (maintainers):

1. In a pull request, set `version` in `pyproject.toml` and move the "Unreleased" changelog entries
   under the new version.
2. After merging, tag the merge commit `vX.Y.Z` and push the tag.
3. The release workflow runs the tests, checks that the tag matches the package version, builds the
   package and publishes it to PyPI.
