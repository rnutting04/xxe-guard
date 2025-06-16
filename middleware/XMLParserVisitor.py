# Generated from XMLParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete generic visitor for a parse tree produced by XMLParser.

class XMLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XMLParser#document.
    def visitDocument(self, ctx:XMLParser.DocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#prolog.
    def visitProlog(self, ctx:XMLParser.PrologContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#doctypedecl.
    def visitDoctypedecl(self, ctx:XMLParser.DoctypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#externalID.
    def visitExternalID(self, ctx:XMLParser.ExternalIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#intSubset.
    def visitIntSubset(self, ctx:XMLParser.IntSubsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#peReference.
    def visitPeReference(self, ctx:XMLParser.PeReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#markupdecl.
    def visitMarkupdecl(self, ctx:XMLParser.MarkupdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#elementdecl.
    def visitElementdecl(self, ctx:XMLParser.ElementdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#contentSpec.
    def visitContentSpec(self, ctx:XMLParser.ContentSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#mixed.
    def visitMixed(self, ctx:XMLParser.MixedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#nameList.
    def visitNameList(self, ctx:XMLParser.NameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#entityDecl.
    def visitEntityDecl(self, ctx:XMLParser.EntityDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#content.
    def visitContent(self, ctx:XMLParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#element.
    def visitElement(self, ctx:XMLParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#reference.
    def visitReference(self, ctx:XMLParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#attribute.
    def visitAttribute(self, ctx:XMLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#chardata.
    def visitChardata(self, ctx:XMLParser.ChardataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#misc.
    def visitMisc(self, ctx:XMLParser.MiscContext):
        return self.visitChildren(ctx)



del XMLParser