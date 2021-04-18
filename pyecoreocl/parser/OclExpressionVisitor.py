# Generated from OclExpression.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OclExpressionParser import OclExpressionParser
else:
    from OclExpressionParser import OclExpressionParser

# This class defines a complete generic visitor for a parse tree produced by OclExpressionParser.

class OclExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OclExpressionParser#UnaryOperation.
    def visitUnaryOperation(self, ctx:OclExpressionParser.UnaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#AttributeNavigation.
    def visitAttributeNavigation(self, ctx:OclExpressionParser.AttributeNavigationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#PrimaryExpression.
    def visitPrimaryExpression(self, ctx:OclExpressionParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#ArithmeticBinaryOperation.
    def visitArithmeticBinaryOperation(self, ctx:OclExpressionParser.ArithmeticBinaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#SimpleName.
    def visitSimpleName(self, ctx:OclExpressionParser.SimpleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#FullQualifiedName.
    def visitFullQualifiedName(self, ctx:OclExpressionParser.FullQualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#ComparisonBinaryOperation.
    def visitComparisonBinaryOperation(self, ctx:OclExpressionParser.ComparisonBinaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#CollectionCall.
    def visitCollectionCall(self, ctx:OclExpressionParser.CollectionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#BooleanBinaryOperation.
    def visitBooleanBinaryOperation(self, ctx:OclExpressionParser.BooleanBinaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#CallExpression.
    def visitCallExpression(self, ctx:OclExpressionParser.CallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#MethodCall.
    def visitMethodCall(self, ctx:OclExpressionParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#ArgumentsExp.
    def visitArgumentsExp(self, ctx:OclExpressionParser.ArgumentsExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#LambdaExp.
    def visitLambdaExp(self, ctx:OclExpressionParser.LambdaExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#primaryExp.
    def visitPrimaryExp(self, ctx:OclExpressionParser.PrimaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#selfExp.
    def visitSelfExp(self, ctx:OclExpressionParser.SelfExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#nestedExp.
    def visitNestedExp(self, ctx:OclExpressionParser.NestedExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#NumberLiteral.
    def visitNumberLiteral(self, ctx:OclExpressionParser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#StringLiteral.
    def visitStringLiteral(self, ctx:OclExpressionParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#BooleanLiteral.
    def visitBooleanLiteral(self, ctx:OclExpressionParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#UnlimitedNaturalLiteral.
    def visitUnlimitedNaturalLiteral(self, ctx:OclExpressionParser.UnlimitedNaturalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#InvalidLiteral.
    def visitInvalidLiteral(self, ctx:OclExpressionParser.InvalidLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#NullLiteral.
    def visitNullLiteral(self, ctx:OclExpressionParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#tupleLiteralExp.
    def visitTupleLiteralExp(self, ctx:OclExpressionParser.TupleLiteralExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#tupleLiteralPartCS.
    def visitTupleLiteralPartCS(self, ctx:OclExpressionParser.TupleLiteralPartCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#collectionLiteralExp.
    def visitCollectionLiteralExp(self, ctx:OclExpressionParser.CollectionLiteralExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#collectionTypeCS.
    def visitCollectionTypeCS(self, ctx:OclExpressionParser.CollectionTypeCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#StringType.
    def visitStringType(self, ctx:OclExpressionParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#IntegerType.
    def visitIntegerType(self, ctx:OclExpressionParser.IntegerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#UnlimitedNaturalType.
    def visitUnlimitedNaturalType(self, ctx:OclExpressionParser.UnlimitedNaturalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#BooleanType.
    def visitBooleanType(self, ctx:OclExpressionParser.BooleanTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#CollectionType.
    def visitCollectionType(self, ctx:OclExpressionParser.CollectionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#BagType.
    def visitBagType(self, ctx:OclExpressionParser.BagTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#OrderedSetType.
    def visitOrderedSetType(self, ctx:OclExpressionParser.OrderedSetTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#SequenceType.
    def visitSequenceType(self, ctx:OclExpressionParser.SequenceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#SetType.
    def visitSetType(self, ctx:OclExpressionParser.SetTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#collectionLiteralPartCS.
    def visitCollectionLiteralPartCS(self, ctx:OclExpressionParser.CollectionLiteralPartCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#typeLiteralExp.
    def visitTypeLiteralExp(self, ctx:OclExpressionParser.TypeLiteralExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#letExp.
    def visitLetExp(self, ctx:OclExpressionParser.LetExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#letVariableCS.
    def visitLetVariableCS(self, ctx:OclExpressionParser.LetVariableCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#typeExpCS.
    def visitTypeExpCS(self, ctx:OclExpressionParser.TypeExpCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#typeNameExpCS.
    def visitTypeNameExpCS(self, ctx:OclExpressionParser.TypeNameExpCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#typeLiteralCS.
    def visitTypeLiteralCS(self, ctx:OclExpressionParser.TypeLiteralCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#tupleTypeCS.
    def visitTupleTypeCS(self, ctx:OclExpressionParser.TupleTypeCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#tuplePartCS.
    def visitTuplePartCS(self, ctx:OclExpressionParser.TuplePartCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#ifExp.
    def visitIfExp(self, ctx:OclExpressionParser.IfExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#numberLiteralExpCS.
    def visitNumberLiteralExpCS(self, ctx:OclExpressionParser.NumberLiteralExpCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#stringLiteralExpCS.
    def visitStringLiteralExpCS(self, ctx:OclExpressionParser.StringLiteralExpCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#booleanLiteralExpCS.
    def visitBooleanLiteralExpCS(self, ctx:OclExpressionParser.BooleanLiteralExpCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#unlimitedNaturalLiteralCS.
    def visitUnlimitedNaturalLiteralCS(self, ctx:OclExpressionParser.UnlimitedNaturalLiteralCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#invalidLiteralExpCS.
    def visitInvalidLiteralExpCS(self, ctx:OclExpressionParser.InvalidLiteralExpCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#nullLiteralExpCS.
    def visitNullLiteralExpCS(self, ctx:OclExpressionParser.NullLiteralExpCSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#unrestrictedName.
    def visitUnrestrictedName(self, ctx:OclExpressionParser.UnrestrictedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OclExpressionParser#unreservedName.
    def visitUnreservedName(self, ctx:OclExpressionParser.UnreservedNameContext):
        return self.visitChildren(ctx)



del OclExpressionParser