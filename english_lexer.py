import ply.lex as lex

# Token list
tokens = (
    'PLEASE',
    'GIVE_ME',
    'SHOW',
    'UPDATE',
    'ALL_THE_INFORMATION',
    'NAME',
    'ROLL_NUMBER',
    'CPI',
    'WHERE',
    'COMPARISON_OPERATOR',
    'STRING',
    'NUMBER',
    'AND',
    'TABLE_NAME',
    'FROM',
    'HAVING',
    'TO',
    'VALUE',
    'MAJOR',
    'SALARY',
    'DELETE',
    'INSERT',
    'INTO',
    'VALUES',
    'ASHUTOSH',
    'NANDINI',
    'VASU'
)

def t_ASHUTOSH(t):
    r'Ashutosh|ashutosh'
    return t

def t_NANDINI(t):
    r'Nandini|nandini'
    return t

def t_VASU(t):
    r'Vasu|vasu'
    return t

# Token regular expressions
def t_TABLE_NAME(t):
    r'students|Students|Faculty|faculty'  # Define pattern for table names (letters, numbers, and underscores, starting with a letter or underscore)
    return t

def t_PLEASE(t):
    r'Please|please'
    return t

def t_HAVING(t):
    r'Having|having'
    return t

def t_TO(t):
    r'To|to'
    return t

def t_FROM(t):
    r'From|from|of\s+the'
    return t

def t_GIVE_ME(t):
    r'give\s+me|Give\s+me'
    return t

def t_SHOW(t):
    r'show|Show'
    return t

def t_UPDATE(t):
    r'update|Update'
    return t

def t_DELETE(t):
    r'delete|Delete'
    return t

def t_INSERT(t):
    r'insert|Insert'
    return t

def t_INTO(t):
    r'into|Into'
    return t

def t_VALUES(t):
    r'values|Values'
    return t

def t_ALL_THE_INFORMATION(t):
    r'all\s+the\s+information|All\s+the\s+information'
    return t

def t_NAME(t):
    r'name|Name'
    return t

def t_ROLL_NUMBER(t):
    r'roll_number|Roll_number|roll_no|Roll_no'
    return t

def t_CPI(t):
    r'cpi|CPI'
    return t

def t_MAJOR(t):
    r'major|MAJOR'
    return t

def t_SALARY(t):
    r'salary|SALARY'
    return t

def t_WHERE(t):
    r'where|Where'
    return t

def t_COMPARISON_OPERATOR(t):
    r'equal\s+to|not\s+equal\s+to|greater\s+than|less\s+than|greater\s+than\s+equal\s+to|less\s+than\s+equal\s+to'
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_AND(t):
    r'and|And'
    return t

#rule to take strings
def t_VALUE(t):
    r'[A-Za-z0-9_]+'
    return t

# Ignored characters (whitespace)
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
