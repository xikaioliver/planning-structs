# planning-structs

Typed STRIPS planning structures in plain Python, with no dependencies: domains, their groundings on
object sets, symbolic action models and traces. It is the structure layer of
[ROSAME](https://github.com/xikaioliver/ROSAME) and of other projects on learning planning models.

```bash
pip install planning-structs
```

## Overview

```python
from planning_structs import Domain, Instance, ActionModel, Trace

# A domain: types (single inheritance), predicates and action schemas with typed parameters.
domain = Domain(types=[("room", None), ("device", None), ("switch", "device")],
                predicates=[("robot-at", ["room"]), ("in", ["device", "room"]), ("on", ["switch"])],
                action_schemas=[("move", ["room", "room"]), ("turn-on", ["switch", "room"])],
                name="switches")

# Its grounding on an object set: propositions (built at once) and actions (built on first use).
instance = Instance(domain, [("r1", "room"), ("r2", "room"), ("s1", "switch")])
print([str(p) for p in instance.propositions])     # robot-at_r1, robot-at_r2, in_s1_r1, ...
print(instance.num_actions)

# The lifted literals ("bindings") an action schema can have over each predicate:
move, robot_at = domain.get_action_schema("move"), domain.get_predicate("robot-at")
print(domain.predicate_arguments[(move, robot_at)])  # [(1,), (2,)]: robot-at(?x1), robot-at(?x2)

# A symbolic action model: per action schema, preconditions, add and delete effects.
model = ActionModel(domain)
model.preconditions["move"] = [(robot_at, (1,))]
model.add_effects["move"] = [(robot_at, (2,))]
model.del_effects["move"] = [(robot_at, (1,))]
print(model)

# A trace: objects, T + 1 states (true atoms, {atom: probability}, or vectors) and T actions.
trace = Trace(objects=[("r1", "room"), ("r2", "room")],
              states=[["(robot-at r1)"], ["(robot-at r2)"]],
              actions=["(move r1 r2)"])

# Data in its own order: name the entries of vector states and the actions integers refer to.
trace = Trace(objects=[("r1", "room"), ("r2", "room")],
              states=[[1.0, 0.0], [0.0, 1.0]],
              actions=[0],
              proposition_order=["(robot-at r1)", "(robot-at r2)"],
              action_order=["(move r1 r2)", "(move r2 r1)"])
```

## Conventions

- **Types** form a tree under `object`; `t.is_child_of(u)` is true when `t` is `u` or a descendant.
- **Bindings.** `domain.predicate_arguments[(schema, predicate)]` lists every way to fill the
  predicate's positions with distinct, type-compatible parameters of the schema, as tuples of 1-based
  parameter positions. In `move(?from, ?to)`, `(connected ?to ?from)` is the binding `(2, 1)`.
- **Grounding order.** Propositions: predicates in domain order, then tuples of *distinct*,
  type-compatible objects in lexicographic order of their positions in the object list. Actions: the
  same for action schemas. Only the sequence of object types matters, not the names.
- **Action models** compare with `==` regardless of literal order; `a.diff(b)` lists the literals
  present in only one of them.

## Versions

Semantic versioning; see [CHANGELOG.md](CHANGELOG.md). Additions arrive in minor releases and stay
compatible with code written for earlier ones.

## License

See [LICENSE](LICENSE).
