# Create a file that is in the tmp directory
file { '/tmp/school':
  ensure  => 'link',
  target  => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}

