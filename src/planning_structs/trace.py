"""
Traces: sequences of states and actions over one object set.

    Trace(objects=[("r1", "room"), ("r2", "room"), ("s1", "switch")],
          states=[["(robot-at r1)", "(off s1)"], ["(robot-at r2)", "(off s1)"]],
          actions=["(move r1 r2)"])

Atoms and actions may be written "(in s1 r2)", "in s1 r2", ("in", "s1", "r2") or ("in", ("s1", "r2")).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional, Sequence, Tuple


@dataclass
class Trace:
    """One trace of T transitions.

    objects  [(name, type), ...]: every object the states and actions mention, including domain
             constants.
    states   T + 1 states. Each state is an iterable of true atoms, a dict {atom: probability} (atoms
             not listed have probability 0), or a vector of probabilities; a whole [T + 1, P] array
             is also accepted. Vector entries follow `proposition_order` if given, otherwise the
             propositions of Instance(domain, objects) in their order.
    actions  T actions, each an action (e.g. "(move r1 r2)"), an integer, or None for an unknown
             action. Integers index `action_order` if given, otherwise Instance(domain, objects).actions.

    Optional, for data that comes in its own order:
    proposition_order  the atoms naming the entries of vector states, in the data's order.
    action_order       the actions that integer actions refer to, in the data's order.

    These fields only describe the data; programs that consume traces resolve and validate them.
    """
    objects: Sequence[Tuple[str, str]]
    states: Any
    actions: Sequence[Any]
    proposition_order: Optional[Sequence[Any]] = None
    action_order: Optional[Sequence[Any]] = None

    def __post_init__(self) -> None:
        if hasattr(self.states, "__len__") and len(self.states) != len(self.actions) + 1:
            raise ValueError(f"a trace with {len(self.actions)} actions needs {len(self.actions) + 1} states, "
                             f"got {len(self.states)}")

    @property
    def length(self) -> int:
        """Number of transitions."""
        return len(self.actions)
