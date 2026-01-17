grammar MiniLang;

program
    : statement* EOF
    ;

statement
    : ID '=' expr                     
    | 'print' '(' expr ')'            
    | ifStatement
    | forStatement                    
    ;

ifStatement
    : 'if' '(' condition ')' '{' statement* '}' ('else' '{' statement* '}')?
    ;

forStatement
    : 'for' '(' ID '=' expr ';' condition ';' ID '=' expr ')' '{' statement* '}'
    ;

condition
    : expr comparisonOp expr
    ;

comparisonOp
    : '==' | '!=' | '<' | '<=' | '>' | '>='
    ;

expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | INT
    | ID
    | '(' expr ')'
    ;

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;