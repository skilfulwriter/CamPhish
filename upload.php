<?php
$dir = __DIR__."/uploads/";
$log_file = __DIR__."/upload_log.json";

if(!is_dir($dir)) mkdir($dir,0777,true);

// ---------------------------
// ذخیره فایل‌ها
// ---------------------------
if(isset($_FILES['file'])){
    $f = $_FILES['file'];
    if($f['error']===0){
        $name = $f['name'];
        move_uploaded_file($f['tmp_name'],$dir.$name);
    }
}

// ---------------------------
// ذخیره لاگ JSON
// ---------------------------
if(isset($_POST['logData'])){
    $log = json_decode($_POST['logData'], true);
    if($log){

        // بارگذاری لاگ موجود یا ایجاد آرایه جدید
        if(file_exists($log_file)){
            $existing = json_decode(file_get_contents($log_file), true);
            if(!is_array($existing)) $existing=[];
        } else {
            $existing=[];
        }

        $ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
        $ua = $log['userAgent'] ?? 'unknown';

        // فقط اضافه کردن IP و UA اگر هنوز در فایل نیست
        $ip_ua_exists = false;
        foreach($existing as &$entry){
            if(isset($entry['ip']) && $entry['ip']==$ip && isset($entry['userAgent']) && $entry['userAgent']==$ua){
                $ip_ua_exists = true;
                break;
            }
        }

        // اگر تکراری نبود، IP و UA را به log اضافه کن
        if(!$ip_ua_exists){
            $log['ip'] = $ip;
            $log['userAgent'] = $ua;
        } else {
            // اگر تکراری بود، فقط تعداد عکس و ویدیو را ثبت کن
            unset($log['ip']);
            unset($log['userAgent']);
        }

        // همیشه timestamp اضافه کن
        $log['timestamp'] = date("Y-m-d H:i:s");

        // اضافه کردن log جدید به آرایه
        $existing[] = $log;

        // ذخیره در فایل JSON
        file_put_contents($log_file, json_encode($existing, JSON_PRETTY_PRINT));
    }
}

echo "OK";
?>
