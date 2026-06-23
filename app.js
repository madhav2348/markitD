async function handleFileSelect() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select a file');
        return;
    }

    const outputArea = document.getElementById('output');
    outputArea.value = 'Converting...';

    try {
        const base64 = await fileToBase64(file);
        
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                filename: file.name,
                content: base64,
                fileType: file.type
            })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        const result = await response.json();
        outputArea.value = result.markdown || result.error || 'No content extracted';
    } catch (error) {
        outputArea.value = `Error: ${error.message}\n\nNote: This webapp requires a backend server running with MarkItDown.`;
    }
}

function fileToBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result.split(',')[1]);
        reader.onerror = reject;
        reader.readAsDataURL(file);
    });
}

function copyToClipboard() {
    const outputArea = document.getElementById('output');
    if (!outputArea.value) {
        alert('Nothing to copy');
        return;
    }
    navigator.clipboard.writeText(outputArea.value).then(() => {
        alert('Copied to clipboard');
    });
}

function downloadMarkdown() {
    const outputArea = document.getElementById('output');
    if (!outputArea.value) {
        alert('Nothing to download');
        return;
    }

    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/markdown;charset=utf-8,' + encodeURIComponent(outputArea.value));
    element.setAttribute('download', 'document.md');
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

function clearOutput() {
    document.getElementById('output').value = '';
    document.getElementById('fileInput').value = '';
}
