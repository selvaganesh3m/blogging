// Get elements by ID
const openDialog = document.getElementById("openDialog");
const closeDialog = document.getElementById("closeDialog");
const dialog = document.getElementById("dialog");

// Add event listeners
openDialog.addEventListener("click", function(event) {
    event.preventDefault(); // Prevent page jump
    dialog.style.display = "block";
});

closeDialog.addEventListener("click", function(event) {
    event.preventDefault(); // Prevent page jump
    dialog.style.display = "none";
});