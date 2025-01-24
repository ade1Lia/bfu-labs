<?php
session_start();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Данные пользователя</title>
</head>
<body>
<h2>Данные пользователя:</h2>
<p>Фамилия: <?php echo $_SESSION['surname']; ?></p>
<p>Имя: <?php echo $_SESSION['name']; ?></p>
<p>Возраст: <?php echo $_SESSION['age']; ?></p>
</body>
</html>
