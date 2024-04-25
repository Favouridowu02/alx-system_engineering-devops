# To install Flask package

exec { 'install flask':
  command     => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.1.1',
}
