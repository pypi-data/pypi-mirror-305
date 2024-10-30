from src.Pylite import Database,email,password

# db = Database.LoadFromSQL("DataBase.db").Save("DataBase.pylite","password")
db = Database()
db.CreateTable("Users").AddColumn(
    ID = int,
    Email = email,
    Password = password
)
db.Users.Insert(ID=1,Email="test@test.com",Password="wooaA1!zae6")
print(db.Users)


