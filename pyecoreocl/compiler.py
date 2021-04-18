from io import StringIO
from antlr4 import CommonTokenStream, InputStream
from .parser import OclExpressionVisitor, OclExpressionParser, OclExpressionLexer


class OCLTuple(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class DummyVisitor(OclExpressionVisitor):
    def __init__(self):
        self.ind = ""
        self.result = ""

    def line(self, s):
        self.result += self.ind + s + "\n"

    def inline(self, s):
        self.result += s

    def indent(self):
        self.ind += "  "

    def unindent(self):
        self.ind = self.ind[2:]

    def visitUnaryOperation(self, ctx):
        self.inline(ctx.text)

    def visitAttributeNavigation(self, ctx):
        self.visit(ctx.expression)
        self.inline(f".{ctx.attname.text}")

    def visitPrimaryExpression(self, ctx):
        return self.visitChildren(ctx)

    def visitArithmeticBinaryOperation(self, ctx):
        self.visit(ctx.left)
        self.inline(f" {ctx.operator.text} ")
        self.visit(ctx.right)

    def visitSimpleName(self, ctx):
        self.inline(ctx.text)

    def visitFullQualifiedName(self, ctx):
        self.inline(ctx.text.replace('::', '.'))

    def visitComparisonBinaryOperation(self, ctx):
        self.visit(ctx.left)
        operator = ctx.operator.text
        operator = operator if operator != '=' else '=='
        self.inline(f" {operator} ")
        self.visit(ctx.right)

    def visitCollectionCall(self, ctx):
        operation = ctx.attname.text
        if operation == 'collect':
            self.visitCollect(ctx)
            return
        if operation == 'select':
            self.visitSelect(ctx)
            return
        if operation == 'isNotEmpty':
            self.inline('len(')
            self.visit(ctx.expression)
            self.inline(') > 0')
            return
        if operation == 'isEmpty':
            self.inline('len(')
            self.visit(ctx.expression)
            self.inline(') == 0')
            return

        self.visit(ctx.expression)
        self.inline(f".{operation}(")
        self.visit(ctx.argExp())
        self.inline(")")

    def visitCollect(self, ctx):
        self.inline("[")
        self.visit(ctx.argExp().oclExp())
        self.inline(f" for {ctx.argExp().varnames[0].text} in ")
        self.visit(ctx.expression)
        self.inline("]")

    def visitSelect(self, ctx):
        self.inline(f"[{ctx.argExp().varnames[0].text}")
        self.inline(f" for {ctx.argExp().varnames[0].text} in ")
        self.visit(ctx.expression)
        self.inline(f" if ")
        self.visit(ctx.argExp().oclExp())
        self.inline("]")

    def visitBooleanBinaryOperation(self, ctx):
        self.visit(ctx.left)
        self.inline(f" {ctx.operator.text} ")
        self.visit(ctx.right)

    def visitCallExpression(self, ctx):
        self.visit(ctx.expression)
        self.inline("(")
        self.visit(ctx.argExp())
        self.inline(")")

    def visitMethodCall(self, ctx):
        if ctx.attname.text == 'oclAsType':
            self.visit(ctx.expression)
            return
        if ctx.attname.text == 'oclIsKindOf':
            self.inline('isinstance(')
            self.visit(ctx.expression)
            self.inline(', ')
            self.visit(ctx.argExp())
            self.inline(')')
            return
        self.visit(ctx.expression)
        self.inline(f".{ctx.attname.text}(")
        self.visit(ctx.argExp())
        self.inline(")")

    def visitArgumentsExp(self, ctx):
        for exp in ctx.oclExp():
            self.visit(exp)
            if exp is not ctx.oclExp()[-1]:
                self.inline(', ')

    def visitLambdaExp(self, ctx):
        return self.visitChildren(ctx)

    def visitNestedExp(self, ctx):
        self.inline('(')
        self.visit(ctx.nested)
        self.inline(')')

    def visitSelfExp(self, ctx):
        self.inline('self')

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
        self.inline('OCLTuple(')
        for part in ctx.tupleLiteralPartCS():
            self.visit(part)
            if part is not ctx.tupleLiteralPartCS()[-1]:
                self.inline(", ")
        self.inline(')')

    def visitTupleLiteralPartCS(self, ctx):
        self.inline(f"{ctx.unrestrictedName().text}=")
        self.visit(ctx.primaryExp())

    def visitCollectionLiteralExp(self, ctx):
        ctype = ctx.collectionTypeCS().text
        if ctype == 'Sequence' or ctype == 'Bag':
            opening = '['
            ending = ']'
        elif ctype == 'Set' and len(ctx.expressions) > 0:
            opening = '{'
            ending = '}'
        elif ctype == 'Set':
            opening = 'set('
            ending = ')'
        self.inline(opening)
        for exp in ctx.expressions:
            self.visit(exp)
            if exp is not ctx.expressions[-1]:
                self.inline(', ')
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
        args = ', '.join(x.unrestrictedName().text for x in ctx.variables)
        call_params = ', '.join(x.unrestrictedName().text for x in ctx.variables)
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


def dummy_compiler(s):
    input_stream = InputStream(s)
    lexer = OclExpressionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OclExpressionParser(stream)
    tree = parser.oclExp()
    visitor = DummyVisitor()
    tree.accept(visitor)
    return visitor.result
