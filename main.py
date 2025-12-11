from task_manager import TaskManager

# Créer le gestionnaire
manager = TaskManager()

# Ajouter des tâches
manager.add_task("Apprendre Git", 
                 "Suivre le cours")
manager.add_task("Faire l'exercice")
manager.add_task("Réviser pour l'exam")

# Compléter une tâche
manager.complete_task(0)
manager.complete_task(1)

# Afficher
print("=== Mes tâches ===")
manager.display_all()

#Supprimer une tache..
def remove_task(self, index):
    """Supprime une tâche par son index."""
    if 0 <= index < len(self.tasks):
        del self.tasks[index]
        return True
    return False