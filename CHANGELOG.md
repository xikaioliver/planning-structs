# Changelog

All notable changes to this package are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0] - 2026-11-06

### Added
- `Trace.proposition_order` and `Trace.action_order` (optional): the data's own order of the entries
  of vector states, and of the actions that integer actions refer to. Both default to `None`, so
  existing code is unaffected.

## [0.1.0] - 2026-11-06

First release, extracted from `rosame` 0.1.0 (`rosame.planning_structs`), where these structures were
developed.

### Added
- `Type`, `Predicate`, `ActionSchema`, `Domain`: typed STRIPS domains, with the lifted bindings of
  every (action schema, predicate) pair.
- `Object`, `Proposition`, `Action`, `Instance`: groundings on object sets, in a fixed documented
  order; grounded actions built on first use.
- `ActionModel`: symbolic lifted action models, with order-independent equality and `diff`.
- `Trace`: objects, states (symbolic or probabilistic) and actions of one trace (previously
  `rosame.Trace`).
