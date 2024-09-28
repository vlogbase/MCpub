document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('custIdForm');
    const results = document.getElementById('results');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const custId = document.getElementById('cust_id').value;

        fetch('/generate_api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ cust_id: custId }),
        })
        .then(response => response.json())
        .then(data => {
            // Removed the line that updates 'apiEndpoint' since it's no longer in the HTML
            // document.getElementById('apiEndpoint').textContent = data.api_endpoint;

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

function copyText(elementId) {
    const element = document.getElementById(elementId);
    const text = element.textContent;
    navigator.clipboard.writeText(text).then(function() {
        alert('Copied to clipboard!');
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}
