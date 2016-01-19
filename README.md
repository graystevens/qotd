#Quote of the Day (QOTD)
An implimentation of [RFC 865](https://tools.ietf.org/html/rfc865), Quote of the Day Protocol, written in Python3


##Usage
```
python qotd.py
```
*Note, you may need to use python3, depending on your setup...*


This will run the `qotd.py` script, opening a TCP and a UDP socket on port 17. On most systems, this will likely throw an error due to only `root` being allowed to bind to ports <1024. To circumvent this, you can use iptables, or [authbind](https://en.wikipedia.org/wiki/Authbind).
A detailed list of options can be seen here: https://www.debian-administration.org/article/386/Running_network_services_as_a_non-root_user.

**iptables**

```
# Redirect *:11117 -> *:17
iptables -t nat -A PREROUTING -p tcp --dport 17 -j REDIRECT --to 11117
iptables -t nat -A PREROUTING -p udp --dport 17 -j REDIRECT --to 11117
```

**authbind**

A great walkthrough can be found here: https://mutelight.org/authbind

```
# Please note, you may need sudo/root for these commands. Proceed with caution.
apt-get install authbind

touch /etc/authbind/byport/17
chown qotduser /etc/authbind/byport/17
chmod 500 /etc/authbind/byport/17

# And then run the script, with authbind!
authbind python qotd.py
```

#Todo
- Make it IPv6 compatible!
