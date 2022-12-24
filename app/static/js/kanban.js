// Adding drag event in the task
for (const draggableElement of document.querySelectorAll('.task')) {
    draggableElement.addEventListener('dragstart', e => {
        e.dataTransfer.setData('text/plain', draggableElement.id)
        console.log(e.clientX - window.innerWidth / 2)
    });
}

// Adding drag event in the task list
for (const dropZone of document.querySelectorAll('.item-box')) {
    dropZone.addEventListener('dragover', e => {
        e.preventDefault();
        dropZone.classList.add('item--over')
    });

    dropZone.addEventListener('dragleave', e => {
        dropZone.classList.remove('item--over');
    });
    
    dropZone.addEventListener('dragend', e => {
        const droppedElementId = e.dataTransfer.getData('text/plain');
        const droppedElement = document.getElementById(droppedElementId);
        droppedElement.style.transform = 'rotate(0deg)';
    });

    dropZone.addEventListener('drop', e => {
        e.preventDefault();
        const droppedElementId = e.dataTransfer.getData('text/plain');
        const droppedElement = document.getElementById(droppedElementId);

        // droppedElement.style.transform = 'rotate(0deg)';
        console.log(dropZone.children[0])
        console.log(droppedElement)
        dropZone.children[0].appendChild(droppedElement);
        dropZone.classList.remove('item--over');
    });
}

// Adding click event in the bar button
for (const btnPencil of document.getElementsByClassName('btn-pencil')) {
    btnPencil.addEventListener('click', e => {
        const modal = document.getElementById('modal')
        modal.style.display = 'flex';
    });
}

// Adding click event in the pencil button
for (const btnBar of document.getElementsByClassName('btn-bar')) {
    btnBar.addEventListener('click', e => {
        alert('Bar event not implemented!');
    });
}

// Adding click event in the add list button
const btnAddList = document.getElementById('add-list');
btnAddList.addEventListener('click', e => {

});

for (const addCard of document.getElementsByClassName('add-card')) {
    addCard.addEventListener('click', e => {
        const modal = document.getElementById('modal')
        modal.style.display = 'flex';
    })
}