import re
import functools
import tokenize
import collections
from typing import Optional, Dict, Set
from enum import Enum
from pathlib import Path

class LineNumberErrors(Enum):
    L001 = 'L001 File is too long (limit: {limit}, total lines: {total_lines})'

DIFF_HUNK_REGEXP = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@.*$")

@functools.lru_cache(maxsize=1)
def stdin_get_value() -> str:
    """Get and cache it so plugins can use it."""
    stdin_value = sys.stdin.buffer.read()
    fd = io.BytesIO(stdin_value)
    try:
        coding, _ = tokenize.detect_encoding(fd.readline)
        fd.seek(0)
        return io.TextIOWrapper(fd, coding).read()
    except (LookupError, SyntaxError, UnicodeError):
        return stdin_value.decode("utf-8")


def config_parser(linenumber_config):
    size_pairs = map(lambda s: s.split('='), linenumber_config)
    return {Path(filename): int(size) for filename, size in size_pairs}

def parse_unified_diff(diff: Optional[str] = None) -> Dict[str, Set[int]]:
    """Parse the unified diff passed on stdin.

    :returns:
        dictionary mapping file names to sets of line numbers
    """
    # Allow us to not have to patch out stdin_get_value
    if diff is None:
        diff = stdin_get_value()

    number_of_rows = None
    current_path = None
    parsed_paths: Dict[str, Set[int]] = collections.defaultdict(set)
    for line in diff.splitlines():
        if number_of_rows:
            if not line or line[0] != "-":
                number_of_rows -= 1
            # We're in the part of the diff that has lines starting with +, -,
            # and ' ' to show context and the changes made. We skip these
            # because the information we care about is the filename and the
            # range within it.
            # When number_of_rows reaches 0, we will once again start
            # searching for filenames and ranges.
            continue

        # NOTE(sigmavirus24): Diffs that we support look roughly like:
        #    diff a/file.py b/file.py
        #    ...
        #    --- a/file.py
        #    +++ b/file.py
        # Below we're looking for that last line. Every diff tool that
        # gives us this output may have additional information after
        # ``b/file.py`` which it will separate with a \t, e.g.,
        #    +++ b/file.py\t100644
        # Which is an example that has the new file permissions/mode.
        # In this case we only care about the file name.
        if line[:3] == "+++":
            current_path = line[4:].split("\t", 1)[0]
            # NOTE(sigmavirus24): This check is for diff output from git.
            if current_path[:2] == "b/":
                current_path = current_path[2:]
            # We don't need to do anything else. We have set up our local
            # ``current_path`` variable. We can skip the rest of this loop.
            # The next line we will see will give us the hung information
            # which is in the next section of logic.
            continue

        hunk_match = DIFF_HUNK_REGEXP.match(line)
        # NOTE(sigmavirus24): pep8/pycodestyle check for:
        #    line[:3] == '@@ '
        # But the DIFF_HUNK_REGEXP enforces that the line start with that
        # So we can more simply check for a match instead of slicing and
        # comparing.
        if hunk_match:
            (row, number_of_rows) = (
                1 if not group else int(group) for group in hunk_match.groups()
            )
            assert current_path is not None
            parsed_paths[current_path].update(range(row, row + number_of_rows))

    # We have now parsed our diff into a dictionary that looks like:
    #    {'file.py': set(range(10, 16), range(18, 20)), ...}
    return parsed_paths


class LineNumberPlugin:
    name = __name__
    version = '0.1.10'

    def __init__(self, tree, total_lines, filename):
        self.total_lines = total_lines
        self.filename = Path(filename)
        if self.diff:
            self.last_changed_lines = {
                Path(f): max(changed_lines)
                for f, changed_lines in parse_unified_diff().items()
                if changed_lines
            }

    @classmethod
    def add_options(cls, options_manager):
        options_manager.add_option(
            '--max-linenumber',
            type='int',
            default=None,
            parse_from_config=True,
            help='Default max line limit for a python module'
        )
        options_manager.add_option(
            '--linenumber',
            type='str',
            comma_separated_list=True,
            default=[],
            parse_from_config=True,
            help='List of modules and their max line nums'
        )

    @classmethod
    def parse_options(cls, options):
        cls.filesizes = config_parser(options.linenumber)
        cls.diff = options.diff
        cls.default_limit = options.max_linenumber

    def run(self):
        filesize_limit = self.filesizes.get(self.filename, self.default_limit)

        if filesize_limit and self.total_lines > filesize_limit:
            message = LineNumberErrors.L001.value.format(
                limit=filesize_limit,
                total_lines=self.total_lines
            )

            # report error on last line of the file
            err_line = self.total_lines - 1

            # if flake is run on diff, then report on last changed line
            if self.diff and self.filename in self.last_changed_lines:
                err_line = self.last_changed_lines[self.filename]

            yield (err_line, 0, message, 1)
