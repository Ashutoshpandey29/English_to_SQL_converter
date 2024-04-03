import ply.yacc as yacc
from english_lexer import tokens

# Define the grammar rules
def p_command(p):
    '''command : PLEASE action attributes FROM table conditions'''
    p[0] = (p[2], p[5], p[3], p[6])  # Passing 'table' as the 4th element
    #add command for insert statement as well

def p_command2(p):
    '''command : PLEASE action attributes INTO table VALUES attributes'''
    p[0] = (p[2], p[5], p[7], p[3])  # Passing 'table' as the 4th element

def p_action(p):
    '''action : GIVE_ME
              | SHOW
              | DELETE
              | INSERT
              | UPDATE'''
    p[0] = p[1]

def p_attributes(p):
    '''attributes : ALL_THE_INFORMATION
                  | attribute_list'''
    p[0] = p[1]

def p_attribute_list(p):
    '''attribute_list : attribute_list_item AND attribute
                      | attribute_list_item'''
    if len(p) > 2:
        p[0] = p[1] + ", " + p[3]
    else:
        p[0] = p[1]

def p_attribute_list_item(p):
    '''attribute_list_item : attribute'''
    p[0] = p[1]

def p_attribute(p):
    '''attribute : NAME
                 | ROLL_NUMBER
                 | MAJOR
                 | SALARY
                 | CPI'''
    p[0] = p[1]

def p_conditions(p):
    '''conditions : WHERE condition_list
                  | HAVING condition_list
                  |'''
    if len(p) > 1:
        p[0] = p[2]
    else:
        p[0] = []

def p_condition_list(p):
    '''condition_list : condition_list_item AND condition
                      | condition
                      | condition TO value'''
    if len(p) > 2:
        
        old=p[1][2]
        now=p[3]
        p[0] = (p[1],old,now)
        print(p[1],old,now)
    else:
        p[0] = p[1]

def p_condition_list_item(p):
    '''condition_list_item : attribute COMPARISON_OPERATOR value'''
    p[0] = (p[1], p[2], p[3])

def p_condition(p):
    '''condition : attribute COMPARISON_OPERATOR value'''
    p[0] = (p[1], p[2], p[3])

def p_value(p):
    '''value : STRING
             | VALUE
             | ASHUTOSH
             | NANDINI
             | VASU
             | NUMBER'''
    p[0] = p[1]

def p_table(p):
    '''table : TABLE_NAME'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Define SQL query generation based on parsed input
def generate_sql(action, table, attributes, conditions):
    if action == "give me":
        if attributes == "all the information":
            return f"SELECT * FROM {table}" + (f" WHERE {conditions[0]} = {conditions[2]}" if conditions else "")

        if (len(conditions)==0):
            return f"SELECT {attributes} FROM {table}"

        if conditions[1] == "equal to":
            if isinstance(conditions[2], str):
                return f"SELECT {attributes} FROM {table} WHERE {conditions[0]} = '{conditions[2]}'"
            else:
                return f"SELECT {attributes} FROM {table} WHERE {conditions[0]} = {conditions[2]}"
            
        elif(conditions[1]=="greater than"):
            return f"SELECT {attributes}  FROM {table}" + (f" WHERE {conditions[0]} > {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="less than"):
            return f"SELECT {attributes} FROM {table}" + (f" WHERE {conditions[0]} < {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="greater than equal to"):
            return f"SELECT {attributes}  FROM {table}" + (f" WHERE {conditions[0]} >= {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="less than equal to"):
            return f"SELECT {attributes}  FROM {table}" + (f" WHERE {conditions[0]} <= {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="not equal to"):
            return f"SELECT {attributes}  FROM {table}" + (f" WHERE {conditions[0]} != {conditions[2]}" if conditions else "")

        else:
            return f"SELECT {attributes} FROM {table}" + (f" WHERE {conditions}" if conditions else "")
    elif action == "show":
        if attributes == "all the information":
            return f"SELECT * FROM {table}" + (f" WHERE {conditions[0]} = {conditions[2]}" if conditions else "")

        if (len(conditions)==0):
            return f"SELECT {attributes} FROM {table}" 

        if(conditions[1]=="equal to"):
            return f"SELECT {attributes} FROM {table}" + (f" WHERE {conditions[0]} = {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="greater than"):
            return f"SELECT {attributes}  FROM {table}" + (f" WHERE {conditions[0]} > {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="less than"):
            return f"SELECT {attributes} FROM {table}" + (f" WHERE {conditions[0]} < {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="greater than equal to"):
            return f"SELECT {attributes}  FROM {table}" + (f" WHERE {conditions[0]} >= {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="less than equal to"):
            return f"SELECT {attributes}  FROM {table}" + (f" WHERE {conditions[0]} <= {conditions[2]}" if conditions else "")
            
        elif(conditions[1]=="not equal to"):
            return f"SELECT {attributes}  FROM {table}" + (f" WHERE {conditions[0]} != {conditions[2]}" if conditions else "")

        else:
            return f"SELECT {attributes} FROM {table}" + (f" WHERE {conditions}" if conditions else "")
    elif action == "update":
        if conditions:
            print(conditions)
            if(conditions[0][1]=="equal to"):
                return f"UPDATE {table} SET {attributes} = {conditions[2]} where {conditions[0][0]}={conditions[1]}"
            
            elif(conditions[0][1]=="greater than"):
                return f"UPDATE {table} SET {attributes} = {conditions[2]} where {conditions[0][0]}>{conditions[1]}"

            elif(conditions[0][1]=="less than"):
                return f"UPDATE {table} SET {attributes} = {conditions[2]} where {conditions[0][0]}<{conditions[1]}"
            
            elif(conditions[0][1]=="greater than equal to"):
                return f"UPDATE {table} SET {attributes} = {conditions[2]} where {conditions[0][0]}>={conditions[1]}"
            
            elif(conditions[0][1]=="less than equal to"):
                return f"UPDATE {table} SET {attributes} = {conditions[2]} where {conditions[0][0]}<={conditions[1]}"
            
            elif(conditions[0][1]=="not equal to"):
                return f"UPDATE {table} SET {attributes} = {conditions[2]} where {conditions[0][0]}!={conditions[1]}"
        
        else:
            return f"UPDATE {table} SET {attributes}"

    elif action == "delete":
        if conditions:
            if(conditions[1]=="equal to"):
                return f"DELETE FROM {table} where {conditions[0]}={conditions[2]}"

            elif(conditions[1]=="greater than"):
                return f"DELETE FROM {table} where {conditions[0]}>{conditions[2]}"

            elif(conditions[1]=="less than"):
                return f"DELETE FROM {table} where {conditions[0]}<{conditions[2]}"

            elif(conditions[1]=="greater than equal to"):
                return f"DELETE FROM {table} where {conditions[0]}>={conditions[2]}"

            elif(conditions[1]=="less than equal to"):
                return f"DELETE FROM {table} where {conditions[0]}<={conditions[2]}"

            elif(conditions[1]=="not equal to"):
                return f"DELETE FROM {table} where {conditions[0]}!={conditions[2]}"

        else:
            return f"DELETE FROM {table}"

    elif action == "insert":
        return f"INSERT INTO {table} VALUES {attributes}"
def sql(input_text):
    while True:
        try:
            # input_text = input("Enter an English sentence (or 'quit' to exit): ")
            # if input_text.lower() == 'quit':
            #     break
            result = parser.parse(input_text)
            if result:
                action, table, attributes, conditions = result
                print("Action:", action)
                print("Attributes:", attributes)
                print("Conditions:", conditions)
                print("Table:", table)  # Print the table name
                # Generate SQL query based on parsed input
                query = generate_sql(action, table, attributes, conditions)
                return query
                #query_builder.build_query(query)
                #print("SQL Query:", query)
                #break
            else:
                print("Unable to parse input.")
                break
        # except KeyboardInterrupt:
        #     print("\nExiting...")
        #     break
        except Exception as e:
            print("")
            break