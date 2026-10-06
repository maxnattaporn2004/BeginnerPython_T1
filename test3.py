app = ctk.CTk()
app.title("MaMax") 
app.geometry("400x400")

pages = {}

def show_page(page_name):
    for page in pages.values():
        page.pack_forget()

    pages[page_name].pack(fill= 'both', expand=True)

class LoginPage(ctk.CTkFrame):
    def __init__(self, master , switch_page):
        super().__init__(master)
        self.pack(fill='both', expand=True)
        self.switch_page = switch_page

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter your name")
        self.entry.pack(pady=20)

        self.label = ctk.CTkLabel(self, text="")
        self.label.pack(pady=10)

        self.button = ctk.CTkButton(self, text="เข้าสู่ระบบ", command=self.login)


    def login(self):
        name = self.entry.get()
        if name == 'admin':
            self.switch_page("home")
        else:
            self.label.configure(text="ชื่อผู้ใช้ไม่ถูกต้อง", text_color="red")
