from user import Admin


admin = Admin("Khanh", "Nguyen", 27, "Ho Chi Minh City")
admin.describe_user()
admin.privileges.items = ["can ban user"]
admin.privileges.show_privileges()