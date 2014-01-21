#!/bin/zsh

selfdir=$0:A:h

dir="${XDG_CONFIG_HOME:-$HOME/.config}/dmenu"
mkdir -p $dir
cp -v $selfdir/dmenurc $dir

echo "Using sudo to install the scripts"
for x in dmenu_any dmenu_sshmux sshmux ; do
  target="/usr/local/bin/$x"
  if [[ ! -f $target ]]; then
    sudo cp -v $selfdir/$x $target
  fi
done
