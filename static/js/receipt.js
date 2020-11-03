function get_receipt(receipt_id) {
    $.post('/receipts/' + receipt_id, {
    }).done(function(response) {
        showReceipt(receipt_id, response);
    }).fail(function() {
        alert('Чек не найден');
    });
}

function showReceipt(receipt_id, receipt)
{
    var html = '<div class="modal fade" id="modalWindow' + receipt_id;
    html += '" tabindex="-1" role="dialog"aria-labelledby="purchaseLabel"' +
    'aria-hidden="true"><div class="modal-dialog"><div class="modal-content">';
    var tableHeaders = ['Название', 'Категория', 'Цена', 'Количество', 'Сумма'];
    var tableFields = ['name', 'category', 'price', 'quantity', 'amount'];
    var divide100 = ['price', 'amount'];
    html += '<table id="classTable" class="table table-bordered"><tr align="left">';
    tableHeaders.forEach(header => html += '<th class="standard-head">' + header + '</th>');
    html += '</tr>';
    receipt['products'].forEach(function addingProduct(product){
        html += '<tr align="left">';
        tableFields.forEach(function addCell(field){
            html += '<td class="standard-cell">';
            if (divide100.includes(field)){
                html += product[field] / 100;
            }
            else html += product[field];
            html += '</td>';
        });
        html += '</tr>';
    });
    html += '<tr><td><a href="/receipt_delete/' + receipt_id;
    html += '" class="btn btn-danger">Удалить</a></td></tr>'
    html += '</table></div></div></div>';
    $('#modal' + receipt_id).html(html);
    $('#modalWindow' + receipt_id).modal();
}
