# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
# disable ssh graphic password input dialog
unset SSH_ASKPASS
