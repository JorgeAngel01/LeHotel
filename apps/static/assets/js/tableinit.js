$(document).ready( function () {
    $('#table_habitaciones').DataTable({
        order: [[1, 'desc']],
        "lengthChange": false ,
        "pagingType": "full_numbers",
        language: {
            url: '//cdn.datatables.net/plug-ins/1.12.1/i18n/es-ES.json'
        }
    });
    $('#table_reservaciones').DataTable({
        order: [[1, 'desc']],
        "lengthChange": false ,
        "pagingType": "full_numbers",
        language: {
            url: '//cdn.datatables.net/plug-ins/1.12.1/i18n/es-ES.json'
        }
    })
} );
