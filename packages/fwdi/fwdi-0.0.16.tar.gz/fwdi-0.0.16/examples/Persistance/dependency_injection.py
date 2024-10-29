from Persistance.guest_controller import GuestController
from Persistance.admin_controller import AdminController
from Persistance.user_controller import UserController
from fwdi.WebApp.web_application import WebApplication


class WebService():
    def AddControllers(app:WebApplication)->None:
        app.map_controller(GuestController())
        app.map_controller(AdminController())
        app.map_controller(UserController())