const del = document.querySelectorAll('btn-delete')

if (del){
    const btnArray = Array.from(del);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete')){
                e.preventDefault();
            }
        });
    });
}
