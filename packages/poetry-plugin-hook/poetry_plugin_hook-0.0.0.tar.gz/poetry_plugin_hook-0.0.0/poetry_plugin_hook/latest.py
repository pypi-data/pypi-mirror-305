import re

from poetry.console.commands.show import ShowCommand

from .redirect import buffered_io, strip_ansi


class LatestCommand(ShowCommand):
    name = "hook latest"
    description = "Check if all top-level dependencies are up-to-date."
    help = ""

    _dependencies = re.compile(
        r"^(?P<package>\w\S+)\s+"
        r"(?P<current>\d\S+)\s+"
        r"(?P<latest>\d\S+)\s+"
        r"(?P<description>\w.*?)$",
        re.MULTILINE,
    )

    _true_options = ["latest", "outdated", "top-level"]
    _del_options = ["no-dev", "tree", "all", "why"]

    def configure(self) -> None:
        """
        Modifiy all options from `poetry show` to fit the `poetry latest` command.

        Returns:
            None
        """

        self.options = [
            option for option in self.options if option.name not in self._del_options
        ]

        for opt in filter(lambda o: o.name in self._true_options, self.options):
            opt._description += " <warning>(option is always True)</warning>"

        super().configure()

    def handle(self) -> int:
        """
        Executes `poetry show -o -T` to check for outdated dependencies.

        Catches stdout to check for dependencies and returns non-zero.

        Returns:
            int: Non-zero if there are outdated dependencies, zero otherwise.
        """

        # force options to True, `poetry show -o -T`
        for option in self._true_options:
            self.io.input.set_option(option, True)

        # redirect output to check for outdated dependencies
        with buffered_io(self) as io:
            super().handle()
            text = io.fetch_output()

        # count outdated dependencies
        outdated = len(
            self._dependencies.findall(
                strip_ansi(text),
            )
        )

        if outdated == 0:
            self.line("All top-level dependencies are up-to-date.")
        else:
            self.line(text)

        return outdated
