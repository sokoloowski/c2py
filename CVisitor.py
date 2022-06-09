# Generated from docs/C.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):
    indent = 0

    # Visit a parse tree produced by CParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CParser.PrimaryExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                txt = child.getText()
                if txt == "printf":
                    txt = "print"
                res += txt
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#genericSelection.
    def visitGenericSelection(self, ctx:CParser.GenericSelectionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#genericAssocList.
    def visitGenericAssocList(self, ctx:CParser.GenericAssocListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#genericAssociation.
    def visitGenericAssociation(self, ctx:CParser.GenericAssociationContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#postfixExpression.
    def visitPostfixExpression(self, ctx:CParser.PostfixExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:CParser.ArgumentExpressionListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#unaryExpression.
    def visitUnaryExpression(self, ctx:CParser.UnaryExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#unaryOperator.
    def visitUnaryOperator(self, ctx:CParser.UnaryOperatorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#castExpression.
    def visitCastExpression(self, ctx:CParser.CastExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:CParser.MultiplicativeExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:CParser.AdditiveExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#shiftExpression.
    def visitShiftExpression(self, ctx:CParser.ShiftExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#relationalExpression.
    def visitRelationalExpression(self, ctx:CParser.RelationalExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#equalityExpression.
    def visitEqualityExpression(self, ctx:CParser.EqualityExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#andExpression.
    def visitAndExpression(self, ctx:CParser.AndExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:CParser.ExclusiveOrExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:CParser.InclusiveOrExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:CParser.LogicalAndExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:CParser.LogicalOrExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:CParser.ConditionalExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:CParser.AssignmentExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:CParser.AssignmentOperatorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx:CParser.ExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#constantExpression.
    def visitConstantExpression(self, ctx:CParser.ConstantExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#declarationSpecifiers.
    def visitDeclarationSpecifiers(self, ctx:CParser.DeclarationSpecifiersContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#declarationSpecifiers2.
    def visitDeclarationSpecifiers2(self, ctx:CParser.DeclarationSpecifiers2Context):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx:CParser.DeclarationSpecifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:CParser.InitDeclaratorListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#initDeclarator.
    def visitInitDeclarator(self, ctx:CParser.InitDeclaratorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:CParser.StorageClassSpecifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        return ""


    # Visit a parse tree produced by CParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx:CParser.StructOrUnionSpecifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#structOrUnion.
    def visitStructOrUnion(self, ctx:CParser.StructOrUnionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#structDeclarationList.
    def visitStructDeclarationList(self, ctx:CParser.StructDeclarationListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#structDeclaration.
    def visitStructDeclaration(self, ctx:CParser.StructDeclarationContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx:CParser.SpecifierQualifierListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#structDeclaratorList.
    def visitStructDeclaratorList(self, ctx:CParser.StructDeclaratorListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#structDeclarator.
    def visitStructDeclarator(self, ctx:CParser.StructDeclaratorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:CParser.EnumSpecifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#enumeratorList.
    def visitEnumeratorList(self, ctx:CParser.EnumeratorListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#enumerator.
    def visitEnumerator(self, ctx:CParser.EnumeratorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#enumerationConstant.
    def visitEnumerationConstant(self, ctx:CParser.EnumerationConstantContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#atomicTypeSpecifier.
    def visitAtomicTypeSpecifier(self, ctx:CParser.AtomicTypeSpecifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#typeQualifier.
    def visitTypeQualifier(self, ctx:CParser.TypeQualifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx:CParser.FunctionSpecifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#alignmentSpecifier.
    def visitAlignmentSpecifier(self, ctx:CParser.AlignmentSpecifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#declarator.
    def visitDeclarator(self, ctx:CParser.DeclaratorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#directDeclarator.
    def visitDirectDeclarator(self, ctx:CParser.DirectDeclaratorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#vcSpecificModifer.
    def visitVcSpecificModifer(self, ctx:CParser.VcSpecificModiferContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#gccDeclaratorExtension.
    def visitGccDeclaratorExtension(self, ctx:CParser.GccDeclaratorExtensionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#gccAttributeSpecifier.
    def visitGccAttributeSpecifier(self, ctx:CParser.GccAttributeSpecifierContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#gccAttributeList.
    def visitGccAttributeList(self, ctx:CParser.GccAttributeListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#gccAttribute.
    def visitGccAttribute(self, ctx:CParser.GccAttributeContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#nestedParenthesesBlock.
    def visitNestedParenthesesBlock(self, ctx:CParser.NestedParenthesesBlockContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#pointer.
    def visitPointer(self, ctx:CParser.PointerContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#typeQualifierList.
    def visitTypeQualifierList(self, ctx:CParser.TypeQualifierListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:CParser.ParameterTypeListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#parameterList.
    def visitParameterList(self, ctx:CParser.ParameterListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:CParser.ParameterDeclarationContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#identifierList.
    def visitIdentifierList(self, ctx:CParser.IdentifierListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#typeName.
    def visitTypeName(self, ctx:CParser.TypeNameContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:CParser.AbstractDeclaratorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#directAbstractDeclarator.
    def visitDirectAbstractDeclarator(self, ctx:CParser.DirectAbstractDeclaratorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#typedefName.
    def visitTypedefName(self, ctx:CParser.TypedefNameContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#initializer.
    def visitInitializer(self, ctx:CParser.InitializerContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#initializerList.
    def visitInitializerList(self, ctx:CParser.InitializerListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#designation.
    def visitDesignation(self, ctx:CParser.DesignationContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#designatorList.
    def visitDesignatorList(self, ctx:CParser.DesignatorListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#designator.
    def visitDesignator(self, ctx:CParser.DesignatorContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx:CParser.StaticAssertDeclarationContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#statement.
    def visitStatement(self, ctx:CParser.StatementContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#labeledStatement.
    def visitLabeledStatement(self, ctx:CParser.LabeledStatementContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#compoundStatement.
    def visitCompoundStatement(self, ctx:CParser.CompoundStatementContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                txt = child.getText()
                if txt == "{":
                    self.indent += 1
                    res += ":\n" + ("\t" * self.indent)
                elif txt == "}":
                    self.indent -= 1
                    res += "\n" + ("\t" * self.indent)
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#blockItemList.
    def visitBlockItemList(self, ctx:CParser.BlockItemListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#blockItem.
    def visitBlockItem(self, ctx:CParser.BlockItemContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CParser.ExpressionStatementContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                txt = child.getText()
                if txt == ";":
                    res += "\n" + ("\t" * self.indent)
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#selectionStatement.
    def visitSelectionStatement(self, ctx:CParser.SelectionStatementContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#iterationStatement.
    def visitIterationStatement(self, ctx:CParser.IterationStatementContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#forCondition.
    def visitForCondition(self, ctx:CParser.ForConditionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#forDeclaration.
    def visitForDeclaration(self, ctx:CParser.ForDeclarationContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#forExpression.
    def visitForExpression(self, ctx:CParser.ForExpressionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#jumpStatement.
    def visitJumpStatement(self, ctx:CParser.JumpStatementContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                txt = child.getText()
                if txt == ";":
                    txt = "\n" + ("\t" * self.indent)
                res += f"{txt} "
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#compilationUnit.
    def visitCompilationUnit(self, ctx:CParser.CompilationUnitContext):
        return self.visitChildren(ctx.translationUnit()) + "\nmain()"


    # Visit a parse tree produced by CParser#translationUnit.
    def visitTranslationUnit(self, ctx:CParser.TranslationUnitContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx:CParser.ExternalDeclarationContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res


    # Visit a parse tree produced by CParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return f"def {res}"


    # Visit a parse tree produced by CParser#declarationList.
    def visitDeclarationList(self, ctx:CParser.DeclarationListContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
        return res



del CParser