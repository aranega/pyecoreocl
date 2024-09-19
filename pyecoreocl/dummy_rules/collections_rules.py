from . import register_rule_set


@register_rule_set
def collection_rule(fun):
    return fun


@collection_rule
def rule_collect_nested(emitter, ctx):
    emitter.inline("(")
    emitter.visit(ctx.argExp().body)
    variables = [arg.text for arg in ctx.argExp().varnames]
    emitter.inline(f" for {', '.join(variables)} in ")
    if len(variables) > 1:
        emitter.inline("itertools.combinations_with_replacement(")
        emitter.visit(ctx.expression)
        emitter.inline(f", {len(variables)})")
    else:
        emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_collect(emitter, ctx):
    emitter.inline("ocl.flatten(")
    emitter.visit(ctx.argExp().body)
    variables = [arg.text for arg in ctx.argExp().varnames]
    emitter.inline(f" for {', '.join(variables)} in ")
    if len(variables) > 1:
        emitter.inline("itertools.combinations_with_replacement(")
        emitter.visit(ctx.expression)
        emitter.inline(f", {len(variables)})")
    else:
        emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_for_all(emitter, ctx):
    emitter.inline(f"all(")
    emitter.visit(ctx.argExp().body)
    variables = [arg.text for arg in ctx.argExp().varnames]
    emitter.inline(f" for {', '.join(variables)} in ")
    if len(variables) > 1:
        emitter.inline("itertools.combinations_with_replacement(")
        emitter.visit(ctx.expression)
        emitter.inline(f", {len(variables)})")
    else:
        emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_exists(emitter, ctx):
    emitter.inline(f"any(")
    emitter.visit(ctx.argExp().body)
    variables = [arg.text for arg in ctx.argExp().varnames]
    emitter.inline(f" for {', '.join(variables)} in ")
    if len(variables) > 1:
        emitter.inline("itertools.combinations_with_replacement(")
        emitter.visit(ctx.expression)
        emitter.inline(f", {len(variables)})")
    else:
        emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_one(emitter, ctx):
    emitter.inline("(len(list(")
    rule_select(emitter, ctx)
    emitter.inline(")) == 1)")


@collection_rule
def rule_select(emitter, ctx):
    variables = [arg.text for arg in ctx.argExp().varnames]
    varnames = ", ".join(variables)
    emitter.inline(f"({varnames}")
    emitter.inline(f" for {varnames} in ")
    if len(variables) > 1:
        emitter.inline("itertools.combinations_with_replacement(")
        emitter.visit(ctx.expression)
        emitter.inline(f", {len(variables)})")
    else:
        emitter.visit(ctx.expression)
    emitter.inline(f" if ")
    emitter.visit(ctx.argExp().body)
    emitter.inline(")")


@collection_rule
def rule_reject(emitter, ctx):
    variables = [arg.text for arg in ctx.argExp().varnames]
    varnames = ", ".join(variables)
    emitter.inline(f"({varnames}")
    emitter.inline(f" for {varnames} in ")
    if len(variables) > 1:
        emitter.inline("itertools.combinations_with_replacement(")
        emitter.visit(ctx.expression)
        emitter.inline(f", {len(variables)})")
    else:
        emitter.visit(ctx.expression)
    emitter.inline(f" if not (")
    emitter.visit(ctx.argExp().body)
    emitter.inline("))")


@collection_rule
def rule_includes(emitter, ctx):
    emitter.visit(ctx.argExp())
    emitter.inline(" in ")
    emitter.visit(ctx.expression)


@collection_rule
def rule_excludes(emitter, ctx):
    emitter.visit(ctx.argExp())
    emitter.inline(" not in ")
    emitter.visit(ctx.expression)


@collection_rule
def rule_not_empty(emitter, ctx):
    emitter.inline("len(")
    emitter.visit(ctx.expression)
    emitter.inline(") > 0")


@collection_rule
def rule_is_empty(emitter, ctx):
    emitter.inline("len(")
    emitter.visit(ctx.expression)
    emitter.inline(") == 0")


@collection_rule
def rule_at(emitter, ctx):
    emitter.visit(ctx.expression)
    emitter.inline("[")
    emitter.visit(ctx.argExp().body[0])
    emitter.inline("]")


@collection_rule
def rule_size(emitter, ctx):
    emitter.inline("len(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_is_unique(emitter, ctx):
    emitter.inline("ocl.is_unique(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_sum(emitter, ctx):
    emitter.inline("sum(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_min(emitter, ctx):
    emitter.inline("min(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_max(emitter, ctx):
    emitter.inline("max(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_count(emitter, ctx):
    emitter.inline("list(")
    emitter.visit(ctx.expression)
    emitter.inline(").count(")
    emitter.visit(ctx.argExp())
    emitter.inline(")")


@collection_rule
def rule_includes_all(emitter, ctx):
    emitter.inline("all(e in ")
    emitter.visit(ctx.expression)
    emitter.inline(" for e in ")
    emitter.visit(ctx.argExp())
    emitter.inline(")")


@collection_rule
def rule_excludes_all(emitter, ctx):
    emitter.inline("all(e not in ")
    emitter.visit(ctx.expression)
    emitter.inline(" for e in ")
    emitter.visit(ctx.argExp())
    emitter.inline(")")


@collection_rule
def rule_as_sequence(emitter, ctx):
    emitter.inline("list(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_as_set(emitter, ctx):
    emitter.inline("set(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_as_bag(emitter, ctx):
    emitter.inline("list(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_any(emitter, ctx):
    emitter.inline("next(iter(")
    emitter.visit(ctx.expression)
    emitter.inline("), None)")


@collection_rule
def rule_sorted_by(emitter, ctx):
    emitter.inline("sorted(")
    emitter.visit(ctx.expression)
    emitter.inline(", key=")
    emitter.visit(ctx.argExp())
    emitter.inline(")")


@collection_rule
def rule_iterate(emitter, ctx):
    emitter.inline("ocl.flatten(")
    emitter.visit(ctx.argExp())
    emitter.inline("(_e, ")
    emitter.visit(ctx.argExp().initializer)
    emitter.inline(") for _e in ")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_including(emitter, ctx):
    emitter.inline("itertools.chain(")
    emitter.visit(ctx.expression)
    emitter.inline(", (")
    emitter.visit(ctx.argExp())
    emitter.inline(",))")


@collection_rule
def rule_append(emitter, ctx):
    rule_including(emitter, ctx)


@collection_rule
def rule_prepend(emitter, ctx):
    emitter.inline("itertools.chain((")
    emitter.visit(ctx.argExp())
    emitter.inline(",), ")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@collection_rule
def rule_excluding(emitter, ctx):
    emitter.inline("_e for _e in ")
    emitter.visit(ctx.expression)
    emitter.inline(" if _e != ")
    emitter.visit(ctx.argExp())


@collection_rule
def rule_select_by_kind(emitter, ctx):
    emitter.inline("_e for _e in ")
    emitter.visit(ctx.expression)
    emitter.inline(" if isinstance(_e, ")
    emitter.visit(ctx.argExp())
    emitter.inline(")")


@collection_rule
def rule_select_by_type(emitter, ctx):
    emitter.inline("_e for _e in ")
    emitter.visit(ctx.expression)
    emitter.inline(" if type(_e) is ")
    emitter.visit(ctx.argExp())


@collection_rule
def rule_first(emitter, ctx):
    emitter.inline("next(iter(")
    emitter.visit(ctx.expression)
    emitter.inline("))")


@collection_rule
def rule_last(emitter, ctx):
    emitter.inline("list(")
    emitter.visit(ctx.expression)
    emitter.inline(")[-1]")


@collection_rule
def rule_index_of(emitter, ctx):
    emitter.inline("next(_i for _i, _e in enumerate(")
    emitter.visit(ctx.expression)
    emitter.inline(") if _e == ")
    emitter.visit(ctx.argExp().body[0])
    emitter.inline(")")


@collection_rule
def rule_closure(emitter, ctx):
    emitter.inline("ocl.closure(")
    emitter.visit(ctx.expression)
    emitter.inline(", ")
    emitter.visit(ctx.argExp())
    emitter.inline(")")


def default_collection_call(emitter, ctx):
    operation = ctx.attname.text
    emitter.visit(ctx.expression)
    emitter.inline(f".{operation}(")
    emitter.visit(ctx.argExp())
    emitter.inline(")")
