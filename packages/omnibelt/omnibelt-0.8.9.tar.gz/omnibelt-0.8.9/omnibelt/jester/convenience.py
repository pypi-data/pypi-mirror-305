import random
from typing import Dict
from .. import pformat
from .imports import *
from tabulate import tabulate



def select(seq: Iterable[Dict[str, Any]], n: int = 10) -> Iterable[Dict[str, Any]]:
	try:
		len(seq)
	except TypeError:
		seq = list(seq)
	if n is None:
		return seq
	if len(seq) <= n:
		return seq
	return random.choices(seq, k=n)



def view(seq: Iterable[Dict[str, Any]], *keys: str | Callable[[Dict[str, Any]], Any], world: None = None,
		 sortby: str | Callable[[Dict[str, Any]], Any] | Iterable[str] = None, descending: bool = False,
		 n: int = None, force: bool = False, allow_patterns:  bool = True, tablefmt: str = 'simple') -> str:
	if world is None:
		world = {}

	seq = select(seq, n=n)

	if sortby is not None:
		if isinstance(sortby, str):
			sortby = lambda item: item.get(sortby)
		elif callable(sortby):
			pass
		else:
			sortby = lambda item: tuple(item.get(key) for key in sortby)
		seq = sorted(seq, key=sortby, reverse=descending)

	existing = {key for item in seq for key in item}

	ops = []
	for key in keys:
		if callable(key):
			ops.append(key)
		elif key in existing:
			ops.append(lambda item: item.get(key))
		elif allow_patterns and isinstance(key, str):
			ops.append(lambda item: pformat(key, item, world))
		else:
			raise ValueError(f"Key '{key}' not found in any item")

	table = []
	for item in seq:
		table.append([op(item) for op in ops])

	print(tabulate(table, tablefmt=tablefmt))

	return seq



def batchify(seq: Iterable[Dict[str, Any]], batch_size: int = 10, *,
			 drop_last: bool = False, shuffle: bool = False) -> Iterable[Dict[str, Any]]:
	if shuffle:
		seq = list(seq)
		random.shuffle(seq)

	seq = iter(seq)

	while True:
		batch = []
		for _ in range(batch_size):
			try:
				batch.append(next(seq))
			except StopIteration:
				if not batch:
					return
				if drop_last:
					return
				break
		yield batch




















