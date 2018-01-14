#Token types
#
#EOF(end of file)token is used to indicate that there is no more input left for ananlynis

INTEGER, PLUS, MINUS, MULTI, DIVID, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTI', "DIVID", 'EOF'
OperKey = {PLUS : '+', MINUS : '-', 'MULTI' : '*', DIVID : '/'} 

class Token(object):
    def __init__(self, type, value):
        #Token type: INTERGER, PULS or EOF
        self.type = type
        #Token value:0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
        )
    
    def __repr__(self):
        return self.__str__(self)

class Operator(object):
    def __init__(self, left, right):
        if left.type != right.type:
            raise TypeError
        self.left = left
        self.right = right

    def calc(self):
        pass

class Operator_Plus(Operator):
    def calc(self):
        return Token(self.left.type, self.left.value + self.right.value)

class Operator_Minus(Operator):
    def calc(self):
        return Token(self.left.type, self.left.value - self.right.value)

class Operator_Multi(Operator):
    def calc(self):
        return Token(self.left.type, self.left.value * self.right.value)
    
class Operator_Divid(Operator):
    def calc(self):
        return Token(self.left.type, self.left.value / self.right.value)

def OperatorFactory(left, right, op):
    if op.type == PLUS:
        return Operator_Plus(left, right)
    if op.type == MINUS:
        return Operator_Minus(left, right)
    if op.type == MULTI:
        return Operator_Multi(left, right)
    if op.type == DIVID:
        return Operator_Divid(left, right)
    raise ValueError


class Interpreter(object):
    def __init__(self, text):
        #client string input, e.g. "3 + 5"
        self.text = text
        #self.pos is a index to self.text
        self.pos = 0
        #current token instance
        self.current_toke = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def operator(self):
        for k, v in OperKey.items():
            if v == self.current_char:
                self.advance()
                return (k, v)
        else:
            self.error()

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            return Token(*self.operator())
    
    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(left.type)
        while self.current_char is not None:
            op = self.current_token
            self.eat(op.type)
            right = self.current_token
            self.eat(right.type)
            opr = OperatorFactory(left, right, op)
            left = opr.calc()
        return left.value

def main():
    while True:
        #'''
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            #text = raw_input('calc> ')
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        #'''
        #text = "10 / 5"
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)
        break


if __name__ == '__main__':
    main()