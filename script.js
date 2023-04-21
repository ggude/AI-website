document.getElementById("invoke-api").addEventListener("click", async () => {
    const apiUrl = "https://pxxzbut94j.execute-api.ap-south-1.amazonaws.com/prod/api-gpt-ml"; // Replace with your API Gateway URL
    const inputText = document.getElementById("input-text").value;

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: inputText
            })
        });
        const data = await response.json();
        document.getElementById("api-response").textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("api-response").textContent = "Error: " + error;
    }
});
