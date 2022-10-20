$(document).ready( function () {
    $('#table_habitaciones').DataTable({
        order: [[3, 'desc']],
        "lengthChange": false ,
        "pagingType": "full_numbers"
    });
} );