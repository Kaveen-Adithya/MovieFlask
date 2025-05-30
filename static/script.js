console.log("MovieFlex loaded 💻");

document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const query = document.getElementById("searchInput").value;
    window.location.href = query ? `/search?query=${encodeURIComponent(query)}` : '/';
});

document.getElementById("searchInput").addEventListener("keyup", function(event) {
    // You could add live filtering here later!
});