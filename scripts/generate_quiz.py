import json
import os

def generate_quiz_html(input_file, output_file):
    # Load JSON data from the input file
    with open(input_file, 'r') as f:
        quiz_data = json.load(f)
    
    # Start building the HTML content
    html_content = '<tr>\n'
    
    for index, item in enumerate(quiz_data):
        if index % 2 == 0 and index > 0:
            html_content += '</tr>\n<tr>\n'  # Start a new row every 2 questions

        html_content += f'''
        <td>
        <div>
            <p class="question">{index + 1}. {item["question"]}</p>
            <ul>
        '''
        for option_index, option in enumerate(item["options"]):
            is_correct = option_index == item["correctIndex"]
            id_attr = f'id="correctString{index + 1}"' if is_correct else ""
            value_attr = 'value="1"' if is_correct else 'value="0"'
            html_content += f'''
            <input class="answer" type="radio" name="q{index + 1}" {value_attr}>
            <label {id_attr}>{option}</label>
            <br>
            '''

        html_content += '''
            </ul>
        </div>
        </td>
        '''
    
    html_content += '</tr>\n'

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    print(f"HTML quiz generated successfully: {output_file}")

# Main logic
if __name__ == "__main__":
    input_filename = input("Enter the input JSON filename (e.g., section_X_quiz.json): ")
    output_filename = input("Enter the output HTML filename (e.g., quiz.html): ")

    # Validate file extensions
    if not input_filename.endswith(".json"):
        print("Error: Input file must be a .json file.")
    elif not output_filename.endswith(".html"):
        print("Error: Output file must be a .html file.")
    elif not os.path.exists(input_filename):
        print("Error: Input file does not exist.")
    else:
        # Generate HTML
        generate_quiz_html(input_filename, output_filename)
