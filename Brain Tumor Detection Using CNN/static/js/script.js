document.addEventListener('DOMContentLoaded', function() {
    const imageUpload = document.getElementById('imageUpload');
    const imagePreview = document.getElementById('imagePreview');
    const imageSection = document.querySelector('.image-section');
    const btnPredict = document.getElementById('btn-predict');
    const result = document.getElementById('result');
    const loader = document.querySelector('.loader');

    // Show image preview and button when file is selected
    imageUpload.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imageSection.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });

    // Handle prediction when button is clicked
    btnPredict.addEventListener('click', function() {
        const file = imageUpload.files[0];
        if (!file) {
            alert('Please upload an image first.');
            return;
        }

        // Show loader while processing
        loader.style.display = 'block';

        // FormData to send file via POST request
        const formData = new FormData();
        formData.append('file', file);

        fetch('/predict', { // Ensure this matches your Flask route
            method: 'POST',
            body: formData
        })
        .then(response => response.json()) // Expecting JSON response
        .then(data => {
            loader.style.display = 'none'; // Hide loader
            if (data.result) {
                result.innerHTML = `<span>${data.result}</span>`;
            } else {
                result.innerHTML = '<span>Error occurred. No result received.</span>';
            }
        })
        .catch(error => {
            loader.style.display = 'none'; // Hide loader on error
            console.error('Error:', error);
            result.innerHTML = '<span>Error occurred.</span>';
        });
    });
});
