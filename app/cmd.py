import argparse

from crud import (
	add_task,
	change_task_status,
	delete_all_tasks,
	delete_task,
	get_all_tasks,
	update_task,
)
from models import Status, Task


STATUSES = (Status.TODO, Status.IN_POGRESS, Status.DONE)


def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(description="Gestionnaire de tâches")
	subparsers = parser.add_subparsers(dest="command", required=True)

	add_parser = subparsers.add_parser("add", help="Ajouter une tâche")
	add_parser.add_argument("description")
	add_parser.add_argument("--status", choices=STATUSES, default=Status.TODO)

	list_parser = subparsers.add_parser("list", help="Lister les tâches")
	list_parser.add_argument("--status", choices=STATUSES)

	update_parser = subparsers.add_parser("update", help="Modifier une tâche")
	update_parser.add_argument("id", type=int)
	update_parser.add_argument("description")
	update_parser.add_argument("--status", choices=STATUSES, default=Status.TODO)

	delete_parser = subparsers.add_parser("delete", help="Supprimer une tâche")
	delete_parser.add_argument("id", type=int)

	subparsers.add_parser("delete-all", help="Supprimer toutes les tâches")

	status_parser = subparsers.add_parser("change-status", help="Changer le statut")
	status_parser.add_argument("id", type=int)
	status_parser.add_argument("status", choices=STATUSES)

	return parser


def run(args: argparse.Namespace) -> int:
	if args.command == "add":
		add_task(Task(args.description, args.status))
		print("Tâche ajoutée")
		return 0

	if args.command == "list":
		for task in get_all_tasks(args.status):
			print(f"[{task['id']}] {task['description']} ({task['status']})")
		return 0

	if args.command == "update":
		updated = update_task(args.id, Task(args.description, args.status))
		if not updated:
			print(f"Tâche introuvable: {args.id}")
			return 1
		print("Tâche modifiée")
		return 0

	if args.command == "delete":
		deleted = delete_task(args.id)
		if not deleted:
			print(f"Tâche introuvable: {args.id}")
			return 1
		print("Tâche supprimée")
		return 0

	if args.command == "delete-all":
		delete_all_tasks()
		print("Toutes les tâches ont été supprimées")
		return 0

	changed = change_task_status(args.id, args.status)
	if not changed:
		print(f"Tâche introuvable: {args.id}")
		return 1
	print("Statut modifié")
	return 0


def main() -> int:
	parser = build_parser()
	return run(parser.parse_args())
