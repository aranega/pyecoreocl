from antlr4 import CommonTokenStream, InputStream

from .dummy_rules import RuleSet, default_collection_call, default_primitive_call
from .parser import OclExpressionVisitor, OclExpressionParser, OclExpressionLexer


class DummyVisitor(OclExpressionVisitor):
    def __init__(self, mode="normal"):
        self.ind = ""
        self.result = ""
        self.mode = mode

    def line(self, s):
        self.result += self.ind + s + "\n"

    def inline(self, s):
        self.result += s

    def indent(self):
        self.ind += "  "

    def unindent(self):
        self.ind = self.ind[2:]

    def visitUnaryOperation(self, ctx):
        operator = ctx.operator.text
        space = "" if operator == "-" else " "
        self.inline(f"{operator}{space}")
        self.visit(ctx.expression)

    def visitAttributeNavigation(self, ctx):
        if self.mode == "strict":
            # In strict mode, we don't accept implicit collect
            self.visit(ctx.expression)
            self.inline(f".{ctx.attname.text}")
            return

        self.inline(f"ocl.geta(")
        self.visit(ctx.expression)
        self.inline(f", '{ctx.attname.text}')")

    def visitPrimaryExpression(self, ctx):
        return self.visitChildren(ctx)

    def visitArithmeticBinaryOperation(self, ctx):
        self.visit(ctx.left)
        self.inline(f" {ctx.operator.text} ")
        self.visit(ctx.right)

    def visitSimpleName(self, ctx):
        self.inline(ctx.text)

    def visitFullQualifiedName(self, ctx):
        self.inline(ctx.text.replace("::", "."))

    def visitComparisonBinaryOperation(self, ctx):
        self.visit(ctx.left)
        operator = ctx.operator.text
        operator = operator if operator != "=" else "=="
        operator = operator if operator != "<>" else "!="
        self.inline(f" {operator} ")
        self.visit(ctx.right)

    def visitCollectionCall(self, ctx):
        # We currently don't support implicity collection wrapping
        operation = ctx.attname.text
        rule = RuleSet.rules_collections.get(operation, default_collection_call)
        rule(self, ctx)

    def visitBooleanBinaryOperation(self, ctx):
        operator = ctx.operator.text
        if operator == "implies":
            self.inline("((not ")
            self.visit(ctx.left)
            self.inline(") or ")
            self.visit(ctx.right)
            self.inline(")")
            return
        self.visit(ctx.left)
        self.inline(f" {operator} ")
        self.visit(ctx.right)

    def visitCallExpression(self, ctx):
        self.visit(ctx.expression)
        self.inline("(")
        self.visit(ctx.argExp())
        self.inline(")")

    def visitMethodCall(self, ctx):
        operation = ctx.attname.text
        rule = RuleSet.rules_primitives.get(operation, default_primitive_call)
        rule(self, ctx)

    def visitArgumentsExp(self, ctx):
        for exp in ctx.oclExp():
            self.visit(exp)
            if exp is not ctx.oclExp()[-1]:
                self.inline(", ")

    def visitLambdaExp(self, ctx):
        variables = [arg.text for arg in ctx.varnames]
        if ctx.iterator:
            variables.append(ctx.iterator.text)
        varnames = ", ".join(variables)
        self.inline(f"(lambda {varnames}: ")
        self.visit(ctx.body)
        self.inline(")")

    def visitNestedExp(self, ctx):
        self.inline("(")
        self.visit(ctx.nested)
        self.inline(")")

    def visitSelfExp(self, ctx):
        self.inline("self")

    def visitNumberLiteral(self, ctx):
        self.inline(ctx.text)

    def visitStringLiteral(self, ctx):
        self.inline(ctx.text)

    def visitBooleanLiteral(self, ctx):
        self.inline(ctx.text.capitalize())

    def visitUnlimitedNaturalLiteral(self, ctx):
        return self.visitChildren(ctx)

    def visitInvalidLiteral(self, ctx):
        self.inline("None")

    def visitNullLiteral(self, ctx):
        self.inline("None")

    def visitTupleLiteralExp(self, ctx):
        self.inline("ocl.OCLTuple(")
        for part in ctx.tupleLiteralPartCS():
            self.visit(part)
            if part is not ctx.tupleLiteralPartCS()[-1]:
                self.inline(", ")
        self.inline(")")

    def visitTupleLiteralPartCS(self, ctx):
        self.inline(f"{ctx.unrestrictedName().text}=")
        self.visit(ctx.primaryExp())

    def visitCollectionLiteralExp(self, ctx):
        ctype = ctx.collectionTypeCS().collectionTypeIdentifier().text
        if ctype == "Sequence" or ctype == "Bag":
            opening = "["
            ending = "]"
        elif ctype == "Set" and len(ctx.expressions) > 0:
            opening = "{"
            ending = "}"
        elif ctype == "Set":
            opening = "set("
            ending = ")"
        elif ctype == "OrderedSet":  # TODO provide a simple light implementation
            opening = "["
            ending = "]"
        self.inline(opening)
        for exp in ctx.expressions:
            self.visit(exp)
            if exp is not ctx.expressions[-1]:
                self.inline(", ")
        self.inline(ending)

    def visitCollectionTypeCS(self, ctx):
        self.visitChildren(ctx)

    def visitStringType(self, ctx):
        return self.visitChildren(ctx)

    def visitIntegerType(self, ctx):
        return self.visitChildren(ctx)

    def visitUnlimitedNaturalType(self, ctx):
        return self.visitChildren(ctx)

    def visitBooleanType(self, ctx):
        return self.visitChildren(ctx)

    def visitCollectionType(self, ctx):
        return self.visitChildren(ctx)

    def visitBagType(self, ctx):
        return self.visitChildren(ctx)

    def visitOrderedSetType(self, ctx):
        self.inline(ctx.text)

    def visitSequenceType(self, ctx):
        self.inline("list")

    def visitSetType(self, ctx):
        self.inline("set")

    def visitCollectionLiteralPartCS(self, ctx):
        if ctx.isInterval:
            self.inline("*range(")
            self.visit(ctx.inf)
            self.inline(", ")
            self.visit(ctx.sup)
            self.inline(")")
        else:
            self.visitChildren(ctx)

    def visitTypeLiteralExp(self, ctx):
        return self.visitChildren(ctx)

    def visitLetExp(self, ctx):
        args = ", ".join(x.unrestrictedName().text for x in ctx.variables)
        self.inline(f"(lambda {args}: ")
        self.visit(ctx.oclExp())
        self.inline(")(")
        for param in ctx.variables:
            self.visit(param.oclExp())
            if param is not ctx.variables[-1]:
                self.inline(", ")
        self.inline(")")

    def visitLetVariableCS(self, ctx):
        self.inline(f"{ctx.unrestrictedName().text} = ")
        self.visit(ctx.oclExp())
        self.line("")

    def visitTypeExpCS(self, ctx):
        return self.visitChildren(ctx)

    def visitTypeNameExpCS(self, ctx):
        return self.visitChildren(ctx)

    def visitTypeLiteralCS(self, ctx):
        return self.visitChildren(ctx)

    def visitTupleTypeCS(self, ctx):
        return self.visitChildren(ctx)

    def visitTuplePartCS(self, ctx):
        return self.visitChildren(ctx)

    def visitIfExp(self, ctx):
        self.visit(ctx.body)
        self.inline(" if ")
        self.visit(ctx.condition)
        self.inline(" else ")
        self.visit(ctx.else_)

    def visitNumberLiteralExpCS(self, ctx):
        return self.visitChildren(ctx)

    def visitStringLiteralExpCS(self, ctx):
        return self.visitChildren(ctx)

    def visitBooleanLiteralExpCS(self, ctx):
        return self.visitChildren(ctx)

    def visitUnlimitedNaturalLiteralCS(self, ctx):
        return self.visitChildren(ctx)

    def visitInvalidLiteralExpCS(self, ctx):
        return self.visitChildren(ctx)

    def visitNullLiteralExpCS(self, ctx):
        return self.visitChildren(ctx)

    def visitUnrestrictedName(self, ctx):
        return self.visitChildren(ctx)

    def visitUnreservedName(self, ctx):
        return self.visitChildren(ctx)


def dummy_compiler(s, mode="normal"):
    input_stream = InputStream(s)
    lexer = OclExpressionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OclExpressionParser(stream)
    tree = parser.oclExp()
    visitor = DummyVisitor(mode=mode)
    tree.accept(visitor)
    return visitor.result
