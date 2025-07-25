# Generated from XMLParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete listener for a parse tree produced by XMLParser.
class XMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by XMLParser#document.
    def enterDocument(self, ctx:XMLParser.DocumentContext):
        pass

    # Exit a parse tree produced by XMLParser#document.
    def exitDocument(self, ctx:XMLParser.DocumentContext):
        pass


    # Enter a parse tree produced by XMLParser#prolog.
    def enterProlog(self, ctx:XMLParser.PrologContext):
        pass

    # Exit a parse tree produced by XMLParser#prolog.
    def exitProlog(self, ctx:XMLParser.PrologContext):
        pass


    # Enter a parse tree produced by XMLParser#doctypedecl.
    def enterDoctypedecl(self, ctx:XMLParser.DoctypedeclContext):
        pass

    # Exit a parse tree produced by XMLParser#doctypedecl.
    def exitDoctypedecl(self, ctx:XMLParser.DoctypedeclContext):
        pass


    # Enter a parse tree produced by XMLParser#externalID.
    def enterExternalID(self, ctx:XMLParser.ExternalIDContext):
        pass

    # Exit a parse tree produced by XMLParser#externalID.
    def exitExternalID(self, ctx:XMLParser.ExternalIDContext):
        pass


    # Enter a parse tree produced by XMLParser#intSubset.
    def enterIntSubset(self, ctx:XMLParser.IntSubsetContext):
        pass

    # Exit a parse tree produced by XMLParser#intSubset.
    def exitIntSubset(self, ctx:XMLParser.IntSubsetContext):
        pass


    # Enter a parse tree produced by XMLParser#peReference.
    def enterPeReference(self, ctx:XMLParser.PeReferenceContext):
        pass

    # Exit a parse tree produced by XMLParser#peReference.
    def exitPeReference(self, ctx:XMLParser.PeReferenceContext):
        pass


    # Enter a parse tree produced by XMLParser#markupdecl.
    def enterMarkupdecl(self, ctx:XMLParser.MarkupdeclContext):
        pass

    # Exit a parse tree produced by XMLParser#markupdecl.
    def exitMarkupdecl(self, ctx:XMLParser.MarkupdeclContext):
        pass


    # Enter a parse tree produced by XMLParser#elementdecl.
    def enterElementdecl(self, ctx:XMLParser.ElementdeclContext):
        pass

    # Exit a parse tree produced by XMLParser#elementdecl.
    def exitElementdecl(self, ctx:XMLParser.ElementdeclContext):
        pass


    # Enter a parse tree produced by XMLParser#contentSpec.
    def enterContentSpec(self, ctx:XMLParser.ContentSpecContext):
        pass

    # Exit a parse tree produced by XMLParser#contentSpec.
    def exitContentSpec(self, ctx:XMLParser.ContentSpecContext):
        pass


    # Enter a parse tree produced by XMLParser#mixed.
    def enterMixed(self, ctx:XMLParser.MixedContext):
        pass

    # Exit a parse tree produced by XMLParser#mixed.
    def exitMixed(self, ctx:XMLParser.MixedContext):
        pass


    # Enter a parse tree produced by XMLParser#nameList.
    def enterNameList(self, ctx:XMLParser.NameListContext):
        pass

    # Exit a parse tree produced by XMLParser#nameList.
    def exitNameList(self, ctx:XMLParser.NameListContext):
        pass


    # Enter a parse tree produced by XMLParser#entityDecl.
    def enterEntityDecl(self, ctx:XMLParser.EntityDeclContext):
        pass

    # Exit a parse tree produced by XMLParser#entityDecl.
    def exitEntityDecl(self, ctx:XMLParser.EntityDeclContext):
        pass


    # Enter a parse tree produced by XMLParser#content.
    def enterContent(self, ctx:XMLParser.ContentContext):
        pass

    # Exit a parse tree produced by XMLParser#content.
    def exitContent(self, ctx:XMLParser.ContentContext):
        pass


    # Enter a parse tree produced by XMLParser#element.
    def enterElement(self, ctx:XMLParser.ElementContext):
        pass

    # Exit a parse tree produced by XMLParser#element.
    def exitElement(self, ctx:XMLParser.ElementContext):
        pass


    # Enter a parse tree produced by XMLParser#reference.
    def enterReference(self, ctx:XMLParser.ReferenceContext):
        pass

    # Exit a parse tree produced by XMLParser#reference.
    def exitReference(self, ctx:XMLParser.ReferenceContext):
        pass


    # Enter a parse tree produced by XMLParser#attribute.
    def enterAttribute(self, ctx:XMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by XMLParser#attribute.
    def exitAttribute(self, ctx:XMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by XMLParser#chardata.
    def enterChardata(self, ctx:XMLParser.ChardataContext):
        pass

    # Exit a parse tree produced by XMLParser#chardata.
    def exitChardata(self, ctx:XMLParser.ChardataContext):
        pass


    # Enter a parse tree produced by XMLParser#misc.
    def enterMisc(self, ctx:XMLParser.MiscContext):
        pass

    # Exit a parse tree produced by XMLParser#misc.
    def exitMisc(self, ctx:XMLParser.MiscContext):
        pass



del XMLParser