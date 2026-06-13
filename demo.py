from __future__ import annotations

import json
import platform
import socket
import sys
from datetime import datetime, timezone


def main() -> None:
    result = {
        "status": "success",
        "message": "Ansible executed the GitHub project successfully.",
        "hostname": socket.gethostname(),
        "operating_system": platform.platform(),
        "python_version": sys.version.split()[0],
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
