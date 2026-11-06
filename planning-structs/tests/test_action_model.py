from helpers import switches_domain

from planning_structs import ActionModel


def model(d, extra_add=()):
    am = ActionModel(d)
    p = d.get_predicate
    am.preconditions["move"] = [(p("robot-at"), (1,)), (p("connected"), (1, 2))]
    am.add_effects["move"] = [(p("robot-at"), (2,))] + list(extra_add)
    am.del_effects["move"] = [(p("robot-at"), (1,))]
    return am


def test_equality_ignores_order_and_diff_explains_differences():
    d = switches_domain()
    a, b = model(d), model(d)
    b.preconditions["move"] = list(reversed(b.preconditions["move"]))
    assert a == b and a.diff(b) == []
    c = model(d, extra_add=[(d.get_predicate("powered"), ())])
    assert a != c
    assert c.diff(a) == ["move: add effect (powered) only in this model"]
    assert a.diff(c) == ["move: add effect (powered) only in the other model"]


def test_schema_and_str():
    d = switches_domain()
    pre, add, dele = model(d).schema("move")
    assert len(pre) == 2 and len(add) == 1 and len(dele) == 1
    assert model(d).schema("turn-on") == ([], [], [])
    assert "move(?x1, ?x2)" in str(model(d)) and "(connected ?x1 ?x2)" in str(model(d))
