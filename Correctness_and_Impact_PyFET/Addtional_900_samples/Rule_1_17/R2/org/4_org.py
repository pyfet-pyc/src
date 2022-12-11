def database_calling():
    new_name = entry19.get()
    if len(new_name) != 0:
        old_name = staff_name.get()
        backend.update_employee_name(new_name, old_name)
        entry19.destroy()
        update_button.destroy()
        if result:
            for i in status:
                update_that_particular_employee(i)
        elif result is None:
            return
    else:
        entry19.destroy()
        update_button.destroy()
        tkinter.messagebox.showinfo("Error", "Please fill entry")
