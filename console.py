#!/usr/bin/python3
""" Import Modules
    Hint ----> 🔐 = to give examples to the programmer about what code is doing
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import aux_functions


class HBNBCommand(cmd.Cmd):
    """ Command line Module Class"""
    classes_list = ['BaseModel', 'User', 'City',
                    'State', 'Place', 'Amenity', 'Review']
    prompt = '(hbnb) '

    def do_quit(self, args):
        """ Quit command to exit the program.
        Usage 🛠:
        1 - quit

        """
        return True

    def emptyline(self):
        " Empty Line "
        pass

    def do_EOF(self, args):
        """ EOF - Press C^d to quit command line """
        print("")
        return True

    def do_create(self, args):
        """ Create a new instance.
        Usage 🛠:
        1 - create <class name>

        """
        if len(args) < 1:
            print("** class name missing **")
        elif args not in self.classes_list:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args)()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        """ Show an instance.
        Usage 🛠:
        1 - show <class> <id>
        2 - <class name>.show("<id>")
        """
        commands = args.split()
        if len(commands) < 1:
            print("** class name missing **")
        elif commands[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            key_to_validate = "{}.{}".format(commands[0], commands[1])
            if key_to_validate not in storage.all():
                print("** no instance found **")
            else:
                for key, obj in storage.all().items():
                    if key == key_to_validate:
                        print(obj)

    def do_destroy(self, args):
        """ Destroy an instance.
        Usage 🛠:
        1 - destroy <class> <id>
        2 - <class name>.destroy("<id>")
        """
        commands = args.split()
        if len(commands) < 1:
            print("** class name missing **")
        elif commands[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            key_to_validate = "{}.{}".format(commands[0], commands[1])
            instances = storage.all()
            if key_to_validate not in instances:
                print("** no instance found **")
            else:
                del instances[key_to_validate]
                storage.save()

    def do_all(self, args):
        """ Print all instances.
        Usage 🛠:
        1 - all <class name>
        2 - all
        3 - <class name>.all()
        """
        if args not in self.classes_list and len(args) > 0:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            list_instances = []
            for key_id in instances.keys():
                key = key_id.split('.')
                if len(args) < 1:
                    list_instances.append(str(instances[key_id]))
                elif key[0] == args:
                    list_instances.append(str(instances[key_id]))
            print(list_instances)

    def do_update(self, args):
        """update an instance.
        Usage 🛠:
        1 - update <class name> <id> <attribute name> "<attribute value>
        2 - <class name>.update(<id>, <attribute name>, <attribute value>)
        3 - <class name>.update(<id>, <dictionary representation>)
        """
        if len(args) < 1:
            print("** class name missing **")
        else:
            comds = args.split()
            if comds[0] not in self.classes_list:
                print("** class doesn't exist **")
            elif len(comds) < 2:
                print('** instance id missing **')
            else:
                instances = storage.all()
                key = "{}.{}".format(comds[0], comds[1])
                if key not in instances:
                    print("** no instance found **")
                if len(comds) < 3:
                    print("** attribute name missing **")
                elif len(comds) < 4:
                    print("** value missing **")
                else:
                    for key_id, obj in instances.items():
                        if key == key_id:
                            value = comds[3].split("\"")
                            # (i.e) evalue if value turns into list 🔐
                            if len(value) > 1:
                                value = value[1]
                            else:
                                value = comds[3]
                            if hasattr(obj, comds[2]):
                                value = type(
                                    getattr(obj, comds[2]))(value)
                                #  (i.e) int(comds[3]) 🔐
                            elif value.isdigit() is True:
                                value = int(value)
                            setattr(obj, comds[2], value)
                            storage.all()[key_id].save()

    def do_count(self, args):
        """ count number of instances.
        Usage 🛠:
        1 - <class name>.count()"""
        count = 0
        instances = storage.all()
        if args not in self.classes_list:
            print("** class doesn't exist **")
        else:
            for key in instances.keys():
                sec_comm = key.split('.')
                # (i.e) User.1233 = User
                if sec_comm[0] == args:
                    count += 1
            print(count)

    def default(self, args):
        """ default method """
        if len(args.split(".")) > 1:
            commands = args.split('.', 1)
            #  (i.e) split till firts coincidence
            #  (i.e) commands = ['__clas__.__name__', 'all()'] 🔐
            try:
                commands[1] = str(commands[1]).replace("'", '"')
                sec_comm = commands[1].split('(')
                #  (i.e) sec_comm = ['all', '('] 🔐
                if sec_comm[0] == 'all':
                    self.do_all(str(commands[0]))
                if sec_comm[0] == 'count':
                    self.do_count(str(commands[0]))
                if sec_comm[0] == 'show':
                    command = sec_comm[1].split('"')
                    #  sec_comm[1] = "123123123") 🔐
                    user_show = str(commands[0] + " " + command[1])
                    #  (i.e) command = ['"' '123123123' , ')'] 🔐
                    #  (i.e) user_show = "class id" = user 123123 🔐
                    self.do_show(user_show)
                if sec_comm[0] == 'destroy':
                    command = sec_comm[1].split('"')
                    user_show = str(commands[0] + " " + command[1])
                    self.do_destroy(user_show)
                if sec_comm[0] == 'update':
                    print("commd -->", commands)
                    command = sec_comm[1].split()
                    command_two = "".join(command)
                    #  (i.e) "123123123"atributo"value 🔐
                    command_three = command_two.replace('\"', " ")
                    #  (i.e) 123123123, atributo, value) 🔐
                    words = ""
                    for letra in command_three:
                        if letra not in ',)':
                            words = words + letra
                            #  (i.e) 121313 { atributo value } 🔐
                    list_2 = words.split()
                    # (i.e) ['id', '{', 'atibuto', ':', 'valor', '}'] 🔐
                    flag = list_2[1].split("'")
                    # (i,e) ['{']
                    if flag[0] is '{':
                        str_list = str(list_2[1:])
                        # (i.e) ['{', 'atribute', ':', 'value', '}'] 🔐
                        new_dict = aux_functions.list_to_dict(str_list)
                        # (i.e) new_dict = {'atibuto': 'value'} 🔐
                        for key, value in new_dict.items():
                            to_do = commands[0] + " " + \
                                str(list_2[0]) + " " + str(key) + \
                                " " + str(value)
                            self.do_update(to_do)
                            # (i.e) class_name id atribute value
                    else:
                        self.do_update(commands[0] + words)
                        # (i.e) class_name id atribute value 🔐
            except Exception:
                cmd.Cmd.default(self, args)
        else:
            cmd.Cmd.default(self, args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
