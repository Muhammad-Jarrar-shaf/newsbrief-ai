const summarizeBtn = document.getElementById("summarizeBtn");

const loading = document.getElementById("loading");

const output = document.getElementById("summaryOutput");

const copyBtn = document.getElementById("copyBtn");


summarizeBtn.addEventListener("click", async () => {

    const url = document.getElementById("urlInput").value;

    if (!url) {

        alert("Please enter a URL.");

        return;
    }

    loading.style.display = "block";

    output.value = "";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/summarize",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({ url })
            }
        );

        const data = await response.json();

        output.value = data.summary;

    } catch (error) {

        output.value = "Something went wrong.";
    }

    loading.style.display = "none";
});


copyBtn.addEventListener("click", () => {

    navigator.clipboard.writeText(output.value);

    alert("Summary copied!");
});