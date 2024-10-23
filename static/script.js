document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('SkimpubIDForm');
    const results = document.getElementById('results');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const SkimpubID = document.getElementById('SkimpubID').value;

        fetch('/generate_api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ SkimpubID: SkimpubID }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('openApiSpec').textContent = data.openapi_spec;
            document.getElementById('integrationInstructions').textContent = data.integration_instructions;
            results.style.display = 'block';
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });
});

function copyText(elementId, button) {
    const element = document.getElementById(elementId);
    const text = element.textContent;
    navigator.clipboard.writeText(text).then(function() {
        const originalText = button.textContent;
        button.textContent = 'Copied!';
        setTimeout(function() {
            button.textContent = originalText;
        }, 2000);
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}
