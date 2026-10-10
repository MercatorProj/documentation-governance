#!/usr/bin/env python3
"""Best-effort checker for local Markdown links and image references."""
from pathlib import Path
import argparse, re, sys, urllib.parse
LINK_RE = re.compile(r'!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+["\'][^)]*["\'])?\)')
REF_RE = re.compile(r'^\s*\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))', re.M)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('root', nargs='?', default='docs', help='docs directory (default: docs)')
    ap.add_argument('--ignore', action='append', default=[], help='substring to ignore in target')
    args=ap.parse_args(); root=Path(args.root).resolve()
    if not root.is_dir(): print(f'error: directory not found: {root}', file=sys.stderr); return 2
    files=list(root.rglob('*.md'))+list(root.rglob('*.mdx'))
    errors=[]; checked=0
    for src in sorted(set(files)):
        try: text=src.read_text(encoding='utf-8', errors='replace')
        except OSError as e: errors.append((src,'',f'cannot read: {e}')); continue
        targets=[]
        targets += [a or b for a,b in LINK_RE.findall(text)]
        targets += [a or b for a,b in REF_RE.findall(text)]
        for raw in targets:
            target=raw.strip().replace('&amp;','&')
            if not target or any(x in target for x in args.ignore): continue
            parsed=urllib.parse.urlsplit(target)
            if parsed.scheme or target.startswith('//') or target.startswith('mailto:') or target.startswith('tel:'): continue
            path=urllib.parse.unquote(parsed.path)
            if not path:
                # Anchor-only link; anchor existence requires Markdown-aware parsing.
                continue
            checked+=1
            candidate=(src.parent/path).resolve() if not path.startswith('/') else (root/path.lstrip('/')).resolve()
            # VitePress public root files can be referenced with /; test root-relative docs path.
            if candidate.exists(): continue
            # Directory links may map to index.md.
            if candidate.is_dir() and any((candidate/n).exists() for n in ('index.md','README.md')): continue
            errors.append((src,raw,'target not found'))
    for src,target,msg in errors: print(f'{src.relative_to(root)}: {msg}: {target}')
    print(f'Checked {checked} local targets across {len(files)} Markdown files; {len(errors)} issue(s).')
    if errors: return 1
    print('Note: this best-effort check does not fully validate anchors, Vue imports, VitePress aliases, or all public-root semantics.')
    return 0
if __name__=='__main__': raise SystemExit(main())
