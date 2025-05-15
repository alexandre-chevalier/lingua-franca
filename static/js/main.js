document.getElementById("form").addEventListener("submit", function(e){
    e.preventDefault();
    const text = document.getElementById('text_to_translate').value;
    const lang = document.getElementById("select_lang").value;

    fetch("/traitement", {
        method : 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            texte: text,
            lang : lang
        })
    })
    .then(response => response.json())
    .then( data => {
        document.getElementById("output").textContent = data.message;
    })
    .catch(error => {
        console.error("Erreur", error);
    })
})
 
 


