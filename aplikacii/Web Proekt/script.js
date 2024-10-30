var selectedRow = null

function onFormSubmit() {
    if (validate()) {
        var formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
        resetForm();
    }
}

function readFormData() {
    var formData = {};
    formData["ime"] = document.getElementById("ime").value;
    formData["prezime"] = document.getElementById("prezime").value;
    formData["fakultet"] = document.getElementById("fakultet").value;
    formData["indeks"] = document.getElementById("indeks").value;
    formData["datum"] = document.getElementById("datum").value;
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("listap").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.ime;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.prezime;
    cell3=newRow.insertCell(2);
    cell3.innerHTML=data.datum;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.fakultet;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.indeks;
    cell6 = newRow.insertCell(5);
    cell6.innerHTML = `<a onClick="onEdit(this)">Edit</a>
                       <a onClick="onDelete(this)">Delete</a>`;
}

function resetForm() {
    document.getElementById("ime").value = "";
    document.getElementById("prezime").value = "";
    document.getElementById("fakultet").value = "";
    document.getElementById("indeks").value = "";
    document.getElementById("datum").value = "";
    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("ime").value = selectedRow.cells[0].innerHTML;
    document.getElementById("prezime").value = selectedRow.cells[1].innerHTML;
    document.getElementById("fakultet").value = selectedRow.cells[2].innerHTML;
    document.getElementById("indeks").value = selectedRow.cells[3].innerHTML;
    document.getElementById("datum").value = selectedRow.cells[4].innerHTML;
}
function updateRecord(formData) {
    selectedRow.cells[0].innerHTML = formData.ime;
    selectedRow.cells[1].innerHTML = formData.prezime;
    selectedRow.cells[2].innerHTML = formData.fakultet;
    selectedRow.cells[3].innerHTML = formData.indeks;
    selectedRow.cells[3].innerHTML = formData.datum;
}

function onDelete(td) {
    if (confirm('Дали сте сигурни дека сакате да го избришете записот?')) {
        row = td.parentElement.parentElement;
        document.getElementById("listap").deleteRow(row.rowIndex);
        resetForm();
    }
}
function validate() {
    isValid = true;
    if (document.getElementById("ime").value == "") {
        isValid = false;
        document.getElementById("imeValidationError").classList.remove("hide");
    } else {
        isValid = true;
        if (!document.getElementById("imeValidationError").classList.contains("hide"))
            document.getElementById("imeValidationError").classList.add("hide");
    }
    return isValid;
}