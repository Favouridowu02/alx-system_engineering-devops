# A Manifest that kills a process named killmenow
exec { 'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
}
