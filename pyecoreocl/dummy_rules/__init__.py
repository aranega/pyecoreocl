class RuleSet:
    rules_collections = {}
    rules_primitives = {}


def register_rule_set(decorator):
    register_name = decorator.__name__.split("_")[0]

    def inner(fun):
        names = fun.__name__[5:].split("_")
        function_name = "".join([names[0], *(f.capitalize() for f in names[1:])])
        getattr(RuleSet, f"rules_{register_name}s")[function_name] = fun
        return fun

    return inner


from .collections_rules import default_collection_call
from .primitives_rules import default_primitive_call