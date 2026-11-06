import random
from itertools import permutations

import pytest
from helpers import fixture_domain, fixture_objects, naive_propositions, switches_domain

from planning_structs import Instance


def test_proposition_order_is_permutations_filtered_by_type():
    rng = random.Random(0)
    for d, objs in ((fixture_domain(), fixture_objects(rng)),
                    (switches_domain(), [("r0", "room"), ("s0", "switch"), ("r1", "room"), ("s1", "switch")])):
        inst = Instance(d, objs)
        assert [(p.predicate.name, tuple(o.name for o in p.args)) for p in inst.propositions] == naive_propositions(d, objs)
        assert all(inst.prop_index[(p.predicate, p.args)] == i for i, p in enumerate(inst.propositions))


def test_actions_are_lazy_and_in_permutation_order():
    d = fixture_domain()
    objs = fixture_objects(random.Random(1))
    inst = Instance(d, objs)
    assert inst._actions is None                       # nothing enumerated yet
    types = {n: d.get_type(t) for n, t in objs}
    names = [n for n, _ in objs]
    expected = [(a.name, args) for a in d.action_schemas for args in permutations(names, a.arity)
                if all(types[o].is_child_of(t) for o, t in zip(args, a.types))]
    assert [(a.action_schema.name, tuple(o.name for o in a.args)) for a in inst.actions] == expected
    assert inst.num_actions == len(expected)


def test_lookups_and_errors():
    d = switches_domain()
    inst = Instance(d, [("r0", "room"), ("r1", "room"), ("s0", "switch")])
    r0, r1 = inst.get_object("r0"), inst.get_object("r1")
    assert inst.get_action(d.get_action_schema("move"), [r0, r1]) is not None
    assert inst.get_action(d.get_action_schema("move"), [r0, r0]) is None          # distinct objects only
    assert inst.get_proposition(d.get_predicate("connected"), [r0, r1]) is not None
    assert inst.get_object("zz") is None
    with pytest.raises(ValueError):
        Instance(d, [("x", "kitchen")])
