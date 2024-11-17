import json

def generate_quiz_html(input_file, output_file):
    # Load JSON data from the input file
    with open(input_file, 'r') as f:
        quiz_data = json.load(f)
    
    # Start building the HTML content
    html_content = '''
    <div class="container">
      <form id="quizForm">
    '''
    
    # Generate questions and options
    for idx, question_data in enumerate(quiz_data):
        question_number = idx + 1
        html_content += f'''
        <!-- Question {question_number} -->
        <div class="question">
          <h2>{question_number}. {question_data["question"]}</h2>
          <ul class="options">
        '''
        for option in question_data["options"]:
            html_content += f'''
            <li>
              <label>
                <input type="checkbox" name="question{question_number}" value="{option["value"]}"> {option["text"]}
              </label>
            </li>
            '''
        html_content += f'''
          </ul>
          <div class="qexplanation" id="{question_number}" style="display:none">
            {question_data["explanation"]}
          </div>
        </div>
        '''
    
    # Add submit button and result section
    html_content += '''
        <button type="button" class="submit-btn" onclick="evaluateQuiz()">Soumettre</button>
      </form>
      <div class="result" id="qresult"></div>
    </div>
    '''
    
    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    print(f"HTML quiz generated successfully: {output_file}")

# Main logic
if __name__ == "__main__":
    input_filename = input("Enter the input JSON filename (e.g., quiz_questions.json): ")
    output_filename = input("Enter the output HTML filename (e.g., quiz.html): ")

    # Validate file extensions
    if not input_filename.endswith(".json"):
        print("Error: Input file must be a .json file.")
    elif not output_filename.endswith(".html"):
        print("Error: Output file must be a .html file.")
    else:
        # Generate HTML
        generate_quiz_html(input_filename, output_filename)
