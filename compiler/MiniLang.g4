grammar MiniLang;

program : statement* EOF ;  // EOF final obligatorio

statement
    : ID '=' expr      # assing
    | 'print' '(' expr ')' # printStmt
    ;

expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | INT
    | ID
    | '(' expr ')'
    ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;  // ignora espacios y saltos de línea
