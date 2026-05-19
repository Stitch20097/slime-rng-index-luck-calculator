#--- Index Luck Calculator ---
#---      Version 2.3      ---

#--- Import ---
import math
import tkinter as tk

#--- Index ---
index = {
    'Goopy': 3, 'Sunset': 5, 'Fin': 8, 'Leafy': 11, 'Meow': 35,'Glo': 57, 'Buggy': 103, 'Boomy': 160, 'Brutis': 263,'Frankenslime': 415, 'Orca': 719, 'Spike': 1260,'Axolotl': 2390, 'Spidey': 4270, 'Mushy': 7770, 'Rocky': 13900,
    'Lucky': 21500, 'Stump': 53800,'Pondy':53800, 'Icy': 86100, 'Orbit': 126000,'Aegis': 215000, 'Wicked': 326000, 'King': 538000,'Guest': 861000, 'Ninja': 1260000, 'Buzz': 2150000,'Stormy': 3070000, 'Bucky': 4780000, 'Pokey': 7180000,
    'SlimeSlime': 10700000, 'Unicorn': 17900000, 'Wizzy': 26900000,'Shelly': 61500000, 'Derpy': 89700000, 'Octo': 134000000,'Halo': 195000000, 'Bomber': 307000000, 'UFO': 478000000,'Witchy': 718000000, 'Blackhole': 1007000000,
    'Ember': 1720000000, 'Pumpkin': 2770000000, 'Ouchy': 4390000000,'Sharky': 6470000000, 'Dino': 10100000000, 'Monke': 15300000000,'Prickly': 23900000000, 'Zoomy': 34200000000,'Waxie': 50100000000, 'Drakey': 74300000000,
    'Germy': 133000000000, 'Palmy': 172000000000,'Melly': 237000000000, 'Snazzy': 269000000000,'Bemmy': 414000000000, 'Mato': 673000000000,'Frosty': 1070000000000, 'Pouchy': 1720000000000,'Hoppity': 2690000000000, 'Sweetie': 3500000000000,
    'Shady': 3990000000000, 'Galaxy': 6950000000000,'Painty': 11300000000000, 'Patty': 18700000000000,'Broclee': 28700000000000, 'Meaty': 43000000000000,'Zappy': 67300000000000,
}
index_lookup = {name.lower(): name for name in index}

COLORS = {
    "bg": "#202124",
    "panel": "#2b2d31",
    "panel_2": "#34373d",
    "border": "#4b4f58",
    "hover": "#424750",
    "text": "#f4f4f5",
    "muted": "#b5bac1",
    "soft": "#d4d7dc",
    "accent": "#22c55e",
    "accent_hover": "#16a34a",
    "blue": "#4dabf7",
    "blue_hover": "#339af0",
    "warning": "#fbbf24",
    "error": "#fb7185",
}


def get_luck(slime):
    slime_name = index_lookup.get(slime.strip().lower())

    if slime_name is None:
        return None, None

    luck = math.ceil(index[slime_name] / 3)
    return slime_name, luck


class LuckCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Slime RNG Index Luck Calculator")
        self.geometry("920x570")
        self.minsize(840, 520)
        self.configure(bg=COLORS["bg"])

        self.slime_names = list(index.keys())
        self.search_text = tk.StringVar(value="")
        self.result_text = tk.StringVar(value="")
        self.slime_text = tk.StringVar(value="")
        self.index_text = tk.StringVar(value="")
        self.status_text = tk.StringVar(value="")
        self.selected_slime = None
        self.hovered_index = None

        self.build_widgets()
        self.refresh_slime_list()
        self.status_text.set("Choose a slime to see the recommended luck.")

    def build_widgets(self):
        outer = tk.Frame(self, bg=COLORS["bg"])
        outer.pack(fill="both", expand=True, padx=24, pady=22)
        outer.columnconfigure(0, weight=3, minsize=260)
        outer.columnconfigure(1, weight=4, minsize=340)
        outer.rowconfigure(2, weight=1)

        title = tk.Label(
            outer,
            text="Slime RNG Index Luck Calculator",
            bg=COLORS["bg"],
            fg=COLORS["text"],
            font=("Segoe UI", 22, "bold"),
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w")

        subtitle = tk.Label(
            outer,
            text="Pick a slime and the recommended luck updates instantly.",
            bg=COLORS["bg"],
            fg=COLORS["muted"],
            font=("Segoe UI", 10),
        )
        subtitle.grid(row=1, column=0, columnspan=2, sticky="w", pady=(4, 0))

        picker = tk.Frame(
            outer,
            bg=COLORS["panel"],
            highlightbackground=COLORS["border"],
            highlightthickness=1,
            bd=0,
        )
        picker.grid(row=2, column=0, sticky="nsew", pady=(22, 0), padx=(0, 14))
        picker.rowconfigure(3, weight=1)
        picker.columnconfigure(0, weight=1)

        tk.Label(
            picker,
            text="Slime Picker",
            bg=COLORS["panel"],
            fg=COLORS["text"],
            font=("Segoe UI", 13, "bold"),
        ).grid(row=0, column=0, sticky="w", padx=18, pady=(18, 4))

        tk.Label(
            picker,
            text="Search or scroll through the index",
            bg=COLORS["panel"],
            fg=COLORS["muted"],
            font=("Segoe UI", 9),
        ).grid(row=1, column=0, sticky="w", padx=18)

        search_shell = tk.Frame(
            picker,
            bg=COLORS["panel_2"],
            highlightbackground=COLORS["border"],
            highlightcolor=COLORS["blue"],
            highlightthickness=1,
            bd=0,
        )
        search_shell.grid(row=2, column=0, sticky="ew", padx=18, pady=(14, 12))
        search_shell.columnconfigure(0, weight=1)

        self.search_entry = tk.Entry(
            search_shell,
            textvariable=self.search_text,
            bg=COLORS["panel_2"],
            fg=COLORS["text"],
            insertbackground=COLORS["text"],
            relief="flat",
            bd=0,
            font=("Segoe UI", 12),
        )
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=12, pady=10)
        self.search_entry.bind("<KeyRelease>", self.on_search_change)
        self.search_entry.bind("<Return>", self.select_first_match)
        self.search_entry.bind("<Down>", self.focus_list)

        list_shell = tk.Frame(picker, bg=COLORS["border"], bd=0)
        list_shell.grid(row=3, column=0, sticky="nsew", padx=18, pady=(0, 18))
        list_shell.rowconfigure(0, weight=1)
        list_shell.columnconfigure(0, weight=1)

        self.slime_list = tk.Listbox(
            list_shell,
            bg=COLORS["panel_2"],
            fg=COLORS["soft"],
            selectbackground=COLORS["blue"],
            selectforeground="#06121f",
            highlightthickness=0,
            relief="flat",
            bd=0,
            font=("Segoe UI", 11),
            activestyle="none",
            exportselection=False,
            cursor="hand2",
        )
        self.slime_list.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
        self.slime_list.bind("<<ListboxSelect>>", self.on_list_select)
        self.slime_list.bind("<Return>", self.select_current_list_item)
        self.slime_list.bind("<Motion>", self.on_list_hover)
        self.slime_list.bind("<Leave>", self.clear_hover)

        scrollbar = tk.Scrollbar(
            list_shell,
            orient="vertical",
            command=self.slime_list.yview,
            bg=COLORS["panel_2"],
            troughcolor=COLORS["panel"],
            activebackground=COLORS["blue"],
            highlightthickness=0,
            bd=0,
        )
        scrollbar.grid(row=0, column=1, sticky="ns", pady=1)
        self.slime_list.configure(yscrollcommand=scrollbar.set)

        result_panel = tk.Frame(
            outer,
            bg=COLORS["panel"],
            highlightbackground=COLORS["border"],
            highlightthickness=1,
            bd=0,
        )
        result_panel.grid(row=2, column=1, sticky="nsew", pady=(22, 0))
        result_panel.columnconfigure(0, weight=1)

        tk.Label(
            result_panel,
            text="Recommended Luck",
            bg=COLORS["panel"],
            fg=COLORS["muted"],
            font=("Segoe UI", 12, "bold"),
        ).grid(row=0, column=0, sticky="w", padx=28, pady=(30, 4))

        self.result_label = tk.Label(
            result_panel,
            textvariable=self.result_text,
            bg=COLORS["panel"],
            fg=COLORS["accent"],
            font=("Segoe UI", 34, "bold"),
            anchor="w",
        )
        self.result_label.grid(row=1, column=0, sticky="ew", padx=28)

        tk.Label(
            result_panel,
            textvariable=self.slime_text,
            bg=COLORS["panel"],
            fg=COLORS["text"],
            font=("Segoe UI", 18, "bold"),
        ).grid(row=2, column=0, sticky="w", padx=28, pady=(22, 0))

        tk.Label(
            result_panel,
            textvariable=self.index_text,
            bg=COLORS["panel"],
            fg=COLORS["soft"],
            font=("Segoe UI", 11),
        ).grid(row=3, column=0, sticky="w", padx=28, pady=(4, 0))

        self.status_label = tk.Label(
            result_panel,
            textvariable=self.status_text,
            bg=COLORS["panel"],
            fg=COLORS["muted"],
            font=("Segoe UI", 10),
        )
        self.status_label.grid(row=4, column=0, sticky="w", padx=28, pady=(18, 0))

        actions = tk.Frame(result_panel, bg=COLORS["panel"])
        actions.grid(row=5, column=0, sticky="w", padx=28, pady=(34, 0))

        self.copy_button = self.make_button(
            actions,
            text="Copy Luck Number",
            bg=COLORS["blue"],
            hover_bg=COLORS["blue_hover"],
            command=self.copy_luck,
        )
        self.copy_button.pack(side="left")

        self.clear_button = self.make_button(
            actions,
            text="Clear Search",
            bg=COLORS["border"],
            hover_bg="#334155",
            command=self.clear_search,
        )
        self.clear_button.pack(side="left", padx=(10, 0))

        self.search_entry.focus_set()

    def make_button(self, parent, text, bg, hover_bg, command):
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg="#ffffff",
            activebackground=hover_bg,
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=18,
            pady=10,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
        )
        button.bind("<Enter>", lambda event: button.configure(bg=hover_bg))
        button.bind("<Leave>", lambda event: button.configure(bg=bg))
        return button

    def refresh_slime_list(self):
        search = self.search_text.get().strip().lower()
        matches = [
            slime_name for slime_name in self.slime_names
            if search in slime_name.lower()
        ]

        self.slime_list.delete(0, "end")
        self.hovered_index = None

        for slime_name in matches:
            self.slime_list.insert("end", slime_name)

        if matches:
            self.status_label.configure(fg=COLORS["muted"])
            self.status_text.set(f"{len(matches)} slime match{'es' if len(matches) != 1 else ''}")
        else:
            self.status_label.configure(fg=COLORS["error"])
            self.status_text.set("No slime found with that name.")

        return matches

    def on_search_change(self, event=None):
        matches = self.refresh_slime_list()

        if len(matches) == 1:
            self.select_slime(matches[0], update_search=False)
        elif not matches:
            self.clear_result()
        else:
            search = self.search_text.get().strip().lower()

            if self.selected_slime and search != self.selected_slime.lower():
                self.clear_result()

    def on_list_select(self, event=None):
        selection = self.slime_list.curselection()

        if selection:
            self.select_slime(self.slime_list.get(selection[0]), update_search=False)

    def on_list_hover(self, event=None):
        if self.slime_list.size() == 0:
            return

        position = self.slime_list.nearest(event.y)
        box = self.slime_list.bbox(position)

        if box is None:
            self.clear_hover()
            return

        top = box[1]
        bottom = top + box[3]

        if event.y < top or event.y > bottom:
            self.clear_hover()
            return

        if position == self.hovered_index:
            return

        self.clear_hover()
        self.hovered_index = position
        self.slime_list.itemconfig(position, bg=COLORS["hover"], fg=COLORS["text"])

    def clear_hover(self, event=None):
        if self.hovered_index is None:
            return

        if self.hovered_index < self.slime_list.size():
            self.slime_list.itemconfig(
                self.hovered_index,
                bg=COLORS["panel_2"],
                fg=COLORS["soft"],
            )

        self.hovered_index = None

    def select_first_match(self, event=None):
        if self.slime_list.size() > 0:
            self.select_slime(self.slime_list.get(0))
        return "break"

    def select_current_list_item(self, event=None):
        selection = self.slime_list.curselection()

        if selection:
            self.select_slime(self.slime_list.get(selection[0]))
        return "break"

    def focus_list(self, event=None):
        if self.slime_list.size() > 0:
            self.slime_list.focus_set()
            self.slime_list.selection_clear(0, "end")
            self.slime_list.selection_set(0)
            self.slime_list.activate(0)
        return "break"

    def select_slime(self, slime_name, update_search=True):
        real_name, luck = get_luck(slime_name)

        if real_name is None:
            self.clear_result()
            return

        if update_search and self.search_text.get() != real_name:
            self.search_text.set(real_name)
            self.refresh_slime_list()

        self.selected_slime = real_name
        result = f"x{luck:,}"
        self.result_text.set(result)
        self.resize_result_text(result)
        self.slime_text.set(real_name)
        self.index_text.set(f"Index chance: 1 / {index[real_name]:,}")
        self.status_label.configure(fg=COLORS["muted"])
        self.status_text.set("Luck is rounded up to the nearest whole number.")

        self.highlight_selected_slime(real_name)

    def resize_result_text(self, result):
        if len(result) >= 19:
            size = 24
        elif len(result) >= 15:
            size = 28
        else:
            size = 34

        self.result_label.configure(font=("Segoe UI", size, "bold"))

    def highlight_selected_slime(self, slime_name):
        for position in range(self.slime_list.size()):
            if self.slime_list.get(position) == slime_name:
                self.slime_list.selection_clear(0, "end")
                self.slime_list.selection_set(position)
                self.slime_list.activate(position)
                self.slime_list.see(position)
                break

    def clear_result(self):
        self.selected_slime = None
        self.result_text.set("")
        self.slime_text.set("")
        self.index_text.set("")

    def copy_luck(self):
        if not self.result_text.get():
            return

        self.clipboard_clear()
        self.clipboard_append(self.result_text.get())
        self.status_label.configure(fg=COLORS["accent"])
        self.status_text.set("Copied luck to clipboard.")

    def clear_search(self):
        self.search_text.set("")
        self.clear_result()
        self.refresh_slime_list()
        self.search_entry.focus_set()


def main():
    app = LuckCalculator()
    app.mainloop()


if __name__ == "__main__":
    main()
