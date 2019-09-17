import os
import sys
import itertools

def usage():
  print 'Usage: python remove-dup.py {name_length} {target_dir} {sort_by: mtime, size} {do_delete: true, false}'
  sys.exit(1)

def main(argv):
  if len(argv) < 3: usage()

  fname_len = int(argv["name_len"])
  dir = os.path.abspath(argv["target_dir"])
  sort_by = argv.get("sort_by", "mtime") # [size, mtime]
  do_delete = argv.get("do_delete", "false") == "true" # [true, flase]

  print("target dir: `%s`, name_len: `%s`, do_delete: `%s`" % (dir, fname_len, do_delete))

  data = []
  for root, dirs, files in os.walk(dir):
    for name in files:
      path = os.path.join(root, name)
      size = os.path.getsize(path)
      mtime = os.path.getmtime(path)
      ext = os.path.splitext(name)[1]

      data.append({ "name": name, "size": size, "path": path, "mtime": mtime, "ext": ext })

  grouped = itertools.groupby(data, key=lambda el: el["name"][:fname_len])
  for k, files in grouped:
    print "=" * 80
    print "Duplicate files grouped by: `%s`" % k
    print "-" * 80
    ls = sorted(files, key=lambda el: -el[sort_by])
    for file in ls:
      print file

    print ""
    if do_delete:
      print "!! Delete files:"
      for f in ls[1:]:
        print "delete file: `%s`" % f["path"]
        os.remove(f["path"])
    else:
      print "Delete files test:"
      for f in ls[1:]:
        print "delete file: `%s`" % f["path"]

    print ""

if __name__ == '__main__':
  arg_names = ['__name__', 'name_len', 'target_dir', 'sort_by', 'do_delete']
  args = dict(zip(arg_names, sys.argv))
  main(args)
