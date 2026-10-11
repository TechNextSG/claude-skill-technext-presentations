# -*- coding: utf-8 -*-
"""Mirror the published decks (root HTML, README, assets/, pdf/, sw.js) into the team's Drive folder and md5-verify
every file (Google Drive sync can corrupt large binaries: reference_google_drive_sync_hazards).
Files in the Drive copy that the repo no longer has are LISTED, not deleted: deleting is the user's call.

    python drive_sync.py            # copy + verify
    python drive_sync.py --check    # verify only, copy nothing
"""
import hashlib, pathlib, shutil, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _cdp import REPO as SRC  # noqa: E402

DST = pathlib.Path(r"G:\Shared drives\Marketing\00. TechNext Folder\07. TechNext Presentations\HTML Presentations")


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    check = "--check" in sys.argv
    files = sorted(SRC.glob("*.html")) + [SRC / "README.md", SRC / "sw.js"]
    files += [p for p in (SRC / "assets").rglob("*") if p.is_file()] + [p for p in (SRC / "pdf").rglob("*") if p.is_file()]
    copied = same = 0
    bad = []
    for p in files:
        rel = p.relative_to(SRC)
        q = DST / rel
        m = md5(p)
        if q.exists() and md5(q) == m:
            same += 1
            continue
        if check:
            bad.append(str(rel))
            continue
        q.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(p, q)
        copied += 1
        if md5(q) != m:
            shutil.copyfile(p, q)
            if md5(q) != m:
                bad.append(str(rel))
    want = {str(p.relative_to(SRC)) for p in files}
    extra = sorted(str(q.relative_to(DST)) for q in DST.rglob("*") if q.is_file() and str(q.relative_to(DST)) not in want)
    print(f"{len(files)} files: {copied} copied, {same} identical, {len(bad)} {'differ' if check else 'failed verification'} {bad[:10]}")
    if extra:
        print(f"in Drive but not in the repo ({len(extra)}; not deleted):", extra[:20], "..." if len(extra) > 20 else "")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
