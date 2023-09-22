from django.db import models

#whatever database you are using, add database in setting.py file
#Using postgres

#creating models, work like Object relational mapper

#writing a model will create a table in database

class person(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    address=models.CharField(max_length=250)
    
    #This function will display all the data on admin side
    #Make object in shell, and pass values
    def __str__(self):
        return self.name
    #NOT CALLING THIS FUNCTION WILL SHOW PERSON OBEJCT()

#student
class Empl(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    Empid=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
    #Crud
    
#create

#Car=car(pass values)


#car.objects.create(attributes=values)


#car_dict{keys:values}
#car.object.create(**car_dict)  
   
   
#read    

#cars=car.objects.all()
#use for loop to iterate and get all
#To print any attribute, of a specific object use cars=car.objects.get(id=1)
class car(models.Model):
    carname=models.CharField(max_length=30)
    speed=models.IntegerField(default=50)
    carmodel=models.CharField(max_length=30)
    
    def __str__(self):
        return self.carname
    
    


class location(models.Model):
    locationname=models.CharField(max_length=30,unique=True)
    ltype=models.CharField(max_length=50)
    lserial=models.IntegerField()
    
    def __str__(self):
        return self.locationname
    
class items(models.Model):
    iname=models.CharField(max_length=30)
    itype=models.CharField(max_length=50)
    iserial=models.IntegerField()
    itemlocation=models.ForeignKey(location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.iname
    
    #After making a model hit command python manage.py makemigrations
    #python manage.py migrate
    #migrations file will be created
    #if you delete the migrations folders, you will have to rename the migration file
    #because it will still have the files somewhere in cache, so it will not read makemigrations with same file name
    #0001_inital.py if deleted, then rename next file to 0002_inital.py
    
    
    
    
    
    
    
    
    
    
    
    
    #update
    #Car=car.objects.all()
    #Car.carmodel="Value"
    #Car.save()
    #cars=car.objects.get(id=1).update(carname="value")
    
    
    #delelte
    #Delete a specific record
    #car.objects.get(id=1).delete()
    #Delete all record
    #car.objects.all().delete()
    