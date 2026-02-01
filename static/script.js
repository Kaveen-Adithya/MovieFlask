console.log("MovieFlex loaded 💻");

document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const query = document.getElementById("searchInput").value;
    window.location.href = query ? `/search?query=${encodeURIComponent(query)}` : '/';
});

document.getElementById("searchInput").addEventListener("keyup", function(event) {
    // You could add live filtering here later!
});# Auto-generated contribution on 2026-01-01 19:37:41
# Commit 8/20
# Random seed: 1655

# Auto-generated contribution on 2026-01-31 16:12:49
# Commit 19/20
# Random seed: 8633

# Auto-generated contribution on 2026-02-01 11:07:08
# Commit 8/20
# Random seed: 6793

