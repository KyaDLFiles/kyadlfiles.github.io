cbox = document.getElementById("show-toc");

function toggleIndex() {
    index = document.getElementById("toc-container");
    if (cbox.checked) {
        index.classList.remove("hide-below-700px");
    } else {
        index.classList.add("hide-below-700px");
    }
}

cbox.addEventListener("click", toggleIndex);
toggleIndex();
