document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const uploadForm = document.getElementById('upload-form');
    const imageInput = document.getElementById('image-upload');
    const fileName = document.getElementById('file-name');
    const promptInput = document.getElementById('prompt-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('image-preview');
    const loadingIndicator = document.getElementById('loading-indicator');
    const resultContainer = document.getElementById('result-container');
    const resultContent = document.getElementById('result-content');
    const errorContainer = document.getElementById('error-container');
    const errorMessage = document.getElementById('error-message');
    
    // Ensure spinner is hidden at startup
    loadingIndicator.classList.add('hidden');
    loadingIndicator.style.display = 'none';

    // Handle file selection
    imageInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        
        if (file) {
            fileName.textContent = file.name;
            analyzeBtn.disabled = false;
            
            // Show image preview
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                previewContainer.classList.remove('hidden');
            };
            reader.readAsDataURL(file);
        } else {
            resetForm();
        }
    });

    // Handle form submission
    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const file = imageInput.files[0];
        if (!file) return;
        
        // Reset previous results
        resultContainer.classList.add('hidden');
        errorContainer.classList.add('hidden');
        
        // Show loading indicator with explicit style
        loadingIndicator.classList.remove('hidden');
        loadingIndicator.style.display = 'flex';
        
        // Create form data
        const formData = new FormData();
        formData.append('image', file);
        
        const prompt = promptInput.value.trim();
        if (prompt) {
            formData.append('prompt', prompt);
        }
        
        try {
            console.log('Starting analysis request...');
            const response = await fetch('/api/analyze', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            console.log('Response received:', data);
            
            // Explicitly stop the spinner
            loadingIndicator.classList.add('hidden'); 
            loadingIndicator.style.display = 'none';
            
            if (data.success) {
                resultContent.textContent = data.content;
                resultContainer.classList.remove('hidden');
            } else {
                errorMessage.textContent = data.error || 'Une erreur est survenue lors de l\'analyse de l\'image.';
                errorContainer.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error during analysis:', error);
            
            // Explicitly stop the spinner
            loadingIndicator.classList.add('hidden');
            loadingIndicator.style.display = 'none';
            
            errorMessage.textContent = 'Une erreur est survenue lors de la communication avec le serveur.';
            errorContainer.classList.remove('hidden');
        }
    });

    // Reset form function
    function resetForm() {
        fileName.textContent = 'Aucun fichier sélectionné';
        analyzeBtn.disabled = true;
        previewContainer.classList.add('hidden');
        resultContainer.classList.add('hidden');
        errorContainer.classList.add('hidden');
        
        // Make sure spinner is hidden
        loadingIndicator.classList.add('hidden');
        loadingIndicator.style.display = 'none';
    }
});