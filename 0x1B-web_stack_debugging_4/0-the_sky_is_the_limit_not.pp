# restart nginx server
exec { 'configure server':
  provider => shell,
  command  => 'service nginx stop && nginx'
}
