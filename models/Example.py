import peewee

DB = MySQLDatabase("",
						host="",
						port=3306,
						user="",
						passwd="")


# This class represent a Table in your database, it must be with the same name, but in lower case. In this case 'example'
class Example(Model):
	id = IntegerField(null=False)
    name = CharField(max_length=800, null=False)

    class Meta:
        database = DB


DB.connect()
