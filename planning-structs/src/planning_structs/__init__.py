"""
Typed STRIPS planning structures: domains, their groundings on object sets, symbolic action models
and traces. No dependencies.
"""
from importlib.metadata import PackageNotFoundError, version

from planning_structs.action_model import ActionModel, Literal
from planning_structs.domain import ActionSchema, Domain, Predicate, Type
from planning_structs.instance import Action, Instance, Object, Proposition
from planning_structs.trace import Trace

try:
    __version__ = version("planning-structs")
except PackageNotFoundError:          # running from a source checkout without installation
    __version__ = "0.0.0+unknown"

__all__ = ["Type", "Predicate", "ActionSchema", "Domain", "Object", "Proposition", "Action", "Instance",
           "ActionModel", "Literal", "Trace", "__version__"]
