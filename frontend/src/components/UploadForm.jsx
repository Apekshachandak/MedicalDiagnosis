import { useState } from 'react';

function UploadForm() {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState(null);

    const handleFileChange = (e) => setFile(e.target.files[0]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('image', file);

        const response = await fetch('http://localhost:5000/analyze_image', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        console.log(data);
        setResult(data);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type='file' onChange={handleFileChange} />
                <button type='submit'>Upload and Analyze</button>
            </form>
            {result && (
                <div>
                    <p>Diagnosis: {result.diagnosis}</p>
                    <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
                </div>
            )}
        </div>
    );
}

export default UploadForm;