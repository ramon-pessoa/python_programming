def build_fs(input):
	fs = {}
	files = input.split('\n')

	current_path = []
	for f in files:
		indentation = 0
		while '\t' in f[:2]:
			indentation += 1
			f = f[1:]

		current_node = fs
		for subdir in current_path[:indentation]:
			current_node = current_node[subdir]

		if '.' in f:
			current_node[f] = True
		else:
			current_node[f] = {}

		current_path = current_path[:indentation]
		current_path.append(f)

	return fs


def longest_path(root):
	paths = []
	for key, node in root.items():
		if node == True:
			paths.append(key)
		else:
			paths.append(key + '/' + longest_path(node))
	# filter out unfinished paths
	paths = [path for path in paths if '.' in path]
	if paths:
		return max(paths, key=lambda path:len(path))
	else:
		return ''


def longest_absolute_path(s):
	return len(longest_path(build_fs(s)))
