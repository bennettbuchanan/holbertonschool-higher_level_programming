import Tkinter as tk
from h_ip import IPThread

class IPView(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        # Entry where user will enter an IP address
        self.ip_entry = tk.Entry(self)
        self.ip_entry.pack()
        self.ip_entry.focus_set()

        # Label of the resolution result
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self, textvariable=self.result_var)
        self.result_label.pack()

        # Submit button
        self.submit_button = tk.Button(self, text='Submit', width=20)
        self.submit_button.config(command=self.submit_ip)
        self.submit_button.pack()

    # Submit action => start a thread
    def submit_ip(self):
        ip = self.ip_entry.get()
        self.result_var.set("loading...")
        t = IPThread(ip, self.display_result)
        t.start()

    # Callback to display the result
    def display_result(self, country_name):
        self.result_var.set(country_name)


# Main
root = tk.Tk()
root.withdraw()
view = IPView(root)
root.mainloop()
