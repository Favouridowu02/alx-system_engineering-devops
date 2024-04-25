# A Manifest that kills a process named killmenow
$process_name=killmenow

exec { 'pkill $process_name':
  command => '/usr/bin/pkill $process_name',
}
