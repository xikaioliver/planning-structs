import pytest
from helpers import fixture_domain, switches_domain


def test_types_and_lookups():
    d = switches_domain()
    assert d.get_type("switch").is_child_of(d.get_type("device"))
    assert not d.get_type("room").is_child_of(d.get_type("device"))
    assert d.get_predicate("in").arity == 2 and d.get_action_schema("turn-on").arity == 2
    assert d.get_predicate("nope") is None and d.get_action_schema("nope") is None


def test_bindings_are_distinct_and_type_compatible():
    d = fixture_domain()
    for (a, p), bindings in d.predicate_arguments.items():
        for x in bindings:
            assert len(set(x)) == len(x) == p.arity
            assert all(a.types[i - 1].is_child_of(t) for i, t in zip(x, p.types))
    z, p2 = d.get_action_schema("z"), d.get_predicate("p2")
    assert d.predicate_arguments[(z, p2)] == [(1, 3), (2, 3)]                                  # B is an A
    assert d.predicate_arguments[(d.get_action_schema("y"), d.get_predicate("p3"))] == []      # needs B, B, C
    assert d.predicate_arguments[(d.get_action_schema("x"), d.get_predicate("p0"))] == [()]    # zero arity


def test_unknown_type_is_an_error():
    from planning_structs import Domain
    with pytest.raises(Exception):
        Domain([("A", None)], [("p", ["Missing"])], [], name="bad")
