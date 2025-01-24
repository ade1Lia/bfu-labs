<!DOCTYPE html>
<html>
<head>
    <title>Доска объявлений</title>
</head>
<body>

<h2>Добавить объявление</h2>
<form method="post" action="">
    Email: <input type="text" name="email"><br><br>
    Категория:
    <select name="category">
        <option value="автомобили">Автомобили</option>
        <option value="недвижимость">Недвижимость</option>
        <option value="работа">Работа</option>
    </select><br><br>
    Заголовок объявления: <input type="text" name="title"><br><br>
    Текст объявления: <textarea name="text" rows="4" cols="50"></textarea><br><br>
    <input type="submit" name="submit" value="Добавить">
</form>

<?php
//обработка добавления объявления
if(isset($_POST['submit'])) {
    $email = $_POST['email'];
    $category = $_POST['category'];
    $title = $_POST['title'];
    $text = $_POST['text'];

    //проверка наличия папки для выбранной категории
    if (!is_dir($category)) {
        mkdir($category);
    }

    //создание имени файла на основе заголовка
    $filename = $category . '/' . $title . '.txt';

    //запись текста объявления в файл
    file_put_contents($filename, $text);

    echo "<p>Объявление успешно добавлено.</p>";
}

//отображение списка объявлений
echo "<h2>Список объявлений</h2>";
echo "<table border='1'>";
echo "<tr><th>Email</th><th>Категория</th><th>Заголовок</th><th>Текст объявления</th></tr>";

//перебор всех файлов в папках категорий
$categories = ['автомобили', 'недвижимость', 'работа'];
foreach ($categories as $category) {
    if (is_dir($category)) {
        $files = scandir($category);
        foreach ($files as $file) {
            if ($file != '.' && $file != '..') {
                $filename = $category . '/' . $file;
                $data = file_get_contents($filename);
                $title = pathinfo($filename, PATHINFO_FILENAME);
                echo "<tr><td>$email</td><td>$category</td><td>$title</td><td>$data</td></tr>";
            }
        }
    }
}

echo "</table>";
?>

</body>
</html>