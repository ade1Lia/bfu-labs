<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Замулдинова Адэля</title>
</head>
<body>
<form action="index2.php" method="post">
    <label>
        <br> Введите Ваш email:
        <input name="email" required type="email">
    </label>
    <label>
        <br> Выберете категорию:
        <select name="category" required>
            <option value="cars">Машинки</option>
            <option value="dolls">Куклы</option>
            <option value="lego">Лего</option>
        </select>
    </label>
    <label>
        <br> Заголовок:
        <input name="title" required type="text">
    </label>
    <label>
        <br>Описание:
        <textarea name="description" ></textarea>
    </label>
    <label>
        <br> <input type="submit">
    </label>
</form>
<?php
$container = 'db';
$username = 'root';
$password = 'helloworld';
$database = 'MySQL';
$port = 3306;

$BASE = new mysqli($container, $username, $password, $database, $port);

foreach ($BASE->query("SELECT * FROM web.ad") as $row) {
    $category = $row['category'];
    $title = $row['title'];
    $description = $row['description'];
    $email = $row['email'];
    echo "<p> $email -> $title -> $description -> $category </p>";
}

?>
</body>
</html>