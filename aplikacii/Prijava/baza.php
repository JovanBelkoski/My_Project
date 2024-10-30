<?php
$servername = "localhost";
$username = "root";
$password = "Fikt_Bitola_EDU123";
$dbname = "prijava";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Поврзувањето не успеа: " . $conn->connect_error);
}

$ime = $_POST['ime'];
$prezime = $_POST['prezime'];
$telefon = $_POST['telefon'];
$email = $_POST['email'];
$pozicija = $_POST['pozicija'];

$sql = "INSERT INTO prijava (ime, prezime, telefon, email, pozicija)
VALUES ('$ime', '$prezime', '$telefon', '$email', '$pozicija')";

if ($conn->query($sql) === TRUE) {
    echo "Податоците се успешно зачувани!";
} else {
    echo "Грешка: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
