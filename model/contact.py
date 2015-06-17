

class Contact:


   def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
   address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
   homepage=None, address2=None, notes=None, phone2=None, ayear=None, byear=None, id=None, name=None, name_2=None):
      self.firstname = firstname
      self.middlename = middlename
      self.lastname = lastname
      self.nickname = nickname
      self.title = title
      self.company = company
      self.address = address
      self.home = home
      self.mobile = mobile
      self.work = work
      self.fax = fax
      self.email = email
      self.email2 = email2
      self.email3 = email3
      self.homepage = homepage
      self.byear = byear
      self.ayear = ayear
      self.address2 = address2
      self.phone2 = phone2
      self.notes = notes
      self.id = id
      self.name = name
      self.name_2 = name_2


   def __repr__(self):
      return "%s:%s" % (self.id, self.name)


   def __eq__(self, other):
      return self.id == other.id and self.name == other.name


