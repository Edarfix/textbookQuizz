function setup_drag_drop() {

const words = document.querySelectorAll('.ddword');
const categories = document.querySelectorAll('.ddcategory');
const wordList = document.getElementById('ddwordList'); // Liste initiale des mots

words.forEach(word => {
  word.addEventListener('dragstart', dragStart);
  word.addEventListener('dragend', dragEnd);
});

categories.forEach(category => {
  category.addEventListener('dragover', dragOver);
  category.addEventListener('dragenter', dragEnter);
  category.addEventListener('dragleave', dragLeave);
  category.addEventListener('drop', drop);
});

// Variables pour stocker l'élément glissé
let draggedElement = null;

function dragStart(e) {
  draggedElement = e.target; // Stocke l'élément glissé
  e.dataTransfer.setData('text/plain', draggedElement.dataset.category);
  setTimeout(() => draggedElement.style.display = "none", 0); // Cache temporairement
}

function dragEnd(e) {
  draggedElement.style.display = "block"; // Réaffiche l'élément
  draggedElement = null; // Réinitialise
}

function dragOver(e) {
  e.preventDefault(); // Permet le drop
}

function dragEnter(e) {
  e.preventDefault(); // Nécessaire pour dragOver
  if (e.target.classList.contains('ddcategory')) {
    e.target.classList.add('drag-over');
  }
}

function dragLeave(e) {
  e.target.classList.remove('drag-over');
}

function drop(e) {
  e.preventDefault();
  e.target.classList.remove('drag-over');
  if (e.target.classList.contains('ddcategory')) {
    e.target.appendChild(draggedElement); // Ajoute l'élément glissé dans la catégorie
  } else {
    wordList.appendChild(draggedElement); // Retourne dans la liste initiale
  }
}
}

function checkAnswers() {
    const words = document.querySelectorAll('.ddword');
const categories = document.querySelectorAll('.ddcategory');

  const resultDiv = document.getElementById('ddresult');
  let score = 0;
  const totalWords = words.length;

  // Réinitialise les couleurs
  words.forEach(word => {
    word.classList.remove('correct', 'incorrect');
  });

  // Vérifie chaque catégorie
  categories.forEach(category => {
    const expectedCategory = category.dataset.category;
    const items = category.querySelectorAll('.ddword');
    items.forEach(item => {
      if (item.dataset.category === expectedCategory) {
        item.classList.add('correct'); // Colore en vert si correct
        score++;
      } else {
        item.classList.add('incorrect'); // Colore en rouge si incorrect
      }
    });
  });

  // Affiche le score
  resultDiv.textContent = `Votre score est : ${score} / ${totalWords}`;
}

