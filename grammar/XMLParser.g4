/*
 [The "BSD licence"]
 Copyright (c) 2013 Terence Parr
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/** XML parser derived from ANTLR v4 ref guide book example */

// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

parser grammar XMLParser;

options {
    tokenVocab = XMLLexer;
}

document
    : prolog? misc*  doctypedecl? misc* element misc* EOF
    ;


prolog
    : XMLDeclOpen attribute* SPECIAL_CLOSE
    ;

doctypedecl
    : DOCTYPE DTD_WS? DTDName DTD_WS? (externalID DTD_WS?)? LBRACK intSubset RBRACK GT
    ;

externalID
    : SYSTEM DTD_WS? DTDSTRING
    | PUBLIC DTD_WS? DTDSTRING DTD_WS? STRING
    ;

intSubset
    : (markupdecl | peReference | DTD_WS)*
    ;

peReference
    : PERCENT DTDName SEMI
    ;

markupdecl
    : elementdecl
    | entityDecl
    ;

elementdecl
    : ELEMENT DTD_WS? DTDName DTD_WS? contentSpec DTD_WS? GT
    ;

contentSpec
    : EMPTY
    | ANY
    | mixed
    ;

mixed
    : LPAREN PCDATA RPAREN
    | LPAREN PCDATA PIPE nameList RPAREN ASTERISK
    ;

nameList
    : Name (PIPE Name)*
    ;

entityDecl
    : ENTITY DTD_WS? PERCENT? DTD_WS? DTDName DTD_WS? DTDSTRING DTD_WS? GT             // internal general or parameter entity
    | ENTITY DTD_WS? PERCENT? DTD_WS? DTDName DTD_WS? SYSTEM DTD_WS? DTDSTRING DTD_WS? GT // external general or parameter entity
    ;

content
    : chardata? ((element | reference | CDATA | PI | COMMENT) chardata?)*
    ;

element
    : '<' Name attribute* CLOSE content '<' '/' Name CLOSE
    | '<' Name attribute* '/>'
    ;

reference
    : EntityRef
    | CharRef
    ;

attribute
    : Name '=' STRING
    ; // Our STRING is AttValue in spec

/** ``All text that is not markup constitutes the character data of
 *  the document.''
 */
chardata
    : TEXT
    | SEA_WS
    ;

misc
    : COMMENT
    | PI
    | SEA_WS
    ;