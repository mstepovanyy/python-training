#!/usr/bin/bash
"""
Phone Book
----------
Write a simple phone book - an application storing a phone contacts information
in a plain (readable) file format.  There shall be a possibility to store
several phone numbers for one person.  It shall be possible to specify a file
path to a phone book in command line arguments; by default it shall point to a
``phonebook.txt`` file in the same folder as an application.

An application shall support the following operations:

    - add a new contact (a First and a Last names) with an arbitrary number of
      associated phone numbers;

    - edit an existing contact information (modify a First or a Last name; add,
      delete, or modify an associated phone number);

    - delete an existing contact information;

    - print a list of first N contacts (unordered or sorted alphabetically);

    - print a specific contact information given a First and a Last names;

    - search a contact information (a First and a Last name) given a phone
      number (efficiency doesn't matter) and print a list of found contacts;
"""

import argparse


def parse(input_args):
    parser = argparse.ArgumentParser(description="Phone Book")
    parser.add_argument("-b", "--book", dest="phone_book", default="phonebook.txt")

    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument("-c", "--create", dest="create_new", default=False, action="store_true")
    action_group.add_argument("-e", "--edit", dest="edit", default=False, action="store_true")
    action_group.add_argument("-d", "--delete", dest="delete", default=False, action="store_true")
    action_group.add_argument("-o", "--output", dest="print", default=False)
    action_group.add_argument("-s", "--search", dest="search", default=False, action="store_true")

    action, unknown = parser.parse_known_args(input_args)
    if action.create_new:
        new_contact_group = argparse.ArgumentParser("New contact")
        new_contact_group.add_argument("-f", "--first_name", dest="first_name", required=True)
        new_contact_group.add_argument("-l", "--last_name", dest="last_name", required=True)
        new_contact_group.add_argument("-p", "--phone", dest="phone", type=str, nargs="+", required=True)
        keys = new_contact_group.parse_args(unknown)

    if action.edit:
        edit_contact_group = argparse.ArgumentParser("Edit contact")
        edit_contact_group.add_argument("-f", "--first_name", dest="f_name_list", nargs="+",
                                        required=True) # first arg used as selector, second as new value
        edit_contact_group.add_argument("-l", "--last_name", dest="l_name_list", nargs="+",
                                        required=True)  # first arg used as selector, second as new value
        edit_contact_group.add_argument("-d", "--delete", dest="d_phone")
        edit_contact_group.add_argument("-a", "--add", dest="a_phone")
        keys = edit_contact_group.parse_args(unknown)

    if action.delete:
        delete_contact_group = argparse.ArgumentParser("Delete contact")
        delete_contact_group.add_argument("-f", "--first_name", dest="first_name", required=True)
        delete_contact_group.add_argument("-l", "--last_name", dest="last_name", required=True)
        keys = delete_contact_group.parse_args(unknown)

    if action.print:
        print_contact_group = argparse.ArgumentParser("Print Contact")
        print_contact_group.add_argument("-n", "--number", dest="print_number_of_phones")
        print_contact_group.add_argument("-f", "--first_name", dest="first_name")
        print_contact_group.add_argument("-l", "--last_name", dest="last_name")
        keys = print_contact_group.parse_args(unknown)

    if action.search:
        search_contact_group = argparse.ArgumentParser("Search contact")
        search_contact_group.add_argument("-f", "--first_name", dest="first_name")
        search_contact_group.add_argument("-l", "--last_name", dest="last_name")
        search_contact_group.add_argument("-n", "--number", dest="search_by_phone")
        keys = search_contact_group.parse_args(unknown)

    return action, keys


if __name__ == "__main__":
    parser = parse("-c -f First -l Last -p 3214325".split())
    parser = parse("-s -f First -l Last -n 3214325".split())
    print(parser)
