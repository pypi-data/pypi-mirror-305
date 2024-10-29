# sopel-pywhat

A Sopel plugin for quickly checking text in pyWhat.

## Installing

Releases are hosted on PyPI, so after installing Sopel, all you need is `pip`:

```shell
$ pip install sopel-pywhat
```

`pywhat` needs to be on Sopel's `$PATH` for this plugin to work. Generally this
is automatic (e.g. if you run Sopel in a venv, or a well-configured shell) but
you should double check the environment if there are errors.

## Using

Use the `.pywhat` command (replace `.` with your bot's prefix, if needed) to
invoke `pywhat`:

```
<dgw> .pywhat AIzajofahiuoifohiawhoiuehfaafjoiawerasdf
<Sopel> Matched on: AIzajofahiuoifohiawhoiuehfaafjoiawerasd | Name: Google API
        Key
<Sopel> Matched on: AIzajofahiuoifohiawhoiuehfaafjoiawerasdf | Name: Amazon Web
        Services Secret Access Key
```

_(The example above is a keyboard-mash. If it happens to match any real API
keys—those are incredible odds!)_
