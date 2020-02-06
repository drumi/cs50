const list = document.getElementById('todo-list')
const itemCountSpan = document.getElementById('item-count')
const uncheckedCountSpan = document.getElementById('unchecked-count')

function newTodo() {
  const todo = prompt('Enter a new TODO:')

  if(todo) {
    itemCountSpan.innerText = Number(itemCountSpan.innerText) + 1;
    uncheckedCountSpan.innerText = Number(uncheckedCountSpan.innerText) + 1;

    const todoItem = document.createElement("li");
    const cbx = document.createElement('input');
    const deleteBtn = document.createElement('button');
    
    deleteBtn.addEventListener('click', onDelete);
    deleteBtn.appendChild(document.createTextNode('Delete'));
    deleteBtn.style.float='right';

    cbx.type = 'checkbox';
    cbx.style.margin='0px 10px 0px 0px'
    cbx.addEventListener('change', onCheck);

    todoItem.appendChild(cbx);
    todoItem.appendChild(document.createTextNode(todo));
    todoItem.appendChild(deleteBtn);
    todoItem.style.clear='both';
    todoItem.appendChild(document.createElement('hr'));

    list.appendChild(todoItem);
  }

  function onCheck() {
    if(this.checked)
      uncheckedCountSpan.innerText = Number(uncheckedCountSpan.innerText) - 1;
    else
      uncheckedCountSpan.innerText = Number(uncheckedCountSpan.innerText) + 1;
  }

  function onDelete() {
    const parent = this.parentElement;
    itemCountSpan.innerText = Number(itemCountSpan.innerText) - 1;
    if(!parent.children[0].checked)
      uncheckedCountSpan.innerText = Number(uncheckedCountSpan.innerText) - 1;
    parent.remove();
  }
}
