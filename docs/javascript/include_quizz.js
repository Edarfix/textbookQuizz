// Function to embed the HTML

async function embedHtmlAtEnd(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const htmlContent = await response.text();
        
        const container = document.getElementById("quizz_container");
        container.innerHTML = htmlContent;
} catch (error) {
        console.error('Error embedding HTML:', error);
    }
}

