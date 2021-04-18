# Generated from OclExpression.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OclExpressionParser import OclExpressionParser
else:
    from OclExpressionParser import OclExpressionParser

# This class defines a complete listener for a parse tree produced by OclExpressionParser.
class OclExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by OclExpressionParser#UnaryOperation.
    def enterUnaryOperation(self, ctx:OclExpressionParser.UnaryOperationContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#UnaryOperation.
    def exitUnaryOperation(self, ctx:OclExpressionParser.UnaryOperationContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#AttributeNavigation.
    def enterAttributeNavigation(self, ctx:OclExpressionParser.AttributeNavigationContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#AttributeNavigation.
    def exitAttributeNavigation(self, ctx:OclExpressionParser.AttributeNavigationContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#PrimaryExpression.
    def enterPrimaryExpression(self, ctx:OclExpressionParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#PrimaryExpression.
    def exitPrimaryExpression(self, ctx:OclExpressionParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#ArithmeticBinaryOperation.
    def enterArithmeticBinaryOperation(self, ctx:OclExpressionParser.ArithmeticBinaryOperationContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#ArithmeticBinaryOperation.
    def exitArithmeticBinaryOperation(self, ctx:OclExpressionParser.ArithmeticBinaryOperationContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#SimpleName.
    def enterSimpleName(self, ctx:OclExpressionParser.SimpleNameContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#SimpleName.
    def exitSimpleName(self, ctx:OclExpressionParser.SimpleNameContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#FullQualifiedName.
    def enterFullQualifiedName(self, ctx:OclExpressionParser.FullQualifiedNameContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#FullQualifiedName.
    def exitFullQualifiedName(self, ctx:OclExpressionParser.FullQualifiedNameContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#ComparisonBinaryOperation.
    def enterComparisonBinaryOperation(self, ctx:OclExpressionParser.ComparisonBinaryOperationContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#ComparisonBinaryOperation.
    def exitComparisonBinaryOperation(self, ctx:OclExpressionParser.ComparisonBinaryOperationContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#CollectionCall.
    def enterCollectionCall(self, ctx:OclExpressionParser.CollectionCallContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#CollectionCall.
    def exitCollectionCall(self, ctx:OclExpressionParser.CollectionCallContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#BooleanBinaryOperation.
    def enterBooleanBinaryOperation(self, ctx:OclExpressionParser.BooleanBinaryOperationContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#BooleanBinaryOperation.
    def exitBooleanBinaryOperation(self, ctx:OclExpressionParser.BooleanBinaryOperationContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#CallExpression.
    def enterCallExpression(self, ctx:OclExpressionParser.CallExpressionContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#CallExpression.
    def exitCallExpression(self, ctx:OclExpressionParser.CallExpressionContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#MethodCall.
    def enterMethodCall(self, ctx:OclExpressionParser.MethodCallContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#MethodCall.
    def exitMethodCall(self, ctx:OclExpressionParser.MethodCallContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#ArgumentsExp.
    def enterArgumentsExp(self, ctx:OclExpressionParser.ArgumentsExpContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#ArgumentsExp.
    def exitArgumentsExp(self, ctx:OclExpressionParser.ArgumentsExpContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#LambdaExp.
    def enterLambdaExp(self, ctx:OclExpressionParser.LambdaExpContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#LambdaExp.
    def exitLambdaExp(self, ctx:OclExpressionParser.LambdaExpContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#primaryExp.
    def enterPrimaryExp(self, ctx:OclExpressionParser.PrimaryExpContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#primaryExp.
    def exitPrimaryExp(self, ctx:OclExpressionParser.PrimaryExpContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#NumberLiteral.
    def enterNumberLiteral(self, ctx:OclExpressionParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#NumberLiteral.
    def exitNumberLiteral(self, ctx:OclExpressionParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#StringLiteral.
    def enterStringLiteral(self, ctx:OclExpressionParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#StringLiteral.
    def exitStringLiteral(self, ctx:OclExpressionParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#BooleanLiteral.
    def enterBooleanLiteral(self, ctx:OclExpressionParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#BooleanLiteral.
    def exitBooleanLiteral(self, ctx:OclExpressionParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#UnlimitedNaturalLiteral.
    def enterUnlimitedNaturalLiteral(self, ctx:OclExpressionParser.UnlimitedNaturalLiteralContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#UnlimitedNaturalLiteral.
    def exitUnlimitedNaturalLiteral(self, ctx:OclExpressionParser.UnlimitedNaturalLiteralContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#InvalidLiteral.
    def enterInvalidLiteral(self, ctx:OclExpressionParser.InvalidLiteralContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#InvalidLiteral.
    def exitInvalidLiteral(self, ctx:OclExpressionParser.InvalidLiteralContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#NullLiteral.
    def enterNullLiteral(self, ctx:OclExpressionParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#NullLiteral.
    def exitNullLiteral(self, ctx:OclExpressionParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#tupleLiteralExp.
    def enterTupleLiteralExp(self, ctx:OclExpressionParser.TupleLiteralExpContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#tupleLiteralExp.
    def exitTupleLiteralExp(self, ctx:OclExpressionParser.TupleLiteralExpContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#tupleLiteralPartCS.
    def enterTupleLiteralPartCS(self, ctx:OclExpressionParser.TupleLiteralPartCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#tupleLiteralPartCS.
    def exitTupleLiteralPartCS(self, ctx:OclExpressionParser.TupleLiteralPartCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#collectionLiteralExp.
    def enterCollectionLiteralExp(self, ctx:OclExpressionParser.CollectionLiteralExpContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#collectionLiteralExp.
    def exitCollectionLiteralExp(self, ctx:OclExpressionParser.CollectionLiteralExpContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#collectionTypeCS.
    def enterCollectionTypeCS(self, ctx:OclExpressionParser.CollectionTypeCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#collectionTypeCS.
    def exitCollectionTypeCS(self, ctx:OclExpressionParser.CollectionTypeCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#StringType.
    def enterStringType(self, ctx:OclExpressionParser.StringTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#StringType.
    def exitStringType(self, ctx:OclExpressionParser.StringTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#IntegerType.
    def enterIntegerType(self, ctx:OclExpressionParser.IntegerTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#IntegerType.
    def exitIntegerType(self, ctx:OclExpressionParser.IntegerTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#UnlimitedNaturalType.
    def enterUnlimitedNaturalType(self, ctx:OclExpressionParser.UnlimitedNaturalTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#UnlimitedNaturalType.
    def exitUnlimitedNaturalType(self, ctx:OclExpressionParser.UnlimitedNaturalTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#BooleanType.
    def enterBooleanType(self, ctx:OclExpressionParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#BooleanType.
    def exitBooleanType(self, ctx:OclExpressionParser.BooleanTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#CollectionType.
    def enterCollectionType(self, ctx:OclExpressionParser.CollectionTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#CollectionType.
    def exitCollectionType(self, ctx:OclExpressionParser.CollectionTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#BagType.
    def enterBagType(self, ctx:OclExpressionParser.BagTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#BagType.
    def exitBagType(self, ctx:OclExpressionParser.BagTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#OrderedSetType.
    def enterOrderedSetType(self, ctx:OclExpressionParser.OrderedSetTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#OrderedSetType.
    def exitOrderedSetType(self, ctx:OclExpressionParser.OrderedSetTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#SequenceType.
    def enterSequenceType(self, ctx:OclExpressionParser.SequenceTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#SequenceType.
    def exitSequenceType(self, ctx:OclExpressionParser.SequenceTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#SetType.
    def enterSetType(self, ctx:OclExpressionParser.SetTypeContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#SetType.
    def exitSetType(self, ctx:OclExpressionParser.SetTypeContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#collectionLiteralPartCS.
    def enterCollectionLiteralPartCS(self, ctx:OclExpressionParser.CollectionLiteralPartCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#collectionLiteralPartCS.
    def exitCollectionLiteralPartCS(self, ctx:OclExpressionParser.CollectionLiteralPartCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#typeLiteralExp.
    def enterTypeLiteralExp(self, ctx:OclExpressionParser.TypeLiteralExpContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#typeLiteralExp.
    def exitTypeLiteralExp(self, ctx:OclExpressionParser.TypeLiteralExpContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#letExp.
    def enterLetExp(self, ctx:OclExpressionParser.LetExpContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#letExp.
    def exitLetExp(self, ctx:OclExpressionParser.LetExpContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#letVariableCS.
    def enterLetVariableCS(self, ctx:OclExpressionParser.LetVariableCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#letVariableCS.
    def exitLetVariableCS(self, ctx:OclExpressionParser.LetVariableCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#typeExpCS.
    def enterTypeExpCS(self, ctx:OclExpressionParser.TypeExpCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#typeExpCS.
    def exitTypeExpCS(self, ctx:OclExpressionParser.TypeExpCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#typeNameExpCS.
    def enterTypeNameExpCS(self, ctx:OclExpressionParser.TypeNameExpCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#typeNameExpCS.
    def exitTypeNameExpCS(self, ctx:OclExpressionParser.TypeNameExpCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#typeLiteralCS.
    def enterTypeLiteralCS(self, ctx:OclExpressionParser.TypeLiteralCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#typeLiteralCS.
    def exitTypeLiteralCS(self, ctx:OclExpressionParser.TypeLiteralCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#tupleTypeCS.
    def enterTupleTypeCS(self, ctx:OclExpressionParser.TupleTypeCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#tupleTypeCS.
    def exitTupleTypeCS(self, ctx:OclExpressionParser.TupleTypeCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#tuplePartCS.
    def enterTuplePartCS(self, ctx:OclExpressionParser.TuplePartCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#tuplePartCS.
    def exitTuplePartCS(self, ctx:OclExpressionParser.TuplePartCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#ifExp.
    def enterIfExp(self, ctx:OclExpressionParser.IfExpContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#ifExp.
    def exitIfExp(self, ctx:OclExpressionParser.IfExpContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#numberLiteralExpCS.
    def enterNumberLiteralExpCS(self, ctx:OclExpressionParser.NumberLiteralExpCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#numberLiteralExpCS.
    def exitNumberLiteralExpCS(self, ctx:OclExpressionParser.NumberLiteralExpCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#stringLiteralExpCS.
    def enterStringLiteralExpCS(self, ctx:OclExpressionParser.StringLiteralExpCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#stringLiteralExpCS.
    def exitStringLiteralExpCS(self, ctx:OclExpressionParser.StringLiteralExpCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#booleanLiteralExpCS.
    def enterBooleanLiteralExpCS(self, ctx:OclExpressionParser.BooleanLiteralExpCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#booleanLiteralExpCS.
    def exitBooleanLiteralExpCS(self, ctx:OclExpressionParser.BooleanLiteralExpCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#unlimitedNaturalLiteralCS.
    def enterUnlimitedNaturalLiteralCS(self, ctx:OclExpressionParser.UnlimitedNaturalLiteralCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#unlimitedNaturalLiteralCS.
    def exitUnlimitedNaturalLiteralCS(self, ctx:OclExpressionParser.UnlimitedNaturalLiteralCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#invalidLiteralExpCS.
    def enterInvalidLiteralExpCS(self, ctx:OclExpressionParser.InvalidLiteralExpCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#invalidLiteralExpCS.
    def exitInvalidLiteralExpCS(self, ctx:OclExpressionParser.InvalidLiteralExpCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#nullLiteralExpCS.
    def enterNullLiteralExpCS(self, ctx:OclExpressionParser.NullLiteralExpCSContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#nullLiteralExpCS.
    def exitNullLiteralExpCS(self, ctx:OclExpressionParser.NullLiteralExpCSContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#unrestrictedName.
    def enterUnrestrictedName(self, ctx:OclExpressionParser.UnrestrictedNameContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#unrestrictedName.
    def exitUnrestrictedName(self, ctx:OclExpressionParser.UnrestrictedNameContext):
        pass


    # Enter a parse tree produced by OclExpressionParser#unreservedName.
    def enterUnreservedName(self, ctx:OclExpressionParser.UnreservedNameContext):
        pass

    # Exit a parse tree produced by OclExpressionParser#unreservedName.
    def exitUnreservedName(self, ctx:OclExpressionParser.UnreservedNameContext):
        pass



del OclExpressionParser