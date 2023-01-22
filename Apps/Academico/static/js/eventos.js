(function () {
    const $eliminarBoton = document.querySelectorAll(".btnEliminar");

    $eliminarBoton.forEach(btn => {
        btn.addEventListener('click', (c) => {
            const confirmacion = confirm('¿Seguro quiere eliminar el Area?');
            if (!confirmacion) {
                c.preventDefault();
            }
        });
    });

})();