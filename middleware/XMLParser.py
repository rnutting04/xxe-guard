# Generated from XMLParser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,261,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,5,0,41,
        8,0,10,0,12,0,44,9,0,1,0,3,0,47,8,0,1,0,5,0,50,8,0,10,0,12,0,53,
        9,0,1,0,1,0,5,0,57,8,0,10,0,12,0,60,9,0,1,0,1,0,1,1,1,1,5,1,66,8,
        1,10,1,12,1,69,9,1,1,1,1,1,1,2,1,2,3,2,75,8,2,1,2,1,2,3,2,79,8,2,
        1,2,1,2,3,2,83,8,2,3,2,85,8,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,3,3,94,
        8,3,1,3,1,3,1,3,3,3,99,8,3,1,3,1,3,3,3,103,8,3,1,3,3,3,106,8,3,1,
        4,1,4,1,4,5,4,111,8,4,10,4,12,4,114,9,4,1,5,1,5,1,5,1,5,1,6,1,6,
        3,6,122,8,6,1,7,1,7,3,7,126,8,7,1,7,1,7,3,7,130,8,7,1,7,1,7,3,7,
        134,8,7,1,7,1,7,1,8,1,8,1,8,3,8,141,8,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,153,8,9,1,10,1,10,1,10,5,10,158,8,10,10,10,12,
        10,161,9,10,1,11,1,11,3,11,165,8,11,1,11,3,11,168,8,11,1,11,3,11,
        171,8,11,1,11,1,11,3,11,175,8,11,1,11,1,11,3,11,179,8,11,1,11,1,
        11,1,11,3,11,184,8,11,1,11,3,11,187,8,11,1,11,3,11,190,8,11,1,11,
        1,11,3,11,194,8,11,1,11,1,11,3,11,198,8,11,1,11,1,11,3,11,202,8,
        11,1,11,3,11,205,8,11,1,12,3,12,208,8,12,1,12,1,12,1,12,1,12,1,12,
        3,12,215,8,12,1,12,3,12,218,8,12,5,12,220,8,12,10,12,12,12,223,9,
        12,1,13,1,13,1,13,5,13,228,8,13,10,13,12,13,231,9,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,243,8,13,10,13,12,13,
        246,9,13,1,13,3,13,249,8,13,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,
        16,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,0,3,1,0,3,4,2,0,5,5,9,9,3,0,1,1,5,5,37,37,289,0,37,1,0,
        0,0,2,63,1,0,0,0,4,72,1,0,0,0,6,105,1,0,0,0,8,112,1,0,0,0,10,115,
        1,0,0,0,12,121,1,0,0,0,14,123,1,0,0,0,16,140,1,0,0,0,18,152,1,0,
        0,0,20,154,1,0,0,0,22,204,1,0,0,0,24,207,1,0,0,0,26,248,1,0,0,0,
        28,250,1,0,0,0,30,252,1,0,0,0,32,256,1,0,0,0,34,258,1,0,0,0,36,38,
        3,2,1,0,37,36,1,0,0,0,37,38,1,0,0,0,38,42,1,0,0,0,39,41,3,34,17,
        0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,45,47,3,4,2,0,46,45,1,0,0,0,46,47,1,0,0,0,
        47,51,1,0,0,0,48,50,3,34,17,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,
        1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,58,3,26,13,
        0,55,57,3,34,17,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,
        1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,62,5,0,0,1,62,1,1,0,0,0,63,
        67,5,8,0,0,64,66,3,30,15,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,
        0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,30,0,0,71,
        3,1,0,0,0,72,74,5,6,0,0,73,75,5,28,0,0,74,73,1,0,0,0,74,75,1,0,0,
        0,75,76,1,0,0,0,76,78,5,26,0,0,77,79,5,28,0,0,78,77,1,0,0,0,78,79,
        1,0,0,0,79,84,1,0,0,0,80,82,3,6,3,0,81,83,5,28,0,0,82,81,1,0,0,0,
        82,83,1,0,0,0,83,85,1,0,0,0,84,80,1,0,0,0,84,85,1,0,0,0,85,86,1,
        0,0,0,86,87,5,13,0,0,87,88,3,8,4,0,88,89,5,14,0,0,89,90,5,12,0,0,
        90,5,1,0,0,0,91,93,5,16,0,0,92,94,5,28,0,0,93,92,1,0,0,0,93,94,1,
        0,0,0,94,95,1,0,0,0,95,106,5,27,0,0,96,98,5,25,0,0,97,99,5,28,0,
        0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,102,5,27,0,0,101,
        103,5,28,0,0,102,101,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,104,
        106,5,34,0,0,105,91,1,0,0,0,105,96,1,0,0,0,106,7,1,0,0,0,107,111,
        3,12,6,0,108,111,3,10,5,0,109,111,5,28,0,0,110,107,1,0,0,0,110,108,
        1,0,0,0,110,109,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,
        1,0,0,0,113,9,1,0,0,0,114,112,1,0,0,0,115,116,5,21,0,0,116,117,5,
        26,0,0,117,118,5,22,0,0,118,11,1,0,0,0,119,122,3,14,7,0,120,122,
        3,22,11,0,121,119,1,0,0,0,121,120,1,0,0,0,122,13,1,0,0,0,123,125,
        5,10,0,0,124,126,5,28,0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,
        1,0,0,0,127,129,5,26,0,0,128,130,5,28,0,0,129,128,1,0,0,0,129,130,
        1,0,0,0,130,131,1,0,0,0,131,133,3,16,8,0,132,134,5,28,0,0,133,132,
        1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,136,5,12,0,0,136,15,
        1,0,0,0,137,141,5,17,0,0,138,141,5,15,0,0,139,141,3,18,9,0,140,137,
        1,0,0,0,140,138,1,0,0,0,140,139,1,0,0,0,141,17,1,0,0,0,142,143,5,
        18,0,0,143,144,5,24,0,0,144,153,5,19,0,0,145,146,5,18,0,0,146,147,
        5,24,0,0,147,148,5,20,0,0,148,149,3,20,10,0,149,150,5,19,0,0,150,
        151,5,23,0,0,151,153,1,0,0,0,152,142,1,0,0,0,152,145,1,0,0,0,153,
        19,1,0,0,0,154,159,5,35,0,0,155,156,5,20,0,0,156,158,5,35,0,0,157,
        155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,
        21,1,0,0,0,161,159,1,0,0,0,162,164,5,11,0,0,163,165,5,28,0,0,164,
        163,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,168,5,21,0,0,167,
        166,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,171,5,28,0,0,170,
        169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,174,5,26,0,0,173,
        175,5,28,0,0,174,173,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,
        178,5,27,0,0,177,179,5,28,0,0,178,177,1,0,0,0,178,179,1,0,0,0,179,
        180,1,0,0,0,180,205,5,12,0,0,181,183,5,11,0,0,182,184,5,28,0,0,183,
        182,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,187,5,21,0,0,186,
        185,1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,190,5,28,0,0,189,
        188,1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,193,5,26,0,0,192,
        194,5,28,0,0,193,192,1,0,0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,
        197,5,16,0,0,196,198,5,28,0,0,197,196,1,0,0,0,197,198,1,0,0,0,198,
        199,1,0,0,0,199,201,5,27,0,0,200,202,5,28,0,0,201,200,1,0,0,0,201,
        202,1,0,0,0,202,203,1,0,0,0,203,205,5,12,0,0,204,162,1,0,0,0,204,
        181,1,0,0,0,205,23,1,0,0,0,206,208,3,32,16,0,207,206,1,0,0,0,207,
        208,1,0,0,0,208,221,1,0,0,0,209,215,3,26,13,0,210,215,3,28,14,0,
        211,215,5,2,0,0,212,215,5,37,0,0,213,215,5,1,0,0,214,209,1,0,0,0,
        214,210,1,0,0,0,214,211,1,0,0,0,214,212,1,0,0,0,214,213,1,0,0,0,
        215,217,1,0,0,0,216,218,3,32,16,0,217,216,1,0,0,0,217,218,1,0,0,
        0,218,220,1,0,0,0,219,214,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,
        0,221,222,1,0,0,0,222,25,1,0,0,0,223,221,1,0,0,0,224,225,5,7,0,0,
        225,229,5,35,0,0,226,228,3,30,15,0,227,226,1,0,0,0,228,231,1,0,0,
        0,229,227,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,231,229,1,0,0,
        0,232,233,5,29,0,0,233,234,3,24,12,0,234,235,5,7,0,0,235,236,5,32,
        0,0,236,237,5,35,0,0,237,238,5,29,0,0,238,249,1,0,0,0,239,240,5,
        7,0,0,240,244,5,35,0,0,241,243,3,30,15,0,242,241,1,0,0,0,243,246,
        1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,247,1,0,0,0,246,244,
        1,0,0,0,247,249,5,31,0,0,248,224,1,0,0,0,248,239,1,0,0,0,249,27,
        1,0,0,0,250,251,7,0,0,0,251,29,1,0,0,0,252,253,5,35,0,0,253,254,
        5,33,0,0,254,255,5,34,0,0,255,31,1,0,0,0,256,257,7,1,0,0,257,33,
        1,0,0,0,258,259,7,2,0,0,259,35,1,0,0,0,42,37,42,46,51,58,67,74,78,
        82,84,93,98,102,105,110,112,121,125,129,133,140,152,159,164,167,
        170,174,178,183,186,189,193,197,201,204,207,214,217,221,229,244,
        248
    ]

class XMLParser ( Parser ):

    grammarFileName = "XMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<!DOCTYPE'", "'<'", "<INVALID>", 
                     "<INVALID>", "'<!ELEMENT'", "'<!ENTITY'", "<INVALID>", 
                     "'['", "']'", "'ANY'", "'SYSTEM'", "'EMPTY'", "'('", 
                     "')'", "'|'", "'%'", "';'", "'*'", "'#PCDATA'", "'PUBLIC'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "CDATA", "EntityRef", "CharRef", 
                      "SEA_WS", "DOCTYPE", "OPEN", "XMLDeclOpen", "TEXT", 
                      "ELEMENT", "ENTITY", "GT", "LBRACK", "RBRACK", "ANY", 
                      "SYSTEM", "EMPTY", "LPAREN", "RPAREN", "PIPE", "PERCENT", 
                      "SEMI", "ASTERISK", "PCDATA", "PUBLIC", "DTDName", 
                      "DTDSTRING", "DTD_WS", "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", 
                      "SLASH", "EQUALS", "STRING", "Name", "S", "PI" ]

    RULE_document = 0
    RULE_prolog = 1
    RULE_doctypedecl = 2
    RULE_externalID = 3
    RULE_intSubset = 4
    RULE_peReference = 5
    RULE_markupdecl = 6
    RULE_elementdecl = 7
    RULE_contentSpec = 8
    RULE_mixed = 9
    RULE_nameList = 10
    RULE_entityDecl = 11
    RULE_content = 12
    RULE_element = 13
    RULE_reference = 14
    RULE_attribute = 15
    RULE_chardata = 16
    RULE_misc = 17

    ruleNames =  [ "document", "prolog", "doctypedecl", "externalID", "intSubset", 
                   "peReference", "markupdecl", "elementdecl", "contentSpec", 
                   "mixed", "nameList", "entityDecl", "content", "element", 
                   "reference", "attribute", "chardata", "misc" ]

    EOF = Token.EOF
    COMMENT=1
    CDATA=2
    EntityRef=3
    CharRef=4
    SEA_WS=5
    DOCTYPE=6
    OPEN=7
    XMLDeclOpen=8
    TEXT=9
    ELEMENT=10
    ENTITY=11
    GT=12
    LBRACK=13
    RBRACK=14
    ANY=15
    SYSTEM=16
    EMPTY=17
    LPAREN=18
    RPAREN=19
    PIPE=20
    PERCENT=21
    SEMI=22
    ASTERISK=23
    PCDATA=24
    PUBLIC=25
    DTDName=26
    DTDSTRING=27
    DTD_WS=28
    CLOSE=29
    SPECIAL_CLOSE=30
    SLASH_CLOSE=31
    SLASH=32
    EQUALS=33
    STRING=34
    Name=35
    S=36
    PI=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(XMLParser.ElementContext,0)


        def EOF(self):
            return self.getToken(XMLParser.EOF, 0)

        def prolog(self):
            return self.getTypedRuleContext(XMLParser.PrologContext,0)


        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def doctypedecl(self):
            return self.getTypedRuleContext(XMLParser.DoctypedeclContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = XMLParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 36
                self.prolog()


            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 39
                    self.misc() 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 45
                self.doctypedecl()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137438953506) != 0):
                self.state = 48
                self.misc()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.element()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137438953506) != 0):
                self.state = 55
                self.misc()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(XMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrologContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XMLDeclOpen(self):
            return self.getToken(XMLParser.XMLDeclOpen, 0)

        def SPECIAL_CLOSE(self):
            return self.getToken(XMLParser.SPECIAL_CLOSE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_prolog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProlog" ):
                listener.enterProlog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProlog" ):
                listener.exitProlog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProlog" ):
                return visitor.visitProlog(self)
            else:
                return visitor.visitChildren(self)




    def prolog(self):

        localctx = XMLParser.PrologContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prolog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(XMLParser.XMLDeclOpen)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 64
                self.attribute()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(XMLParser.SPECIAL_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoctypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOCTYPE(self):
            return self.getToken(XMLParser.DOCTYPE, 0)

        def DTDName(self):
            return self.getToken(XMLParser.DTDName, 0)

        def LBRACK(self):
            return self.getToken(XMLParser.LBRACK, 0)

        def intSubset(self):
            return self.getTypedRuleContext(XMLParser.IntSubsetContext,0)


        def RBRACK(self):
            return self.getToken(XMLParser.RBRACK, 0)

        def GT(self):
            return self.getToken(XMLParser.GT, 0)

        def DTD_WS(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.DTD_WS)
            else:
                return self.getToken(XMLParser.DTD_WS, i)

        def externalID(self):
            return self.getTypedRuleContext(XMLParser.ExternalIDContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_doctypedecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoctypedecl" ):
                listener.enterDoctypedecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoctypedecl" ):
                listener.exitDoctypedecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoctypedecl" ):
                return visitor.visitDoctypedecl(self)
            else:
                return visitor.visitChildren(self)




    def doctypedecl(self):

        localctx = XMLParser.DoctypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_doctypedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(XMLParser.DOCTYPE)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 73
                self.match(XMLParser.DTD_WS)


            self.state = 76
            self.match(XMLParser.DTDName)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 77
                self.match(XMLParser.DTD_WS)


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16 or _la==25:
                self.state = 80
                self.externalID()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 81
                    self.match(XMLParser.DTD_WS)




            self.state = 86
            self.match(XMLParser.LBRACK)
            self.state = 87
            self.intSubset()
            self.state = 88
            self.match(XMLParser.RBRACK)
            self.state = 89
            self.match(XMLParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExternalIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYSTEM(self):
            return self.getToken(XMLParser.SYSTEM, 0)

        def DTDSTRING(self):
            return self.getToken(XMLParser.DTDSTRING, 0)

        def DTD_WS(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.DTD_WS)
            else:
                return self.getToken(XMLParser.DTD_WS, i)

        def PUBLIC(self):
            return self.getToken(XMLParser.PUBLIC, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_externalID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternalID" ):
                listener.enterExternalID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternalID" ):
                listener.exitExternalID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExternalID" ):
                return visitor.visitExternalID(self)
            else:
                return visitor.visitChildren(self)




    def externalID(self):

        localctx = XMLParser.ExternalIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_externalID)
        self._la = 0 # Token type
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(XMLParser.SYSTEM)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 92
                    self.match(XMLParser.DTD_WS)


                self.state = 95
                self.match(XMLParser.DTDSTRING)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(XMLParser.PUBLIC)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 97
                    self.match(XMLParser.DTD_WS)


                self.state = 100
                self.match(XMLParser.DTDSTRING)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 101
                    self.match(XMLParser.DTD_WS)


                self.state = 104
                self.match(XMLParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntSubsetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def markupdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MarkupdeclContext)
            else:
                return self.getTypedRuleContext(XMLParser.MarkupdeclContext,i)


        def peReference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.PeReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.PeReferenceContext,i)


        def DTD_WS(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.DTD_WS)
            else:
                return self.getToken(XMLParser.DTD_WS, i)

        def getRuleIndex(self):
            return XMLParser.RULE_intSubset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntSubset" ):
                listener.enterIntSubset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntSubset" ):
                listener.exitIntSubset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntSubset" ):
                return visitor.visitIntSubset(self)
            else:
                return visitor.visitChildren(self)




    def intSubset(self):

        localctx = XMLParser.IntSubsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_intSubset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 270535680) != 0):
                self.state = 110
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 11]:
                    self.state = 107
                    self.markupdecl()
                    pass
                elif token in [21]:
                    self.state = 108
                    self.peReference()
                    pass
                elif token in [28]:
                    self.state = 109
                    self.match(XMLParser.DTD_WS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PeReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(XMLParser.PERCENT, 0)

        def DTDName(self):
            return self.getToken(XMLParser.DTDName, 0)

        def SEMI(self):
            return self.getToken(XMLParser.SEMI, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_peReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeReference" ):
                listener.enterPeReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeReference" ):
                listener.exitPeReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPeReference" ):
                return visitor.visitPeReference(self)
            else:
                return visitor.visitChildren(self)




    def peReference(self):

        localctx = XMLParser.PeReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peReference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(XMLParser.PERCENT)
            self.state = 116
            self.match(XMLParser.DTDName)
            self.state = 117
            self.match(XMLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarkupdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementdecl(self):
            return self.getTypedRuleContext(XMLParser.ElementdeclContext,0)


        def entityDecl(self):
            return self.getTypedRuleContext(XMLParser.EntityDeclContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_markupdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMarkupdecl" ):
                listener.enterMarkupdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMarkupdecl" ):
                listener.exitMarkupdecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMarkupdecl" ):
                return visitor.visitMarkupdecl(self)
            else:
                return visitor.visitChildren(self)




    def markupdecl(self):

        localctx = XMLParser.MarkupdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_markupdecl)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.elementdecl()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.entityDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELEMENT(self):
            return self.getToken(XMLParser.ELEMENT, 0)

        def DTDName(self):
            return self.getToken(XMLParser.DTDName, 0)

        def contentSpec(self):
            return self.getTypedRuleContext(XMLParser.ContentSpecContext,0)


        def GT(self):
            return self.getToken(XMLParser.GT, 0)

        def DTD_WS(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.DTD_WS)
            else:
                return self.getToken(XMLParser.DTD_WS, i)

        def getRuleIndex(self):
            return XMLParser.RULE_elementdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementdecl" ):
                listener.enterElementdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementdecl" ):
                listener.exitElementdecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementdecl" ):
                return visitor.visitElementdecl(self)
            else:
                return visitor.visitChildren(self)




    def elementdecl(self):

        localctx = XMLParser.ElementdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elementdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(XMLParser.ELEMENT)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 124
                self.match(XMLParser.DTD_WS)


            self.state = 127
            self.match(XMLParser.DTDName)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 128
                self.match(XMLParser.DTD_WS)


            self.state = 131
            self.contentSpec()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 132
                self.match(XMLParser.DTD_WS)


            self.state = 135
            self.match(XMLParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMPTY(self):
            return self.getToken(XMLParser.EMPTY, 0)

        def ANY(self):
            return self.getToken(XMLParser.ANY, 0)

        def mixed(self):
            return self.getTypedRuleContext(XMLParser.MixedContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_contentSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContentSpec" ):
                listener.enterContentSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContentSpec" ):
                listener.exitContentSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContentSpec" ):
                return visitor.visitContentSpec(self)
            else:
                return visitor.visitChildren(self)




    def contentSpec(self):

        localctx = XMLParser.ContentSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_contentSpec)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(XMLParser.EMPTY)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(XMLParser.ANY)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.mixed()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MixedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(XMLParser.LPAREN, 0)

        def PCDATA(self):
            return self.getToken(XMLParser.PCDATA, 0)

        def RPAREN(self):
            return self.getToken(XMLParser.RPAREN, 0)

        def PIPE(self):
            return self.getToken(XMLParser.PIPE, 0)

        def nameList(self):
            return self.getTypedRuleContext(XMLParser.NameListContext,0)


        def ASTERISK(self):
            return self.getToken(XMLParser.ASTERISK, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_mixed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMixed" ):
                listener.enterMixed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMixed" ):
                listener.exitMixed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMixed" ):
                return visitor.visitMixed(self)
            else:
                return visitor.visitChildren(self)




    def mixed(self):

        localctx = XMLParser.MixedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_mixed)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(XMLParser.LPAREN)
                self.state = 143
                self.match(XMLParser.PCDATA)
                self.state = 144
                self.match(XMLParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(XMLParser.LPAREN)
                self.state = 146
                self.match(XMLParser.PCDATA)
                self.state = 147
                self.match(XMLParser.PIPE)
                self.state = 148
                self.nameList()
                self.state = 149
                self.match(XMLParser.RPAREN)
                self.state = 150
                self.match(XMLParser.ASTERISK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.Name)
            else:
                return self.getToken(XMLParser.Name, i)

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PIPE)
            else:
                return self.getToken(XMLParser.PIPE, i)

        def getRuleIndex(self):
            return XMLParser.RULE_nameList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameList" ):
                listener.enterNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameList" ):
                listener.exitNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameList" ):
                return visitor.visitNameList(self)
            else:
                return visitor.visitChildren(self)




    def nameList(self):

        localctx = XMLParser.NameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_nameList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(XMLParser.Name)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 155
                self.match(XMLParser.PIPE)
                self.state = 156
                self.match(XMLParser.Name)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTITY(self):
            return self.getToken(XMLParser.ENTITY, 0)

        def DTDName(self):
            return self.getToken(XMLParser.DTDName, 0)

        def DTDSTRING(self):
            return self.getToken(XMLParser.DTDSTRING, 0)

        def GT(self):
            return self.getToken(XMLParser.GT, 0)

        def DTD_WS(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.DTD_WS)
            else:
                return self.getToken(XMLParser.DTD_WS, i)

        def PERCENT(self):
            return self.getToken(XMLParser.PERCENT, 0)

        def SYSTEM(self):
            return self.getToken(XMLParser.SYSTEM, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_entityDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityDecl" ):
                listener.enterEntityDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityDecl" ):
                listener.exitEntityDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityDecl" ):
                return visitor.visitEntityDecl(self)
            else:
                return visitor.visitChildren(self)




    def entityDecl(self):

        localctx = XMLParser.EntityDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_entityDecl)
        self._la = 0 # Token type
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(XMLParser.ENTITY)
                self.state = 164
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 163
                    self.match(XMLParser.DTD_WS)


                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 166
                    self.match(XMLParser.PERCENT)


                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 169
                    self.match(XMLParser.DTD_WS)


                self.state = 172
                self.match(XMLParser.DTDName)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 173
                    self.match(XMLParser.DTD_WS)


                self.state = 176
                self.match(XMLParser.DTDSTRING)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 177
                    self.match(XMLParser.DTD_WS)


                self.state = 180
                self.match(XMLParser.GT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(XMLParser.ENTITY)
                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 182
                    self.match(XMLParser.DTD_WS)


                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 185
                    self.match(XMLParser.PERCENT)


                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 188
                    self.match(XMLParser.DTD_WS)


                self.state = 191
                self.match(XMLParser.DTDName)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 192
                    self.match(XMLParser.DTD_WS)


                self.state = 195
                self.match(XMLParser.SYSTEM)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 196
                    self.match(XMLParser.DTD_WS)


                self.state = 199
                self.match(XMLParser.DTDSTRING)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 200
                    self.match(XMLParser.DTD_WS)


                self.state = 203
                self.match(XMLParser.GT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ElementContext)
            else:
                return self.getTypedRuleContext(XMLParser.ElementContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.ReferenceContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CDATA)
            else:
                return self.getToken(XMLParser.CDATA, i)

        def PI(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PI)
            else:
                return self.getToken(XMLParser.PI, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = XMLParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5 or _la==9:
                self.state = 206
                self.chardata()


            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 214
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 209
                        self.element()
                        pass
                    elif token in [3, 4]:
                        self.state = 210
                        self.reference()
                        pass
                    elif token in [2]:
                        self.state = 211
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [37]:
                        self.state = 212
                        self.match(XMLParser.PI)
                        pass
                    elif token in [1]:
                        self.state = 213
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 217
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5 or _la==9:
                        self.state = 216
                        self.chardata()

             
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.Name)
            else:
                return self.getToken(XMLParser.Name, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = XMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(XMLParser.OPEN)
                self.state = 225
                self.match(XMLParser.Name)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 226
                    self.attribute()
                    self.state = 231
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 232
                self.match(XMLParser.CLOSE)
                self.state = 233
                self.content()
                self.state = 234
                self.match(XMLParser.OPEN)
                self.state = 235
                self.match(XMLParser.SLASH)
                self.state = 236
                self.match(XMLParser.Name)
                self.state = 237
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(XMLParser.OPEN)
                self.state = 240
                self.match(XMLParser.Name)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 241
                    self.attribute()
                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 247
                self.match(XMLParser.SLASH_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EntityRef(self):
            return self.getToken(XMLParser.EntityRef, 0)

        def CharRef(self):
            return self.getToken(XMLParser.CharRef, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = XMLParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XMLParser.Name, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = XMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(XMLParser.Name)
            self.state = 253
            self.match(XMLParser.EQUALS)
            self.state = 254
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChardataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(XMLParser.TEXT, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_chardata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChardata" ):
                listener.enterChardata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChardata" ):
                listener.exitChardata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChardata" ):
                return visitor.visitChardata(self)
            else:
                return visitor.visitChildren(self)




    def chardata(self):

        localctx = XMLParser.ChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not(_la==5 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MiscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(XMLParser.COMMENT, 0)

        def PI(self):
            return self.getToken(XMLParser.PI, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_misc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMisc" ):
                listener.enterMisc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMisc" ):
                listener.exitMisc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMisc" ):
                return visitor.visitMisc(self)
            else:
                return visitor.visitChildren(self)




    def misc(self):

        localctx = XMLParser.MiscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137438953506) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





