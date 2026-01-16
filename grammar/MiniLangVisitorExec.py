
class MiniLangInterpreter:
    def __init__(self):
        self.memory = {}
        self.output = []
    
    def execute(self, tree):
        """Ejecuta el árbol de análisis sintáctico"""
        self._visit(tree)
        return "\n".join(self.output) if self.output else "✅ Programa ejecutado correctamente (sin salida)"
    
    def _visit(self, node):
        """Visita recursivamente cada nodo del árbol"""
        if node is None:
            return 0
        
        
        rule_name = type(node).__name__
        
        
        if rule_name == 'ProgramContext':
            for stmt in node.statement():
                self._visit(stmt)
            return None
        
        
        elif rule_name == 'StatementContext':
            
            if node.ID() and node.expr():
                var_name = node.ID().getText()
                value = self._visit(node.expr())
                self.memory[var_name] = value
            
            
            elif node.getChildCount() > 0 and node.getChild(0).getText() == 'print':
                value = self._visit(node.expr())
                self.output.append(str(value))
            
            
            elif node.ifStatement():
                self._visit(node.ifStatement())
            
            
            elif node.forStatement():
                self._visit(node.forStatement())
        
        
        elif rule_name == 'IfStatementContext':
            condition = self._visit(node.condition())
            all_statements = node.statement()
            
            
            has_else = False
            for child in node.children:
                if hasattr(child, 'getText') and child.getText() == 'else':
                    has_else = True
                    break
            
            if has_else:
                
                stmt_count_before_else = 0
                for child in node.children:
                    if hasattr(child, 'getText') and child.getText() == 'else':
                        break
                    if child in all_statements:
                        stmt_count_before_else += 1
                
                if_statements = all_statements[:stmt_count_before_else]
                else_statements = all_statements[stmt_count_before_else:]
                
                if condition:
                    for stmt in if_statements:
                        self._visit(stmt)
                else:
                    for stmt in else_statements:
                        self._visit(stmt)
            else:
                if condition:
                    for stmt in all_statements:
                        self._visit(stmt)
        
        
        elif rule_name == 'ForStatementContext':
            
            all_exprs = node.expr()
            
            
            var_name = node.ID(0).getText()
            init_value = self._visit(all_exprs[0])
            self.memory[var_name] = init_value
            
            
            while self._visit(node.condition()):
                
                for stmt in node.statement():
                    self._visit(stmt)
                
                
                update_var = node.ID(1).getText()
                update_value = self._visit(all_exprs[1])
                self.memory[update_var] = update_value
        
        
        elif rule_name == 'ConditionContext':
            all_exprs = node.expr()
            left = self._visit(all_exprs[0])
            right = self._visit(all_exprs[1])
            op = node.comparisonOp().getText()
            
            if op == "==": return left == right
            elif op == "!=": return left != right
            elif op == "<": return left < right
            elif op == "<=": return left <= right
            elif op == ">": return left > right
            elif op == ">=": return left >= right
            return False
        
        
        elif rule_name == 'ExprContext':
            
            if node.INT():
                return int(node.INT().getText())
            
            
            elif node.ID():
                var_name = node.ID().getText()
                return self.memory.get(var_name, 0)
            
            
            elif hasattr(node, 'op') and node.op:
                all_exprs = node.expr()
                left = self._visit(all_exprs[0])
                right = self._visit(all_exprs[1])
                
                if node.op.text == "+": return left + right
                elif node.op.text == "-": return left - right
                elif node.op.text == "*": return left * right
                elif node.op.text == "/": return left // right if right != 0 else 0
            
            
            elif node.getChildCount() == 3 and node.getChild(0).getText() == '(':
                all_exprs = node.expr()
                return self._visit(all_exprs[0])
            
            return 0
        
        return 0