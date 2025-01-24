<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Доска объявлений</title>
</head>
<body>
<h2>Добавить объявление</h2>
<form action="submit.php" method="post">
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br>

    <label for="title">Заголовок объявления:</label><br>
    <input type="text" id="title" name="title" required><br>

    <label for="text">Текст объявления:</label><br>
    <textarea id="text" name="text" rows="4" required></textarea><br>

    <label for="category">Категория:</label><br>
    <input type="text" id="category" name="category" required><br><br>

    <input type="submit" value="Добавить">
</form>
</body>
</html>

<?php

require_once "vendor/autoload.php";

use Google\Spreadsheet\DefaultServiceRequest;
use Google\Spreadsheet\ServiceRequestFactory;

// Функция для записи данных в Google Таблицу
function addEntryToGoogleSheet($email, $title, $text, $category)
{
    $client = new Google_Client();
    $client->setApplicationName('Google Sheets API PHP');
    $client->setScopes(Google_Service_Sheets::SPREADSHEETS);
    $client->setAccessType('offline');
    $client->setAuthConfig('C:\web labs\weblab4-420618-1f07ab7f67b7.json');

    $service = new Google_Service_Sheets($client);

    $spreadsheetId = '1lr2su0KF6Afbst5C6KrnmH-dQqsosK4WAxF8ZvkcSWM/edit#gid=0';
    $range = 'Sheet1'; // Название листа в таблице

    $values = [
        [$email, $title, $text, $category]
    ];

    $body = new Google_Service_Sheets_ValueRange([
        'values' => $values
    ]);

    $params = [
        'valueInputOption' => 'RAW'
    ];

    $result = $service->spreadsheets_values->append($spreadsheetId, $range, $body, $params);
    if ($result->getUpdates()->getUpdatedCells() > 0) {
        echo 'Объявление успешно добавлено!';
    } else {
        echo 'Произошла ошибка при добавлении объявления';
    }
}

// Получаем данные из POST запроса
$email = $_POST['email'];
$title = $_POST['title'];
$text = $_POST['text'];
$category = $_POST['category'];

// Добавляем запись в Google Таблицу
addEntryToGoogleSheet($email, $title, $text, $category);