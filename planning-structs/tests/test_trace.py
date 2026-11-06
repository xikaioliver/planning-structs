import pytest

from planning_structs import Trace


def test_trace_forms_and_length():
    objs = [("r1", "room"), ("r2", "room")]
    t = Trace(objs, [["(robot-at r1)"], {"(robot-at r2)": 0.9}], ["(move r1 r2)"])
    assert t.length == 1
    assert Trace(objs, [["(robot-at r1)"], ["(robot-at r1)"]], [None]).length == 1     # unknown action


def test_states_must_be_one_more_than_actions():
    with pytest.raises(ValueError):
        Trace([("r1", "room")], [["(robot-at r1)"]], ["(move r1 r2)"])
