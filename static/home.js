let itemDescParagraphEl = document.querySelectorAll(".item-desc-paragraph")

console.log(itemDescParagraphEl)
for (let i = 0; i < itemDescParagraphEl.length; i++){
    let itemDescription = itemDescParagraphEl[i].textContent
    itemDescParagraphEl[i].textContent = itemDescription.slice(0,100) + "..."
}


console.log(itemDescParagraphEl)
