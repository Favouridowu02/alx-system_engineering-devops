# To install Flask package
exec { 'usr/bin/pip3 install Flask==2.1.0':
  path        => ['usr/bin'],
  refreshonly => true,
}
