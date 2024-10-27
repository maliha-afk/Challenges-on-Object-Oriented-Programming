class room:
    def __init__(self,room_number,room_type,price,avaliable):
        self.room_number=room_number
        self.room_type=room_type
        self.price=price
        self.avaliable=True
    
    def book_room(self):
       if self.avaliable==True:
          self.avaliable=False
          return True 


    def release_room(self):
        self.avaliable=True

    def roominfo(self):
        print(f"room number: {self.room_number}\n room type: {self.room_type}\n room price: {self.price}/night")

class Customer:
    def __init__(self,id,contact_number,name):
        self.id=id
        self.contact_number=contact_number
        self.name=name

    def customerinfo(self):
        print(f"customer name{self.name}\n customer id{self.id}\n customer contact_number{self.contact_number}")


class booking:
    def __init__(self,customer,room,nights):
        self.customer=customer
        self.room=room
        self.nights=nights

    def total_price(self):
       total_price= self.nights*self.room.price
       print(f"total price: {total_price}")

    def book(self):
       if self.room.book_room()==True:
        print("room booked sucesfully!")
        print(f"customer details:\n name: {self.customer.name}, id: {self.customer.id}, contact_number: {self.customer.contact_number}")
        print(f"room details:\n room number{self.room.room_number}\n room type{self.room.room_type}")
        print(f"total price: {self.total_price()} $ ")
       else:
           print("room ")
           return False
    
    
    def cancel(self):
        self.room.release_room()    
        print("room canceled")

room101=room(101,"2 bed AC",3500,True)
customer1=Customer("Atiya",12345,12344524045)
Customer2=Customer("Irfan",32145,75983804728)
book1=booking(customer1,room101,3)
book1.book()
book1.cancel()