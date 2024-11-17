function evaluateQuiz() {
    const form = document.getElementById('quizForm');
    const resultDiv = document.getElementById('qresult');
    const explanationDiv = document.getElementById('qexplanation');

    let score = 0;
    let totalQuestions = 0;

    // Parcourir les questions
    const questions = form.querySelectorAll('.question');
    questions.forEach(question => {
      totalQuestions++;
      const inputs = question.querySelectorAll('input[type="checkbox"]');
      let isCorrect = true;

      inputs.forEach(input => {
        const label = input.parentElement;
        if (input.checked && input.value === "incorrect") {
          label.classList.add("incorrect");
          isCorrect = false;
        } else if (input.value === "correct") {
          label.classList.add("correct");
          if (!input.checked) {
            isCorrect = false;
          }
        }
      });
      expl = question.querySelector('div.qexplanation');
      console.log(expl);
      expl.style.display = 'initial'; // show explanation

      if (isCorrect) {
        score++;
      }
    });

    // Afficher le score
    resultDiv.textContent = `Votre score est : ${score} / ${totalQuestions}`;

  }
