// Adding drag event in the task
for (const draggableElement of document.querySelectorAll('.task')) {
    draggableElement.addEventListener('dragstart', e => {
        e.dataTransfer.setData('text/plain', draggableElement.id)
        // let deg = e.clientX - window.innerWidth / 2 > 0 ? -3: 3;
        // e.currentTarget.style.transform = `rotate(${deg}deg)`;
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
        
        dropZone.children[0].appendChild(droppedElement);
        dropZone.classList.remove('item--over');
    });
}

// Adding click event in the bar button
for (const btnPencil of document.getElementsByClassName('btn-pencil')) {
    btnPencil.addEventListener('click', e => {
        alert('Pencil event not implemented!');
    });
}

// Adding click event in the pencil button
for (const btnBar of document.getElementsByClassName('btn-bar')) {
    btnBar.addEventListener('click', e => {
        alert('Bar event not implemented!');
    });
}

// Adding click event in the add card button
for (const btnAddCard of document.getElementsByClassName('add-card')) {
    btnAddCard.addEventListener('click', e => {
        fetch('/kanban', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: 'TESTE'
            })
        }).then(res => {
            return res.json()
        })
        console.log(e.target.value);
    });
}

// Adding click event in the add list button
const btnAddList = document.getElementById('add-list');
btnAddList.addEventListener('click', e => {
    alert('Add list not implemented');
});