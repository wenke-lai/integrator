from base64 import b64encode
from pathlib import Path
from typing import Optional


class UserData:
    def __init__(self, path: Optional[Path] = None) -> None:
        """Create a new EC2 User Data script.

        Args:
            script (str): The user data script.
        """
        self.script = ""

        if path:
            self.execute(path)

    def append(self, *commands: list[str]) -> None:
        """Append commands to the user data script.

        Args:
            *commands (list[str]): The commands to append.
        """
        self.script += "\n".join(commands)
        self.script += "\n"

    def execute(self, path: Path | str) -> None:
        """Append a script to user data

        Args:
            path (Path|str): The path of the script.
        """
        if not Path(path).is_file():
            raise FileNotFoundError(f"Invalid file path: {path}")

        with open(path, "r", encoding="utf-8") as fr:
            self.append(fr.read())

    def download_and_execute(self, bucket: str, filename: str) -> None:
        source_path = f"s3://{bucket}/{filename}"
        target_path = f"/tmp/{filename}"
        self.append(
            f"mkdir -p $(dirname {target_path})",
            f"aws s3 cp {source_path} {target_path}",
            f"sh -x {target_path}",
        )

    def b64encode(self) -> str:
        """Base64 encode the user data script.

        Returns:
            str: The base64 encoded user data script.
        """
        return b64encode(self.script.encode()).decode()
