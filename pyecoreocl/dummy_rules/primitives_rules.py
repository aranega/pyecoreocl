from . import register_rule_set


@register_rule_set
def primitive_rule(fun):
    return fun


@primitive_rule
def rule_size(emitter, ctx):
    emitter.inline("len(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@primitive_rule
def rule_ocl_as_type(emitter, ctx):
    # type_element = ctx.argExp().body[0].text
    # if type_element in ("list", "set", "dict"):
    #     emitter.inline(f"(lambda _x: ")
    #     emitter.inline(f"_x if isinstance(_x, Iterable) and not isinstance(_x, (bytes, str)) else _e for _e in _x")
    #     emitter.inline(")(")
    #     emitter.inline(f"{type_element}(")
    #     emitter.visit(ctx.expression)
    #     emitter.inline("))")

    #     return
    emitter.visit(ctx.expression)


@primitive_rule
def rule_ocl_is_type_of(emitter, ctx):
    emitter.inline("(type(")
    emitter.visit(ctx.expression)
    emitter.inline(") is ")
    emitter.visit(ctx.argExp())
    emitter.inline(")")


@primitive_rule
def rule_ocl_is_kind_of(emitter, ctx):
    emitter.inline("isinstance(")
    emitter.visit(ctx.expression)
    emitter.inline(", ")
    emitter.visit(ctx.argExp())
    emitter.inline(")")


@primitive_rule
def rule_concat(emitter, ctx):
    emitter.inline('f"{')
    emitter.visit(ctx.expression)
    emitter.inline("}{")
    emitter.visit(ctx.argExp())
    emitter.inline('}"')


@primitive_rule
def rule_substring(emitter, ctx):
    arg1, arg2 = [arg.text for arg in ctx.argExp().body]
    arg2 = f"({arg2} + 1)"
    emitter.inline("(")
    emitter.visit(ctx.expression)
    emitter.inline(f")[{arg1}:{arg2}]")


@primitive_rule
def rule_to_integer(emitter, ctx):
    emitter.inline("int(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@primitive_rule
def rule_to_real(emitter, ctx):
    emitter.inline("float(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@primitive_rule
def rule_to_upper_case(emitter, ctx):
    emitter.visit(ctx.expression)
    emitter.inline(".upper()")


@primitive_rule
def rule_index_of(emitter, ctx):
    emitter.visit(ctx.expression)
    emitter.inline(".index(")
    args = [arg.text for arg in ctx.argExp().body]
    args = ", ".join(args)
    emitter.inline(f"{args})")


@primitive_rule
def rule_to_lower_case(emitter, ctx):
    emitter.visit(ctx.expression)
    emitter.inline(".lower()")


@primitive_rule
def rule_equals_ignore_case(emitter, ctx):
    emitter.inline("(")
    emitter.visit(ctx.expression)
    emitter.inline(".upper() == ")
    emitter.visit(ctx.argExp())
    emitter.inline(".upper())")


@primitive_rule
def rule_at(emitter, ctx):
    emitter.visit(ctx.expression)
    emitter.inline("[")
    emitter.visit(ctx.argExp())
    emitter.inline("]")


@primitive_rule
def rule_characters(emitter, ctx):
    emitter.inline("list(")
    emitter.visit(ctx.expression)
    emitter.inline(")")


@primitive_rule
def rule_toBoolean(emitter, ctx):
    emitter.inline("(")
    emitter.visit(ctx.expression)
    emitter.inline(" in ('True', 'true'))")


def default_primitive_call(emitter, ctx):
    emitter.visit(ctx.expression)
    emitter.inline(f".{ctx.attname.text}(")
    emitter.visit(ctx.argExp())
    emitter.inline(")")
