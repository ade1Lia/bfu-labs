<?php

//поиск совпадений
$str = 'ahb acb aeb aeeb adcb axeb';

//выражение для поиска 'abba', 'adca', 'abea'
$pattern = '/a..b/';

//поиск совпадений
preg_match_all($pattern, $str, $matches);

//вывод результатов
echo "Найденные строки:\n";
foreach ($matches[0] as $match) {
    echo $match . "\n";
}

$str = 'a1b2c3';

//выражение для поиска цифр
$pattern = '/(\d+)/';

//функция замены с использованием callback
$new_str = preg_replace_callback($pattern, function($matches) {
    $number = $matches[0];
    return pow($number, 3);
}, $str);

//вывод преобразованной строки
echo $new_str;

?>