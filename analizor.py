import ply.lex as lex

# Define keywords
keywords = {
    'WRITE': 'WRITE',
    'READ': 'READ',
    'IF': 'IF',
    'ELSE': 'ELSE',
    'RETURN': 'RETURN',
    'BEGIN': 'BEGIN',
    'END': 'END',
    'MAIN': 'MAIN',
    'STRING': 'STRING',
    'INT': 'INT',
    'REAL': 'REAL'
}

# List of tokens
tokens = [
    'IDENT', 'INT_CONSTANT', 'REAL_CONSTANT', 'QSTRING',
    'SEMICOLON', 'COMMA', 'LPAREN', 'RPAREN',
    'ASSIGN_OP', 'EQ', 'NEQ', 'ADD_OP', 'MULT_OP',
    'COMMENT'
] + list(keywords.values())

# Regular expressions for simple tokens
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN_OP = r':='
t_EQ = r'=='
t_NEQ = r'!='
t_ADD_OP = r'\+|\-'
t_MULT_OP = r'\*|/'

# Regular expression for identifiers (IDENT)
def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENT')  # Check if it is a keyword
    return t

# Regular expressions for numeric constants (INT_CONSTANT, REAL_CONSTANT)
def t_REAL_CONSTANT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT_CONSTANT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regular expression for string literals (QSTRING)
def t_QSTRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

# Comments
def t_COMMENT(t):
    r'/\*\*.*?\*/'
    pass  # Ignore comments

# Newline (useful for tracking line numbers in analysis)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Main function for testing the lexer
def test_lexer():
    # Build the lexer
    lexer = lex.lex()
    
    # Read the input file
    file_name = input("Enter the input file name: ")
    with open(file_name) as f:
        contents = f.read()
    
    # Process the file contents
    lexer.input(contents)
    
    # Iterate and display recognized tokens
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == '__main__':
    test_lexer()
