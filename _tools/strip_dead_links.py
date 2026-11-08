#!/usr/bin/env python3
"""Remove Liquid links to posts that are not published yet. Usage: strip_dead_links.py <file>"""
import sys,re,glob,os
f=sys.argv[1]
have=set(re.sub(r'^\d{4}-\d\d-\d\d-','',os.path.basename(p))[:-3] for p in glob.glob('_posts/*.md'))
t=open(f).read()
def rep(m):
    return m.group(0) if m.group(2) in have else m.group(1)
t2=re.sub(r"\[([^\]]+)\]\(\{\{ '/posts/([^/']+)/' \| relative_url \}\}\)",rep,t)
if t2!=t: open(f,'w').write(t2); print('stripped dead links in',f)
