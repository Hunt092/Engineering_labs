<html>
<h1>Connecting MYSQL Database with PHP</h1>
<h2>Connecting->Creating Database->Creating Table->Inserting
Data->Updating Data->Displaying</h2>
</html>
<?php
$servername = "localhost";
$username = "root";
$password = "password123";
$dbname = "wtassign";
$conn = new mysqli($servername, $username, $password,$dbname);
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
echo "\nConnected successfully";
echo "<br>";
$sql = "CREATE DATABASE wtAssign";
if ($conn->query($sql) === TRUE) {
echo "Database created successfully";
echo "<br>";
} else {
echo "Error creating database: " . $conn->error;
echo "<br>";
}
$sql = "CREATE TABLE Guests (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(50),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE
CURRENT_TIMESTAMP
)";
if ($conn->query($sql) === TRUE) {
echo "\nTable Guests created successfully";
echo "<br>";
} else {
echo "\nError creating table: " . $conn->error;
echo "<br>";
}
$sql = "INSERT INTO Guests (firstname, lastname, email)
VALUES ('Ron', 'Mate', 'ron@example.com')";
if ($conn->query($sql) === TRUE) {
echo "\nNew record created successfully";
echo "<br>";
} else {
echo "\nError: " . $sql . "<br>" . $conn->error;
}
$sql = "SELECT id, firstname, lastname FROM Guests";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
while($row = $result->fetch_assoc()) {
echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " .
$row["lastname"]. "<br>";
}
} else {
echo "0 results";
}
$sql = "UPDATE Guests SET lastname='Doe' WHERE id=2";
if ($conn->query($sql) === TRUE) {
echo "Record updated successfully";
echo "<br>";
} else {
echo "Error updating record: " . $conn->error;
}
$conn->close();
?>

