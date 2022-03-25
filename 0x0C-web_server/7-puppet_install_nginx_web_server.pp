# Setup nginx server

package { 'nginx':
  ensure     => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect':
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/a location /redirect_me {\\n\\treturn 301 https://google.com; listen 80; \\n\\t}\\n" /etc/nginx/sites-available/default',
  returns  => [0, 1],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
