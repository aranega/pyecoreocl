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


def default_primitive_call(emitter, ctx):
    emitter.visit(ctx.expression)
    emitter.inline(f".{ctx.attname.text}(")
    emitter.visit(ctx.argExp())
    emitter.inline(")")
