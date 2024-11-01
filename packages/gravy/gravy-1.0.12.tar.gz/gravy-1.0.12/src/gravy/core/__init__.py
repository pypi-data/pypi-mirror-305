from typing import *

import click
import preparse

__all__ = ["calculate", "main", "score"]

_VALUES = {
    "A": 1.8,
    "C": 2.5,
    "D": -3.5,
    "E": -3.5,
    "F": 2.8,
    "G": -0.4,
    "H": -3.2,
    "I": 4.5,
    "K": -3.9,
    "L": 3.8,
    "M": 1.9,
    "N": -3.5,
    "P": -1.6,
    "Q": -3.5,
    "R": -4.5,
    "S": -0.8,
    "T": -0.7,
    "V": 4.2,
    "W": -0.9,
    "X": None,
    "Y": -1.3,
    "-": None,
}


def score(seq: Iterable):
    """Calculate the GRAVY score."""
    answers = [_VALUES[str(k)] for k in seq]
    answers = [v for v in answers if v is not None]
    if len(answers):
        return sum(answers) / len(answers)
    else:
        return float("nan")


calculate = score  # for legacy


@preparse.PreParser(posix=False).click()
@click.command(add_help_option=False)
@click.option(
    "--format",
    "f",
    help="format of the output",
    default=".5f",
    show_default=True,
)
@click.help_option("-h", "--help")
@click.version_option(None, "-V", "--version")
@click.argument("seq")
def main(seq, f):
    """calculate the GRAVY score of seq"""
    ans = score(seq)
    out = format(ans, f)
    click.echo(out)
