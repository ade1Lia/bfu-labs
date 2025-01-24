<?php
session_start();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Сохраненные данные</title>
</head>
<body>
<h2>Сохраненные данные:</h2>
<ul>
    <?php
    foreach ($_SESSION['userdata'] as $key => $value) {
        echo "<li>$key: $value</li>";
    }
    ?>
</ul>
</body>
</html>
