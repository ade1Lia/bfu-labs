<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Сохраняем данные из формы в сессию
    $_SESSION['surname'] = $_POST['surname'];
    $_SESSION['name'] = $_POST['name'];
    $_SESSION['age'] = $_POST['age'];
    header("Location: page2.php");
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Форма</title>
</head>
<body>
<h2>Введите фамилию, имя и возраст:</h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
    Фамилия: <input type="text" name="surname"><br><br>
    Имя: <input type="text" name="name"><br><br>
    Возраст: <input type="text" name="age"><br><br>
    <input type="submit" value="Отправить">
</form>
</body>
</html>
