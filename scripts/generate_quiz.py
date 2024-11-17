import json
import os


def generate_quiz_html(input_path, output_path):
    # Load JSON data from the input file
    with open(input_path, 'r') as f:
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
    with open(output_path, 'w') as f:
        f.write(html_content)
    
    print(f"HTML quiz generated successfully: {output_path}")

# Main logic
if __name__ == "__main__":
    # Set the input and output paths
    input_path = os.getcwd()+"/docs/quizzes/json/"
    output_path = os.getcwd()+"/docs/quizzes/html/"

    # Process all JSON files in the input directory
    for filename in os.listdir(input_path):
        if filename.endswith(".json"):
            input_filename = os.path.join(input_path, filename)
            output_filename = os.path.join(output_path, filename.replace(".json", ".html"))
            
            # Generate HTML
            try:
                generate_quiz_html(input_filename, output_filename)
                print(f"Generated: {output_filename}")
            except Exception as e:
                print(f"Error processing {input_filename}: {e}")
