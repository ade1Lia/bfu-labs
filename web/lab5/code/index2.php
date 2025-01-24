<?php
function redirectToHome()
{
    header('Location: /index.php');
    exit();
}
if (false === isset($_POST['email'], $_POST['category'], $_POST['title'], $_POST['description'])){
    redirectToHome();
}
$container = 'db';
$username = 'root';
$password = 'helloworld';
$database = 'MySQL';
$port = 3306;

$BASE = new mysqli($container, $username, $password, $database, $port);
$category = $_POST['category'];
$title = $_POST['title'];
$description = $_POST['description'];
$email = $_POST['email'];

$stmt = $BASE->prepare("INSERT INTO web.ad(email, title, description, category) VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssss",$email, $title, $description, $category);
$stmt->execute();

$stmt->close();
$BASE->close();
redirectToHome();