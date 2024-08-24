# This puppet file is to solve the 500 status code error fixes bad `phpp` extensions to `php` in the wordpress file `wp-settings.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin'
}
