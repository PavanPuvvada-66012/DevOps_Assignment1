"""
This module is a test project to save workouts and their duration
"""

import tkinter as tk
from tkinter import messagebox


class FitnessTrackerApp: # pylint: disable=too-many-instance-attributes

    """
    A Tkinter-based fitness tracker application.

    This class manages the GUI and stores user workouts,
    allowing users to add and track their fitness activities.
    """

    def __init__(self, master):
        """
        Function block to initate the App
        """
        self.master = master
        master.title("ACEestFitness and Gym")

        self.workouts = []

        # Labels and Entries for adding workouts
        self.workout_label = tk.Label(master, text="Workout:")
        self.workout_label.grid(row=0, column=0, padx=5, pady=5)
        self.workout_entry = tk.Entry(master)
        self.workout_entry.grid(row=0, column=1, padx=5, pady=5)

        self.duration_label = tk.Label(master, text="Duration (minutes):")
        self.duration_label.grid(row=1, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(master)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(master, text="Add Workout", command=self.add_workout)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Workouts", command=self.view_workouts)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

    def add_workout(self):
        """
        Add a new workout to the tracker.
        """
        workout = self.workout_entry.get()
        duration_str = self.duration_entry.get()

        if not workout or not duration_str:
            messagebox.showerror("Error", "Please enter both workout and duration.")
            return

        try:
            duration = int(duration_str)
            self.workouts.append({"workout": workout, "duration": duration})
            messagebox.showinfo("Success", f"'{workout}' added successfully!")
            self.workout_entry.delete(0, tk.END)
            self.duration_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Duration must be a number.")

    def view_workouts(self):
        """
        Method to see the logged workouts
        """

        if not self.workouts:
            messagebox.showinfo("Workouts", "No workouts logged yet.")
            return

        workout_list = "Logged Workouts:\n"
        for i, entry in enumerate(self.workouts):
            workout_list += f"{i+1}. {entry['workout']} - {entry['duration']} minutes\n"
        messagebox.showinfo("Workouts", workout_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()
