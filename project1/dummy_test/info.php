<?php

$str = 'Hello PHP ;)';

function counter(string $data) {
	return strlen($data);
}

echo $str .' '. counter($str) . "\n";
