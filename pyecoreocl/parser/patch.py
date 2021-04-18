import antlr4


antlr4.ParserRuleContext.text = property(lambda self: self.getText())
