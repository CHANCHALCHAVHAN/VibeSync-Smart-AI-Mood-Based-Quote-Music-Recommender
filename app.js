function getRecommendations() {
    let mood = document.getElementById("mood").value;

    fetch("/get_recommendations", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mood: mood })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("emoji").innerText = data.emoji;
        document.getElementById("music-link").innerHTML = `<a href="${data.spotify_link}" target="_blank">${data.music}</a>`;
        document.getElementById("quote").innerText = `“${data.quote}”`;
        document.getElementById("affirmation").innerText = `🌟 ${data.affirmation}`;

        document.getElementById("result-section").style.display = "block";
        document.getElementById("result-section").scrollIntoView({behavior: "smooth"});
    })
    .catch(error => {
        console.error("Error fetching data: ", error);
    });
}
