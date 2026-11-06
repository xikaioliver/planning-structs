"""Test-only domains defined in code (invented for testing; not from any paper)."""
import random
from itertools import permutations

from planning_structs import Domain


def fixture_domain() -> Domain:
    """Abstract names, typing with inheritance (B is an A), arities 0 to 3."""
    return Domain([("A", None), ("B", "A"), ("C", None)],
                  [("p0", []), ("p1", ["A"]), ("p2", ["A", "C"]), ("p3", ["B", "B", "C"])],
                  [("x", ["B", "C"]), ("y", ["A", "A"]), ("z", ["B", "B", "C"])], name="fixture")


def fixture_objects(rng: random.Random):
    return ([(f"a{i}", "A") for i in range(rng.randint(1, 2))] + [(f"b{i}", "B") for i in range(rng.randint(2, 3))]
            + [(f"c{i}", "C") for i in range(rng.randint(1, 2))])


def switches_domain() -> Domain:
    """A robot moves between rooms and turns switches on and off."""
    return Domain([("switch", "device"), ("room", None), ("device", None)],
                  [("powered", []), ("robot-at", ["room"]), ("in", ["device", "room"]), ("connected", ["room", "room"]),
                   ("on", ["switch"]), ("off", ["switch"])],
                  [("move", ["room", "room"]), ("turn-on", ["switch", "room"]), ("turn-off", ["switch", "room"])],
                  name="switches")


def naive_propositions(domain: Domain, objects):
    """Proposition order by definition: permutations filtered by type."""
    types = {n: domain.get_type(t) for n, t in objects}
    names = [n for n, _ in objects]
    return [(p.name, args) for p in domain.predicates for args in permutations(names, p.arity)
            if all(types[o].is_child_of(t) for o, t in zip(args, p.types))]
