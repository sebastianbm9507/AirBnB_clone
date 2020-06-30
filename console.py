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
            if args == 'BaseModel':
                new_instance = BaseModel()
            elif args == 'User':
                new_instance = User()
            elif args == 'City':
                new_instance = City()
            elif args == 'Place':
                new_instance = Place()
            elif args == 'Amenity':
                new_instance = Amenity()
            elif args == 'State':
                new_instance = State()
            elif args == 'Review':
                new_instance = Review()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """ Show an instance.
        Usage 🛠:
        1 - show <class> <id>
        2 - <class name>.show("<id>")
        """
        commands = args.split()
        if len(commands[0]) < 1:
            print("** class name missing **")
        elif commands[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(commands) < 1:
            print("** instance id missing **")
        else:
            key_to_validate = "{}.{}".format(commands[0], commands[1])
            instances = storage.all()
            if key_to_validate not in instances:
                print("** no instance found **")
            else:
                print(str(instances[key_to_validate]))

    def do_destroy(self, args):
        """ Destroy an instance.
        Usage 🛠:
        1 - destroy <class> <id>
        2 - <class name>.destroy("<id>")
        """
        commands = args.split()
        if len(commands[0]) < 1:
            print("** class name missing **")
        elif commands[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(commands) < 1:
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
                    for key_id, obj in storage.all().items():
                        if key == key_id:
                            flag = comds[2].split("'")
                            if flag[0] is '{':
                                str_list = str(comds[2:])
                                new_dict = list_to_dict(str_list)
                                for key, value in new_dict.items():
                                    if hasattr(obj, key):
                                        value = type(getattr(obj, key))(value)
                                    #  (i.e) int(comds[3]) 🔐
                                    elif value.isdigit() is True:
                                        value = int(value)
                                    setattr(obj, key, value)
                                    storage.save()
                                else:
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
                                    storage.save()
