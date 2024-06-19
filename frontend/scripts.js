const uploadBox = document.getElementById('upload-box');
const fileInput = document.getElementById('file-input');
const fileDisplay = document.getElementById('file-display');

uploadBox.addEventListener('click', () => fileInput.click());

uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = '#000';
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.style.borderColor = '#ccc';
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = '#ccc';
    const files = e.dataTransfer.files;
    fileInput.files = files;
    uploadFile(files[0]);
});

fileInput.addEventListener('change', () => {
    uploadFile(fileInput.files[0]);
});

async function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        if (response.ok) {
            const fileUrl = `http://localhost:5000/processed/${data.filename}`;
            displayFile(fileUrl, data.filename);
        } else {
            alert(`Error: ${data.error}`);
        }
    } catch (error) {
        console.error('Error uploading file:', error);
    }
}

function displayFile(url, filename) {
    if (filename.endsWith('.png') || filename.endsWith('.jpg') || filename.endsWith('.jpeg')) {
        fileDisplay.innerHTML = `<img src="${url}" alt="Processed Image">`;
    } else if (filename.endsWith('.mp4') || filename.endsWith('.avi') || filename.endsWith('.mov')) {
        fileDisplay.innerHTML = `<video controls>
            <source src="${url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>`;
    }
}
