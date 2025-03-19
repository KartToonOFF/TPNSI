const uploadForm = document.querySelector(".uploadForm");
const results = document.querySelector(".results");

uploadForm.addEventListener("submit", async(e) =>{
    e.preventDefault(); 

    const formData = new FormData();
    const image = document.querySelector('.image').files[0];
    formData.append('image', image);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if(response.ok) {
            const data = await response.json();

            if (data.results) {
                results.innerHTML = '<h3>Résultats :</h3><p>Téléchargement de l image réussi </p>';
            } else {
                results.innerHTML = `<p>Aucune image trouvée.</p>`;
            }

        } else {
            throw new Error('Erreur lors de upload')
        }
    } catch (error){
        console.log(error)
        results.innerHTML = `<p>Une erreur est survenue lors de l'envoi de l'image.</p>`;
    }
})

const dragdrop = document.querySelector(".dragDrop");