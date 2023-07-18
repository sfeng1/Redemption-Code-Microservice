import pandas
import mysql.connector
from datetime import date


mydb = mysql.connector.connect(
  host="localhost",
  user="sfeng1 ",
  password="mysql@HotSvsLoL1203"
  ,database="cs361"
)

my_cursor = mydb.cursor()
curr_input = None


def input_handler():
    new_input = str(input("Enter an input: "))
    return new_input


def startup():
    print("Welcome to the code management tool!")
    print("Enter a NUMBER below to start a task or enter HELP to see a list of options.\n")

    valid_input = ["1", "2", "help", "HELP"]
    curr_input = input_handler()

    while curr_input not in valid_input:
        print("Invalid input, try again!")
        curr_input = input_handler()

    if (curr_input.lower() == "help"):
        startup_help()
    elif (curr_input.lower() == "1"):
        ingest_warn()
    elif (curr_input.lower() == "2"):
        print("TBD")


def startup_help(carried_input = None):
    curr_input = carried_input
    print("\nHere is the list of tasks currently available:\n")
    print("Enter 1 : upload codes from a CSV into the tool")
    print("Enter 2 : lookup a code that already exists in the tool \n")
    print("Enter a NUMBER below to enter the respective flow or BACK to return.")

    valid_input = ["1", "2", "back", "BACK"]
    curr_input = input("Enter an input: ")

    while curr_input not in valid_input:
        print("Invalid input, try again!")
        curr_input = input_handler()

    if (curr_input.lower() == "back"):
        print("\n")
        startup()
    elif (curr_input.lower() == "1"):
        ingest_warn()
    elif (curr_input.lower() == "2"):
        print("TBD")


def ingest_warn(carried_input=None):
    curr_input = carried_input
    print("\nThis task will add codes from a .CSV file to the tool database.")
    print("These codes will then be available for easy retrieval.\n")
    print("Each code takes up space in the database and ingesting a large amount of codes will take more time.")
    print("Consider breaking up very large amounts into batches before ingesting.")

    curr_input = input("\nEnter 1 to acknowledge and continue:")
    while curr_input != "1":
        curr_input = input("Enter 1 to acknowledge and continue:")

    ingest_file()


def ingest_file(carried_input=None):
    curr_input = carried_input
    print("\nPlease place the .CSV file that contains all the codes in the same folder as the tool.")
    print("Then type the name of the file below (i.e. “codes.csv”).")
    print("\nYou may also enter BACK to return to the startup page or CUSTOM to specify an alternate file location")

    file_name = input("Enter file name:")
    if file_name.lower()==("back"):
        print("\n")
        startup()
    elif file_name.lower()==("custom"):
        ingest_file_help()
    else:
        fp = pandas.read_csv(file_name)
        ingest_name(file_pointer=fp)

def ingest_file_help(carried_input=None):
    curr_input = carried_input
    print("\nAdvanced users can enter the full file path below to grab the file from anywhere in the system.")
    print("For example: “/home/username/documents/codes.csv” will grab the codes.csv file from the documents folder.")
    print("\nYou may also enter BACK to return to the previous screen.\n")

    file_name = input("Enter file name:")
    if file_name.lower()==("back"):
        ingest_file()
    else:
        fp = pandas.read_csv(file_name)
        ingest_name(file_pointer=fp)

def ingest_name(carried_input=None, file_pointer=None):
    curr_input = carried_input
    print("\nNow enter the name that will be associated with each ingested code (i.e. “blue backpack”).")
    print("This name will be used to retrieve these codes in the future.\n")
    print("Enter BACK if you want to return to the last screen.\n")

    code_name = str(input("Enter the name you want to associate with each code:"))

    if code_name.lower() == "back":
        ingest_file()
    else:
        ingest_comment(file_pointer=file_pointer, input_name=code_name)


def ingest_comment(carried_input=None, file_pointer=None, input_name=None):
    curr_input = carried_input
    comment = None
    print("\nNow you can enter a comment that is applied to each ingested code.")
    print("This can be used purely for record keeping or to retrieve subsets of these codes in the future.")
    print("\nEnter a comment below (i.e. “Europe Promotion”) or HELP to see advanced use cases.\n")

    comment = str(input("Enter a comment:"))

    if comment.lower() == "help":
        ingest_comment_help(file_pointer=file_pointer, input_name=input_name)
    else:
        value_list = []
        for index, row in file_pointer.iterrows():
            rowtuple = tuple((row['Redeem_Code'], input_name, comment))
            value_list.append(rowtuple)
            if index == 10:
                break

        sql = "INSERT INTO redeem_code (code_string, code_name, code_comment) VALUES (%s, %s, %s)"
        val = value_list

        my_cursor.executemany(sql, val)
        mydb.commit()
        insert_count = str(my_cursor.rowcount)
        insert_complete(input_name=input_name, comment_name=comment, i_count=insert_count)


def ingest_comment_help(file_pointer=None, input_name=None):
    print("\n")
    print("Comments can be combined with the code name to retrieve specific subsets of keys.\n")
    print("For example, the name can be used to denote the item (jacket) and the comment is used to store the territory (NA, EU, or SA).")
    print("When retrieving keys in the future, you can then request only [jacket] + [EU] keys.\n")

    user_input = input("Enter BACK to return to the previous screen:")
    while user_input.lower() != "back":
        user_input = input("Enter BACK to return to the previous screen:")

    ingest_comment(file_pointer=file_pointer, input_name=input_name)


def insert_complete(input_name=None, comment_name=None, i_count=None):
    print("\n" + i_count + " codes have been ingested with " + input_name + " as the name and" + comment_name + "as the comment.")
    print("Enter QUIT to exit or 1 to ingest another file.")

    valid_input = ["1", "quit", "QUIT"]
    user_input = str(input("Enter 1 or QUIT:"))

    while user_input not in valid_input:
        user_input = str(input("Enter 1 or QUIT:"))

    if user_input.lower() == "quit":
        quit()
    elif user_input == 1:
        startup()

def main():
    startup()

if __name__ == "__main__":
    main()
    