# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 11:32:07 2017

@author: 진건지역아동센터
"""

class Contact:
    def __init__(self,name,phone,addr,email):
        self.name = name
        self.phone = phone
        self.addr = addr
        self.email = email
    def info_print(self):
        print('name = ', self.name)
        print('phone = ', self.phone)
        print('addr = ' , self.addr)
        print('email = ' , self.email)
        
def print_contact(manlist):
    for x in manlist:
        x.info_print()
    
    
def set_contact():
    name = input('name = ')
    phone = input('phone =')
    addr = input('addr =')
    email = input('email =')
    man = Contact(name , phone , addr , email)
    return (man)
    
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    a = input("메뉴선택: ")
    print(a)
    return int(a)

def delete_contact(manlist, name):
    for i , man in enumerate(manlist):
        if man.name == name:
            del manlist[i]

def run():
    manlist = []
    while 1:
        menu=print_menu()
        if menu== 1:
            man = set_contact()
            manlist.append(man)
        elif menu ==2:
            print_contact(manlist)
        elif menu ==3:
            name = input("name : ")
            delete_contact(manlist, name)
        elif menu == 4:
            break
    print(len(manlist))

if __name__ == '__main__':
    run()
    