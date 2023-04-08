script>
$('#sortTable').DataTable();
$(document).ready(function(){
  document.getElementById( 'item_id' ).style.display = 'none';
});


</script>
<script>
function fetchRow(button)
{
      // Get the parent row of the button
      let row = button.parentNode.parentNode;

      // Initialize an empty array to store the values of the row
      let rowValues = [];

      // Iterate through the cells of the row
      for (let i = 0; i < row.cells.length; i++) {
        // Push the value of the cell to the rowValues array
        rowValues.push(row.cells[i].innerHTML);
      }

          // Get the div element where the row data will be inserted
          var item_box = document.getElementById('add_row');
          var new_item = document.createElement('div');

          new_item.className="row mb-4 d-flex justify-content-between align-items-center ity";
          new_item.innerHTML = '<div class="col-md-5 col-lg-5 col-xl-5" id="parentRow">\n' +

                                                                    '<h6 class="text-black mb-0" id="item">' + rowValues[1] + " " + rowValues[2] + '</h6>\n' +
                                                                    '<hr class="my-4">\n' +
                                                                '</div>\n' +
                                                                '<div class="col-md-3 col-lg-3 col-xl-2 d-flex" style="margin-bottom: 40px;"><button class="btn btn-link px-2" onclick="this.parentNode.querySelector(\'input[type=number]\').stepDown()">\n' +
                                                                                                                  '<i class="fas fa-minus"></i>\n' +
                                                                                                                '</button>\n'+
                                                                    '<input id="form1" min="1" name="quantity" value="1" type="number" class="form-control form-control-sm"/>\n' +
                                                                    '<button class="btn btn-link px-2" onclick="this.parentNode.querySelector(\'input[type=number]\').stepUp(); logNewValue(\''+rowValues[0]+'\')">\n' +
                                                                        '<i class="fas fa-plus"></i>\n' +
                                                                    '</button>\n' +
                                                               '</div>\n' +
                                                                '<div class="col-md-3 col-lg-2 col-xl-2">\n' +
                                                                    '<h6 class="mb-0" id="unit">'+ rowValues[3] +'</h6>\n' +
                                                                    '<hr class="my-4">\n' +
                                                                '</div>\n' +
                                                                '<div class="col-md-1 col-lg-1 col-xl-1 text-end">\n' +
                                                                    '<a href="" class="text-muted deleteLink" id="deleteLink"><i class="fas fa-times deleteLink"></i></a>\n' +
                                                                    '<hr class="my-4">\n' +
                                                                '</div>\n';


         item_box.appendChild(new_item);
         item_id = rowValues[0];
         fetch('/add_to_cart',
          {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({item_id})
            });
  }
             $(document).on("click", '#deleteLink', function(event)
             {
                    event.preventDefault();
                    $(this).closest('.row').remove();
              });

              function logNewValue(qty_id)
            {
                 var upQty = document.querySelector('input').value;



            }
function logNewValue(qty_id) {
var upQty = document.querySelector('input').value;
  fetch('/update_qty', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({qty_id},{upQty})
    });
}
