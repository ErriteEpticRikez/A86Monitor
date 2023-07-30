
"""

The A86Monitor program, its documentation, and any other auxiliary resources involved in building, installing
and running the program are licensed under the GNU General Public License. This includes,
but is not limited to, all the files in the official source distribution, as well as the source distribution itself.

A copy of the GNU General Public License can be found in the file LICENSE in the top directory of the official
source distribution.
The license is also available in several formats through the World Wide Web,
via http://www.gnu.org/licenses/licenses.html#GPL,
 or you can write the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

A86Monitor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""
import json

from errors import PingError

from monitor.config.jsonManager import addTarget, addEmail, delTarget
from monitor.configuratorpa.utils import combineTargetsStringList
from ping3 import verbose_ping

finished = False
print("A86Monitor Configurator V1.1")
while not finished:
    with open("monitor.json", "r") as jsonFile:
        monitordata = json.load(jsonFile)
        jsonFile.close()
        targets = monitordata["targets"]
    doMore = None
    more = True
    menu = int(input("Welcome to A86 Configurator\n Please choose an option \n 1. Add Target \n 2. Delete Target"
                 "\n 3. Add Email to notify \n 4. Add Sender Email \n 5. Set Password\n 6. Sender Email\n 7. Delete Receipient\n"
                     " 8. Set Outgoing Email Server\n"))
    print("Test")
    if menu == 1:
        more = True
        while more:
            more = False
            target_name = input("Please input target name. This is what the monitored target will be referred to in emails!\n")
            ip = input("Please input the IP of the target that will be pinged. If you havent set this to a static IP. You should"
                       " do this before setting it here!\n")
            try:
                verbose_ping(ip)
                addTarget(target_name, ip)
                doMore = input("Added Task, do you want to add another target? Use Y for Yes and N for No\n")
                if doMore.lower() == "y":
                    more = True
            except PingError as Ex:
                print("Was not able to ping target with IP " + ip + " could not add target")
    elif menu == 2:
        while more:
            more = False
            if len(monitordata["targets"]["target-list"]) == 0:
                print("There are no targets configured")
            else:
                output = combineTargetsStringList(monitordata["targets"]["target-list"])
                target_id = str(input(output))
                delTarget(monitordata["targets"]["target-list"][int(target_id) - 1])
                doMore = input("Deleted Task, do you want to delete another target? Use Y for Yes and N for No \n")
                if doMore.lower() == "y":
                    more = True
    elif menu == 3:
        while more:
            more = False
            email_input = input("Please enter the email you would like to add\n")
            if isinstance(email_input, str):
                monitordata["emails"].append(email_input)
                jsonFile = open("monitor.json", "w+")
                jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
                jsonFile.close()
                doMore = input("Added email, do you want to add another email? Use Y for Yes and N for No")
                if doMore.lower() == "y":
                    more = True
            else:
                print("Incorrect Input given")
    elif menu == 4:
        sender_name = input("What do you want the name on the sender to be?")
        if isinstance(sender_name, str):
            monitordata["sender-name"] = sender_name
            jsonFile = open("monitor.json", "w+")
            jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
            jsonFile.close()
            doMore = input("Sender name has been set!")

        else:
            print("Incorrect Input given")
    elif menu == 5:
        sender_password = input("Please enter the password for the sender\n")
        if isinstance(sender_password, str):
            monitordata["password"] = sender_password
            jsonFile = open("monitor.json", "w+")
            jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
            jsonFile.close()
            doMore = input("Sender password has been set!")

        else:
            print("Incorrect Input given")
    elif menu == 6:
        sender_password = input("Please enter the email for the sender\n")
        if isinstance(sender_password, str):
            monitordata["sender"] = sender_password
            jsonFile = open("monitor.json", "w+")
            jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
            jsonFile.close()
            doMore = input("Sender email has been set!")

        else:
            print("Incorrect Input given")
    elif menu == 7:
        while more:
            more = False
            if len(monitordata["emails"]) == 0:
                print("There are no emails configured")
            else:
                output = combineTargetsStringList(monitordata["emails"])
                target_id = int(input(output))
                monitordata["emails"].remove(monitordata["emails"][target_id - 1])
                jsonFile = open("monitor.json", "w+")
                jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
                jsonFile.close()
                doMore = input("Deleted Task, do you want to delete another target? Use Y for Yes and N for No \n")
                if doMore.lower() == "y":
                    more = True
    elif menu == 8:
        sender_server = input("Please enter the email server for the sender.\n")
        if isinstance(sender_server, str):
            monitordata["sender-server"] = sender_server
            sender_port:int = int(input("Please enter the email server port."))
            if isinstance(sender_port, int):
                monitordata["sender-port"] = sender_port
                jsonFile = open("monitor.json", "w+")
                jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
                jsonFile.close()



    exit = input("Do you want to return to the Main Menu?")
    if exit.lower() == "n":
        finished = True

