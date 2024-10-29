"""sopel-pywhat

A Sopel plugin for quickly checking text in pyWhat.

Copyright 2024, dgw, technobabbl.es

Licensed under the Eiffel Forum License 2.
"""
from __future__ import annotations

import subprocess

from sopel import plugin


@plugin.command('pywhat')
def pywhat_identify(bot, trigger):
    """Identify text using pyWhat."""
    if not (text := trigger.group(2)):
        bot.reply('You need to provide some text to identify.')
        return

    out = subprocess.run(
        ['pywhat', '--only-text', text],
        capture_output=True,
        text=True,
    )

    results = out.stdout.split('\n\n')
    groups = []
    for result in results:
        if result:
            relevant_lines = (
                line for line in result.splitlines()
                if line.startswith(('Matched on:', 'Name:', 'Description:'))
            )
            groups.append(' | '.join(relevant_lines))

    for group in groups:
        bot.say(group)
