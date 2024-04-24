# To install Flask package
exec { 'apt update':
  command     => '/usr/bin/apt update',
  refreshonly => true,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
