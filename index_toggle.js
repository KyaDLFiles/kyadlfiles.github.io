cbox = document.getElementById("show-index");

function toggleIndex() {
    index = document.getElementById("index");
    if (cbox.checked) {
        index.classList.remove("hidden");
    } else {
        index.classList.add("hidden");
    }
}

cbox.addEventListener("click", toggleIndex);
toggleIndex();