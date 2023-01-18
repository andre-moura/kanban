// Adding drag event in the task
for (const draggableElement of document.querySelectorAll('.task')) {
    draggableElement.addEventListener('dragstart', e => {
        e.dataTransfer.setData('text/plain', draggableElement.id)
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
        const list_id = droppedElement.parentNode.parentNode.id.replace('list_', '');
        const kanban_id = droppedElement.parentNode.parentNode.parentNode.parentNode.id.replace('kanban_', '');
        
        fetch('/drag-task', {
            method: 'POST',
            body: JSON.stringify({
                kanban_id: kanban_id,
                list_id: list_id,
                task_id: droppedElementId.replace('task_', 'task')    
            }),
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        })
        .then(response => response.json())
    });

    dropZone.addEventListener('drop', e => {
        e.preventDefault();
        const droppedElementId = e.dataTransfer.getData('text/plain');
        const droppedElement = document.getElementById(droppedElementId);

        dropZone.children[0].appendChild(droppedElement);
        dropZone.classList.remove('item--over');
    });
}

// Adding click event in the bar button
for (const btnPencil of document.getElementsByClassName('btn-pencil')) {
    btnPencil.addEventListener('click', e => {
        const modal = document.getElementById('modal')
        const btnEditTask = document.getElementById('task_id')
        btnEditTask.value = `btn_edit_${e.target.id.replace('task_', '')}`
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
const btnAddList = document.getElementById('add_list');
btnAddList.addEventListener('click', e => {
    const modal = document.getElementById('modal_list')
    modal.style.display = 'flex';
});

for (const addCard of document.getElementsByClassName('add-card')) {
    addCard.addEventListener('click', e => {
        const modal = document.getElementById('modal')
        const btnTask = document.getElementsByName('btn_add_task')[0]
        btnTask.value = `btn_${e.target.id}`;
        modal.style.display = 'flex';
    })
}