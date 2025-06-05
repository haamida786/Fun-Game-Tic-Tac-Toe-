const cells = document.querySelectorAll('.cell');
const statusText = document.getElementById('status');
const resetBtn = document.getElementById('reset');

cells.forEach((cell, index) => {
    cell.addEventListener('click', () => makeMove(index));
});

resetBtn.addEventListener('click', () => {
    fetch('/reset', { method: 'POST' })
        .then(res => res.json())
        .then(data => updateBoard(data));
});

function makeMove(index) {
    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cell: index })
    })
    .then(res => res.json())
    .then(data => updateBoard(data));
}

function updateBoard(data) {
    data.board.forEach((val, i) => {
        cells[i].textContent = val;
    });
    statusText.textContent = data.status;
}
