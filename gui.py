import tkinter as tk
import mysql.connector
import english_parser

def submit_data():
    user_input = input_box.get()
    query = english_parser.sql(user_input)  # Generate SQL query using user input
    output_box2.delete(1.0, tk.END)  # Clear existing text in output_box
    print(query)
    output_box2.insert(tk.END, "Generated SQL Query:\n" + query)  # Print generated SQL query
    execute_query(query)  # Execute the generated SQL query

def execute_query(query):
    # Replace these credentials with your MySQL database credentials
    db = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="",
    )

    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    db.commit()

    # Clear existing text in output_box
    output_box.delete(1.0, tk.END)

    # Display fetched data in the output_box with proper formatting
    for row in data:
        formatted_row = '\t\t'.join(map(str, row)) + '\n\n'  # Add extra newline for spacing
        output_box.insert(tk.END, formatted_row)

    db.close()

root = tk.Tk()
root.title("English to SQL Converter")

# Define font style
font_style = ('Helvetica', 12, "bold")

# Create a frame
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)  # Adjust padding

# Create two subframes
left_frame = tk.Frame(frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Add dark blue strip with heading in the left frame
header_label = tk.Label(left_frame, text="ENGLISH TO SQL CONVERTER", font=('Times New Roman', 14, 'bold'), bg='dark blue', fg='white')
header_label.pack(fill=tk.X)

# Adding Background Image to Left Frame
bg_image = tk.PhotoImage(file="im.png")
bg_label = tk.Label(left_frame, image=bg_image)
bg_label.pack(fill=tk.BOTH, expand=True)

# Right Frame (Data Submission)
submit_label = tk.Label(right_frame, text="Enter the sentence for which you want to generate SQL query:", font=font_style)
submit_label.pack(pady=10)

input_box = tk.Entry(right_frame, font=font_style, width=50)  # Reduce width of the input box
input_box.pack(pady=10)

submit_button = tk.Button(right_frame, text="Submit", font=font_style, command=submit_data, bg='dark blue', fg='white')
submit_button.pack(pady=10)

output_box = tk.Text(right_frame, font=font_style, height=10, bg='light blue')  # Adjust height of output_box
output_box.pack(pady=10)

output_box2 = tk.Text(right_frame, font=font_style, height=3)  # Adjust height of output_box2
output_box2.pack(pady=10)

root.mainloop()
