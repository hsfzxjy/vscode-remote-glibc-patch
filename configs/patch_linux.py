import sys
import re

target_linux_version = sys.argv[1]
v0, v1, v2 = map(int, target_linux_version.split("."))

template_path = sys.argv[2]
with open(template_path, "r") as f:
    template = f.read()


def sub_CT_LINUX_VERSION(template):
    return re.sub(
        r'^CT_LINUX_VERSION="(.*)"',
        f'CT_LINUX_V_{v0}_{v1}=y\nCT_LINUX_VERSION="{target_linux_version}"',
        template,
        flags=re.MULTILINE,
    )


def sub_CT_LINUX_OLDER_LATER(template):
    def sub1(match: re.Match[str]) -> str:
        x = int(match.group(1))
        y = int(match.group(2))
        if (x, y) <= (v0, v1):
            return f"CT_LINUX_{x}_{y}_or_later"
        else:
            return f"CT_LINUX_{x}_{y}_or_older"

    template = re.sub(
        r"CT_LINUX_(\d+)_(\d+)_or_(later|older)",
        sub1,
        template,
        flags=re.MULTILINE,
    )

    def sub2(match: re.Match[str]) -> str:
        x = int(match.group(2))
        y = int(match.group(3))
        if (x, y) <= (v0, v1):
            return f"CT_LINUX_later_than_{x}_{y}"
        else:
            return f"CT_LINUX_older_than_{x}_{y}"

    template = re.sub(
        r"CT_LINUX_(older|later)_than_(\d+)_(\d+)",
        sub2,
        template,
        flags=re.MULTILINE,
    )
    return template


def sub_CT_GLIBC_MIN_KERNEL(template):
    return re.sub(
        r"CT_GLIBC_MIN_KERNEL=\"(.*)\"",
        f'CT_GLIBC_MIN_KERNEL="{target_linux_version}"',
        template,
        flags=re.MULTILINE,
    )


if __name__ == "__main__":
    template = sub_CT_LINUX_VERSION(template)
    template = sub_CT_LINUX_OLDER_LATER(template)
    template = sub_CT_GLIBC_MIN_KERNEL(template)
    sys.stdout.write(template)
